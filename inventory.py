#========The beginning of the class==========
# defines shoe class 
class Shoe:

    # defines shoe types 
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # defines methods to access class variables
    def get_country(self):
        return self.country

    def get_code(self):
        return self.code

    def get_product(self):
        return self.product
       
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    # print string representation
    def __str__(self):
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: £{self.cost}, Quantity: {self.quantity}"

    # print raw data 
    def get_all_data(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============

# reads shoe info from data fileß
def read_shoes_data():
    try:
        file = open("inventory.txt", "r")
        for line in file:
            try:
                split_line = line.strip().split(",")
                # skips the header line
                if split_line[0] == "Country":
                    continue
                # extracts the different shoe values
                country = split_line[0]
                code = split_line[1]
                product = split_line[2]
                cost = int(split_line[3])
                quantity = int(split_line[4])

                # creates shoe object and adds to list
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
                print(f"Loading shoe: {shoe.get_product()}")
            except:
                # if one line of data is not valid
                print("Error reading shoe data line, skipping to next line")
        print("\nShoe data read correctly")
    except:
        # if data file is not valid
        print("Error reading shoe data file")

# allows the user to create their own shoe and adds to the list and fileß
def capture_shoes():
    try:
        # gets shoe info
        country = input("Enter shoe's country of origin: ")
        code = input("Enter shoe's code: ")
        product = input("Enter shoe's product name: ")
        cost = int(input("Enter cost of shoe: "))
        quantity = int(input("Enter quantity of shoe's: "))

        # creates shoe and adds to list
        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)
        print(f"\nCreated shoe: {shoe.get_product()}")
    
    except:
        print("Error incurred whilst entering data, please try again.")

# prints out all shoe data
def view_all():
    for shoe in shoe_list:
        print(shoe)

# finds lowest quanity shoe and asks the user to restock
def re_stock():
    try:
        # calls function to find lowest quanity shoe
        shoe_with_lowest_qty = get_shoe_with_lowest_qty()

        # asks the user how much they want to set the quantity to
        print(f"Shoe with lowest quantity is:\n{shoe_with_lowest_qty}\n")
        new_quantity = int(input(f"Please enter updated quantity: "))

        # updates quantity
        shoe_with_lowest_qty.set_quantity(new_quantity)

        # rewrites shoe data file
        file = open("inventory.txt", "w")
        file.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoe_list:
            file.write(f"{shoe.get_all_data()}\n")
        file.close()
    except:
        print("Error retocking shoes, please try again")

# allows user to search for a shoe
def seach_shoe():
    # gets shoe code from user
    shoe_code = input("Enter shoe code: ")

    # searches for code and returns shoe if found
    for shoe in shoe_list:
        if shoe_code == shoe.get_code():
            return shoe 

# prints out each shoes total stock value
def value_per_item():
    for shoe in shoe_list:
        cost = shoe.get_cost()
        quantity = shoe.get_quantity()
        value = cost * quantity
    
        print(f"Shoe: {shoe.get_product()}, Cost: £{cost}, Quantity: {quantity}, Total Value: {value}")
    

# finds the shoe with highest quantity and prints it out
def highest_qty():
    # sets first shoe to be highest
    highest_qty_index = 0
    highest_qty_value = shoe_list[0].get_quantity()

    # loops through and checks if we have any higher
    for index in range(len(shoe_list)):
        shoe = shoe_list[index]
        quantity = shoe.get_quantity()

        # updates highest quantiy shoe if there is one
        if quantity > highest_qty_value:
            highest_qty_value = quantity
            highest_qty_index = index

    # gets highest quantity shoe from list and prints it 
    shoe = shoe_list[highest_qty_index]
    print(f"For sale:\n{shoe.get_product()}, £{shoe.get_cost()}, quantity: {shoe.get_quantity()}")
        
# finds the shoe with lowest quantity and prints it out
def get_shoe_with_lowest_qty():
    # sets first shoe to be lowest
    lowest_qty_index = 0
    lowest_qty_value = shoe_list[0].get_quantity()

    # loops through and checks if we have any lower
    for index in range(len(shoe_list)):
        shoe = shoe_list[index]
        quantity = shoe.get_quantity()

        # updates lower quantiy shoe if there is one
        if quantity < lowest_qty_value:
            lowest_qty_value = quantity
            lowest_qty_index = index

    # gets lowest quantity shoe from list and returns it 
    shoe_with_lowest_quantity = shoe_list[lowest_qty_index]
    return shoe_with_lowest_quantity



#==========Main Menu=============

# read shoe data into list
read_shoes_data()

# menu to allow users to interact with the shoe data
while True:
    menu = input('''Select one of the following options below:
rd - read shoe data
cs - create shoe
va - view all shoes
rs - restock shoes
ss - search shoes
vv - view shoe values
vh - view highest quantity shoe
e - Exit
: ''').lower()

    if menu == 'rd':
        print()
        read_shoes_data()
        print()

    elif menu == 'cs':
        print()
        capture_shoes()
        print()

    elif menu == 'va':
        print()
        view_all()
        print()

    elif menu == 'rs':
        print()
        re_stock()
        print()

    elif menu == 'ss':
        print()
        shoe = seach_shoe()
        if shoe != None:
            print(shoe)
        else:
            print("Could not find shoe")
        print()

    elif menu == 'vv':
        print()
        value_per_item()
        print()

    elif menu == 'vh':
        print()
        highest_qty()
        print()

    elif menu == 'e':
        print()
        print('Goodbye!!!')
        print()
        exit()
    else:
        # if they enter an invalid option
        print("You have made an invalid choice, please try again")
        print()    
