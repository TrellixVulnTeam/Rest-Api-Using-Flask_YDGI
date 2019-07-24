import os
import unittest
import tempfile
import pytest
import run

app = run.create_app()


def test_get_data():
    with app.test_client() as test_url:
        url = test_url.get("http://127.0.0.1:5000/api/pagination")
        assert url.status_code == 200


def test_without_ratio():
    with app.test_client() as test_url:
        url = test_url.get("http://127.0.0.1:5000/api/pagination?page=1")
        assert url.status_code == 200


def test_get_req_without_api():
    with app.test_client() as test_url:
        url = test_url.get("http://127.0.0.1:5000")
        assert url.status_code == 404


def test_less_ratio():
    with app.test_client() as test_url:
        url = test_url.get("http://127.0.0.1:5000/api/pagination?feed_ratio=[{'feed':12,'ratio':16}, {'feed':16,'ratio':16}]&page=1")
        assert url.status_code == 404


def test__more_ratio():
    with app.test_client() as test_url:
        url = test_url.get("http://127.0.0.1:5000/api/pagination?feed_ratio=[{'feed':12,'ratio':16}, {'feed':16,'ratio':16},{'feed':12,'ratio':16}, {'feed':16,'ratio':16}]&page=1")
        assert url.status_code == 404


def test_with_page_number_and_ratio():
    with app.test_client() as test_url:
        url = test_url.get("http://127.0.0.1:5000/api/pagination?feed_ratio=[{'feed':11,'ratio':16}, {'feed':12,'ratio':16}, {'feed':16,'ratio':16}]&page=1")
        assert url.status_code == 200


def test_page_number_and_no_ratio():
    with app.test_client() as test_url:
        url = test_url.get("http://127.0.0.1:5000/api/pagination?feed_ratio=[]&page=1")
        assert url.status_code == 404


def test_page_1_data_count():
    with app.test_client() as test_url:
        url = test_url.get("http://127.0.0.1:5000/api/pagination?page=1")
        data = url.get_json()
        data_count = len(data['data'])
        assert data_count == 48


