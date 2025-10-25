#!/usr/bin/env python3
"""
Demo script to showcase the Reading Comprehension Tool
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from colorama import init, Fore, Style
init(autoreset=True)

from difficulty_levels import DifficultyLevel
from reading_passages import PassageDatabase, ReadingPassage
from questions import QuestionBank
from evaluator import Evaluator

def print_header(text):
    print(f"\n{Fore.CYAN}{Style.BRIGHT}{'='*70}")
    print(f"{text.center(70)}")
    print(f"{'='*70}{Style.RESET_ALL}\n")

def print_divider():
    print(f"{Fore.BLUE}{'-'*70}{Style.RESET_ALL}")

def demo_passages():
    """Show available passages by grade"""
    print_header("Available Reading Passages")

    for grade in ['K', '1', '2', '3', '4', '5']:
        passages = PassageDatabase.get_passages_by_grade(grade)
        if passages:
            print(f"\n{Fore.YELLOW}{Style.BRIGHT}Grade {grade}:{Style.RESET_ALL}")
            for p in passages:
                print(f"  • {p['title']} ({p['type']})")

def demo_passage_content():
    """Show a sample passage and questions"""
    print_header("Sample Passage Demo")

    # Get a Grade 1 passage
    passage = PassageDatabase.get_passage_by_id('g1_1')

    print(f"{Fore.YELLOW}Title: {passage.title}")
    print(f"Grade: {passage.grade} | Type: {passage.type.title()}{Style.RESET_ALL}\n")

    print(passage.content)
    print_divider()

    # Show questions
    questions = QuestionBank.get_questions_for_passage('g1_1')

    print(f"\n{Fore.CYAN}{Style.BRIGHT}Comprehension Questions:{Style.RESET_ALL}\n")

    for i, q in enumerate(questions, 1):
        print(f"{Fore.GREEN}Question {i} ({q.type}):{Style.RESET_ALL}")
        print(f"{q.text}\n")
        for key, value in sorted(q.options.items()):
            print(f"  {key}. {value}")
        print(f"\n{Fore.YELLOW}Correct Answer: {q.correct_answer}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Explanation: {q.explanation}{Style.RESET_ALL}\n")
        print_divider()

def demo_evaluation():
    """Show evaluation and feedback system"""
    print_header("Evaluation System Demo")

    evaluator = Evaluator()

    # Sample question
    questions = QuestionBank.get_questions_for_passage('g1_1')
    question = questions[0]

    print(f"{Fore.CYAN}Question:{Style.RESET_ALL} {question.text}\n")

    # Test correct answer
    print(f"{Fore.GREEN}{Style.BRIGHT}Testing CORRECT answer:{Style.RESET_ALL}")
    result = evaluator.evaluate_answer(question, question.correct_answer)
    print(f"Feedback: {result['feedback']}")
    print(f"Explanation: {result['explanation']}\n")

    # Test wrong answer
    print(f"{Fore.RED}{Style.BRIGHT}Testing WRONG answer:{Style.RESET_ALL}")
    wrong_answers = [a for a in ['A', 'B', 'C', 'D'] if a != question.correct_answer]
    result = evaluator.evaluate_answer(question, wrong_answers[0])
    print(f"Feedback: {result['feedback']}")
    print(f"Explanation: {result['explanation']}\n")

def demo_grade_levels():
    """Show grade level information"""
    print_header("Grade Level Difficulty System")

    levels = DifficultyLevel.get_all_levels()

    for grade, info in levels.items():
        print(f"{Fore.YELLOW}{Style.BRIGHT}Grade {grade}: {info['name']}{Style.RESET_ALL}")
        print(f"  {info['description']}")
        print(f"  Word Count Range: {info['word_count_range']}")
        print(f"  Complexity: {info['complexity']}")
        print()

def main():
    """Run all demos"""
    print_header("Reading Comprehension Tool - Demo")
    print(f"{Fore.GREEN}This demo showcases the features of the reading tool{Style.RESET_ALL}\n")

    demos = [
        ("1. Grade Level System", demo_grade_levels),
        ("2. Available Passages", demo_passages),
        ("3. Sample Passage & Questions", demo_passage_content),
        ("4. Evaluation System", demo_evaluation),
    ]

    for title, demo_func in demos:
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}>>> {title}{Style.RESET_ALL}")
        demo_func()

    print_header("Demo Complete")
    print(f"{Fore.GREEN}To use the full interactive tool, run: python main.py{Style.RESET_ALL}\n")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nDemo interrupted. Goodbye!")
        sys.exit(0)
