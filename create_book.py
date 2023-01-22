import csv
 
FILENAME = "PhoneBook.csv"
 
contacts = [
    ["Ivan", 89111156455],
    ["Roman", 89183434576],
    ["Igor", 89558342211]
]

def create_contacts(contacts):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)
     
create_contacts(contacts)