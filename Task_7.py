class Person:

  def __init__(self, name, age): #creating the instance of an Object
    self.name = name
    self.age = age

p1 = Person("John", 36) #Creating the Object
p2 = Person("Daniel", 25)

print(p1.name, "is" , p1.age, "Years old")
print(p2.name, "is", p2.age, "years old")
