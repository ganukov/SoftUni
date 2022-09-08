from Object_oriented_programming.Inheritance.Multilple_Inheritance.person import Person
from Object_oriented_programming.Inheritance.Multilple_Inheritance.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'
