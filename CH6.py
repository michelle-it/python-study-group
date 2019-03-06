'''6.1. Make a class called Thing with no contents and print it. 
Then, create an object called example from this class and also print it. 
Are the printed values the same or different? '''

class Thing():
    pass
print(Thing)

example = Thing()
print(example)

'''6.2. Make a new class called Thing2 and 
assign the value 'abc' to a class attribute called letters. 
Print letters.'''

class Thing2():
    letters = 'abc'

print('letters:',Thing2.letters)

'''6.3. Make yet another class called, of course, Thing3. 
This time, assign the value 'xyz' to an instance (object) attribute called letters. 
Print letters. Do you need to make an object from the class to do this?'''

class Thing3():
    def __init__(self, name):
        self.name = name

letters = Thing3('xyz')
print('letters:',letters.name)

'''6.4. Make a class called Element, 
with instance attributes name, symbol, and number. 
Create an object of this class with the values 'Hydrogen', 'H', and 1.'''

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

Hydrogen = Element('Hydrogen', 'H', 1)
print('name:',Hydrogen.name, ' symbol:',Hydrogen.symbol, ' number',Hydrogen.number)

'''6.5. Make a dictionary with these keys and values: 
'name': 'Hydrogen', 'symbol': 'H', 'number': 1
Then, create an object called hydrogen from class Element using this dictionary.'''

dictionary = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**dictionary)
print(hydrogen.name, hydrogen.symbol, hydrogen.number)

'''6.6. For the Element class, 
define a method called dump() 
that prints the values of the object’s attributes (name, symbol, and number). 
Create the hydrogen object from this new definition and use dump() 
to print its attributes.'''

class Elements:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print('name =',self.name, ' symbol=',self.symbol, ' number=',self.number)

hydrogen = Elements(**dictionary)
print(hydrogen.dump())

'''6.7. Call print(hydrogen). 
In the definition of Element, change the name of method dump to __str__, 
create a new hydrogen object, and call print(hydrogen) again.
'''

class element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return ('name=%s, symbol=%s, number=%s' %(self.name, self.symbol, self.number))

hydrogen = element(**dictionary)
print(hydrogen)

'''6.8. Modify Element to make the attributes name, symbol, and number private. 
Define a getter property for each to return its value.'''

class elements:
    def __init__(self, name, symbol, number):
        self._name = name
        self._symbol = symbol
        self._number = number
    @property
    def name(self):
        return self._name
    @property
    def symbol(self):
        return self._symbol
    @property
    def number(self):
        return self._number

hydrogen = elements('Hydrogen', 'H', 1)
print('name =',hydrogen.name, ' symbol=',hydrogen.symbol, ' number=',hydrogen.number)

'''6.9. Define three classes: Bear, Rabbit, and Octothorpe. 
For each, define only one method: eats(). 
This should return 'berries' (Bear), 'clover' (Rabbit), or 'campers' (Octothorpe). 
Create one object from each and print what it eats.'''

class Bear():
    def eats(self):
        return 'berries'
class Rabbit():
    def eats(self):
        return 'clover'
class Octothorpe():
    def eats(self):
        return 'campers'

Bear = Bear()
Rabbit = Rabbit()
Octothorpe = Octothorpe()

print('Bear:',Bear.eats(), ' Rabbit:',Rabbit.eats(), ' Octothorpez:',Octothorpe.eats())

'''6.10. Define these classes: 
Laser, Claw, and SmartPhone. 
Each has only one method: does(). 
This returns 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (Smart Phone). 
Then, define the class Robot that has one instance (object) of each of these. 
Define a does() method for the Robot that prints what its component objects do.'''

class Laser():
    def does(self):
        return 'disintegrate'
class Claw():
    def does(self):
        return 'crush'
class Smart＿Phone():
    def does(self):
        return 'ring'

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smart_phone = Smart＿Phone()
    def does(self):
        return ('Laser = %s, Claw = %s, Smart＿Phone = %s' %(self.laser.does(), self.claw.does(), self.smart_phone.does()))

Robot = Robot()
print(Robot.does())