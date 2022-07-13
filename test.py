from sleeper.api.UserAPIClient import UserAPIClient

if __name__ == "__main__":
    username = "john"
    user_id = ""

    client = UserAPIClient(username=username)

    user = client.get_user()
    print()
