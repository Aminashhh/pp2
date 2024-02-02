#1 example
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
#2 example
class Student(Person):
  pass
#3 example
x = Student("Mike", "Olsen")
x.printname()
#4 example
 #class Student(Person):
   #def __init__(self, fname, lname):
    #add properties etc.
#5 example
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
#6 example
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
#7 example
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
#8 example
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
#9 example
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

