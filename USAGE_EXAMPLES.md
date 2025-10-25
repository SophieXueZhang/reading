# Usage Examples

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the tool:
```bash
python main.py
```

## Example Session Flow

### For a Kindergarten Student

```
1. Start the program
2. Select option 1 (Start Reading Practice)
3. Choose grade level: K
4. Select passage: "The Little Red Hen"
5. Read the story carefully
6. Answer 3 comprehension questions
7. Get immediate feedback on each answer
8. View session summary showing accuracy
9. See recommendations for improvement
```

### For a 5th Grade Student

```
1. Start the program
2. Select option 1 (Start Reading Practice)
3. Choose grade level: 5
4. Select passage: "The Revolutionary World of Renewable Energy"
5. Read the informational text
6. Answer 4 advanced comprehension questions
7. Receive detailed explanations
8. View performance by question type
9. Get personalized recommendations
```

## Viewing Progress

```
1. From main menu, select option 2 (View Progress Report)
2. See:
   - Total passages read
   - Overall accuracy percentage
   - Performance by grade level
   - Recent reading sessions
   - Improvement trend
```

## Question Types by Grade Level

### Kindergarten - Grade 1
- Main Idea
- Detail
- Sequence
- Vocabulary

### Grade 2 - Grade 3
- Main Idea
- Supporting Details
- Inference
- Vocabulary in Context
- Cause and Effect
- Character Analysis

### Grade 4 - Grade 5
- Theme Analysis
- Character Development
- Author's Purpose
- Compare and Contrast
- Symbolism
- Making Connections
- Critical Thinking
- Text Structure

## Tips for Parents and Teachers

1. **Start at the Right Level**: Choose passages slightly below or at the student's current reading level for confidence building.

2. **Regular Practice**: Short, consistent practice sessions (15-20 minutes) are more effective than long, infrequent ones.

3. **Discuss Answers**: Talk about why answers are correct or incorrect. The explanations provided are great conversation starters.

4. **Track Progress**: Use the progress report to identify strengths and areas for improvement.

5. **Encourage Rereading**: It's okay to go back and reread parts of the passage before answering questions.

6. **Celebrate Growth**: Focus on improvement over time rather than just accuracy percentages.

## Sample Progress Report

```
Overall Statistics:
-----------------------------------------------------------
Total Passages Read: 12
Total Questions Answered: 38
Total Correct Answers: 31
Overall Accuracy: 81.6%

Passages by Grade Level:
-----------------------------------------------------------
Grade 2: 5 passage(s)
Grade 3: 7 passage(s)

Recent Sessions:
-----------------------------------------------------------
- The Friendship Garden (Grade 2)
  Accuracy: 100.0% (3/3)
- Honeybees: Nature's Helpers (Grade 3)
  Accuracy: 66.7% (2/3)
- The Mystery of the Missing Books (Grade 3)
  Accuracy: 100.0% (3/3)

Trend: Improving! Accuracy increased by 8.3%
```

## Customization Ideas

### Adding Your Own Passages

1. Open `src/reading_passages.py`
2. Add new passage to the `PASSAGES` list
3. Follow the existing format:
   - Unique ID
   - Title
   - Grade level
   - Type (story, informational, poetry)
   - Content

### Adding Questions

1. Open `src/questions.py`
2. Add questions to the `QUESTIONS` dictionary
3. Use the passage ID as the key
4. Include:
   - Question type
   - Question text
   - Multiple choice options
   - Correct answer
   - Explanation

## Educational Standards Alignment

This tool supports key reading comprehension skills aligned with Common Core State Standards:

- **CCSS.ELA-LITERACY.RL.K-5**: Reading Literature
- **CCSS.ELA-LITERACY.RI.K-5**: Reading Informational Text
- **CCSS.ELA-LITERACY.RF.K-5**: Reading Foundational Skills

Specific skills addressed:
- Main idea and key details
- Making inferences
- Vocabulary acquisition
- Text structure analysis
- Character and theme analysis
- Integration of knowledge and ideas
