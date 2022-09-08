from unittest import TestCase, main
from testing_exam.vehicle.project.vehicle import Vehicle


class TestVehicle(TestCase):
    FUEL = 100
    HORSE_POWER = 120
    FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test__if_constructor__works__properly(self):
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.FUEL_CONSUMPTION, self.vehicle.fuel_consumption)
        self.assertEqual(self.FUEL, self.vehicle.capacity)

    def test__drive__with_wrong_kilometers__expect_exep(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(200)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test__drive__with_right_kilometers__expect__fuel_to_decrease(self):
        self.vehicle.drive(50)
        self.FUEL -= 50 * 1.25
        self.assertEqual(self.FUEL, self.vehicle.fuel)

    def test__refuel__with_wrong_data__expect__exep(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(50)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test__refuel__with_proper_data__expect__fuel_to_raise(self):
        self.vehicle.fuel -= 1
        self.vehicle.refuel(1)
        self.assertEqual(100, self.vehicle.fuel)

    def test__str__expect__proper_str(self):
        result = f"The vehicle has {self.vehicle.horse_power} " \
                 f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        actual = f"The vehicle has {self.HORSE_POWER} " \
                 f"horse power with {self.FUEL} fuel left and {self.FUEL_CONSUMPTION} fuel consumption"

        self.assertEqual(actual, result)

    if __name__ == "__main__":
        main()
