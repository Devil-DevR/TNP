import pythonTNP as Q

def mainMenu(user_details, DSA, DBMS, Python):
    current_user = None  # To store the logged-in user

    while True:
        ch = Q.Menu()
        if ch == 1: 
            if not current_user: 
                new_user = Q.registration(user_details)
                if new_user:
                    current_user = new_user 
            else:
                print("You are already logged in. Log out to register a new user.")
        elif ch == 2:  
            if not current_user:
                current_user = Q.login(user_details)
            else:
                print(f"You are already logged in as {current_user['Username']}.")
        elif ch == 3: 
            if current_user:  
                Q.attemptQuiz(DSA, DBMS, Python, current_user)
            else:
                print("You must log in first!")
        elif ch == 4:  
            if current_user and 'score' in current_user:
                Q.showResult(current_user)  
            else:
                print("You haven't attempted any quiz yet.")
        elif ch == 5:
            print("Saving user details and exiting...")
            Q.writeUserDetails(user_details)  
            exit()
        else:
            print("Wrong Choice. Please try again.")

DSA = Q.DSAQues()
DBMS = Q.DBMSQues()
PY = Q.PythonQues()

userList = Q.readUserDetails()
UserIdandPWD = Q.EmailandPassword(userList)
mainMenu(UserIdandPWD, DSA, DBMS, PY)
