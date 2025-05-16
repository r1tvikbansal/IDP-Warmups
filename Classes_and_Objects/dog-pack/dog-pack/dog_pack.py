# Write your solution here!
class DogPack:
    def __init__(self):
        self._dogs = []
        
    def add_dog(self, dog):
        DogPack._dogs.append(dog)
    
    def all_bark(self):
        for dog in DogPack._dogs:
            dog.bark()