#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   IMPORT MODULE
# annotations enables you to use the class Person as a data type inside the class itself
from __future__ import annotations

class Person:
    """
    This class stores information about a person
    
    Methods
    -------
    __init__(self, name, surname, age)
    getAge()
    getFullName()
    setSurname(surname)
    greet(other)
    """
    
    def __init__(self, name: str, surname: str, age: int):
        """
        Create an instance of the Person class

        Parameters
        ----------
        name : str
            Name of the person.
        surname : str
            Surname of the person.
        age : int
            The persons age.
        """
        # Save the parameters of the methods as attributes of the class
        self.name = str(name).strip()
        self.surname = str(surname).strip()
        self.age = int(age)
        
    def getAge(self) -> int:
        """
        Return the age of a person.

        Returns
        -------
        age : int
            The age of the person.
        """
        return self.age
    
    def getFullName(self) -> str:
        """
        Return the full name of a person.

        Returns
        -------
        str
            The full name of the person.

        """
        return " ".join([self.name, self.surname])
    
    def setSurname(self, new_surname: str):
        """
        Change the surname of a person.

        Parameters
        ----------
        new_surname : str
            The new surname of the person.
        """
        self.surname = str(new_surname).strip()
        
    def greetYou(self, other: Person):
        """
        Greet another person.

        Parameters
        ----------
        other : Person
            An instance of the Person class.
        """
        print(f"Hi, {other.getFullName()}! My name is {self.getFullName()}.")

if __name__ == "__main__":
    # Create instances of the class
    person1 = Person("Marie", "Mustermann", 22)
    person2 = Person("Max", "Mustermann", 20)

    # Show some properties of the class
    print(f"Call method: {person1.getFullName()}")
    person1.setSurname("Müller")
    person2.greetYou(person1)
    print(f"It is possible to access attributes: {person2.name}")