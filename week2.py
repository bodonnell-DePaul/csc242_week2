class Point:
    'A simple class representing a 2D point in space'

    def setx(self, value):
        "sets the x value"
        self.x = value
        pass

    def sety(self,value):
        'sets the y value'
        self.y = value

    def get(self):
        return (self.x, self.y)
    
    def move(self,x,y):
        self.x += x
        self.y +=y

    def __str__(self):
        return "({},{})".format(self.x, self.y)


    def __repr__(self):
        return "Point({},{})".format(self.x, self.y)

class Animal:
    'represents an animal'
    def setSpecies(self, species):
        'sets the animal species'
        self.spec = species
    def setLanguage(self, language):
        'sets the animal language'
        self.lang = language
    def speak(self):
        'prints a sentence by the animal'
        print('I am a {} and I {}.'.format(self.spec, self.lang))

        


p1 = Point()
p1.setx(10)
p1.sety(-25)
val = p1.get()
p1.move(y=1000,x=499)
print('This is my Point')
print(p1)
print(id(p1))
print(p1.x, p1.y)

p2 = Point()
p2.setx(-500)
p2.sety(1500)
val = p2.get()
p2.move(y=-15,x=900)
print('This is my Point')
print(p2)
print(id(p2))
print(p2.x, p2.y)

aList = [1,2,3]
print('This is my list')
print(aList)