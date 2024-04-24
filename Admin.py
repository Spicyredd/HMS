from Doctor import Doctor
from Patient import Patient
import os
import csv
import datetime

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address
        self.__details = []
        self.__op = ''

    def get_address(self):
        return self.__address
    
    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')
        
        # check if the username and password match the registered ones
        #ToDo1
        
        
        if self.__username == username and self.__password == password:
            return self.__username
        

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        first_name = input("Enter the first name: ")        
        surname_name = input("Enter the surname name: ")        
        speciality = input("Enter the speciality: ")   
        
        return first_name,surname_name,speciality
        
    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """
        self.__doctors = doctors
            
        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3
        op  = input("Input:")
                
        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            #ToDo4
            new_doctor = self.get_doctor_details()
            first_name = new_doctor[0]
            surname = new_doctor[1]
            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    #ToDo5
                    break
                    # save time and end the loop
            else:
            #ToDo6
                doctors.append(Doctor(new_doctor[0], new_doctor[1], new_doctor[2]))# add the doctor ...
                with open('doctors.csv', 'a', newline='') as f:                           # ... to the list of doctors
                    writer = csv.writer(f)
                    writer.writerow(new_doctor)
                print('Doctor registered.')
            self.__op = ''

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7
            print('ID |          Full name           |  Speciality')
            for ID,i in enumerate(doctors):
                print(f'{ID+1:3}|{i.__str__()}')
            
            self.__op = ''
            
                    

        # Update
        elif op == '3':
            self.__op = ''
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                
                        break
                        
                    else:
                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')
            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = input('Input: ') # make the user input lowercase
            count = 0
            temp_list = []

            #ToDo8
            temp_obj = doctors[index]
            if op == "1":
                new_first_name = input("Enter the new first name: ")
                temp_obj.set_first_name(new_first_name)
                if os.path.exists('doctors.csv'):
                    with open('doctors.csv') as f, open('temp_data.csv', 'w', newline = '') as w:
                        reader = csv.reader(f)
                        writer = csv.writer(w)
                        for doc in reader:
                            if index != count:
                                writer.writerow(doc)
                            else:
                                  temp_list.append(new_first_name)
                                  temp_list.append(doc[1])
                                  temp_list.append(doc[2])
                                  writer.writerow(temp_list)
                            count += 1
                else:
                    with open('doctors.csv', 'w') as f:
                        pass
                os.replace('temp_data.csv', 'doctors.csv')
                            

            if op == "2":
                new_surname = input("Enter the new surname: ")
                temp_obj.set_surname(new_surname)
                if os.path.exists('doctors.csv'):
                    with open('doctors.csv') as f, open('temp_data.csv', 'w', newline = '') as w:
                        reader = csv.reader(f)
                        writer = csv.writer(w)
                        for doc in reader:
                            if index != count:
                                writer.writerow(doc)
                            else:
                                  temp_list.append(doc[0])
                                  temp_list.append(new_surname)
                                  temp_list.append(doc[2])
                                  writer.writerow(temp_list)
                            count += 1
                    os.replace('temp_data.csv', 'doctors.csv')
                
                else:
                    with open('doctors.csv', 'w') as f:
                        pass
                
            if op == "3":
                new_speciality = input("Enter the new speciality name: ")
                temp_obj.set_speciality(new_speciality)
                if os.path.exists('doctors.csv'):
                    with open('doctors.csv') as f, open('temp_data.csv', 'w', newline = '') as w:
                        reader = csv.reader(f)
                        writer = csv.writer(w)
                        for doc in reader:
                            if index != count:
                                writer.writerow(doc)
                            else:
                                  temp_list.append(doc[0])
                                  temp_list.append(doc[1])
                                  temp_list.append(new_speciality)
                                  writer.writerow(temp_list)
                            count += 1
                    os.replace('temp_data.csv', 'doctors.csv')
                            
                else:
                    with open('doctors.csv', 'w') as f:
                        pass

        # Delete
        elif op == '4':
            self.__op = ''
            try:
                #ToDo9
                print("-----Delete Doctor-----")
                print('ID |          Full Name           |  Speciality')
                self.view(doctors)
                doctor_index = int(input('Enter the ID of the doctor to be deleted: '))
                if len(doctors) < doctor_index:
                    print('The id entered is incorrect')
                else:
                    doctors.pop(doctor_index - 1)
                    count = 0
                    if os.path.exists('doctors.csv'):
                        with open('doctors.csv') as f, open('temp_data.csv', 'w', newline = '') as w:
                            reader = csv.reader(f)
                            writer = csv.writer(w)
                            for doc in reader:
                                if doctor_index - 1 != count:
                                    writer.writerow(doc)
                                count += 1
                    else:
                        with open('doctors.csv', 'w') as f:
                            pass
                        
                    os.replace('temp_data.csv', 'doctors.csv')

                    print('Doctor deleted')
                    
            except ValueError:
                print('Please enter numbers only.')
            # except:
            #     print('Please enter valid ID.')
            except Exception as e:
                print(e)
        
        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')
    
    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo10
        for ID,patient in enumerate(patients):
            print(f'{ID+1:^3}|{patient.__str__()}')

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                temp_pat = patients[patient_index]
                temp_doc = doctors[doctor_index]          
                temp_pat.link(temp_doc.full_name())
                temp_doc.add_patient(temp_pat.full_name())
                temp_doc.set_appointments(temp_pat.full_name())
                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        #ToDo12
        print("-----Discharge Patient-----")
        try:
            patient_index = int(input('Please enter the patient ID: ')) - 1
            # discharge_patients.append(patients[patient_index])
            # patients.pop(patient_index)
            discharge_patients.append(patients[patient_index])
            patients.pop(patient_index)
            with open('patients.csv') as p_read, open('temp_data.csv', 'w', newline = '') as p_write:
                reader = csv.reader(p_read)
                writer = csv.writer(p_write)
                for index, data in enumerate(reader):
                    if index != patient_index:
                        writer.writerow(data)
                    else:
                        if os.path.exists('discharged_patients.csv'):
                            with open('discharged_patients.csv', 'a', newline = '') as f:
                                csv.writer(f).writerow(data)
                        else:
                            with open('discharged_patients.csv', 'w', newline = '') as f:
                                csv.writer(f).writerow(data)
                            
            os.replace('temp_data.csv', 'patients.csv')
        except ValueError:
            print('Please enter numbers only.')
        except IndexError:
            print('ID does not exist.')
        except:
            print('Please enter valid ID.')
            
    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo13
        for ID,patient in enumerate(discharged_patients):
            print(f'{ID+1:^3}|{patient.__str__()}')

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = input('Input: ')

        temp_lst = []
        if op == "1":
            #ToDo14
            new_username = input('Enter the new username: ')
            self.__username = new_username
            with open('admin.csv') as f:
                data = csv.reader(f)
                count = 1
                for datum in data:
                    for dat in datum:
                        if count != 1:
                            temp_lst.append(dat)
                        else:
                            temp_lst.append(new_username)
                        count += 1
            with open('temp.csv','w', newline = '') as j:
                writer = csv.writer(j)
                writer.writerow(temp_lst)
            os.replace('temp.csv', 'admin.csv')

        elif op == "2":
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password
                
            with open('admin.csv') as f:
                data = csv.reader(f)
                count = 1
                for datum in data:
                    for dat in datum:
                        if count != 2:
                            temp_lst.append(dat)
                        else:
                            temp_lst.append(new_username)
                        count += 1
                        
            with open('temp.csv','w', newline = '') as j:
                writer = csv.writer(j)
                writer.writerow(temp_lst)
            os.replace('temp.csv', 'admin.csv')

        elif op == "3":
            #ToDo15
            new_address = input('Enter the new address: ')
            self.__address = new_address
            
            with open('admin.csv') as f:
                data = csv.reader(f)
                count = 1
                for datum in data:
                    for dat in datum:
                        if count != 3:
                            temp_lst.append(dat)
                        else:
                            temp_lst.append(new_username)
                        count += 1
                        
            with open('temp.csv','w', newline = '') as j:
                writer = csv.writer(j)
                writer.writerow(temp_lst)
            os.replace('temp.csv', 'admin.csv')

        else:
            #ToDo16
            print('Invalid Option choose again.')
            return self.update_details()
        
    def add_patient(self, patients):
            patient = []
            symptoms = ''
            print('----Add patient----')
            fn = input('Enter the first name: ')
            patient.append(fn)
            ln = input('Enter the last name: ')
            patient.append(ln)
            age = input('Enter the age: ')
            patient.append(age)
            mobile = input('Enter the phone: ')
            patient.append(mobile)
            postcode = input('Enter the postcode: ')
            patient.append(postcode)
            
            
            while True:
                var_symptoms = input('Enter the symptoms: ')
                user_flag = input('Do you want to add more symptoms?(Y/N) ')
                symptoms = symptoms + f'{var_symptoms} '
                if user_flag[0].lower() != 'y':
                    break
            patient.append(symptoms)
            patient.append('5')
            
            try:
                with open('patients.csv', 'a',newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(patient)
            except FileExistsError:
                with open('patients.csv', 'w', newline= '') as f:
                    writer = csv.writer(f)
                    writer.writerow(fn,ln,age,mobile,postcode, symptoms)
            patients.append(Patient(fn, ln, age, mobile, postcode, symptoms))
        
    def get_details(self, data):
        return data[:7]
    
    def patient_family(self, patients):
        patients_dict = {}
        for patient in patients:
            if patient.full_name().split(' ')[1] in patients_dict:
                patients_dict[patient.full_name().split(' ')[1]].append(patient)
            else:
                patients_dict[patient.full_name().split(' ')[1]] = [patient] 
        
        print(f'|{'Family Name':15}|{'Patient':15}')
        for family in patients_dict:
            for patient in patients_dict[family]:
                print(f'|{family:15}|{patient.full_name():15}|')
            
    def mgmt_report(self, patients, doctors):
        print('----- Management Report -----')
        print('Choose the report to be made.')
        print('1- Total no. of doctors.')
        print('2- No. of patients per doctor.')
        print('3- Total no. of appointments per month per doctor.')
        print('4- No. of patients based on illness types.')
        option = input('Option: ')
        
        if option == '1':
            print(f'The total number of doctors in the system: {len(doctors)}')
            doc_num = {'Doctor': {len(doctors)}}
        
        elif option == '2':
            doc = [x.get_doc() for x in patients if x.get_doc() != 'None']
            doc_uni = list(set(doc))
            doc_uni_dict = dict.fromkeys(doc_uni)
            
            print('----- Total no. of patients per doctor -----')
                        
            for i in doc_uni:
                doc_uni_dict[i] = doc.count(i)
            
            for num in doc_uni_dict:
                print(f'{num:20}|{doc_uni_dict[num]:3}')
                
        elif option == '3':
            print('----- Total no. of appointments per month per doctor -----')
            doc_name = []
            doc_appoint = {}
            with open('appointments.csv') as f:
                reader = csv.reader(f)
                for i in reader:
                    tdate = i[0].split('-')
                    if datetime.date.today() - datetime.timedelta(days = 30) <= datetime.date(int(tdate[0]), int(tdate[1]), int(tdate[2])):
                        doc_name.append(i[1])
                            
                doc_uni_name = set(doc_name)
                for i in doc_uni_name:
                    print(f'{i:20}|{doc_name.count(i):3}')
                    doc_appoint[i] = doc_name.count(i)
                    
                    
        elif option == '4':
            with open('patients.csv') as f:
                reader = csv.reader(f)
                patient_illness = [x[5] for x in reader if x[5] != '']
                illnese_data = {}
                patient_illness_unique = set(patient_illness)
                
                print('----- Total number of patients based on illness type -----')
                
                for illness in patient_illness_unique:
                    print(f'{illness:20}|{patient_illness.count(illness):3}')
                    illnese_data[illness] = patient_illness.count(illness)

        else:
            print('Invalid Option.')