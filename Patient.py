from Person import Person
import csv
import os
class Patient(Person):
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms = '', doctor = 'None'):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """
    


        #ToDo1
        # self.__first_name = first_name
        # self.__surname = surname
        self.__age = age
        self.__mobile = mobile 
        self.__postcode = postcode
        self.__symptoms = symptoms
        self.__doctor = doctor
        super().__init__(first_name, surname)
        
       
    
    # def full_name(self) :
    #     """full name is first_name and surname"""
    #     #ToDo2
    #     return f"{self.__first_name} {self.__surname}"


    def get_doctor(self) :
        #ToDo3
        return self.__doctor
    
    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor
        with open('patients.csv') as f_read, open('temp_data.csv', 'w', newline = '') as f_write:
            reader = list(csv.reader(f_read))
            writer = csv.writer(f_write)
            for data in reader:
                if self.full_name() == f'{data[0]} {data[1]}':
                     if len(data) < 6:
                         data.append('')
                     elif len(data) > 6:
                         data.pop(-1)
                     data.append(doctor)
                     writer.writerow(data)
                else:
                    writer.writerow(data)
        
    

        os.replace('temp_data.csv', 'patients.csv')
    
    def get_doc(self):
        return self.__doctor
            
    def print_symptoms(self):
        """prints all the symptoms"""
        #ToDo4
        # for symptom in self.__symptoms:
        #     print(symptom)
        new_symptoms = self.__symptoms.split(' ')
        for symptom in new_symptoms:
            print(symptom)
        

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'