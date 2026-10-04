import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="Request url"
    )
    parser.addoption(
        "--status_code",
        default=200,
        type=int,
        help="Response status code"
    )
