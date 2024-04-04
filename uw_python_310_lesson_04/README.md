# Assignment 4: Validating data

## Objectives
In this assignment you will learn how to validate data in your
automated interview.

## Instructions
1. Start by reviewing the entire problem described below.
1. When you are familiar with the requirements, start to plan how you will write the Python code.
1. As you write the code be sure to test it frequently.
1. Submit your complete assignment when you are sure you have implemented all of the requirements.

### Basics
You will recall that from last week's assignment we have two csv files:

Firstly, `questions.csv`
```csv
question_id,question
12,What is your phone number?
10,What is your email?
```
Secondly, `answers.csv`
```csv
interviewee,question_id,answer
Anubhaw,12,(555) 555 - 5555
Anubhaw,10,arya0@uw.edu
```

In this week's assignment we are going to modify our previous scripts to add additional complexity, including validation and exception tracking code.

### Part 1
We'll start by modifying the first program (which printed out the questions and added a new one).
1. Read in all the questions in the csv
1. For each question
    1. Ask the user to validate that the question is correct. Validate the input is either yes or no.
        1. If yes, it means the user is happy with the wording. No further action is needed
        1. If no, ask the user to input the new question that'll replace the current one. This question must be 10 to 30 characters long.
    2. Ask the user if the question is needed or not. Validate the input is either yes or no.
        1. If the user wants to delete the question, ask if they are sure. Validate the user's input, and then either delete the question or move on.
1. Now that all the current questions have been audited, prints them all out to the console, formatted nicely (try playing around with [string formatting](https://stackabuse.com/padding-strings-in-python/#format)).
1. Asks the user for a new question to add to the CSV file
    1. Validate that the question is between 10 and 30 character long
1. Save all the questions back into `questions.csv` 

HINT: You may want to use write mode instead of append mode when writing the final file.


### Part 2
Now we'll modify the second program (which runs the interview and saves the answer):
1. Add code to make sure that the email address is provided and that it is in a valid
email format. 
1. Make sure that if the email fails any validation that the incorrect value is displayed, and
that the user is asked to provide the email address again.
1. Verify that answers have been provided to each question. If an answer is missing, reprompt
the user and save the answer.

REMINDER: Take care to maintain the relationships between questions and answers.


### Part 3
Finally, we'll modify the third program (which printed out the question and corresponding answers)
1. Read in all questions in the `questions.csv` file
1. Read in all answers in the `answers.csv` file
1. Delete any answers that no longer have a valid question (see the deleted question from Part 1) 
1. Prints out the questions, one at a time, along with the corresponding set of answers from all interviewees. Format it nicely!
    1. Answers must be sorted by the interviewee's names, alphabetically.
3. Updates the `answers.csv` file now that the answers have been cleaned up.
