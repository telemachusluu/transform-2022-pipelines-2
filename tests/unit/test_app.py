#!/usr/bin/env python

import pytest
from project.app import app


def test_index_route():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Hello World!"
