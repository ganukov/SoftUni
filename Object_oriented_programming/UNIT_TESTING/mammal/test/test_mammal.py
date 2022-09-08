from unittest import TestCase, main
from testing_exam.mammal.project.mammal import Mammal


class TestMammal(TestCase):
    KINGDOM = 'animals'
    NAME = 'Simon'
    MAMMAL_TYPE = 'Cat'
    SOUND = 'Meow'

    def setUp(self) -> None:
        self.mammal = Mammal(self.NAME, self.MAMMAL_TYPE, self.SOUND)

    def test_mammal_init_should_create_proper_obj(self):
        self.assertEqual(self.NAME, self.mammal.name)
        self.assertEqual(self.MAMMAL_TYPE, self.mammal.type)
        self.assertEqual(self.SOUND, self.mammal.sound)
        self.assertEqual(self.KINGDOM, self.mammal._Mammal__kingdom)

    def test_make_sound_returns_proper_result(self):
        result = self.mammal.make_sound()
        expected = f'{self.NAME} makes {self.SOUND}'
        self.assertEqual(expected, result)

    def test_get_kingdom_returns_animals(self):
        result = self.mammal.get_kingdom()
        self.assertEqual(self.KINGDOM, result)

    def test_info_returns_proper_string(self):
        actual = self.mammal.info()
        expected = f"{self.NAME} is of type {self.MAMMAL_TYPE}"
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
