class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname
    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)

class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rabbitId = Rabbit.tag
        Rabbit.tag += 1
    def get_rabbitId(self):
        return str(self.rabbitId).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        return Rabbit(0, self, other)
    def __eq__(self, other):
        parents_same = self.parent1.rabbitId == other.parent1.rabbitId and self.parent2.rabbitId == other.parent2.rabbitId
        parents_opposite = self.parent2.rabbitId == other.parent1.rabbitId and self.parent1.rabbitId == other.parent2.rabbitId
        return parents_same or parents_opposite
    def speak(self):
        print("meep")
    def __str__(self):
        return "rabbit:" + str(self.name) + ":" + str(self.age)

peter = Rabbit(5)
print(peter)
peter.speak()
peter.set_name('Peter')

hopsy = Rabbit(3)
hopsy.set_name('Hopsy')
cotton = Rabbit(1, peter, hopsy)
cotton.set_name('Cottontail')
print(cotton)
print(cotton.get_parent1())

mopsy = peter + hopsy
mopsy.set_name('Mopsy')
print(mopsy.get_parent1())
print(mopsy.get_parent2())
print(mopsy == cotton)

heter = hopsy + peter
heter.set_name('Heter')
print(heter == mopsy)
