class APIResponse:
    """
    Should be inherited by all top-level API response objects to store information about the API call.
    """

    def __init__(self, url=None):
        self.url = url
