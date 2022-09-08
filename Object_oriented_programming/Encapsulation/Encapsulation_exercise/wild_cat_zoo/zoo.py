from Object_oriented_programming.Encapsulation.Encapsulation_exercise.wild_cat_zoo.animal import Animal
from Object_oriented_programming.Encapsulation.Encapsulation_exercise.wild_cat_zoo.worker import Worker
from Object_oriented_programming.Encapsulation.Encapsulation_exercise.wild_cat_zoo.tiger import Tiger
from Object_oriented_programming.Encapsulation.Encapsulation_exercise.wild_cat_zoo.lion import Lion
from Object_oriented_programming.Encapsulation.Encapsulation_exercise.wild_cat_zoo.cheetah import Cheetah
from Object_oriented_programming.Encapsulation.Encapsulation_exercise.wild_cat_zoo.keeper import Keeper
from Object_oriented_programming.Encapsulation.Encapsulation_exercise.wild_cat_zoo.caretaker import Caretaker
from Object_oriented_programming.Encapsulation.Encapsulation_exercise.wild_cat_zoo.vet import Vet

class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget < price:
            return 'Not enough budget'
        if len(self.animals) == self.__animal_capacity:
            return 'Not enough space for animal'

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return 'Not enough space for worker'
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        all_salary = sum(w.salary for w in self.workers)
        if all_salary <= self.__budget:
            self.__budget -= all_salary
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        all_care = sum(t.money_for_care for t in self.animals)
        if all_care <= self.__budget:
            self.__budget -= all_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals\n'
        lions = [repr(x) for x in self.animals if isinstance(x,Lion)]
        tigers = [repr(x) for x in self.animals if isinstance(x,Tiger)]
        cheetahs = [repr(x) for x in self.animals if isinstance(x,Cheetah)]
        result += f'----- {len(lions)} Lions:\n' + '\n'.join(lions) + '\n'
        result += f'----- {len(tigers)} Tigers:\n' + '\n'.join(tigers) + '\n'
        result += f'----- {len(cheetahs)} Cheetahs:\n' + '\n'.join(cheetahs)
        return result

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'
        keepers = [repr(x) for x in self.workers if isinstance(x, Keeper)]
        caretakers = [repr(x) for x in self.workers if isinstance(x, Caretaker)]
        vets = [repr(x) for x in self.workers if isinstance(x, Vet)]
        result += f'----- {len(keepers)} Keepers:\n' + '\n'.join(keepers) + '\n'
        result += f'----- {len(caretakers)} Caretakers:\n' + '\n'.join(caretakers) + '\n'
        result += f'----- {len(vets)} Vets:\n' + '\n'.join(vets)
        return result
