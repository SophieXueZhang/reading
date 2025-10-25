"""
Progress tracking system for student performance
"""

import json
import os
from datetime import datetime


class ProgressTracker:
    """Tracks and manages student reading comprehension progress"""

    def __init__(self, data_file='data/user_progress.json'):
        self.data_file = data_file
        self.progress_data = self._load_progress()

    def _load_progress(self):
        """Load progress data from file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return self._create_new_progress_data()
        return self._create_new_progress_data()

    def _create_new_progress_data(self):
        """Create new progress data structure"""
        return {
            'sessions': [],
            'overall_stats': {
                'total_passages_read': 0,
                'total_questions_answered': 0,
                'total_correct': 0,
                'passages_by_grade': {
                    'K': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0
                }
            }
        }

    def save_progress(self):
        """Save progress data to file"""
        # Ensure data directory exists
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)

        with open(self.data_file, 'w') as f:
            json.dump(self.progress_data, f, indent=2)

    def record_session(self, grade, passage_id, passage_title, results):
        """
        Record a completed reading session

        Args:
            grade: Grade level
            passage_id: ID of the passage
            passage_title: Title of the passage
            results: List of question results
        """
        session = {
            'date': datetime.now().isoformat(),
            'grade': grade,
            'passage_id': passage_id,
            'passage_title': passage_title,
            'total_questions': len(results),
            'correct_answers': sum(1 for r in results if r['correct']),
            'accuracy': (sum(1 for r in results if r['correct']) / len(results) * 100) if results else 0,
            'results': results
        }

        self.progress_data['sessions'].append(session)

        # Update overall stats
        self.progress_data['overall_stats']['total_passages_read'] += 1
        self.progress_data['overall_stats']['total_questions_answered'] += len(results)
        self.progress_data['overall_stats']['total_correct'] += sum(1 for r in results if r['correct'])
        self.progress_data['overall_stats']['passages_by_grade'][grade] += 1

        self.save_progress()

    def get_overall_stats(self):
        """Get overall statistics"""
        stats = self.progress_data['overall_stats']

        if stats['total_questions_answered'] > 0:
            overall_accuracy = (stats['total_correct'] / stats['total_questions_answered']) * 100
        else:
            overall_accuracy = 0

        return {
            'total_passages_read': stats['total_passages_read'],
            'total_questions_answered': stats['total_questions_answered'],
            'total_correct': stats['total_correct'],
            'overall_accuracy': overall_accuracy,
            'passages_by_grade': stats['passages_by_grade']
        }

    def get_recent_sessions(self, limit=5):
        """Get recent reading sessions"""
        sessions = self.progress_data['sessions']
        return sessions[-limit:] if sessions else []

    def get_grade_performance(self, grade):
        """Get performance statistics for a specific grade"""
        grade_sessions = [s for s in self.progress_data['sessions'] if s['grade'] == grade]

        if not grade_sessions:
            return None

        total_questions = sum(s['total_questions'] for s in grade_sessions)
        total_correct = sum(s['correct_answers'] for s in grade_sessions)
        avg_accuracy = (total_correct / total_questions * 100) if total_questions > 0 else 0

        return {
            'passages_read': len(grade_sessions),
            'total_questions': total_questions,
            'total_correct': total_correct,
            'average_accuracy': avg_accuracy
        }

    def get_improvement_trend(self):
        """Analyze if the student is improving over time"""
        sessions = self.progress_data['sessions']

        if len(sessions) < 2:
            return "Not enough data to determine trend"

        # Compare first half vs second half
        mid_point = len(sessions) // 2
        first_half = sessions[:mid_point]
        second_half = sessions[mid_point:]

        first_half_avg = sum(s['accuracy'] for s in first_half) / len(first_half)
        second_half_avg = sum(s['accuracy'] for s in second_half) / len(second_half)

        improvement = second_half_avg - first_half_avg

        if improvement > 5:
            return f"Improving! Accuracy increased by {improvement:.1f}%"
        elif improvement < -5:
            return f"Declining. Accuracy decreased by {abs(improvement):.1f}%"
        else:
            return "Stable performance"
