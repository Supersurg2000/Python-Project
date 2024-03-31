Vehicle Inventory Management System

Overview
The Vehicle Inventory Management System is designed to facilitate the management of a vehicle inventory, including cars, trucks, and other automobiles. It allows for the addition, removal, and updating of vehicle attributes within the inventory. This README provides guidance on setup, usage, and features of the system.

Features
Add New Vehicle: Add vehicles to the inventory with comprehensive details.
Remove a Vehicle: Remove vehicles from the inventory as necessary.
Update Vehicle Attributes: Modify the details of existing vehicles in the inventory.
View Inventory: Display a list of all vehicles currently in the inventory.
Export Inventory: Capability to output all vehicle inventory details to a text file for external use.
Vehicle Attributes
Each vehicle in the inventory is characterized by the following attributes:

name (string): The name or designation of the vehicle.
make (string): The manufacturer of the vehicle.
model (string): The model name or number of the vehicle.
color (string): The color of the vehicle.
year (int): The manufacturing year of the vehicle.
mileage (int): The current mileage of the vehicle.
Methods
Constructor: Initializes a new vehicle with specified attributes.
Add New Vehicle: Adds a new vehicle to the inventory.
Remove a Vehicle: Removes a specified vehicle from the inventory.
Update Vehicle Attributes: Updates any attribute of an existing vehicle.
View Inventory: Lists all vehicles currently in the inventory.
Export Inventory: Outputs the vehicle inventory to a text file.
Usage
Adding a Vehicle:
To add a vehicle, the user will be prompted to enter vehicle details such as name, make, model, color, year, and mileage.

Removing a Vehicle:
To remove a vehicle, the user must enter the vehicle number of the vehicle to be removed.

Updating Vehicle Attributes:
The user can update the attributes of any vehicle by entering the vehicle number and the new details for the vehicle.

Viewing the Inventory:
The inventory can be viewed at any time, listing all vehicles with their details.

Exporting the Inventory:
When the user chooses to exit the program, the vehicle inventory is automatically saved to a text file.

Source Code
The provided source code implements all features of the Vehicle Inventory Management System, including the class definitions, methods for managing the inventory, and a user interface for interacting with the system through a command-line menu.
