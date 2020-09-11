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
#     found_breeds = 0
#     for breed_type in pet_shop:
#         if breed_type == True:
#             found_breeds.append(breed_type)
#     return found_breeds


# test 10 & 11
# def find_pet_by_name(pet_shop, pet_name):
#     if pet_name == pet_name:
#         return pet_shop["pets"][]
#     else:
#         return None


# def find_pet_by_name(pet_shop, pet_name):
#     for name in pet_shop:
#         if name == False:
#             return None


# test 12
# def remove_pet_by_name(pet_shop, pet_name):


# test 13
#  def add_pet_to_stock(pet_shop, new_pet)


# test 14
def get_customer_cash(customers):
    return customers["cash"]


# test 15
# def remove_customer_cash(name, money):


# test 16
def get_customer_pet_count(customers):
    return len(customers["pets"])


# test 17
def add_pet_to_customer(customer, new_pet):
#    add pets from new_pet dict 
#    to customers dict in the pets key
    return get_customer_pet_count

