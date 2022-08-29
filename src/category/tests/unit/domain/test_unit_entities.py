from dataclasses import is_dataclass
from datetime import datetime

import unittest
from category.domain.entities import Category

class TestCategoryUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Category))

    def test_constructor(self):
        category = Category('Movie', 'this is the description')
        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'this is the description')
        self.assertEqual(category.is_active, True)
        self.assertIsInstance(category.created_at, datetime)

    def test_if_created_at_is_generated_in_constructor(self):
        category1 = Category('Movie', 'Description')
        category2 = Category('Movie', 'Description')

        self.assertNotEqual(category1.created_at, category2.created_at)