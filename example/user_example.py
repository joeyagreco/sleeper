from sleeper.api import UserAPIClient
from sleeper.model import User

if __name__ == "__main__":
    # get a user by username
    user_1: User = UserAPIClient.get_user(username="my_username")

    # get a user by ID
    user_2: User = UserAPIClient.get_user(user_id="my_user_id")
