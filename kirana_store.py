# Define items
items = ["Daal", "Cheeni", "Salt", "Suzi", "Besan"]

# Define product price
Daal_price = 80
Cheeni_price = 50
Salt_price = 20
Suzi_price = 15
Besan_price = 60

# Taking input from custumer
custumer_input = input("Enter the item name [Daal, Cheeni, Salt, Besan, Suzi] : ")

# Applying conditions
if custumer_input in items:
    quantity = int(input("Enter the quantity in Kg : "))
    if custumer_input == "Daal":
        price = quantity * Daal_price
        bill = print("Daal",quantity,"Kg", "Rs.",price)
    elif custumer_input == "Cheeni":
        price = quantity * Cheeni_price
        bill = print("Cheeni",quantity,"Kg", "Rs.",price)
    elif custumer_input == "Salt":
        price = quantity * Salt_price
        bill = print("Salt",quantity,"Kg", "Rs.",price)
    elif custumer_input == "Besan":
        price = quantity * Besan_price
        bill = print("Besan",quantity,"Kg", "Rs.",price)
    elif custumer_input == "Suzi":
        price = quantity * Suzi_price
        bill = print("Suzi",quantity,"Kg", "Rs.",price)
else:
    print("Invalid input")
