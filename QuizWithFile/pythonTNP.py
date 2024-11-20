import random

def inp():
    user=input("Enter Username : ")
    enrollmentNo=input("Enter Enrollment Number : ")
    emailId=input("Enter Email Id : ")
    pwd=input("Enter your Password : ")
    return [user,enrollmentNo,emailId,pwd]

def registration(user_details):
    user, enrollment_no, email, pwd = inp()
    for user_info in user_details:
        if user_info["EmailID"] == email:
            print("Already Registered")
            return None
    new_user = {
        "Username": user,
        "EnrollmentNo": enrollment_no,
        "EmailID": email,
        "Password": pwd
    }
    user_details.append(new_user)
    writeUserDetails(user_details)
    print("Successfully Registered!")
    return new_user


def login(user_details):
    user, enrollment_no, email, pwd = inp()
    for user_info in user_details:
        if user_info["EmailID"] == email:
            if user_info["Password"] == pwd:
                print("Successfully Logged In!!!")
                return user_info  
            else:
                print("Wrong Password!!")
                return None
    print("User Not Found, please Register first")
    return None

def Menu():
    print('''
        Please Make your Choice:
        1. Registration.
        2. Login.
        3. Attempt Quiz.
        4. Show Result.
        5. Exit.
    ''')
    i=int(input())
    return i

def QuizMenu():
    print('''
        Which Quiz you want to Attempt:
        1. DSA.
        2. DBMS.
        3. Python.
    ''')
    i=int(input())
    return i

def question(st):
    li=[]
    for lines in st:
        a,b,c,d,e,f=lines.split('&&&&')
        temp=[a,b,c,d,e,f]
        li.append(temp)
    return li

def questionDisplay(arraylist):
    random.shuffle(arraylist)  
    for index, ques in enumerate(arraylist):
        print(f"Q{index + 1}: {ques[0]}")  
        print(f"1. {ques[1]}")
        print(f"2. {ques[2]}")
        print(f"3. {ques[3]}")
        print(f"4. {ques[4]}")
        ans = int(input("Your Answer(1-4): "))
        if ques[ans] == ques[5]:
            return True
    return False

def marking(topic):
    arraylist=question(topic)
    marks=0
    for ques in arraylist:
        if questionDisplay(ques):
            marks+=1
    print(f"Your Score: {marks}.")

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
            attemptQuiz(DSA, DBMS, Python, current_user)

        # Save the score for the user
        current_user['score'] = score
        print(f"Your score is: {score}")

    else:
        print("You must log in first!")

def marks(topic,totalMarks):
    totalMarks[topic]=marking(topic)


def DSAQues():
    with open('DSA.txt','r') as file:
        question=file.readlines()
    return question
def DBMSQues():
    with open('DBMS.txt','r') as file:
        question=file.readlines()
    return question
def PythonQues():
    with open('Python.txt','r') as file:
        question=file.readlines()
    return question

def appendUserdetails(details):
    a,b,c,d=details
    with open('userDetails.txt','a') as file:
        file.write(f"User:{a},EnrollNO:{b},EmailID:{c},Password:{d}")

def ProcessDetails(st):
    userDetails=[]
    for lines in st:
        templine=lines.split(',')
        dic={}
        for word in templine:
            temp=word.split(':')
            dic.update({temp[0]:temp[1]})
        userDetails.append(dic)
    return userDetails

def EmailandPassword(userDetails):
    dic={}
    for user in userDetails:
        dic.update({user["EmailID"]:user["Password"]})
    return dic

def getUserdetails():
    with open('userDetails.txt','r') as file:
        details=file.readlines()
    return ProcessDetails(details)

def showResult(current_user):
    if 'score' in current_user:
        print(f"Your Score: {current_user['score']}")
    else:
        print("No quiz attempted. Please attempt a quiz first.")

def readUserDetails():
    user_details = []
    try:
        with open('userDetails.txt', 'r') as file:
            details = file.readlines()
            for line in details:
                line = line.strip()
                user_info = {}
                temp = line.split(',')
                for word in temp:
                    key, value = word.split(':')
                    user_info[key.strip()] = value.strip()
                user_details.append(user_info)
    except FileNotFoundError:
        pass  
    return user_details

def writeUserDetails(user_details):
    with open('userDetails.txt', 'w') as file:
        for user in user_details:
            file.write(f"User:{user['Username']}, EnrollNO:{user['EnrollmentNo']}, EmailID:{user['EmailID']}, Password:{user['Password']}\n")
