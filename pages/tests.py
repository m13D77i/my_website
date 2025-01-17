from idlelib.rpc import response_queue

from django.test import TestCase
from django.shortcuts import reverse

# TDD ----> Test Driven Development

class PagesAppTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass
    # test for home page
    def test_home_page_for_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_for_url_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_page_for_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is a test")

    def test_home_page_for_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "pages/home.html")

    # test for about me page

    def test_about_page_for_url(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
    def test_about_page_for_url_name(self):
        res = self.client.get(reverse("about_me"))
        self.assertEqual(res.status_code, 200)

    def test_about_page_for_content(self):
        res = self.client.get(reverse("about_me"))
        self.assertContains(res, "AboutMe")

    def test_about_page_for_template(self):
        res = self.client.get(reverse("about_me"))
        self.assertTemplateUsed(res, "pages/about.html")

    # test for contact me page
    def test_contact_page_for_url(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    def test_contact_page_for_url_name(self):
        res = self.client.get(reverse("contact"))
        self.assertEqual(res.status_code, 200)

    def test_contact_page_for_content(self):
        res = self.client.get(reverse("contact"))
        self.assertContains(res, "ContactMe")

    def test_contact_page_for_template(self):
        res = self.client.get(reverse("contact"))
        self.assertTemplateUsed(res, "pages/contact.html")



