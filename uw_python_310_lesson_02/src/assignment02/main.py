def main():
    ## Question 1
    questions = ("name",
                 "conference ID",
                 "organization",
                 "email",
                 "food preferences")
    question_answers = []

    for question in questions:
        if question[-1].lower() == "s":
            answer = input("What are your " + question + "? ")
            print(f"Your {question} are {answer}.")
        else:
            answer = input("What is your " + question + "? ")
            print(f"Your {question} is {answer}.")
        question_answers.append(answer)

    ## Question 2
    sessions = ("Python for Beginners", 
    "Database Development With Python",
    "Python for Data Science", 
    "Advanced Python for Application Developers")
    session_answers = []
    for session in sessions:
        answer = ""
        while answer.upper() not in ["Y", "N"]:
            answer = input("Do you wish to attend " + session + "? (Y or N) ")
        answer = answer.upper()
        if answer == "Y":
            print("Ok, I've recorded your interest in attending " + session + ".")
        else:
            print("Ok, I've recorded your disinterest in attending " + session + ".")
        session_answers.append(answer)




if __name__ == "__main__":
    main()
