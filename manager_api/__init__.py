#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import partial
from typing import Sequence, Optional

from inflection import underscore
from pydantic import BaseModel
from uplink import auth, Body, Consumer, delete, get, json, loads, post, put, response_handler, returns

from .model import *


def verify_success(response):
    result = response.json()
    if not result["Success"]:
        raise RuntimeError(f"{response.request.method} {response.request.url}: {result['Error']}")
    return response


class Result(BaseModel):
    Key: str
    Name: Optional[str]
    Timestamp: Optional[int]


class Manager(Consumer):
    @returns.json(Sequence[Result])
    @get("/api.json")
    def list_businesses(self):
        """List all businesses."""

    def get_business(self, name):
        """Get business with specified `name`."""
        businesses = {r.Name: r.Key for r in self.list_businesses()}
        return Business(self, businesses[name])

    @returns.json(Sequence[Result])
    @get("/api/{business_key}.json")
    def _list_endpoints(self, business_key):
        pass

    @returns.json(Sequence[Result])
    @get("/api/{business_key}/{endpoint_key}.json")
    def _list_objects(self, business_key, endpoint_key):
        pass

    @json
    @returns.json
    @response_handler(verify_success)
    @post("/api/{business_key}/{object_key}.json")
    def _post_object(self, business_key, object_key, object: Body(type=BaseModel)):
        pass

    @returns.json
    @get("/api/{business_key}/{object_key}.json")
    def _get_object(self, business_key, object_key):
        pass

    @json
    @returns.json
    @response_handler(verify_success)
    @put("/api/{business_key}/{object_key}.json")
    def _put_object(self, business_key, object_key, object: Body(type=BaseModel)):
        pass

    @returns.json
    @response_handler(verify_success)
    @delete("/api/{business_key}/{object_key}.json")
    def _delete_object(self, business_key, object_key):
        pass


class Business:
    def __init__(self, api, business_key):
        self._api = api
        self._key = business_key
        for item in api._list_endpoints(business_key):
            model = globals()[item.Name]
            method_suffix = underscore(item.Name)
            if not model.Singleton:
                setattr(self, f"list_{method_suffix}", partial(self._list, model))
                setattr(self, f"create_{method_suffix}", partial(self._create, model))
                setattr(self, f"get_{method_suffix}", partial(self._get, model))
                setattr(self, f"update_{method_suffix}", partial(self._update, model))
                setattr(self, f"delete_{method_suffix}", partial(self._delete, model))
            else:
                setattr(self, f"get_{method_suffix}", partial(self._get, model, item.Key))
                setattr(self, f"update_{method_suffix}", partial(self._update, model, item.Key))

    def _lookup(self, model, key):
        if type(key) is UUID:
            return key
        try:
            return UUID(key)
        except ValueError:
            results = [r for r in self._list(model) if r.Name == key]
            #list(filter(lambda r: r.Name == key, self._list(model)))
            if not results:
                raise KeyError(f"Could not find {type(model).__name__} with name \"{key}\"")
            elif len(results) > 1:
                raise KeyError(f"More than one {type(model).__name__} with name \"{key}\"")
            else:
                return results[0].Key

    def _list(self, model):
        return self._api._list_objects(self._key, model.Key)

    def _create(self, model, object):
        if model.Key != object.Key:
            raise TypeError(f"Object {type(object).__name__} is not a {type(model).__name__}")
        result = self._api._post_object(self._key, object.Key, object)
        return result["Key"]

    def _get(self, model, key):
        return model(**self._api._get_object(self._key, self._lookup(model, key)))

    def _update(self, model, key, object):
        if model.Key != object.Key:
            raise TypeError(f"Object {type(object).__name__} is not a {type(model).__name__}")
        self._api._put_object(self._key, self._lookup(model, key), object)

    def _delete(self, model, key):
        self._api._delete_object(self._key, self._lookup(model, key))
