class Employee:

    bonus = 0.5
    
    def __init__(self, name, age, gender, salary):
        self.name = name
        self.gender = gender
        self.age = int(age)
        self.salary = salary

    def getSalary(self):
        return int(self.salary + (Employee.bonus * self.salary))

    def showStatus(self):
        print("Nama\t\t:", self.name)
        print("Umur\t\t:", self.age)
        print("Jenis kelamin   :", self.gender)
        print("Gaji\t\t:", self.getSalary())


class Rectangle:
    def __init__ (self, length, width):
        self.length = length
        self.width = width

    def getArea(self):
        return int(self.length * self.width)


class Strings:
    def getString(self, str):
        self.str = str

    def printString(self):
        return self.str.upper()


if __name__ == "__main__":
    
    # Employee
    print("Kelas Employee")
    emp1 = Employee("Emp1", 18, "Male", 600)
    emp1.showStatus()
    print()

    # Rectangle
    print("Kelas Rectangle")
    rec = Rectangle(100, 20)
    print(rec.getArea())
    print()

    # Strings
    print("Kelas Strings")
    str = Strings()
    str.getString(input("=> "))
    print(str.printString())
    print()
    