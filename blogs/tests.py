from django.core.urlresolvers import resolve
from django.test import TestCase

from .views import *


# Create your tests here.

class Blogs_Url_View_Mapping_Test(TestCase):
    def test_url_resolves_to_blogs_page_view(self):
        found = resolve("/blogs/")
        self.assertEqual(found.func, blogs_home)

    def test_url_resolves_to_blogs_details_by_id_view(self):
        found = resolve('/blogs/1/')
        self.assertEqual(found.func, blog_details_by_id)

    def test_url_resolves_to_blogs_details_by_slug_view(self):
        found = resolve('/blogs/slug-slug/')
        self.assertEqual(found.func, blog_details_by_slug)

    def test_url_resolves_to_blogs_delete_by_id_view(self):
        found = resolve("/blogs/123/delete/")
        self.assertEqual(found.func, blog_delete_by_id)

    def test_url_resolves_to_blogs_delete_by_slug_view(self):
        found = resolve("/blogs/slug-slug/delete/")
        self.assertEqual(found.func, blog_delete_by_slug)

    def test_url_resolves_to_blogs_create_view(self):
        found = resolve("/blogs/create/")
        self.assertEqual(found.func, blog_create)

    def test_url_resolves_to_blogs_edit_by_id_view(self):
        found = resolve("/blogs/123/edit/")
        self.assertEqual(found.func, blog_edit_by_id)

    def test_url_resolves_to_blogs_edit_by_slug_view(self):
        found = resolve("/blogs/slug-slug/edit/")
        self.assertEqual(found.func, blog_edit_by_slug)

