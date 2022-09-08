import unittest

class CatTests(unittest.TestCase):
    NAME = 'Simon'

    def setUp(self) -> None:
        self.cat = Cat(self.NAME)

    def test_eat__expect_size_to_increment(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_eat__expect_fed_to_be_true(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)

    def test__eat__is_fed__expect_exception(self):
        # Arrange
        self.cat.eat()
        # Act/Assert
        with self.assertRaises(Exception) as ex:
            self.cat.eat() # Act

        self.assertIsNotNone(ex)

    def test__sleep__when_fed_is_false__expect_to_raise(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertIsNotNone(ex)

    def test__sleep__expect_sleepy_to_be_false(self):
        # Arrange
        self.cat.eat()
        # Act
        self.cat.sleep()
        # Assert
        self.assertFalse(self.cat.sleepy)

if __name__ == '__main__':
    unittest.main()
