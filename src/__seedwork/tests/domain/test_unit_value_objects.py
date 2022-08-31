from dataclasses import FrozenInstanceError, is_dataclass
import unittest
from unittest.mock import patch
from __seedwork.domain.exceptions import InvalidUuidException

from __seedwork.domain.value_objects import UniqueEntityId

class TestUniqueEntityIdUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(UniqueEntityId))

    def test_throw_exception_when_uuid_is_invalid(self):
        with self.assertRaises(InvalidUuidException) as assert_error:
            UniqueEntityId('fake id')
        self.assertEqual(assert_error.exception.args[0], 'ID must be a valid UUID')

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(UniqueEntityId))

    def test_throw_exception_when_uuid_is_invalid_complete(self):
        with patch.object(
            UniqueEntityId,
            '_UniqueEntityId__validate',
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate
        ) as mock_validate:
            with self.assertRaises(InvalidUuidException) as assert_error:
                UniqueEntityId('fake id')
            mock_validate.assert_called_once()
            self.assertEqual(
                assert_error.exception.args[0], 'ID must be a valid UUID')

    def test_accept_uuid_passed_in_constructor(self):
        with patch.object(
            UniqueEntityId,
            '_UniqueEntityId__validate',
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate
        ) as mock_validate:
            value_object = UniqueEntityId(
                'af46842e-027d-4c91-b259-3a3642144ba4')
            mock_validate.assert_called_once()
            self.assertEqual(
                value_object.id, 'af46842e-027d-4c91-b259-3a3642144ba4')

        uuid_value = uuid.uuid4()
        value_object = UniqueEntityId(uuid_value)
        self.assertEqual(value_object.id, str(uuid_value))

    def test_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = UniqueEntityId()
            value_object.id = 'fake id'

    def test_convert_to_str(self):
        value_object = UniqueEntityId()
        self.assertEqual(value_object.id, str(value_object))