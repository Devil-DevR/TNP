import sqlite3

DB_FILE = "quiz_app.db"

def setup_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quizzes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quiz_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quiz_id INTEGER NOT NULL,
            question TEXT NOT NULL,
            options TEXT NOT NULL,
            answer TEXT NOT NULL,
            FOREIGN KEY (quiz_id) REFERENCES quizzes (id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            quiz_id INTEGER NOT NULL,
            score INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (quiz_id) REFERENCES quizzes (id)
        )
    ''')

    conn.commit()
    conn.close()

def populate():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Seed quizzes
    quizzes = [("Python Quiz",), ("Math Quiz",)]
    cursor.executemany("INSERT INTO quizzes (name) VALUES (?)", quizzes)

    # Seed quiz questions
    questions = [
    # Python Quiz
    (1, "What is the output of 2 + 2 * 2?", "4,5,6,3", "6"),
    (2, "Which of the following is a mutable data structure?", "List,Tuple,String,Integer", "List"),
    (3, "What is used to define a function in Python?", "def,func,function,define", "def"),
    (4, "Which of the following is a valid Python data type?", "int,float,bool,str", "int"),
    (5, "Which keyword is used to create anonymous functions?", "lambda,def,return,call", "lambda"),
    (6, "Which loop is used to iterate over a sequence in Python?", "for,while,if,else", "for"),
    (7, "Which function is used to display output in Python?", "print,input,output,write", "print"),
    (8, "Which keyword is used to declare a global variable in Python?", "global,local,nonlocal,static", "global"),
    (9, "Which function returns the number of items in an object?", "range,len,sum,average", "range"),
    (10, "Which value is considered as a boolean True in Python?", "True,False,yes,no", "True"),
    # DSA Quiz
    (1, "Which of the following is a linear data structure?", "Array,Linked List,Tree,Graph", "Array"),
    (2, "Which data structure follows LIFO (Last In First Out) principle?", "Stack,Queue,Priority Queue,Deque", "Stack"),
    (3, "Which sorting algorithm is known for its divide and conquer approach?", "Insertion,Merge,Selection,Quick", "Quick"),
    (4, "Which search algorithm works by dividing the search space in half?", "Binary Search,Linear Search,Jump Search,Fibonacci Search", "Binary Search"),
    (5, "Which of the following is a key-value data structure?", "Hash Map,Set,List,Tuple", "Hash Map"),
    (6, "Which algorithm is used to explore a graph by visiting each node level by level?", "DFS,BFS,Topological Sort,Prim", "DFS"),
    (7, "Which sorting algorithm is considered the fastest on average?", "Bubble Sort,Insertion Sort,Quick Sort,Merge Sort", "Merge Sort"),
    # DBMS Quiz
    (1, "Which of the following is a relational database management system?", "SQL,MySQL,PostgreSQL,MongoDB", "SQL"),
    (2, "What process is used to organize a database to reduce redundancy?", "Normalization,Denormalization,Normalization Forms,Transactions", "Normalization"),
    (3, "Which key uniquely identifies a record in a table?", "Primary Key,Foreign Key,Unique Key,Composite Key", "Primary Key"),
    (4, "Which of the following ensures that database transactions are processed reliably?", "ACID,BASE,SQL,NoSQL", "ACID"),
    (5, "Which operation combines data from two tables based on a related column?", "Join,Union,Intersection,Difference", "Join"),
    (6, "Which of the following is used to define the structure of a database?", "DDL,DML,DCL,TCL", "DDL")
]

    cursor.executemany("INSERT INTO quiz_questions (quiz_id, question, options, answer) VALUES (?, ?, ?, ?)", questions)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    populate()
    print("Database setup complete with seed data!")
