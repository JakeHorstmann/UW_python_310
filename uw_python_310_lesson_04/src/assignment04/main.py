import csv


## Question 1
def clear_csv(file="questions.csv"):
    with open(file, "w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows([])


def setup_questions_csv(file="questions.csv"):
    with open(file, "w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        fields = ["question_id", "question"]
        question_ids = [12, 10]
        questions = ["phone number", "email"]
        writer.writerow(fields)

        for row in range(len(questions)):
            col_1 = question_ids[row]
            col_2 = f"What is your {questions[row]}?"
            writer.writerow([col_1, col_2])


## Question 2
def read_csv(file="questions.csv"):
    with open(file, "r") as f:
        reader = csv.reader(f, delimiter=",")
        fields = next(reader)
        for row in reader:
            col = 0
            for field in fields:
                print(f"{field.upper()}: {row[col]}")
                col += 1
            print("*" * 40)

def verify_questions(file = "questions.csv"):
    with open(file, "r") as f:
        reader = csv.reader(f,delimiter=",")
        fields = next(reader)
        id_column = fields.index("question_id")
        question_column = fields.index("question")
        replacements = {}
        csv_row = 1
        for row in reader:
            question_id = row[id_column]
            question = row[question_column]
            ans = ""
            while ans not in ["yes", "no"]:
                print(f"Please verify this question: {question}")
                ans = input("Does the question look correct? (YES/NO) ").lower()
                if ans not in ["yes", "no"]:
                    print("Please input yes or no")
            if ans == "no":
                new_question = ""
                while not (validate_question_length(new_question)):
                    new_question = input("Please enter a new question that is 10-30 characters long: ")
                replacements[csv_row] = [question_id, new_question]
            else:
                print("This question is verified")
            csv_row += 1
    return replacements

def replace_questions(replacements, file = "questions.csv"):
    # replace old lines with new question if needed
    with open(file, "r") as f:
        reader = csv.reader(f,delimiter=",")
        content = []
        csv_row = 0
        for row in reader:
            if csv_row in replacements.keys():
                content.append(replacements[csv_row])
            else:
                content.append(row)
            csv_row += 1
    # replace the file with new stuff
    with open(file, "w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        for row in content:
            writer.writerow(row)
    
        

def add_question(file="questions.csv"):
    question = input("Please enter a question that is 10-30 characters long: ")
    while not validate_question_length(question):
        print("Question is not 10-30 characters long")
        question = input("Please enter a question that is 10-30 characters long: ")
    question_id = generate_question_id()
    with open(file, "a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow([question_id, question])


def generate_question_id(file="questions.csv"):
    with open(file, "r") as f:
        reader = csv.reader(f, delimiter=",")
        fields = next(reader)
        id_column = fields.index("question_id")
        max_id = -99999999
        for row in reader:
            max_id = max([max_id, int(row[id_column])])
    return max_id + 1


## Question 3


def setup_answers_csv(file="answers.csv"):
    with open(file, "w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        fields = ["interviewee", "question", "answer"]
        interviewees = ["Anubhaw", "Anubhaw"]
        question_ids = [12, 10]
        answers = ["(555) 555 - 5555", "arya@uw.edu"]
        writer.writerow(fields)

        for row in range(len(answers)):
            col_1 = interviewees[row]
            col_2 = question_ids[row]
            col_3 = answers[row]
            writer.writerow([col_1, col_2, col_3])


def get_question_answers(question_file="questions.csv", answer_file="answers.csv"):
    name = input("What is your name? ")
    while not validate_not_empty(name):
        print("Please enter a non-empty value.")
        name = input("What is your name? ")
    question_ids = []
    answers = []
    with open(question_file, "r") as ans_f:
        reader = csv.reader(ans_f, delimiter=",")
        fields = next(reader)
        question_ids_col = fields.index("question_id")
        question_col = fields.index("question")
        for row in reader:
            question_id = row[question_ids_col]
            question = row[question_col]
            answer = input(f"{question} ")
            if "email" in question.lower():
                while not validate_email(answer):
                    print(f"{answer} is not a valid email.")
                    answer = input("Please enter a valid email: ")
            else:
                while not validate_not_empty(answer):
                    print("Please enter a non-empty value.")
                    answer = input(f"{question}")
            question_ids.append(question_id)
            answers.append(answer)
    return name, question_ids, answers


def append_answers(name, question_ids, answers, file="answers.csv"):
    with open(file, "r") as f:
        reader = csv.reader(f, delimiter=",")
        fields = next(reader)
    with open(file, "a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        name_col = fields.index("interviewee")
        question_col = fields.index("question")
        answer_col = fields.index("answer")
        for index in range(len(answers)):
            write = ["", "", ""]
            write[name_col] = name
            write[question_col] = question_ids[index]
            write[answer_col] = answers[index]
            writer.writerow(write)


## Question 5
def create_question_answer_relationship(
    question_file="questions.csv", answer_file="answers.csv"
):
    questions = {}
    answers = {}
    with open(question_file, "r") as question_f:
        reader = csv.reader(question_f, delimiter=",")
        question_fields = next(reader)
        question_id_col = question_fields.index("question_id")
        question_col = question_fields.index("question")
        for row in reader:
            question_id = row[question_id_col]
            question = row[question_col]
            questions[question_id] = question
            if question_id not in answers:
                answers[question_id] = []

    with open(answer_file, "r") as answer_f:
        reader = csv.reader(answer_f, delimiter=",")
        answer_fields = next(reader)
        name_col = answer_fields.index("interviewee")
        question_col = answer_fields.index("question")
        answer_col = answer_fields.index("answer")
        for row in reader:
            name = row[name_col]
            question_id = row[question_col]
            answer = row[answer_col]
            answers[question_id].append([name, answer])
    return questions, answers


def print_question_answer_relationship(all_questions, all_answers):
    for question_id in all_questions.keys():
        question = all_questions[question_id]
        answers = all_answers[question_id]
        print(f"Question ID {question_id}: {question}")
        print("Answers:")
        for answer in answers:
            name = answer[0].title()
            question_answer = answer[1].lower()
            print(f"{name} answered {question_answer}")
        print("*" * 40)

def clean_answers(questions, answers, replaced):
    replaced_ids = [id[0] for id in replaced.values()]
    question_ids = []
    for id in questions.keys():
        question_ids.append(id)
    for question_id in answers.keys():
        question_answers = answers[question_id]
        if question_id in replaced_ids:
            print(answers[question_id])
            print(answers[question_id][-1])
            answers[question_id] = [answers[question_id][-1]]
        else:
            clean_answers = sorted(question_answers, key = lambda x: x[0].lower())
            answers[question_id] = clean_answers
    return answers

def write_csv(answers, file = "answers.csv"):
    print(answers)
    with open(file, "w", newline = "") as f:
        writer = csv.writer(f, delimiter=",")
        fields = ["interviewee", "question", "answer"]
        writer.writerow(fields)
        for id in answers:
            for answer in answers[id]:
                writer.writerow(answer)
        
def validate_question_length(question):
    question_len = len(question)
    if (question_len >= 10) and (question_len <= 30):
        return True
    else:
        return False

def validate_not_empty(value):
    if value != "":
        return True
    else:
        return False
    
def validate_email(email):
    if ("@" in email) and ("." in email):
        return True
    else:
        return False
    
def main():
    ## Clear the CSV to make sure it's clean
    clear_csv()
    ## Set up beginning questions in CSV
    setup_questions_csv()
    ## Verify the questions in the CSV. Change them if needed
    replace = verify_questions()
    replace_questions(replace)
    ## Read the questions in the CSV
    read_csv()
    ## Add a question to the csv
    add_question()
    ## Set up beginning answers in CSV
    setup_answers_csv()
    ## Get answers to questions in questions.csv
    name, question_ids, answers = get_question_answers()
    ## Write answers to the csv
    append_answers(name, question_ids, answers)
    ## Get questions and answers
    questions, answers = create_question_answer_relationship()
    ## Clean answers up
    answers = clean_answers(questions, answers, replace)
    ## Print out cleaned answers
    print_question_answer_relationship(questions, answers)
    ## Rewrite CSV with cleaned answers
    write_csv(answers)

if __name__ == "__main__":
    main()