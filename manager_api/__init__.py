#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base64 import urlsafe_b64encode
from requests import Session
from urllib.parse import urljoin

from . import model
from .object import Object


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
        # Populate classes of available endpoints
        request = self.get("")
        for item in request.json():
            name = item["Name"]
            base = getattr(model, name)
            if not hasattr(base, "Guid") or base.Guid != item["Key"]:
                continue
            cls = type(name, (base,), {"_session": self})
            setattr(self, name, cls)

    def request(self, method, url, **kwargs):
        kwargs["auth"] = self._auth
        url = urljoin(self._url, url)
        url = url.rstrip("/") + ".json"
        return super().request(method, url, **kwargs)
