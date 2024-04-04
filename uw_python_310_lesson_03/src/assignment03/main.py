import csv


## Question 1
def clear_csv(file="questions.csv"):
    with open(file, "w") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows([])


def setup_questions_csv(file="questions.csv"):
    with open(file, "w") as f:
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


def add_question(file="questions.csv"):
    question = input("Please enter the question you'd like to add to the database: ")
    question_id = generate_question_id()
    with open(file, "a") as f:
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
    with open(file, "w") as f:
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
            question_ids.append(question_id)
            answers.append(answer)
    return name, question_ids, answers


def write_answers(name, question_ids, answers, file="answers.csv"):
    with open(file, "r") as f:
        reader = csv.reader(f, delimiter=",")
        fields = next(reader)
    with open(file, "a") as f:
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


def main():
    clear_csv()
    ## Question 1
    setup_questions_csv()
    ## Question 2
    read_csv()
    add_question()
    ## Question 3
    setup_answers_csv()
    ## Question 4
    read_csv(file="answers.csv")
    name, question_ids, answers = get_question_answers()
    write_answers(name, question_ids, answers)
    ## Question 5
    questions, answers = create_question_answer_relationship()
    print_question_answer_relationship(questions, answers)


if __name__ == "__main__":
    main()
