person = {'name' : 'Vignesh', 'age' : 21} #creating dictionary with key and values
print(person['name'])
print(person['age'])
person['age'] = 22 #changing the key age value
print(person)
person['location'] = 'Trichy' #updating new key to an existing dictionary
print(person)

class person:

    def __init__(self, name):
        self.name = name

     def say_hi(self):
        print('hello,My name ', self.name)

    def ask(self):
        print('what is your profession? ', self.name)

p = person("nikhil")
p.say_hi()
p.ask()