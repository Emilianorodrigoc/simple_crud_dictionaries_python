import dictionaries

# Function that executes the initial system message
def start_message():
    print("\n") #Add line breaks
    print("*" * 51)
    title_one = "Welcome to Cinema" 
    title_two = "Good Movies"
    print("*",(title_one.upper().center(47, " ")),"*")
    print ("*",(title_two.upper().center(47, " ")),"*")
    print("*" * 51, "\n")

# Function that runs the options menu
def query_message():
    print("*","Admin Section".upper().center(46),"*")
    print("-"*50)
    print("What do you want to do?:")
    print("1. Consult")
    print("2. Create")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")
    entry_data = str(input("Answer: "))
    return entry_data # We return the entered value, as a string to use it in the system
   

    
# Function that queries records
def consult (data_query):
    if data_query in dictionaries.register.keys():
        # Show the consulted values on the screen
        print('\n')
        print("*"*50)
        print(f"Data found for DNI {data_query}:")
        print(f"Name: {dictionaries.register[data_query][0]}")
        print(f"Adress: {dictionaries.register[data_query][1]}")
        print(f"Age: {dictionaries.register[data_query][2]}")
        print(f"City: {dictionaries.register[data_query][3]}")
        print("-"*50)
        print("\n")
    else:
        print("The registered ID is not found.")
        print("-"*50)

# Function that creates records
def create (dni,name,adress,age,city):
    dictionaries.register[dni] = [name,adress,age,city]
    print("Record created successfully")
    print("-"*50)

# Function that update records
def update(data_query):
    if data_query in dictionaries.register.keys():
        print("Replace the new DNI data: ")
        name = input("Name: ")
        adress = input("Adress: ")
        age= input("Age: ")
        city = input("City: ")
        dictionaries.register[data_query] = [name,adress,age,city]
        print("Updated user")
        print("-"*50)
    else:
        print("User not found")

# Function than delete records
def delete (data_query):
    if data_query in dictionaries.register.keys():
        del dictionaries.register[data_query]
        print("It was deleted correctly")
        print("-"*50)
    else:
        print("ID not found")