from unittest import TestCase, main

from Object_oriented_programming.UNIT_TESTING.hero.project.hero import Hero


class TestHero(TestCase):
    USERNAME = 'George'
    LEVEL = 99
    HEALTH = 100
    DAMAGE = 50

    def setUp(self) -> None:
        self.hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)

    def test__constructor__if_takes_proper_data(self):
        self.assertEqual(self.USERNAME, self.hero.username)
        self.assertEqual(self.LEVEL, self.hero.level)
        self.assertEqual(self.HEALTH, self.hero.health)
        self.assertEqual(self.DAMAGE, self.hero.damage)

    def test__battle__if_username_exists__expect_exep(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(Hero('George', 99, 100, 50))
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test__battle__if_health_less_than_zero__expect_exep(self):
        with self.assertRaises(ValueError) as ex:
            self.hero.health -= 105
            self.hero.battle(Hero('Ivan', 99, 100, 50))
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test__battle__if_health_is_equal_to_0__expect_exep(self):
        with self.assertRaises(ValueError) as ex:
            self.hero.health -= 100
            self.hero.battle(Hero('Ivan', 99, 100, 50))
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test__battle__if_enemy_health_is_less_than_0__expect_exep(self):
        hero = Hero('Ivan', 99, -101, 50)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(hero)
        self.assertEqual(f"You cannot fight {hero.username}. He needs to rest", str(ex.exception))

    def test__battle__if_enemy_health_is_equal_to_0__expect_exep(self):
        hero = Hero('Ivan', 99, 0, 50)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(hero)
        self.assertEqual(f"You cannot fight {hero.username}. He needs to rest", str(ex.exception))

    def test__battle__player_dmg(self):
        actual_dmg = self.DAMAGE * self.LEVEL
        expecting_dmg_pl = self.hero.damage * self.hero.level

        self.assertEqual(actual_dmg, expecting_dmg_pl)

    def test__battle__if_player_heath_less_than_0_and_enemy_less_than_0(self):
        enemy_hero = Hero('Ivan', 2, 100, 50)
        our_hero = Hero('George', 2, 100, 50)
        self.assertEqual('Draw', our_hero.battle(enemy_hero))
        self.assertEqual(0, enemy_hero.health)
        self.assertEqual(0, our_hero.health)

    def test__battle__if_our_player_wins__expect_message(self):
        enemy_hero = Hero('Ivan', 1, 100, 50)
        our_hero = Hero('George', 2, 100, 50)
        expected = 'You win'
        result = our_hero.battle(enemy_hero)
        self.assertEqual(result, expected)

    def test__battle__if_our_player_wins__expect__increment(self):
        enemy_hero = Hero('Ivan', 1, 100, 50)
        our_hero = Hero('George', 2, 100, 50)
        our_hero.battle(enemy_hero)

        self.assertEqual(our_hero.level, 3)
        self.assertEqual(our_hero.health, 55)
        self.assertEqual(our_hero.damage, 55)

    def test__battle__if_enemy_player_wins__expect_message(self):
        enemy_hero = Hero('Ivan', 2, 100, 50)
        our_hero = Hero('George', 1, 100, 50)
        expected = 'You lose'
        result = our_hero.battle(enemy_hero)
        self.assertEqual(result, expected)

    def test__battle__if_enemy_player_wins__expect__increment(self):
        enemy_hero = Hero('Ivan', 2, 100, 50)
        our_hero = Hero('George', 1, 100, 50)
        our_hero.battle(enemy_hero)

        self.assertEqual(enemy_hero.level, 3)
        self.assertEqual(enemy_hero.health, 55)
        self.assertEqual(enemy_hero.damage, 55)

    def test__str__expect__proper_string(self):
        result = str(self.hero)
        actual = f"Hero {self.USERNAME}: {self.LEVEL} lvl\n" \
                 f"Health: {self.HEALTH}\n" \
                 f"Damage: {self.DAMAGE}\n"
        self.assertEqual(actual, result)


if __name__ == '__main__':
    main()
