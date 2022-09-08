from Object_oriented_programming.Static_and_Class_Methods.hotel_rooms.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number and room.is_taken == False and room.capacity >= people > 0:
                self.guests += people
                room.is_taken = True

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number and room.is_taken == True:
                room.is_taken = False

    def status(self):
        return f'Hotel {self.name} has {self.guests} total guests\n' \
               f'Free rooms: {", ".join([str(x.number) for x in self.rooms if x.is_taken == False])}\n' \
               f'Taken rooms: {", ".join([str(x.number) for x in self.rooms if x.is_taken == True])}'
