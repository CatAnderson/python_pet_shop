# WRITE YOUR FUNCTIONS HERE

# test 1
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


# test 2
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


# test 3 & 4
def add_or_remove_cash(pet_shop, num):
    pet_shop["admin"]["total_cash"] += num 


# test 5
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


# test 6
def increase_pets_sold(pet_shop, num):
    pet_shop["admin"]["pets_sold"] += num


# test 7
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


# test 8 & 9
# def get_pets_by_breed(pet_shop, breed_type):
#     found_breeds = []
#     for breed_type in pet_shop:
#         if breed_type == True:
#             found_breeds.append(breed_type)
#     return found_breeds

# needs a loop which goes through the list of "pets", 
# finds all the pets with the breed_type that is 
# in the argument and store that in a list to be invoked.


# test 10 & 11
# def find_pet_by_name(pet_shop, pet_name):
#     if pet_name == pet_name:
#         return pet_shop["pets"][]
#     else:
#         return None

# needs a if statement which goes through the list of "pets", 
# to find the pets_name that is in the argument and 
# if it finds it then return it....else return None


# test 12
# def remove_pet_by_name(pet_shop, pet_name):
# delete the "name" from "pets" list - .pop
# then use the function above (find_pet_by_name) 
# to find name - wont be able to find name as was deleted


# test 13
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


# test 14
def get_customer_cash(customers):
    return customers["cash"]


# test 15
def remove_customer_cash(customer, money):
    customer["cash"] -= money 


# test 16
def get_customer_pet_count(customers):
    return len(customers["pets"])


# # test 17
def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet)
 
