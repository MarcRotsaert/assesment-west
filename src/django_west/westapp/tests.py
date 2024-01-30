from django.test import TestCase
import westapp.views as views
# Create your tests here.

class ReturnLowest(TestCase):
    # def setUp(self):
    
    def test_return_lowest1(self):
        number = 10
        result = views.return_lowest(number)
        self.assertEqual(result, 2520)

    def test_return_lowest2(self):
        number = 25
        result = views.return_lowest(number)
        self.assertEqual(result, 26771144400)

    def test_return_lowest3(self):
        number = 25
        result = views.return_lowest(number, 5)
        self.assertEqual(result, "Takes too long")
