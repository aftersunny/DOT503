from mockito import mock, verify
import unittest

from helloworld import helloworld

class HelloWorldTest(unittest.TestCase):
    def test_should_issue_hello_world_message(self):
        out = mock()
        helloworld(out)
        verify(out).write("Hello world of Python\n")

    def test2(self):
        out = mock()
        helloworld(out)
        verify(out).write("Hello world of Python\n")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
