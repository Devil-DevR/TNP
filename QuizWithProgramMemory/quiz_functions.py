import random

def inp():
    user = input("Enter Username: ")
    enrollmentNo = input("Enter Enrollment Number: ")
    emailId = input("Enter Email Id: ")
    pwd = input("Enter your Password: ")
    return [user, enrollmentNo, emailId, pwd]

def registration(user_details):
    user, enrollmentNo, emailId, pwd = inp()
    for user_info in user_details:
        if user_info["EmailID"] == emailId:
            print("Already Registered")
            return None
    new_user = {
        "Username": user,
        "EnrollmentNo": enrollmentNo,
        "EmailID": emailId,
        "Password": pwd,
        "score": None  
    }
    user_details.append(new_user)
    print("Successfully Registered!")
    return new_user

def login(user_details):
    user, enrollmentNo, emailId, pwd = inp()
    for user_info in user_details:
        if user_info["EmailID"] == emailId:
            if user_info["Password"] == pwd:
                print("Successfully Logged In!!!")
                return user_info
            else:
                print("Wrong Password!!")
                return None
    print("User Not Found, please Register first")
    return None

def QuizMenu():
    print('''Which Quiz you want to Attempt:
        1. DSA.
        2. DBMS.
        3. Python.
    ''')
    i = int(input())
    return i

def questionDisplay(ques):
    print(f"Question: {ques[0]}")
    print(f"Options: \n1. {ques[1]}\n2. {ques[2]}\n3. {ques[3]}\n4. {ques[4]}")
    ans = int(input("Your Answer (1-4): "))
    if ques[ans] == ques[5]:
        return True
    return False

def marking(topic):
    random.shuffle(topic) 
    sel_topic=topic[:5]
    marks = 0
    for ques in sel_topic:
        if questionDisplay(ques):
            marks += 1
    return marks

def attemptQuiz(DSA, DBMS, Python, current_user):
    if current_user:  
        ch = QuizMenu()
        score = 0
        if ch == 1:
            score = marking(DSA)
        elif ch == 2:
            score = marking(DBMS)
        elif ch == 3:
            score = marking(Python)
        else:
            print("Wrong Option, Try Again")
            return attemptQuiz(DSA, DBMS, Python, current_user)

        current_user['score'] = score
        print(f"Your score is: {score}")
    else:
        print("You must log in first!")

def showResult(current_user):
    if 'score' in current_user:
        print(f"Your Score: {current_user['score']}")
    else:
        print("No quiz attempted. Please attempt a quiz first.")
