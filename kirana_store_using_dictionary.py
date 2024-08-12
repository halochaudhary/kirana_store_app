# List of items with their corresponding prices stored in a dictionary
items_prices = {
    "Daal": 80,
    "Cheeni": 50,
    "Salt": 20,
    "Suzi": 15,
    "Besan": 60
}

# Input from the customer
custumer_input = input("Enter the item name [Daal, Cheeni, Salt, Besan, Suzi]: ")

# Check if the item is in the list
if custumer_input in items_prices:
    quantity = int(input("Enter the quantity in Kg: "))
    
    # Calculate the price
    price = quantity * items_prices[custumer_input]
    
    # Print the bill
    print(f"{custumer_input} {quantity} Kg Rs. {price}")
else:
    print("Invalid input")
