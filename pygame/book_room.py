class Guest:
    def __init__(self,name,age,rooms):
        self.name = name
        self.age = age
        self.rooms = rooms

class Hotel:
    def __init__(self):
        self.rooms = {}
        
        
    def is_free(self,room_number):
        if room_number in self.rooms.keys():
            return False
        return True
        


    def book_room(self,guest,rooms, room_number):
        if self.is_free(room_number) == True:
            rooms.ke(room_number)
        else:
            print("комната занята ")
    
    def free_room(self,rooms, room_number):
        if self.is_free(room_number) == False:
            rooms.discard(room_number)
        else:
            print("комната итак свободна")

    def list_booked_rooms(rooms):
        for room in rooms:
            print(f"Room {room} is booked.")