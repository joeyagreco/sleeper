from sleeper.api import AvatarAPIClient

if __name__ == "__main__":
    # get avatar by ID and save locally
    AvatarAPIClient.get_avatar(
        avatar_id="my_avatar_id", save_to_path="C:\\Desktop\\avatar\\my_avatar.png"
    )

    # can pass in the "thumbnail" parameter to get a smaller-sized avatar
    AvatarAPIClient.get_avatar(
        avatar_id="my_avatar_id", save_to_path="C:\\Desktop\\avatar\\my_avatar.png", thumbnail=True
    )
