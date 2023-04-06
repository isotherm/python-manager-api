#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base64 import urlsafe_b64encode
from inspect import isclass
import re
from requests import Session
from urllib.parse import urljoin


def _b64encode(string):
    if hasattr(string, "encode"):
        string = string.encode()
    return urlsafe_b64encode(string).decode().rstrip("=")


class Business(Session):
    def __init__(self, url, username, password, name):
        # Initialize persistent options
        self._url = url
        self._name = name
        self._api_url = urljoin(url, f"api/{_b64encode(name)}/")
        self._auth = (username, password)
        super().__init__()
        # Create session-specific classes
        from . import model
        for name in model.__all__:
            attr = getattr(model, name)
            if isclass(attr):
                attr = type(name, (attr,), {"_session": self})
            setattr(model, name, attr)
        # Update forward references
        ns = {c: getattr(model, c) for c in ["Dict", "List", "Optional"]}
        ns["model"] = model
        for name in model.__all__:
            attr = getattr(model, name)
            if not isclass(attr):
                continue
            base = attr.__bases__[0]
            localns = ns.copy()
            for k, v in base.__dict__.items():
                if isclass(v) and issubclass(v, model.ManagerBaseModel):
                    v = type(k, (v,), {})
                    v.update_forward_refs(**ns)
                    setattr(base, k, v)
                    localns[k] = v
            attr.update_forward_refs(**localns)
        # Populate classes of available endpoints
        request = self.get("")
        for item in request.json():
            name = item["Name"]
            try:
                base = getattr(model, name)
                assert(base.Guid == item["Key"])
                setattr(self, name, base)
            except (AssertionError, AttributeError):
                continue

    def request(self, method, url, **kwargs):
        kwargs["auth"] = self._auth
        url = urljoin(self._api_url, url)
        url = url.rstrip("/") + ".json"
        return super().request(method, url, **kwargs)

    def _get_url(self, action, uuid=None):
        action = re.sub(r'(?<!^)(?=[A-Z])', '-', action).lower()
        name = self._name.encode()
        protobuf = b"\xa2\x06" + bytes([len(name)]) + name
        if uuid:
            protobuf += b"\xc2\x0c\x12"
            protobuf += b"\x09" + uuid.bytes_le[:8]
            protobuf += b"\x11" + uuid.bytes_le[8:]
        protobuf = _b64encode(protobuf)
        return urljoin(self._url, f"{action}?{protobuf}")


__all__ = [
    "Business",
]
