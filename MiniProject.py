import csv

# Function to store amount and category in a dictionary and write to a CSV file
def amount():
    dict = {}
    while True:
        amount = float(input("\nEnter the amount: "))
        category = input("\nEnter the category: ")
        dict[category] = dict.get(category, 0) + amount #It will fill the entered value of amount and category in the dictionary named dict
        cont = input("\nDo you want to continue? (yes/no): ")  #Provide a choice to user to insert as many function they wanted to
        if cont.lower() != "yes":
            break
    with open('Expenses.csv', 'w', newline='') as csvfile:  #Open a CSV file of a name Expenses.csv in write mode
        fieldnames = ['category', 'amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for category, amount in dict.items():
            writer.writerow({'category': category, 'amount': amount})  #It will write the data in a csv file


# Function to read the total amount based on category
def total():
    category = input("\nEnter the category : ")
    try:  # It is used if any error occur during the reading of data then the compilation will not terminate 
        with open('Expenses.csv', 'r') as csvfile:  #Open the Expenses.csv file in read mode
            reader = csv.DictReader(csvfile)
            total_amount = sum(float(row['amount']) for row in reader if row['category'] == category) #It will fetch all the amount based on category and total it
            print(f"Total amount for {category}: {total_amount}")  #Prints the total amount based on category 
    except FileNotFoundError:
        print("No data found to display.")  #When try block failed to execute or gives back a error then it will print the message in except block


# Function to sum all the amounts and give the total
def sum_all():
    try:
        with open('Expenses.csv', 'r') as csvfile:
            r = csv.DictReader(csvfile)
            a = sum(float(row['amount']) for row in r)  #It will fetch the amount of all the category and retun the summ of all amount to variable a
            print(f"Total amount: {a}")  #it will print the Sum of all the amount
    except:
        print("No data found to display.")  #it will execute after the failure of try block


#Summary function stores the total function and sum all function to get the summary 
def summary():
    print("\nPlease chose what you want :\n")
    print("\n1--> Total Spending\n2--> Total Overall Spending\n3--> Back to Main Menu\n4--> Exit\n")
    a=input("\nEnter your Choice : ")
    if a=="1":
        total()
    elif a=="2":
        sum_all()
    elif a=="3":
        main()
    elif a=="4":
        exit()
    else:
        print("\nYou have Entered the Wrong Choice, please select the correct Choice\n")
        summary()

# Main function
def main():
    while True:
        print("***********..........___....Main Menu....___..........***********\n")
        print("1--> Add an Expense\n2--> View Summaries\n3--> Exit the Program\n\n")
        choice = input("\nEnter your choice : ")
        if choice == "1":
            amount()
        elif choice == "2":
            summary()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

main()
