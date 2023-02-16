#!/usr/bin/python3
""" unittest """
import unittest
from models.base import Base

from io import StringIO


class Test_Base(unittest.TestCase):
    """ unittest """
    def test_init(self):
        b = Base()
        self.assertEqual(b.id, 1)

        b = Base(10)
        self.assertEqual(b.id, 10)



        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

        d = [{ 'id': 12}]
        result = Base.to_json_string(d)
        self.assertEqual(result, '[{"id": 12}]')



        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

        result = Base.from_json_string(None)
        self.assertEqual(result, [])

        d = '[{"id": 12}]'
        result = Base.from_json_string(d)
        self.assertEqual(result, [{"id": 12}])