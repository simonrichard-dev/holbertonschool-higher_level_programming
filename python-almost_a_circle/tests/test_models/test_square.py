#!/usr/bin/python3
""" unittest """
import unittest
import os
from models.square import Square
from models.base import Base

from io import StringIO
from contextlib import redirect_stdout


class Test_Square(unittest.TestCase):
    """ unittest """

    def test_init(self):
        r = Square(8, 4, 2, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.area(), 64)

        r = Square(8)
        self.assertEqual(r.width, 8)

        self.assertRaisesRegex(
            TypeError, "width must be an integer", Square, "8", 4, 2, 10)
        self.assertRaisesRegex(
            TypeError, "x must be an integer", Square, 8, "4", 2, 10)
        self.assertRaisesRegex(
            TypeError, "y must be an integer", Square, 8, 4, "2", 10)
        self.assertRaisesRegex(
            ValueError, "width must be > 0", Square, -1, 4, 2, 10)
        self.assertRaisesRegex(
            ValueError, "x must be >= 0", Square, 8, -1, 2, 10)
        self.assertRaisesRegex(
            ValueError, "y must be >= 0", Square, 8, 1, -2, 10)
        self.assertRaisesRegex(TypeError, "", Square, )
        self.assertRaisesRegex(
            ValueError, "width must be > 0", Square, 0, 4, 2, 10)

        r1 = Square(1)
        expected_output = '#\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            r1.display()
            result = buffer.getvalue()
        self.assertEqual(result, expected_output)

        r1 = Square(1, 1, 1)
        expected_output = '\n #\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            r1.display()
            result = buffer.getvalue()
        self.assertEqual(result, expected_output)

        r = Square(1, 3, 4)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 3)
        self.assertEqual(r.width, 3)

        r = Square(14, 12, 15, 25)
        self.assertEqual(str(r), "[Square] (25) 12/15 - 14")

        r = Square(2, 6, 8, 22)
        self.assertEqual(r.to_dictionary(), {'id': 22, 'size': 2,
                                             'x': 6, 'y': 8})

        r = Square.create(**{'id': 5, 'width': 1,
                             'x': 4, 'y': 5})
        answer = Square(1, 4, 5, 5)
        self.assertEqual(str(r), str(answer))

        r = Square.create(**{'id': 89, 'width': 1,
                             'x': 3})
        answer = Square(1, 3, 0, 89)
        self.assertEqual(str(r), str(answer))

        r = Square.create(**{'id': 89, 'width': 1})
        answer = Square(1, 0, 0, 89)
        self.assertEqual(str(r), str(answer))

        r = Square(2)
        Square.save_to_file([r])
        with open("Square.json", "r") as f:
            content = f.read()
        expected_output = '[{"id": 19, "size": 2, "x": 0, "y": 0}]'
        self.assertEqual(content, expected_output)
        os.remove("Square.json")

        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            content = f.read()
        expected_output = '[]'
        self.assertEqual(content, expected_output)
        os.remove("Square.json")

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            content = f.read()
        expected_output = '[]'
        self.assertEqual(content, expected_output)
        os.remove("Square.json")



        r1 = Square(10)
        Square.save_to_file([r1])
        squares = Square.load_from_file()
        self.assertIsInstance(squares[0], Square)
        self.assertEqual(squares[0].width, 10)
        os.remove("Square.json")

        r = Square.load_from_file()
        self.assertTrue(isinstance(r, list))
        self.assertEqual(r, [])