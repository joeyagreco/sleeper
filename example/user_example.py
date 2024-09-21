from sleeper.api import get_user

if __name__ == "__main__":
    # get a user by username
    user_1 = get_user(identifier="my_username")

    # get a user by ID
    user_2 = get_user(identifier="my_user_id")
