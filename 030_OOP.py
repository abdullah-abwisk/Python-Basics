# ''' Object Oriented Programming '''

# # make a class
# class Person:
#     # class attributes/properties
#     name = "John"
#     occupation = "Engineer"
#     age = 30
    
#     # class methods
#     def info(self):
#         return self.name + " is an " + self.occupation + " aged " + str(self.age)
    
# # create an object
# p1 = Person()
# print(p1.name) # John
# print(p1.occupation) # Engineer
# print(p1.age) # 30
# print(p1.info) # <bound method Person.info of <__main__.Person object at 0x0000021D3A3A3A90>>
# print(p1.info()) # John is an Engineer aged 30

# # class with constructor
# class Person:
#     def __init__(self, name, occupation, age):
#         self.name = name
#         self.occupation = occupation
#         self.age = age
        
#     def info(self):
#         return self.name + " is an " + self.occupation + " aged " + str(self.age)
    
# # create an object
# p1 = Person("John", "Engineer", 30)
# p2 = Person("Jane", "Doctor", 25)
# print(p1.info()) # John is an Engineer aged 30
# print(p2.info()) # Jane is an Doctor aged 25

# # create a class with decorator (getters and setters)
# class Person:
#     def __init__(self, name, age, occupation):
#         self._name = None
#         self._age = None
#         self._occupation = None

#         # Use setters to validate initial values
#         self.name = name
#         self.age = age
#         self.occupation = occupation

#     # Getter for name
#     @property
#     def name(self):
#         return self._name

#     # Setter for name with validation
#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str) or not value.strip():
#             raise ValueError("Name must be a non-empty string.")
#         self._name = value.strip()

#     # Getter for age
#     @property
#     def age(self):
#         return self._age

#     # Setter for age with validation
#     @age.setter
#     def age(self, value):
#         if not isinstance(value, int) or value < 0:
#             raise ValueError("Age must be a non-negative integer.")
#         self._age = value

#     # Getter for occupation
#     @property
#     def occupation(self):
#         return self._occupation

#     # Setter for occupation with validation
#     @occupation.setter
#     def occupation(self, value):
#         if not isinstance(value, str) or not value.strip():
#             raise ValueError("Occupation must be a non-empty string.")
#         self._occupation = value.strip()

# # Example usage
# try:
#     person = Person("John Doe", 30, "Software Engineer")
#     print(person.name)  # John Doe
#     print(person.age)   # 30
#     print(person.occupation)  # Software Engineer

#     person.age = 35
#     print(person.age)  # 35

#     # Invalid example (will raise ValueError)
#     person.age = -5
# except ValueError as e:
#     print(e)
    
    
# # Inheritance in Python
# class Person:   # Parent class
#     def __init__(self, name, age, occupation):
#         self.name = name
#         self.age = age
#         self.occupation = occupation

#     def info(self):
#         return self.name + " is an " + self.occupation + " aged " + str(self.age)

# class Employee(Person):  # Child class
#     def __init__(self, name, age, occupation, salary):
#         super().__init__(name, age, occupation)
#         self.salary = salary

#     def info(self): # Overriding the info method
#         return super().info() + " and earns " + str(self.salary) + " per month."
    
# # Example usage
# employee = Employee("John Doe", 30, "Software Engineer", 5000)
# print(employee.info())  # John Doe is an Software Engineer aged 30 and earns 5000 per month.


# Private members in Python
class Person:
    def __init__(self, name, age, occupation):
        self.__name = name # Private member
        self.__age = age # Private member
        self.__occupation = occupation # Private member

    def info(self):
        return self.__name + " is an " + self.__occupation + " aged " + str(self.__age)
    
# Example usage
person = Person("John Doe", 30, "Software Engineer")
# print(person.__name) # AttributeError: 'Person' object has no attribute '__name'
print(person._Person__name) # John Doe (Name mangling)
print(person.__dir__) # <built-in method __dir__ of Person object at 0x0000021D3A3A3A90>
print(person.__dir__()) # ['_Person__name', '_Person__age', '_Person__occupation', '__module__', '__init__', 'info', '__doc__', '__dict__', '__weakref__']


# Static methods in Python
class Math:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            return "Division by zero!"
        return x / y
    
# Example usage
print(Math.add(5, 3))  # 8
print(Math.subtract(5, 3))  # 2
print(Math.multiply(5, 3))  # 15
print(Math.divide(5, 3))  # 1.6666666666666667
print(Math.divide(5, 0))  # Division by zero!
# print(Math.divide(5))  # TypeError: divide() missing 1 required positional argument:
# print(Math.divide())  # TypeError: divide() missing 2 required positional arguments: 'x' and 'y'


# Instance vs Class variables
class Person:
    # Class variable
    count = 0

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
        Person.count += 1

    def info(self):
        return self.name + " is " + str(self.age) + " years old."
    
# Example usage
person1 = Person("John Doe", 30)
person2 = Person("Jane Doe", 25)
print(Person.count)  # 2
print(person1.count)  # 2
print(person2.count)  # 2
print(person1.info())  # John Doe is 30 years old.
print(person2.info())  # Jane Doe is 25 years old.
# print(person1.count = 10)  # SyntaxError: can't assign to function call


# class method
class Person:
    # Class variable
    count = 0

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
        Person.count += 1

    def info(self):
        return self.name + " is " + str(self.age) + " years old."

    @classmethod
    def get_count(cls):
        return cls.count
    
# Example usage
person1 = Person("John Doe", 30)
person2 = Person("Jane Doe", 25)
print(Person.get_count())  # 2
print(person1.get_count()) # 2
print(person2.get_count()) # 2
print(person1.info())  # John Doe is 30 years old.
print(person2.info())  # Jane Doe is 25 years old.
# print(person1.get_count = 10)  # SyntaxError: can't assign to function


# class method with constructor
class Person:
    # Class variable
    count = 0

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
        Person.count += 1

    def info(self):
        return self.name + " is " + str(self.age) + " years old."

    @classmethod
    def from_string(cls, string):
        name, age = string.split(",")
        return cls(name, int(age))
    
# Example usage
person1 = Person("John Doe", 30)
person2 = Person.from_string("Jane Doe,25")
print(Person.count)  # 2
print(person1.info())  # John Doe is 30 years old.


