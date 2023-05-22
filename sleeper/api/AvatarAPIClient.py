from sleeper.api.SleeperAPIClient import SleeperAPIClient


class AvatarAPIClient(SleeperAPIClient):
    @classmethod
    def get_avatar(cls, *, avatar_id: str, save_to_path: str, **kwargs) -> None:
        thumbnail = kwargs.pop("thumbnail", False)
        if thumbnail:
            url = cls._build_route(
                cls._SLEEPER_CDN_BASE_URL, None, cls._AVATARS_ROUTE, cls._THUMBS_ROUTE, avatar_id
            )
        else:
            url = cls._build_route(cls._SLEEPER_CDN_BASE_URL, None, cls._AVATARS_ROUTE, avatar_id)
        image_file = cls._get_image_file(url)
        image_file.save(save_to_path)
