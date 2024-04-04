# Assignment 2: Automated Interviewer

## Objectives
In this assignment we will develop an application that captures data
for use in a Python program.
## Instructions
1. Start by reviewing the problem described below.
1. When you are familiar with the requirements, start to plan how you
will write the Python code.
1. As you write the code be sure to test it frequently.
1. Submit your complete assignment when you are sure you have implemented
all of the requirements.

### Basics
Let’s build an automated interviewer! The purpose of this Python program is 
to operate in a welcome booth at the Seattle Python Users conference. All 
delegates will be expected to line up at one of the many terminals and enter 
their details into the program you are going to write.

1. The program will ask each of the following questions and then display the answer. For example, it asks “what is your name” and it displays “your name is Fred”. Add more if you wish to be creative!
    1. What is your name?
    1. What is your conference ID?
    1. Which organization do you represent?
    1. What is your email address?
    1. State any food preferences?
1. The program will then prompt the user if they wish to attend the following sessions and, using conditionals, print back out confirmation of their attendance. For example, it asks "Do you wish to attend Python for beginners? (Y or N)" and the user enters Y, it displays "Ok, I've recorded your interest to attend Python for beginners." Similarly, if the user enters N, the program displays, "Ok, I've recorded your disinterest to attend Python for beginners." Feel free to be more creative!
    1. Python for beginners
    1. Database development with Python
    1. Python for data science
    1. Advanced Python for application developers
1. The automated interviewer now serves its purpose from the perspective of the user of the program. But the number of questions and answers makes it a little messy to maintain. Copy your code into a new python file, consult the documentation on tuples and lists, and rewrite the program so that a simple change to the question tuple is all that is needed to record all the relevant answers.
  1. Redesign the program so that the list of questions is stored in a tuple so that all the questions are in one place and it becomes really easy to add one.
  1. But what about the answers? How can we record the answer to every question without making any changes to the program other than adding a new question (or removing an existing question) from the tuple?
