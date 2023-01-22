import csv
 
FILENAME = "PhoneBook.csv"
 
contacts = [
    ["Ivan", 89111156455],
    ["Roman", 89183434576],
    ["Igor", 89558342211]
]
 
with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(contacts)
     
 
# with open(FILENAME, "a", newline="") as file:
#     user = ["Sam", 31]
#     writer = csv.writer(file)
#     writer.writerow(user)