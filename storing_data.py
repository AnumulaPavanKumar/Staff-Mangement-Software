from pymongo import MongoClient   # Impoting the pymongo
import pandas as pd               #impoting the pandas
def function():      # using the fuction to enter the data into the database
    connection = MongoClient(host="localhost", port=27017)

    data_base = connection.Demo_project    #  conecting to Demo project(database)
    collection = data_base.Staff_details   # connecting staff details(collection) in demo project(database)

    No_of_staff = int(input('enter the staff numbers: '))   # input providing to the user to enter the number of staff to enter the data

    for i in range(0, No_of_staff):  # using for loop to set a range using No_of_staff
        read_data = collection.find()  # read the collection to know the How many records stored in the collection
        df = pd.DataFrame(read_data)# the read_data is converted into the dataframe
        a = len(df.index)    # to calculate the no of records stored in the collection
        if a < 50:
            Name = input("Enter the  Full Name of the staff member " + str(i + 1))  # input providing to the user to enter the name of the staff
            Age = input("Enter the Age of the staff member " + str(i + 1))         # input providing to the user to enter the Age of the staff
            Gender = input("Enter the Gender of the staff member " + str(i + 1))   # input providing to the user to enter the Gender of the staff
            Address = input("Enter the Address of the staff member " + str(i + 1))  # input providing to the user to enter the Address of the staff
            Designation = input("Enter the Designation of the staff member " + str(i + 1))   # input providing to the user to enter the Designation of the staff
            Date_of_joining = input("Enter the Date_of_joining of the staff member " + str(i + 1))   # input providing to the user to enter the Date_of_joining of the staff
            Salary = (input("Enter the Salary of the staff member " + str(i + 1)))     # input providing to the user to enter the Salary of the staff
            Date_of_birth = (input("Enter the Date_of_birth of the staff member " + str(i + 1)))   # input providing to the user to enter the Date_of_birth of the staff
            Previous_job_history = input("Enter the Previous_job_history of the staff member " + str(i + 1))   # input providing to the user to enter the Previous_job_history of the staff

            data = {
                "Name": Name,
                "Age": Age,
                "Gender": Gender,
                "Address": Address,
                "Designation": Designation,
                "Date_of_joining": Date_of_joining,
                "Salary": Salary,
                "Date_of_birth": Date_of_birth,
                "Previous_job_history": Previous_job_history
            }                                                     # converted the above values into the dictionary using of key and value
            inserting_data = collection.insert_one(data)          # inserting the above given data is stored into the collection
            print(inserting_data)


    else:         # using else condition to print when the limit of the collection is exceeded
        print('you are not allowed to add the data because the you are exceeded the limit')
