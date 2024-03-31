vehicle_count = 0 # Will help initiate count matching positioning of object in list
class Automobile: # creates Automobile class
    vehicle_list = [] # starts to create the list where vehicle will be stored
    def __init__(self, v_count, name, make, model, color, year, mileage): # transfers over input data to object
        self.count = v_count
        self.name = name
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage
        Automobile.vehicle_list.append(self)


    def get_count(self): #created the get function for future use when calling for class specific data
        return self.count

    def set_name(self, name): #created the set function for future use when changing class specific data
        self.name = name

    def get_name(self): #created the get function for future use when calling for class specific data
        return self.name

    def set_make(self, make): #created the set function for future use when changing class specific data
        self.make = make

    def get_make(self): #created the get function for future use when calling for class specific data
        return self.make

    def set_model(self, model): #created the set function for future use when changing class specific data
        self.model = model

    def get_model(self): #created the get function for future use when calling for class specific data
        return self.model

    def set_color(self, color): #created the set function for future use when changing class specific data
        self.color = color

    def get_color(self): #created the get function for future use when calling for class specific data
        return self.color

    def set_year(self, year): #created the set function for future use when changing class specific data
        self.year = year

    def get_year(self): #created the get function for future use when calling for class specific data
        return self.year

    def set_mileage(self, mileage): #created the set function for future use when changing class specific data
        self.mileage = mileage

    def get_mileage(self): #created the get function for future use when calling for class specific data
        return self.mileage

    def __str__(self): #Creates data that can be retreived by user when wanting to see list. This function uses the get function from above to call on data that will be viewed by user
        return "Vehicle#:" + str(self.get_count()) + " vehicle name:" + self.get_name() + " make:" + self.get_make() + " model:" + str(self.get_model()) + " color:" + self.get_color() + " year:" + str(self.get_year()) + " mileage:" + str(self.get_mileage())


    def del_vehicle(self): # function that uses the input of user to delete vehicle based on position on list
        index = int(input("Enter the vehicle # of vehicle to be removed: ")) # create index number from user input
        if index >= 0 and index < len(Automobile.vehicle_list): # Creates limit based on number of vehicles in inventory
            make = Automobile.vehicle_list[index].get_make() # create make name to be called in print
            model = Automobile.vehicle_list[index].get_model() # create model name to be called in print
            Automobile.vehicle_list.pop(index) # uses input as index number to remove from list
            print(make, model, "has been removed from the vehicle inventory") # calls on make and model from above
        else:
            print("Invalid Vehicle#") # catches non applicable input from user and gives invalid vehicle message


    def update_vehicle(self): # function that uses the user input to make changes to exisiting vehicle objects in list
        index = int(input("Enter the Vehicle# of vehicle to be updated: ")) #creates a number that will be used
        if index >= 0 and index < len(Automobile.vehicle_list): # creates limit based on vehicles in existing list
            make = input("Enter new make: ") # following lines will connect the user input to the class's self specific data and using the index, the user changes the vehicle that matches the index with positioning
            model = input("Enter new model: ")
            color = input("Enter new color: ")
            year = int(input("Enter new year: "))
            mileage = int(input("Enter new mileage: "))
            Automobile.vehicle_list[index].set_make(make)
            Automobile.vehicle_list[index].set_model(model)
            Automobile.vehicle_list[index].set_color(color)
            Automobile.vehicle_list[index].set_year(year)
            Automobile.vehicle_list[index].set_mileage(mileage)
            print("update complete") # confirmation message of completion
        else:
            print("Invalid index") # catches invalid inputs and notifies user


def main(): # gets called on to initiate program and saves when closed
    menu = {}
    menu['1']="Add a Vehicle."
    menu['2']="Update a Vehicle"
    menu['3']="View Inventory"
    menu['4']="Delete a Vehicle."
    menu['5']="Save File & Exit"

    outfile = open('Inventory-Module 8-Sergio Rodriguez.txt', 'w')

    for v in Automobile.vehicle_list:
        outfile.write(str(v) + "\n")

    outfile.close()

user=True # creates a loop that forces the program into starting and not stoping until broken by the save and exit otion.
while user: # print will display what the user will see
    input('\n----Press ENTER to bring up the menu----')
    print ("""
    1.Add Vehicle
    2.Update Vehicle
    3.View Inventory
    4.Delete Vehicle
    5.Save File & Exit
    """)
    inp=input("Select the number that matches what you want to do? ")

    if inp=="1": # if user selects 1, they will be asked to input vehicles data that will be transefered to __init__
        v_count=vehicle_count
        name=input("Enter vehicle name:")
        make=input("Enter vehicle make: ")
        model=input("Enter vehicle model: ")
        color=input("Enter vehicle color: ")
        year=input("Enter vehicle year: ")
        mileage=input("Enter vehicle mileage: ")

        vehicle = Automobile(vehicle_count, name, make, model, color, year, mileage) # allows user to see what they have added
        print('\nJUST ADDED--', vehicle)
        vehicle_count += 1 # creates a count that will match the vehicle's position

    elif inp=="2": # sends user to function where they will update vehicle information
        Automobile.update_vehicle('')

    elif inp=="3": # allows user to see objects in list
      for i in Automobile.vehicle_list:
        print(i)

    elif inp=="4": # sends user to function where they will be asked input info to identify and delete vehicle
      Automobile.del_vehicle('')

    elif inp=="5": # terminates programs
      print("\n Closing. Thank you")
      break

    elif inp!="": # advises user of invalid entry
      print("\n Invaild Entry")

if __name__ == "__main__":main() #Initates program