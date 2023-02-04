# -*- coding: utf-8 -*-

from __future__ import annotations

from requests import Session
from typing import ClassVar, Optional
from uuid import UUID

from pydantic import BaseModel


class Object(BaseModel):
    _session: ClassVar[Session]
    Key: Optional[UUID]
    Name: Optional[str]
    Timestamp: Optional[int]

    def __init__(self, Key=None, **kwargs):
        kwargs.update({"Key": Key})
        return super().__init__(**kwargs)

    def __hash__(self):
        return hash(self.Key or self.Guid)

    @classmethod
    def validate(cls, value):
        if isinstance(value, str) or isinstance(value, UUID):
            value = {"Key": value}
        return super().validate(value)

    @staticmethod
    def _parse_response(response):
        result = response.json()
        if result is None or (isinstance(result, dict) and not result.get("Success", False)):
            raise RuntimeError(f"{response.request.method} {response.request.url}: {result['Error']}")
        return result

    @property
    def _path(self):
        return f"{self.Guid}/{self.Key}"

    @classmethod
    def list(self):
        """List all of the objects of the given type."""
        response = self._session.get(self.Guid)
        result = response.json()
        return [self.parse_obj(r) for r in result]

    def create(self):
        response = self._session.post(self.Guid, data=self.json())
        result = self._parse_response(response)
        self.Key = result["Key"]

    def read(self):
        result = self._session.get(self._path).json()
        result["Key"] = self.Key
        self.__init__(**result)

    def update(self):
        response = self._session.put(self._path, data=self.json())
        self._parse_response(response)

    def delete(self):
        response = self._session.delete(self._path)
        self._parse_response(response)
        self.Key = None

    def json(self, exclude_none=True, **kwargs):
        return super().json(exclude_none=exclude_none, models_as_dict=False, **kwargs)

    class Config:
        arbitrary_types_allowed = True,
        fields = {
            "Timestamp": {"exclude": True},
        }
        json_encoders = {
            "Object": lambda v: v.Key,
        }
