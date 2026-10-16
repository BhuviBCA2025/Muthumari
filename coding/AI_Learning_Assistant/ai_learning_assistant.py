# ==========================================
# AI POWERED LEARNING ASSISTANT
# No API Key | No External Libraries
# ==========================================

import random

def show_title():
    print("\n" + "=" * 45)
    print("     AI LEARNING ASSISTANT")
    print("       Learn Smart Every Day!")
    print("=" * 45)

def ai_tutor():
    topic = input("\nEnter a topic: ").strip().lower()

    lessons = {
        "python": """
PYTHON PROGRAMMING

Definition:
Python is a high-level programming language.

Features:
1. Simple and easy to learn.
2. Supports object-oriented programming.
3. Used in AI, automation and web development.

Example:
name = "Rajesh"
print("Hello", name)

Output:
Hello Rajesh
""",
        "c#": """
C# PROGRAMMING

Definition:
C# is an object-oriented programming language
developed by Microsoft.

Features:
1. Strongly typed language.
2. Supports OOP concepts.
3. Used in .NET applications.

Example:
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Hello World");
    }
}

Output:
Hello World
""",
        "oops": """
OOP CONCEPTS

1. Encapsulation:
   Wrapping data and methods into a class.

2. Inheritance:
   Reusing properties and methods of another class.

3. Polymorphism:
   One interface can have different implementations.

4. Abstraction:
   Hiding implementation details and exposing
   essential features.
""",
        "sql": """
SQL

Definition:
SQL is used to manage data in relational databases.

Example:
SELECT * FROM Employees;

This query retrieves all columns and rows
from the Employees table.
""",
        "html": """
HTML

Definition:
HTML stands for HyperText Markup Language.
It structures web pages.

Example:
<h1>Hello World</h1>
<p>Welcome to learning!</p>
"""
    }

    if topic in lessons:
        print(lessons[topic])
    else:
        print("\nNo predefined lesson found for:", topic)
        print("Try: Python, C#, OOPS, SQL or HTML.")

def generate_notes():
    topic = input("\nEnter a topic for notes: ")
    print("\nSTUDY NOTES:", topic)
    print("-" * 35)
    print("1. Learn the definition of", topic)
    print("2. Understand the important concepts.")
    print("3. Study the syntax and examples.")
    print("4. Practice with real-world problems.")
    print("5. Revise and answer practice questions.")

def generate_quiz():
    questions = [
        {
            "q": "Which language is commonly used with .NET?",
            "options": ["A. C#", "B. HTML", "C. CSS", "D. SQL"],
            "answer": "A"
        },
        {
            "q": "Which SQL command retrieves data?",
            "options": ["A. INSERT", "B. SELECT",
                        "C. DELETE", "D. UPDATE"],
            "answer": "B"
        },
        {
            "q": "What does HTML structure?",
            "options": ["A. Databases", "B. Networks",
                        "C. Web pages", "D. Operating systems"],
            "answer": "C"
        }
    ]

    random.shuffle(questions)
    score = 0

    print("\nQUIZ TIME!")

    for item in questions:
        print("\n" + item["q"])
        for option in item["options"]:
            print(option)

        answer = input("Your answer: ").strip().upper()

        if answer == item["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. Correct answer:",
                  item["answer"])

    print(f"\nYour score: {score}/{len(questions)}")

def study_plan():
    print("\n7-DAY PROGRAMMING STUDY PLAN")
    plan = [
        "Day 1: Fundamentals",
        "Day 2: Variables and data types",
        "Day 3: Conditions and loops",
        "Day 4: Methods and functions",
        "Day 5: OOP concepts",
        "Day 6: Practical coding exercises",
        "Day 7: Revision and quiz"
    ]

    for day in plan:
        print(day)

def main():
    while True:
        show_title()
        print("1. AI Tutor")
        print("2. Generate Study Notes")
        print("3. Practice Quiz")
        print("4. Create Study Plan")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            ai_tutor()
        elif choice == "2":
            generate_notes()
        elif choice == "3":
            generate_quiz()
        elif choice == "4":
            study_plan()
        elif choice == "5":
            print("Thank you! Keep learning every day.")
            break
        else:
            print("Invalid choice. Select 1 to 5.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
