from unittest import TestCase
from io import StringIO

from main import main, pprint


class MainTestCase(TestCase):

    def test_main(self):
        result = main()
        self.assertTrue(result)

    def test_pprint(self):
        buffer = StringIO()
        pprint('test', out=buffer)
        self.assertEqual('test', buffer.getvalue())

    def test_true(self):
        value = True
        self.assertTrue(True)
