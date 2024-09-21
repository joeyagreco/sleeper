import unittest

from sleeper.api._utils import add_filters, build_route


class TestUtils(unittest.TestCase):
    def test_build_route_with_str_paths(self):
        resp = build_route("https://foo", "bar", "/baz")
        self.assertEqual("https://foo/bar/baz", resp)

    def test_build_route_with_int_and_str_paths(self):
        resp = build_route("https://foo", "bar", 1)
        self.assertEqual("https://foo/bar/1", resp)

    def test_build_route_base_url_ends_with_slash(self):
        resp = build_route("https://foo/", "bar", "/baz")
        self.assertEqual("https://foo/bar/baz", resp)

    def test_build_route_ending_path_ends_with_slash(self):
        resp = build_route("https://foo/", "bar", "/baz/")
        self.assertEqual("https://foo/bar/baz", resp)

    def test_add_filters_no_filters_given(self):
        resp = add_filters("https://foo")
        self.assertEqual("https://foo", resp)

    def test_add_filters_filters_given(self):
        resp = add_filters("https://foo", ("bar", "baz"), ("qux", 1))
        self.assertEqual("https://foo?bar=baz&qux=1", resp)

    def test_add_filters_url_already_has_filters(self):
        resp = add_filters(
            "https://foo?bar=baz",
            ("qux", 1),
        )
        self.assertEqual("https://foo?bar=baz&qux=1", resp)
