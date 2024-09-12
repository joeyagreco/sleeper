from sleeper.api.avatar import get_avatar

if __name__ == "__main__":
    # get avatar by ID
    avatar_bytes = get_avatar(avatar_id="my_avatar_id")

    # save locally
    with open(
        "my_avatar.png",
        "wb",
    ) as file:
        file.write(avatar_bytes)

    # can pass in the "thumbnail" parameter to get a smaller-sized avatar
    get_avatar(
        avatar_id="my_avatar_id",
        as_thumbnail=True,
    )
