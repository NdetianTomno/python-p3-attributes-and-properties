#!/usr/bin/env python3

from person import Person

import io
import sys
import unittest
from person import Person

class TestPerson(unittest.TestCase):
    def test_empty_name(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name="")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "Name must be a string between 1 and 25 characters.\n")

    def test_non_string_name(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name=123)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "Name must be a string between 1 and 25 characters.\n")

    def test_long_name(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name="This name is longer than 25 characters.")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "Name must be a string between 1 and 25 characters.\n")

    def test_valid_name(self):
        person = Person(name="John Doe")
        self.assertEqual(person.name, "John Doe")

    def test_invalid_job(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name="John Doe", job="Invalid Job")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "Job must be in the list of approved jobs.\n")

    def test_valid_job(self):
        person = Person(name="John Doe", job="Sales")
        self.assertEqual(person.job, "Sales")

if __name__ == '__main__':
    unittest.main()
