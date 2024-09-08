from typing import Any, Optional

import requests

# TODO: add tests for these


def build_route(base_url: str, version: Optional[str], *args) -> str:
    args = (str(arg).replace("/", "") for arg in args)
    if version is not None:
        return f"{base_url}/{version}/{'/'.join(args)}"
    else:
        return f"{base_url}/{'/'.join(args)}"


def get(url: str) -> Optional[dict[Any, Any] | list[Any]]:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def add_filters(url: str, *args) -> str:
    """
    Adds filters to the given url.
    """
    if len(args) > 0:
        symbol = "?"
        for i, arg in enumerate(args):
            if i > 0:
                symbol = "&"
            if arg[0] is not None and arg[1] is not None:
                url = f"{url}{symbol}{arg[0]}={arg[1]}"
    return url
