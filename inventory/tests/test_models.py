from django.test import Client, TestCase
from model_mommy import mommy


class KidTestModel(TestCase):

    def setUp(self):
        """
        Set up all the tests
        """
        self.item = mommy.make('Item')

    def test_model_item(self):
        self.assertEquals(str(self.item), self.item.item)
