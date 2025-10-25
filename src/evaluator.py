"""
Answer evaluation and feedback system
"""

class Evaluator:
    """Evaluates student answers and provides feedback"""

    @staticmethod
    def evaluate_answer(question, user_answer):
        """
        Evaluate a user's answer to a question

        Args:
            question: Question object
            user_answer: User's answer (A, B, C, or D)

        Returns:
            dict with 'correct', 'feedback', and 'explanation'
        """
        is_correct = question.check_answer(user_answer)

        if is_correct:
            feedback = "Excellent! That's correct!"
        else:
            feedback = f"Not quite. The correct answer is {question.correct_answer}."

        return {
            'correct': is_correct,
            'feedback': feedback,
            'explanation': question.explanation,
            'question_type': question.type
        }

    @staticmethod
    def generate_performance_summary(results):
        """
        Generate a summary of student performance

        Args:
            results: List of evaluation results

        Returns:
            dict with performance metrics
        """
        if not results:
            return {
                'total_questions': 0,
                'correct_answers': 0,
                'accuracy': 0,
                'performance_by_type': {}
            }

        total = len(results)
        correct = sum(1 for r in results if r['correct'])
        accuracy = (correct / total) * 100 if total > 0 else 0

        # Performance by question type
        type_performance = {}
        for result in results:
            q_type = result['question_type']
            if q_type not in type_performance:
                type_performance[q_type] = {'correct': 0, 'total': 0}

            type_performance[q_type]['total'] += 1
            if result['correct']:
                type_performance[q_type]['correct'] += 1

        # Calculate accuracy for each type
        for q_type in type_performance:
            stats = type_performance[q_type]
            stats['accuracy'] = (stats['correct'] / stats['total']) * 100

        return {
            'total_questions': total,
            'correct_answers': correct,
            'accuracy': accuracy,
            'performance_by_type': type_performance
        }

    @staticmethod
    def get_performance_level(accuracy):
        """
        Get performance level description based on accuracy

        Args:
            accuracy: Percentage accuracy (0-100)

        Returns:
            str describing performance level
        """
        if accuracy >= 90:
            return "Outstanding! You have excellent reading comprehension skills!"
        elif accuracy >= 80:
            return "Great job! You're doing very well!"
        elif accuracy >= 70:
            return "Good work! Keep practicing to improve further."
        elif accuracy >= 60:
            return "You're making progress. Try reading more carefully."
        else:
            return "Keep practicing! Reading comprehension takes time to develop."

    @staticmethod
    def get_recommendations(performance_by_type):
        """
        Get personalized recommendations based on performance

        Args:
            performance_by_type: Dict of performance by question type

        Returns:
            List of recommendation strings
        """
        recommendations = []

        for q_type, stats in performance_by_type.items():
            if stats['accuracy'] < 70:
                if q_type == 'Main Idea':
                    recommendations.append(
                        "Practice identifying the main idea by asking: "
                        "'What is this passage mostly about?'"
                    )
                elif q_type == 'Detail' or q_type == 'Supporting Details':
                    recommendations.append(
                        "Improve detail recognition by reading more carefully "
                        "and underlining important facts."
                    )
                elif q_type == 'Inference':
                    recommendations.append(
                        "Work on making inferences by thinking about what the "
                        "text suggests but doesn't directly say."
                    )
                elif q_type == 'Vocabulary' or q_type == 'Vocabulary in Context':
                    recommendations.append(
                        "Build vocabulary by using context clues to figure out "
                        "word meanings."
                    )
                elif q_type == 'Sequence':
                    recommendations.append(
                        "Practice sequence by paying attention to time order words "
                        "like 'first,' 'then,' 'next,' and 'finally.'"
                    )
                elif q_type == 'Cause and Effect':
                    recommendations.append(
                        "Understand cause and effect by looking for words like "
                        "'because,' 'so,' 'since,' and 'therefore.'"
                    )
                elif q_type == 'Theme' or q_type == 'Theme Analysis':
                    recommendations.append(
                        "Identify themes by thinking about the deeper message or "
                        "lesson in the story."
                    )
                elif q_type == 'Character Analysis' or q_type == 'Character Traits':
                    recommendations.append(
                        "Analyze characters by paying attention to what they say, "
                        "do, and how they change."
                    )

        if not recommendations:
            recommendations.append(
                "You're doing great! Continue practicing with different types "
                "of texts to maintain your skills."
            )

        return recommendations
