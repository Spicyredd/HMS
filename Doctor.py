from Person import Person
from datetime import date
import os
import csv

class Doctor(Person):
    """A class that deals with the Doctor operations"""

    def __init__(self, first_name, surname, speciality):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """
        self.__first_name = first_name
        self.__surname = surname
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []
        super().__init__(first_name, surname)
    
    # def full_name(self) :
    #     #ToDo1
    #     return f"{self.__first_name} {self.__surname}"
    
    def get_first_name(self) :
        #ToDo2
        return self.__first_name

    # def set_first_name(self, new_first_name):
    #     #ToDo3
    #     self.__first_name = new_first_name

    def get_surname(self) :
        #ToDo4
        return self.__surname

    # def set_surname(self, new_surname):
    #     #ToDo5
    #     self.__surname = new_surname

    def get_speciality(self) :
        #ToDo6
        return self.__speciality

    def set_speciality(self, new_speciality):
        #ToDo7
        self.__speciality = new_speciality

    def add_patient(self, patient):
        self.__patients.append(patient)

    def get_patients(self):
        return self.__patients
    
    def set_appointments(self, appoint):
        self.__appointments.append(date.today())
        self.__appointments.append(self.full_name())
        self.__appointments.append(appoint)
        if os.path.exists('appointments.csv'):
            with open('appointments.csv', 'a', newline = '') as f:
                writer = csv.writer(f)
                writer.writerow(self.__appointments)
        else:
            with open('appointments.csv', 'w', newline = '') as f:
                writer = csv.writer(f)
                writer.writerow(self.__appointments)
                
    def __str__(self) :
        return f'{self.full_name():^30}|{self.__speciality:^15}'
    
