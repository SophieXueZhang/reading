#!/usr/bin/env python3
"""
Reading Comprehension Tool for Elementary Students
Main entry point
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    COLOR_SUPPORT = True
except ImportError:
    COLOR_SUPPORT = False
    print("Note: Install 'colorama' for colored output (pip install colorama)")

from difficulty_levels import DifficultyLevel
from reading_passages import PassageDatabase, ReadingPassage
from questions import QuestionBank
from evaluator import Evaluator
from progress_tracker import ProgressTracker


class ReadingComprehensionTool:
    """Main application class"""

    def __init__(self):
        self.tracker = ProgressTracker()
        self.evaluator = Evaluator()

    def print_colored(self, text, color=None, style=None):
        """Print colored text if colorama is available"""
        if COLOR_SUPPORT and color:
            print(color + (style or '') + text + Style.RESET_ALL)
        else:
            print(text)

    def print_header(self, text):
        """Print a formatted header"""
        self.print_colored("\n" + "=" * 60, Fore.CYAN, Style.BRIGHT)
        self.print_colored(text.center(60), Fore.CYAN, Style.BRIGHT)
        self.print_colored("=" * 60 + "\n", Fore.CYAN, Style.BRIGHT)

    def print_divider(self):
        """Print a divider line"""
        self.print_colored("-" * 60, Fore.BLUE)

    def display_welcome(self):
        """Display welcome message"""
        self.print_header("Reading Comprehension Tool")
        self.print_colored("Welcome! This tool helps improve reading comprehension skills.", Fore.GREEN)
        self.print_colored("You will read passages and answer questions about them.\n", Fore.GREEN)

    def display_main_menu(self):
        """Display main menu and get user choice"""
        self.print_divider()
        print("\nMain Menu:")
        print("1. Start Reading Practice")
        print("2. View Progress Report")
        print("3. Help & Instructions")
        print("4. Exit")
        self.print_divider()

        while True:
            choice = input("\nEnter your choice (1-4): ").strip()
            if choice in ['1', '2', '3', '4']:
                return choice
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

    def select_grade_level(self):
        """Let user select their grade level"""
        self.print_header("Select Grade Level")

        levels = DifficultyLevel.get_all_levels()
        for grade, info in levels.items():
            print(f"{grade}. {info['name']} - {info['description']}")

        self.print_divider()

        while True:
            grade = input("\nEnter your grade level (K, 1, 2, 3, 4, 5): ").strip().upper()
            if DifficultyLevel.is_valid_level(grade):
                return grade
            print("Invalid grade level. Please enter K, 1, 2, 3, 4, or 5.")

    def select_passage(self, grade):
        """Let user select a reading passage"""
        self.print_header(f"Grade {grade} Reading Passages")

        passages = PassageDatabase.get_passages_by_grade(grade)

        if not passages:
            self.print_colored("No passages available for this grade level.", Fore.RED)
            return None

        for i, passage in enumerate(passages, 1):
            print(f"{i}. {passage['title']} ({passage['type'].title()})")

        self.print_divider()

        while True:
            try:
                choice = input(f"\nSelect a passage (1-{len(passages)}): ").strip()
                idx = int(choice) - 1
                if 0 <= idx < len(passages):
                    return passages[idx]['id']
            except ValueError:
                pass
            print(f"Invalid choice. Please enter a number between 1 and {len(passages)}.")

    def display_passage(self, passage):
        """Display a reading passage"""
        self.print_header(passage.title)
        self.print_colored(f"Grade Level: {passage.grade} | Type: {passage.type.title()}\n", Fore.YELLOW)

        # Display passage with word wrap
        words = passage.content.split()
        line = ""
        for word in words:
            if len(line) + len(word) + 1 <= 70:
                line += word + " "
            else:
                print(line)
                line = word + " "
        if line:
            print(line)

        print()
        self.print_divider()
        input("\nPress Enter when you're done reading...")

    def ask_questions(self, passage_id):
        """Ask comprehension questions and collect answers"""
        questions = QuestionBank.get_questions_for_passage(passage_id)

        if not questions:
            self.print_colored("No questions available for this passage.", Fore.RED)
            return []

        results = []

        self.print_header("Comprehension Questions")

        for i, question in enumerate(questions, 1):
            print(f"\nQuestion {i} of {len(questions)} ({question.type})")
            self.print_divider()
            print(f"\n{question.text}\n")

            for key, value in sorted(question.options.items()):
                print(f"{key}. {value}")

            # Get user's answer
            while True:
                answer = input("\nYour answer (A, B, C, or D): ").strip().upper()
                if answer in ['A', 'B', 'C', 'D']:
                    break
                print("Invalid input. Please enter A, B, C, or D.")

            # Evaluate answer
            result = self.evaluator.evaluate_answer(question, answer)
            results.append(result)

            # Show immediate feedback
            if result['correct']:
                self.print_colored(f"\n{result['feedback']}", Fore.GREEN, Style.BRIGHT)
            else:
                self.print_colored(f"\n{result['feedback']}", Fore.RED, Style.BRIGHT)

            self.print_colored(f"Explanation: {result['explanation']}", Fore.CYAN)

            if i < len(questions):
                input("\nPress Enter for the next question...")

        return results

    def display_session_summary(self, results):
        """Display summary of the reading session"""
        summary = self.evaluator.generate_performance_summary(results)

        self.print_header("Session Summary")

        print(f"Total Questions: {summary['total_questions']}")
        print(f"Correct Answers: {summary['correct_answers']}")
        self.print_colored(f"Accuracy: {summary['accuracy']:.1f}%", Fore.YELLOW, Style.BRIGHT)

        performance_level = self.evaluator.get_performance_level(summary['accuracy'])
        self.print_colored(f"\n{performance_level}", Fore.GREEN, Style.BRIGHT)

        # Performance by question type
        if summary['performance_by_type']:
            print("\nPerformance by Question Type:")
            self.print_divider()
            for q_type, stats in summary['performance_by_type'].items():
                print(f"{q_type}: {stats['correct']}/{stats['total']} ({stats['accuracy']:.1f}%)")

        # Recommendations
        recommendations = self.evaluator.get_recommendations(summary['performance_by_type'])
        if recommendations:
            print("\nRecommendations for Improvement:")
            self.print_divider()
            for i, rec in enumerate(recommendations, 1):
                print(f"{i}. {rec}")

        print()
        self.print_divider()

    def start_reading_practice(self):
        """Start a reading practice session"""
        # Select grade level
        grade = self.select_grade_level()

        # Select passage
        passage_id = self.select_passage(grade)
        if not passage_id:
            return

        # Get and display passage
        passage = PassageDatabase.get_passage_by_id(passage_id)
        self.display_passage(passage)

        # Ask questions
        results = self.ask_questions(passage_id)

        if results:
            # Display summary
            self.display_session_summary(results)

            # Record progress
            self.tracker.record_session(grade, passage_id, passage.title, results)
            self.print_colored("\nYour progress has been saved!", Fore.GREEN)

    def view_progress_report(self):
        """Display progress report"""
        self.print_header("Progress Report")

        stats = self.tracker.get_overall_stats()

        if stats['total_passages_read'] == 0:
            self.print_colored("No reading sessions completed yet.", Fore.YELLOW)
            self.print_colored("Start practicing to see your progress!", Fore.YELLOW)
            return

        print("Overall Statistics:")
        self.print_divider()
        print(f"Total Passages Read: {stats['total_passages_read']}")
        print(f"Total Questions Answered: {stats['total_questions_answered']}")
        print(f"Total Correct Answers: {stats['total_correct']}")
        self.print_colored(f"Overall Accuracy: {stats['overall_accuracy']:.1f}%",
                          Fore.YELLOW, Style.BRIGHT)

        print("\nPassages by Grade Level:")
        self.print_divider()
        for grade, count in stats['passages_by_grade'].items():
            if count > 0:
                print(f"Grade {grade}: {count} passage(s)")

        # Recent sessions
        recent = self.tracker.get_recent_sessions()
        if recent:
            print("\nRecent Sessions:")
            self.print_divider()
            for session in recent:
                print(f"- {session['passage_title']} (Grade {session['grade']})")
                print(f"  Accuracy: {session['accuracy']:.1f}% ({session['correct_answers']}/{session['total_questions']})")

        # Improvement trend
        trend = self.tracker.get_improvement_trend()
        print(f"\nTrend: {trend}")

        print()
        self.print_divider()

    def show_help(self):
        """Display help and instructions"""
        self.print_header("Help & Instructions")

        print("How to Use This Tool:")
        print()
        print("1. Start Reading Practice:")
        print("   - Choose your grade level (K-5)")
        print("   - Select a passage to read")
        print("   - Read carefully and take your time")
        print("   - Answer comprehension questions")
        print("   - Get immediate feedback and explanations")
        print()
        print("2. View Progress Report:")
        print("   - See your overall statistics")
        print("   - Track improvement over time")
        print("   - Review recent reading sessions")
        print()
        print("3. Question Types:")
        print("   - Main Idea: What is the passage mostly about?")
        print("   - Supporting Details: Specific facts from the text")
        print("   - Inference: What can you figure out from clues?")
        print("   - Vocabulary: What do words mean in context?")
        print("   - Sequence: What happened in order?")
        print("   - Cause and Effect: Why did things happen?")
        print("   - Theme: What is the deeper message?")
        print("   - Character Analysis: What are characters like?")
        print()
        print("Tips for Success:")
        print("   - Read the passage slowly and carefully")
        print("   - Think about what you read")
        print("   - Reread parts you don't understand")
        print("   - Use context clues for unknown words")
        print("   - Practice regularly to improve!")
        print()
        self.print_divider()

    def run(self):
        """Main application loop"""
        self.display_welcome()

        while True:
            choice = self.display_main_menu()

            if choice == '1':
                self.start_reading_practice()
            elif choice == '2':
                self.view_progress_report()
            elif choice == '3':
                self.show_help()
            elif choice == '4':
                self.print_colored("\nThank you for using Reading Comprehension Tool!", Fore.GREEN, Style.BRIGHT)
                self.print_colored("Keep reading and learning!\n", Fore.GREEN)
                break

            input("\nPress Enter to continue...")


def main():
    """Main entry point"""
    try:
        app = ReadingComprehensionTool()
        app.run()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
