from Object_oriented_programming.Static_and_Class_Methods.Static_and_Class_Methods_exercise.movie_world.dvd import DVD
from Object_oriented_programming.Static_and_Class_Methods.Static_and_Class_Methods_exercise.movie_world.customer import Customer


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            for dvd in self.dvds:
                if customer_id == customer.id and customer.age < dvd.age_restriction and dvd.is_rented == False:
                    return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
                elif customer_id == customer.id and customer.age >= dvd.age_restriction and dvd.is_rented == False:
                    customer.rented_dvds.append(dvd)
                    dvd.is_rented = True
                    return f"{customer.name} has successfully rented {dvd.name}"
                elif customer.id == customer_id and dvd.is_rented == True and dvd not in customer.rented_dvds:
                    return "DVD is already rented"
            for x in customer.rented_dvds:
                if x.id == dvd_id:
                    return f"{customer.name} has already rented {x.name}"

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            for dvd in customer.rented_dvds:
                if customer.id == customer_id:
                    if dvd_id == dvd.id:
                        customer.rented_dvds.remove(dvd)
                        dvd.is_rented = False
                        return f"{customer.name} has successfully returned {dvd.name}"
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        new_line = '\n'
        return f'{new_line.join([str(customer) for customer in self.customers])}\n{new_line.join([str(dvd) for dvd in self.dvds])}'
