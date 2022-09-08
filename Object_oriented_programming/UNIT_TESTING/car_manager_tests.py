import unittest



class CarTests(unittest.TestCase):

    def test__is_init_properly__right_data(self):
        example = Car('a', 'b', 1, 4)
        self.assertEqual('a', example.make)
        self.assertEqual('b', example.model)
        self.assertEqual(1, example.fuel_consumption)
        self.assertEqual(4, example.fuel_capacity)
        self.assertEqual(0, example.fuel_amount)

    def test__make__with_right_data(self):
        example = Car('a', 'b', 1, 4)
        result = example.make
        self.assertEqual('a', result)

    def test__make_with_wrong_data(self):
        example = Car('a', 'b', 1, 4)
        with self.assertRaises(Exception) as ex:
            example.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))
        with self.assertRaises(Exception) as ex:
            example.make = 0
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test__model_with_right_data(self):
        example = Car('a', 'b', 1, 4)
        result = example.model
        self.assertEqual('b', result)

    def test__mode_with_wrong_data(self):
        example = Car('a', 'b', 1, 4)
        with self.assertRaises(Exception) as ex:
            example.model = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))
        with self.assertRaises(Exception) as ex:
            example.model = 0
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test__fuel_consumption__with_right_data(self):
        example = Car('a', 'b', 1, 4)
        result = example.fuel_consumption
        self.assertEqual(1, result)

    def test__fuel_consumption__with_wrong_data(self):
        example = Car('a', 'b', 1, 4)
        with self.assertRaises(Exception) as ex:
            example.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))
        with self.assertRaises(Exception) as ex:
            example.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test__fuel_capacity__with_right_data(self):
        example = Car('a', 'b', 1, 4)
        result = example.fuel_capacity
        self.assertEqual(4, result)

    def test__fuel_capacity__with_wrong_data(self):
        example = Car('a', 'b', 1, 4)
        with self.assertRaises(Exception) as ex:
            example.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))
        with self.assertRaises(Exception) as ex:
            example.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test__fuel_amount__with_right_data(self):
        example = Car('a', 'b', 1, 4)
        result = example.fuel_amount
        self.assertEqual(0, result)

    def test__fuel_amount__with_wrong_data(self):
        example = Car('a', 'b', 1, 4)
        with self.assertRaises(Exception) as ex:
            example.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test__refuel__with_0_or_negative_data(self):
        example = Car('a', 'b', 1, 4)
        with self.assertRaises(Exception) as ex:
            example.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
        with self.assertRaises(Exception) as ex:
            example.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test__refuel__with_more_fuel(self):
        example = Car('a', 'b', 1, 4)
        result = example.refuel(6)
        self.assertEqual(4, result)

    def test__refuel__with_right_fuel(self):
        example = Car('a', 'b', 1, 4)
        result = example.refuel(4)
        self.assertEqual(4, result)

    def test_refuel_proper_data_smaller_than_capacity(self):
        car = Car("a", "b", 1, 4)
        result = car.refuel(2)
        self.assertEqual(None, result)
        self.assertEqual(2, car.fuel_amount)

    def test__drive__if_not_enough_fuel(self):
        example = Car('a', 'b', 1, 4)
        with self.assertRaises(Exception) as ex:
            example.drive(1000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test__drive__with_enought_fuel(self):
        example = Car('a', 'b', 1, 4)
        example.refuel(4)
        example.drive(200)
        self.assertEqual(2, example.fuel_amount)


if __name__ == '__main__':
    unittest.main()