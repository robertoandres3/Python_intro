

# Readme Evaluation:

# Menu:
# We have a menu that allows us to have different options from 1 to 7 so our customers can choose the one they need. Each option corresponds to a case (the options we can choose):

# 1. Add products to inventory: You can add the product name, its price, and the available quantity.

# 2. View products in inventory: Here we can see the added and existing products in this list, easily searching for them by name.

# 3. Print all products: With this option, we can see in detail all the products we have in our list, knowing both the name of the searched product and its price and corresponding quantity.

# 4. Update product prices: If you have a product and its value changes, with this option, we can update the new price without having to delete it, simply by modifying its price. 5. Delete products from inventory: Here we can delete a product that is no longer available by choosing option 5. This will allow us to delete the product simply by entering its name.

# 6. Calculate total inventory value: This option allows us to add the product value to the available quantities, obtaining the total for all products.

# 7. Exit: If we want to exit the application and complete queries or actions in our menu, we can easily do so with option 7.

# Methods:

# 1. Lower: Allows each piece of data added to a variable to be written in lowercase.

# 2. Add: Allows us to add data to a list.

# Functions: This is a set of instructions that lead us to a result.

# 1. Update_produc= This function allows us to add the name, price, and quantity of the product we are recording.
# Title: This is the name of our product.
# Price: This is the individual price of our product. Quantity: How many units of this product do I have?
# 2. Search_product= This function is used to search for a product in our list, check if it exists, and what data it contains.
# It then prints all the stored data for the product we are searching for.
# 3. Print_product = This function allows us to print all the data on our list in an organized manner, showing its name, price, and quantity.
# 4. Delete_product = We can delete a piece of data from our list that we no longer want to keep. We search for it by name and, after executing it correctly, we notify the customer that the deletion was successful.

# 5. Product_quantity = This function is used to update data. In this case, it allows us to change the product's price by updating it to the new price and saving it.

# 6. Total = With this function, we can see the total for each product and multiply the price by its corresponding quantity, adding another value at the end that corresponds to the sum of all the product totals.



# list of all products within a dictionary

inventory = [
    {"title": "sauce", "price": 2000, "quantity": 5},
    {"title": "tomato", "price": 700, "quantity": 3},
    {"title": "onion", "price": 500, "quantity": 5},
    {"title": "meat", "price": 10000, "quantity": 10},
    {"title": "avocado", "price": 5000, "quantity": 5}]


# Add products to the list with their name, price, and quantity.
# We create conditions so that the price and quantity values ​​are integers and are greater than 0. Otherwise, we print an error. We do not break the loop until a correct value is added.

def add_produc():

    while True: 
        
        try:
            title= input("Enter the name from product: ").lower()
            if title in inventory:
                print('El producto ya existe.')
                continue
            price= int(input("Enter the price: "))
            if price  > 0:
                quantity= int(input("Enter quantity of product to add: "))
                if quantity > 0:

                    print("Data added successfully")  
                    inventory.append({"title": title, "price": price,  "quantity": quantity})
                    break
                        
                        
                    
                else:
                        print("ERROR: the quantity must greater than 0. Try again")   
                    

                    
            else:
                print("ERROR: The quantity must greater than 0. Try again")
        except ValueError:
            print("Write in correct number ")

#We create a function to search for a product, asking the customer for the name of the product they want to search for.
#We print all the data from our list.
def search_product():
    namesearch= input("Enter name from product to search: ").lower().strip()
    for x in inventory:
        if namesearch == x["title"]:
            print(f"{x['title']}  price: {x['price']} quantity: {x['quantity']}")
            
            break
    else:
        print("Not found")

#here we print all the data we have in the list

def print_product():
    for x in inventory:
     print (f"{x["title"]}  price: {x["price"]} quantity: {x["quantity"]}")


#we change the value of the product by searching for it by name

def update_product():
    searchname= input ("Enter the name from product than want to update: ").lower().strip()
    while True:
        try:
            for x in inventory:
                if x ["title"] == searchname:

                    newprice = int(input("Write your new price: "))
                    if newprice >0:
                        x["price"] = newprice
                        print("Update price")
                                      
                    else:
                        print("Add a number greath that 0")
            
        except ValueError:
            print("ERROR: Add a correct value number ")
        break

#we eliminate a product that we search for by name

def remove_product():

    nameremove = input("Write the name from product than you want remove: ").lower()

    for x in inventory:
        if x ["title"] == nameremove:
            inventory.remove(x)
            print (" Product Remove")
            break
    else:
        print("Product doesn't exist")   

#We create a mathematical operation to be able to multiply the prices with the quantity and then we print the entire sum of the numbers

def total():
    total= 0
    
    for x in inventory:
        total = x["price"] * x["quantity"]

        print (f"Product:" , x["title"] , "its price is: ", x["price"] , "quantity is:" ,x["quantity"] , "and your total is: " ,total)
        
    print (f"Your total values of all products is:" , (sum(x['price'] * x['quantity'] for x in inventory)))






#We create a menu of options so that the person can choose the option they need

while True:

    print("\033[34m\n \033[01m >>> MENÚ <<< \033[0m\n" \
    "1. Add product to the inventory\n" \
    "2. Consult products in inventory\n" \
    "3. Print every the products\n"
    "4. Update price of products\n" \
    "5. Remove products from inventory\n" \
    "6. Calculate the total value from inventory\n" \
    "7. Exit\n")
    
    option= input("Write an option: ")

    match option:
        case "1":
            add_produc()
        case "2":
            search_product()
        case "3":
            print_product()

        case "4":
            update_product()
        case "5":
            remove_product()
        case "6":
            total()
        case "7":
            print("Godbye....")
            break