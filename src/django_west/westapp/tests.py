import unittest
from django.test import TestCase, RequestFactory, Client
import westapp.views as views

# Create your tests here.
from django.http import HttpResponse


# @unittest.SkipTest
class ReturnLowest(TestCase):
    # def setUp(self):

    def test_return_lowest(self):
        number = 10
        result = views.return_lowest(number)
        self.assertEqual(result, 2520)
        number = 15
        result = views.return_lowest(number)
        self.assertEqual(result, 360360)
        number = 25
        result = views.return_lowest(number)
        self.assertEqual(result, 26771144400)

    def test_return_lowest_timeout(self):
        number = 25
        result = views.return_lowest(number, 5)
        self.assertEqual(result, "Takes too long")


# @unittest.SkipTest
class Lowest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_lowest_type(self):
        request = self.factory.get("/algoritm")
        response = views.lowest(request)
        self.assertIsInstance(response, HttpResponse)

    def test_lowest_value(self):
        request = self.factory.get("/algoritm/?number=10")
        response = views.lowest(request)
        self.assertEqual(response.status_code, 200)


class Algoritm(TestCase):
    def test_api_call(self):
        client = Client()
        response = client.get("/algoritm/", {"number": "5"})
        self.assertTemplateUsed(response, "base.html")
        self.assertEqual(response.context["lowest"], 60)
