# Import files
import dictionaries
import functions

# Create the controller that will manage all the actions of the system
def controller ():
    # We start the system in True state (On). It will only turn off if the status is False.
    status_sistem = True # System Status
    functions.start_message()
    while(status_sistem == True):
        entry_data = functions.query_message() # Response selection
        if(entry_data=="1"):
            data_query = str(input("Ingrese DNI: "))
            functions.consult(data_query)
        elif(entry_data=="2"):
            print("Ingrese los siguientes campos:")
            dni= str(input("DNI: "))
            name = input("Nombre: ")
            adress = input("Apellido: ")
            age= input("Edad: ")
            city = input("Ciudad: ")
            functions.create(dni,name,adress,age,city)
        elif(entry_data=="3"):
            data_query = str(input("Ingrese DNI: "))
            functions.update(data_query)
        elif(entry_data=="4"):
            data_query = str(input("Ingrese DNI:"))
            functions.delete(data_query)
        elif(entry_data =="5"):
            print("\n")
            print("Finalizó el sistema")
            print("\n")
            status_sistem = False
            break
        else:
            print("No elegiste opciones disponibles, reintentar")

# Start de system
controller()
    