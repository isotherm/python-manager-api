#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base64 import urlsafe_b64encode
from inspect import isclass
from requests import Session
from urllib.parse import urljoin


class Business(Session):
    def __init__(self, url, username, password, name):
        # Calculate API URL for this business
        name = bytes(name, encoding="utf-8")
        name = urlsafe_b64encode(name).decode("utf-8")
        name = name.rstrip("=")
        url = urljoin(url, f"api/{name}/")
        # Initialize persistent options
        self._url = url
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
        url = urljoin(self._url, url)
        url = url.rstrip("/") + ".json"
        return super().request(method, url, **kwargs)


__all__ = [
    "Business",
]
