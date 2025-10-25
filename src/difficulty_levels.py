"""
Difficulty level management for different grade levels
"""

class DifficultyLevel:
    """Manages difficulty levels for different grades"""

    LEVELS = {
        'K': {
            'name': 'Kindergarten',
            'description': 'Simple sentences, basic vocabulary',
            'word_count_range': (20, 50),
            'complexity': 'very_simple'
        },
        '1': {
            'name': 'Grade 1',
            'description': 'Short stories with simple plots',
            'word_count_range': (50, 100),
            'complexity': 'simple'
        },
        '2': {
            'name': 'Grade 2',
            'description': 'Developing stories with clear sequence',
            'word_count_range': (100, 150),
            'complexity': 'basic'
        },
        '3': {
            'name': 'Grade 3',
            'description': 'Stories with multiple characters and events',
            'word_count_range': (150, 250),
            'complexity': 'intermediate'
        },
        '4': {
            'name': 'Grade 4',
            'description': 'Complex narratives and informational texts',
            'word_count_range': (250, 400),
            'complexity': 'advanced'
        },
        '5': {
            'name': 'Grade 5',
            'description': 'Advanced texts with abstract concepts',
            'word_count_range': (400, 600),
            'complexity': 'very_advanced'
        }
    }

    @classmethod
    def get_level_info(cls, grade):
        """Get information about a specific grade level"""
        return cls.LEVELS.get(grade.upper(), None)

    @classmethod
    def get_all_levels(cls):
        """Get all available grade levels"""
        return cls.LEVELS

    @classmethod
    def is_valid_level(cls, grade):
        """Check if a grade level is valid"""
        return grade.upper() in cls.LEVELS
