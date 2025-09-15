'''class Example:
    def __init__(self):
        self.name = "Vivek"
obj = Example()
print(obj.name)'''
'''class Example:
    def __init__(self):
        self._age = 19
obj = Example()
print(obj._age)
class Example:
    def __init__(self):
        self.__salary = 50000
obj = Example()
print(obj._Example__salary)'''
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        self.__salary = salary

obj = Employee("Rahul",10000)
print(obj.get_name())
print(obj.get_salary())
print(obj.set_name("Vivek"))
print(obj.set_salary(12000))