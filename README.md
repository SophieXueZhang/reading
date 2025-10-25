# Reading Comprehension Tool for Elementary Students

An interactive tool designed to improve reading comprehension skills for American elementary school students (Grades K-5).

## Features

- **Grade-Appropriate Content**: Reading passages tailored for different grade levels (K-5)
- **Multiple Question Types**:
  - Main Idea
  - Supporting Details
  - Inference
  - Vocabulary in Context
  - Sequence of Events
  - Author's Purpose
- **Instant Feedback**: Immediate evaluation with explanations
- **Progress Tracking**: Monitor student performance over time
- **Diverse Content**: Stories, informational texts, and poetry

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the tool:
```bash
python main.py
```

Follow the interactive prompts to:
1. Select a grade level
2. Choose a reading passage
3. Read and answer comprehension questions
4. Get instant feedback and explanations
5. View your progress

## Project Structure

```
reading-comprehension-tool/
├── main.py                  # Main entry point
├── src/
│   ├── reading_passages.py  # Reading passage database
│   ├── questions.py          # Question generation and management
│   ├── evaluator.py          # Answer evaluation system
│   ├── progress_tracker.py   # Progress tracking
│   └── difficulty_levels.py  # Grade level management
└── data/
    └── user_progress.json    # User progress data
```

## Educational Benefits

- Improves reading comprehension skills
- Builds vocabulary
- Develops critical thinking
- Encourages independent reading
- Provides structured practice
- Tracks learning progress

## License

MIT License
