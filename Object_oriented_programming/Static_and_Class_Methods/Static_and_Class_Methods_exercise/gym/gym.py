from Object_oriented_programming.Static_and_Class_Methods.Static_and_Class_Methods_exercise.gym.equipment import Equipment
from Object_oriented_programming.Static_and_Class_Methods.Static_and_Class_Methods_exercise.gym.customer import Customer
from Object_oriented_programming.Static_and_Class_Methods.Static_and_Class_Methods_exercise.gym.trainer import Trainer
from Object_oriented_programming.Static_and_Class_Methods.Static_and_Class_Methods_exercise.gym.subscription import Subscription
from Object_oriented_programming.Static_and_Class_Methods.Static_and_Class_Methods_exercise.gym.exercise_plan import ExercisePlan


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def __find_by_id(self, entities, entity_id):
        for entity in entities:
            if entity.id == entity_id:
                return entity

    def subscription_info(self, subscription_id: int):
        subscription = self.__find_by_id(self.subscriptions,subscription_id)
        customer = self.__find_by_id(self.customers,subscription_id)
        trainer = self.__find_by_id(self.trainers,subscription_id)
        plan = self.__find_by_id(self.plans,subscription_id)
        equipment = self.__find_by_id(self.equipment,subscription_id)

        return f'{subscription}\n' \
               f'{customer}\n' \
               f'{trainer}\n' \
               f'{equipment}\n' \
               f'{plan}'
