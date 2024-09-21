from typing import Any

import requests

# TODO: add tests for these


def build_route(base_url: str, *paths: str | int) -> str:
    if base_url.endswith("/"):
        base_url = base_url[:-1]

    paths = tuple(str(p).strip("/") for p in paths)
    url = f"{base_url}/{'/'.join(paths)}"
    return url.strip("/")


def get(url: str) -> Any:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_content(url: str) -> bytes:
    response = requests.get(url)
    response.raise_for_status()
    return response.content


def add_filters(url: str, *args: tuple[str, Any]) -> str:
    """
    Adds filters to the given url.
    """
    symbol = "?"
    if "?" in url:
        symbol = "&"
    for arg in args:
        if arg[0] is not None and arg[1] is not None:
            url = f"{url}{symbol}{arg[0]}={arg[1]}"
        else:
            raise ValueError("filters not formatted correctly")
        symbol = "&"
    return url
