#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import the Person class from previous example 2
from example_02_object_person import Person

class Student(Person):
    """
    This class inherites from class Person and does stuff.
    """
    
    def __init__(self, name: str, surname: str, age: int, major: str):
        """
        Initialise class

        Parameters
        ----------
        name : str
            Name of the person.
        surname : str
            Surname of the person.
        age : int
            The persons age.
        major : str
            The students major.

        Returns
        -------
        Instance of the class Student.

        """
        # Call the constructor of the base class
        Person.__init__(self, name, surname, age)
        # Save the parameter as attribute
        self.major = str(major).strip()

    def getFullName(self):
        """
        Return the full name and major of the student.

        Returns
        -------
        str
            The full name and major of the student.

        """
        return f"{self.name} {self.surname} ({self.major})"
    
    
if __name__ == "__main__":
    # Create instances of the new class
    student1 = Student("Marie", "Müller", 22, "Mathematics")
    student2 = Student("Max", "Mustermann", 20, "Engineering")
    
    # Show properties of the inherited class
    print(student2.getFullName())
    student2.setSurname("Schmidt")
    student2.greetYou(student1)
    student1.greetYou(Person("Herbert", "Schmidt", 21))
