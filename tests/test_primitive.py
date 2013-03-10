"""Tests for the pyjava module.

This package contains tests for the primitive data types wrapped by PyJava,
directly used by the user.
"""


import unittest

import pyjava


class Test_boolean(unittest.TestCase):
    def setUp(self):
        self.bool_ = pyjava.getclass('java.lang.Boolean')
        self.True_ = self.bool_(True)
        self.False_ = self.bool_(False)

    def test_class(self):
        self.assertEqual(self.bool_._pyjava_classname, 'java.lang.Boolean')

    def test_value(self):
        self.assertTrue(self.True_.booleanValue() is True)
        self.assertTrue(self.False_.booleanValue() is False)


class Test_byte(unittest.TestCase):
    pass  # TODO


class Test_character(unittest.TestCase):
    def setUp(self):
        self.character = pyjava.getclass('java.lang.Character')
        self.v = self.character(u'v')

    def test_class(self):
        self.assertEqual(self.character._pyjava_classname,
                                                       'java.lang.Character')

    def test_value(self):
        self.assertTrue(self.v.charValue() == u'v')

    def test_numericvalue(self):
        numericV = self.character.getNumericValue('V')
        self.assertEqual(numericV, 31)
