from sleeper.api.constants import AVATARS_ROUTE, SLEEPER_CDN_BASE_URL, THUMBS_ROUTE
from sleeper.api.util import build_route, get_content


def get_avatar(*, avatar_id: str, as_thumbnail: bool = False) -> bytes:
    if as_thumbnail:
        url = build_route(
            SLEEPER_CDN_BASE_URL,
            None,
            AVATARS_ROUTE,
            THUMBS_ROUTE,
            avatar_id,
        )
    else:
        url = build_route(SLEEPER_CDN_BASE_URL, None, AVATARS_ROUTE, avatar_id)

    return get_content(url)
