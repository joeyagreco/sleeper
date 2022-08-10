from requests import HTTPError


class MockResponse:
    def __init__(self, data: dict | list, status_code: int, **kwargs):
        self.__data = data
        self.content = kwargs.pop("content", None)
        self.status_code = status_code

    def json(self):
        return self.__data

    def raise_for_status(self):
        """
        This is meant to closely resemble the actual raise_for_status method found here:
        https://requests.readthedocs.io/en/latest/_modules/requests/models/#Response.raise_for_status
        """
        http_error_msg = ""
        if 400 <= self.status_code < 500:
            http_error_msg = (
                f"{self.status_code} Client Error"
            )

        elif 500 <= self.status_code < 600:
            http_error_msg = (
                f"{self.status_code} Server Error"
            )

        if http_error_msg:
            raise HTTPError(http_error_msg, response=self)
