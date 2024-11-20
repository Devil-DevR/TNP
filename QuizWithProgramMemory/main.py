import quiz_functions as Q

user_details = []
current_user = None

DSA = [
    ["What is an array?", "Collection of elements", "A single value", "A pointer", "An object", "Collection of elements"],
    ["What is a linked list?", "A sequence of nodes", "An array", "A type of loop", "A function", "A sequence of nodes"],
    ["What is a stack?", "LIFO structure", "FIFO structure", "A type of array", "A function", "LIFO structure"],
    ["What is a queue?", "FIFO structure", "LIFO structure", "A type of array", "A function", "FIFO structure"],
    ["What is a binary tree?", "A tree structure with 2 children", "A type of linked list", "A graph", "A stack", "A tree structure with 2 children"],
    ["What is a graph?", "A collection of nodes and edges", "A type of array", "A tree", "A stack", "A collection of nodes and edges"],
    ["What is a hash table?", "A structure for fast lookups", "A type of array", "A stack", "A queue", "A structure for fast lookups"],
    ["What is recursion?", "A function that calls itself", "A loop", "A stack", "An array", "A function that calls itself"],
    ["What is dynamic programming?", "A method to solve problems by breaking them down", "A sorting algorithm", "A data structure", "A stack", "A method to solve problems by breaking them down"],
    ["What is quicksort?", "A sorting algorithm", "A searching algorithm", "A data structure", "A loop", "A sorting algorithm"]
]

DBMS = [
    ["What is SQL?", "Structured Query Language", "Standard Query Language", "Simple Query Language", "Sequential Query Language", "Structured Query Language"],
    ["What is a primary key?", "A unique identifier for rows", "A type of index", "A data type", "A foreign key", "A unique identifier for rows"],
    ["What is a foreign key?", "A key used to link two tables", "A primary key", "An index", "A unique key", "A key used to link two tables"],
    ["What is normalization?", "Process of organizing data to reduce redundancy", "A type of indexing", "A type of query", "A data structure", "Process of organizing data to reduce redundancy"],
    ["What is a relational database?", "A database using tables to store data", "A type of hash map", "A collection of files", "A queue", "A database using tables to store data"],
    ["What is an index?", "A database structure that speeds up data retrieval", "A type of query", "A foreign key", "A primary key", "A database structure that speeds up data retrieval"],
    ["What is a view in SQL?", "A virtual table based on a query", "A stored procedure", "A data type", "A type of index", "A virtual table based on a query"],
    ["What is ACID?", "A set of properties for database transactions", "A type of query", "A data structure", "A foreign key", "A set of properties for database transactions"],
    ["What is a stored procedure?", "A set of SQL statements stored in the database", "A type of index", "A data type", "A query", "A set of SQL statements stored in the database"],
    ["What is a transaction?", "A sequence of operations performed as a single unit", "A type of index", "A query", "A data type", "A sequence of operations performed as a single unit"]
]

Python = [
    ["What is a Python tuple?", "Immutable sequence", "Mutable sequence", "String", "Function", "Immutable sequence"],
    ["What is the output of 2 + 3?", "5", "23", "6", "None of the above", "5"],
    ["What is a list in Python?", "An ordered collection of items", "A tuple", "A string", "A dictionary", "An ordered collection of items"],
    ["What is a dictionary in Python?", "A collection of key-value pairs", "A list", "A set", "A string", "A collection of key-value pairs"],
    ["What is a function in Python?", "A block of code that performs a specific task", "A variable", "A data type", "A loop", "A block of code that performs a specific task"],
    ["What is a class in Python?", "A blueprint for creating objects", "A function", "A data type", "A variable", "A blueprint for creating objects"],
    ["What is an exception in Python?", "An error that occurs during execution", "A data type", "A loop", "A function", "An error that occurs during execution"],
    ["What is slicing in Python?", "Accessing parts of a sequence", "A type of loop", "A data structure", "A function", "Accessing parts of a sequence"],
    ["What is a lambda function?", "A small anonymous function", "A variable", "A loop", "A class", "A small anonymous function"],
    ["What is a module in Python?", "A file containing Python code", "A data type", "A class", "A function", "A file containing Python code"]
]

def mainMenu():
    global current_user
    while True:
        print('''
        Please make your choice:
        1. Registration
        2. Login
        3. Attempt Quiz
        4. Show Result
        5. Exit
        ''')
        choice = int(input())

        if choice == 1: 
            if current_user:
                print("You are already logged in. Log out to register a new user.")
            else:
                current_user = Q.registration(user_details)
        elif choice == 2: 
            if current_user:
                print(f"You are already logged in as {current_user['Username']}.")
            else:
                current_user = Q.login(user_details)
        elif choice == 3: 
            if current_user:
                Q.attemptQuiz(DSA, DBMS, Python, current_user)
            else:
                print("You must log in first!")
        elif choice == 4: 
            if current_user:
                Q.showResult(current_user)
            else:
                print("You must log in first!")
        elif choice == 5: 
            print("Exiting the program...")
            break
        else:
            print("Invalid option, please try again.")

mainMenu()
