from pymongo import MongoClient    #importing pymango

connection = MongoClient(host="localhost", port=27017)  #establishing the conection to the mangodb

data_base = connection.Demo_project     #  conecting to Demo project(database)
collection = data_base.Staff_details    # connecting staff details collection in demo project(database)
collection1 = data_base.Deleted_data    # connecting Deleted_data collection in demo project(database)

def function3():      # using fuction to the delete and insert operation
    name = input('enter the staff name which you want to delete')   #input providing to the user for which one they want to delete
    read_data = collection.find({'Name': name})  # first read the data which is given by the user
    for i in read_data:        # using for loop for reading the data
        inserting = collection1.insert_one(i)  # before the deleting data it will be storing in the other collection
        deleted_data =collection.delete_one(i) # deleting the data given by the user
        print(inserting ,deleted_data)
