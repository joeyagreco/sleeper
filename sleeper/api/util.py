from typing import Any, Optional

import requests


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
