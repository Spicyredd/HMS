# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
import csv
import os

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    # admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    # doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    # patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
    admin = ''
    with open('admin.csv') as f:
        data = csv.reader(f)
        for i in data:
            admin = Admin(i[0],i[1],i[2])
    
    doctors = []
    
    if os.path.exists('doctors.csv'):
        with open('doctors.csv') as f:
            doctor_data = csv.reader(f)
            for doctor in doctor_data:
                temp_data = Doctor(*admin.get_details(doctor))
                doctors.append(temp_data)
    
    else:
        with open('doctors.csv', 'w'):
            pass
    
    patients = []

    if os.path.exists('patients.csv'):
        with open('patients.csv') as f:
            patient_data = csv.reader(f)
            for patient in patient_data:
                temp_data = Patient(*admin.get_details(patient))
                patients.append(temp_data)

    else:
        with open('patients.csv', 'w') as f:
            pass
    discharged_patients = []
    if os.path.exists('discharged_patients.csv'):
        with open('discharged_patients.csv') as f:
            patient_data = csv.reader(f)
            for patient in patient_data:
                temp_data = Patient(*admin.get_details(patient))
                discharged_patients.append(temp_data)
                
    else:
        with open('discharged_patients.csv', 'w') as f:
            csv.writer(f)

    if os.path.exists('appointments.csv') == False:
        with open('appointments.csv', 'w'):
            pass
    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin detais')
        print(' 6- Add patient')
        print(' 7- Show patients family')
        print(' 8- Management Report')
        print(' 9- View Patients')   
        print(' 10- Quit')
        
        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
         #ToDo1
          admin.doctor_management(doctors)

        elif op == '2':
            # 2- View or discharge patients
            #ToDo2
            admin.view_patient(patients)

            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    #ToDo3
                    admin.discharge(patients, discharged_patients)

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')

        elif op == '3':
            # 3 - view discharged patients
            #ToDo4
            admin.view_discharge(discharged_patients)

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin detais
            admin.update_details()
            
        elif op == '6':
            # 6- add patients
            admin.add_patient(patients)
            
        elif op == '7':
            # 7- show patients family
            admin.patient_family(patients)
            
        elif op == '8':
            # 8- Management Report
            admin.mgmt_report(patients, doctors)
        
        elif op == '9':
            admin.view_patient(patients)   
           
        elif op == '10':
            # 9- Quit
            #ToDo5
            break
        
        
        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()