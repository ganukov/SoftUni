from Object_oriented_programming.Static_and_Class_Methods.Static_and_Class_Methods_exercise.movie_world.customer import Customer

from Object_oriented_programming.Static_and_Class_Methods.Static_and_Class_Methods_exercise.movie_world.dvd import DVD

from Object_oriented_programming.Static_and_Class_Methods.Static_and_Class_Methods_exercise.movie_world.movie_world import MovieWorld

movie_world = MovieWorld("Test")
d = DVD("A", 1, 1254, "February", 10)
c = Customer("Pesho", 20, 4)
c2 = Customer("Gosho", 26, 2)
movie_world.add_customer(c)
movie_world.add_customer(c2)
movie_world.add_dvd(d)
movie_world.rent_dvd(4, 1)
print(movie_world.rent_dvd(2, 1))