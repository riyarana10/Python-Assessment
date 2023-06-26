# 

import pickle
import csv

def create_hospital_list():
    hospitals = []
    while True:
        hospital_name = input("Enter hospital name (or 'q' to quit): ")
        if hospital_name.lower() == 'q':
            break
        address = input("Enter hospital address: ")
        hospital = {'hospital_name': hospital_name, 'address': address}
        hospitals.append(hospital)
    return hospitals

def write_to_pickle(hospitals, filename):
    with open(filename, 'wb') as file:
        pickle.dump(hospitals, file)
    print("Data written to pickle file successfully.")

def read_from_pickle(filename):
    with open(filename, 'rb') as file:
        hospitals = pickle.load(file)
    return hospitals

def write_to_csv(hospitals, filename):
    fieldnames = ['hospital_name', 'address']
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(hospitals)
    print("Data written to CSV file successfully.")

# Create a list of hospitals
hospitals = create_hospital_list()

# Write the list to a pickle file
pickle_filename = 'hospitals.pickle'
write_to_pickle(hospitals, pickle_filename)

# Read the pickle file and write the data to a CSV file
hospitals_from_pickle = read_from_pickle(pickle_filename)
csv_filename = 'hospitals.csv'
write_to_csv(hospitals_from_pickle, csv_filename)