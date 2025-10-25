"""
Question generation and management system
"""

class Question:
    """Represents a single comprehension question"""

    def __init__(self, question_id, passage_id, question_type, question_text,
                 options, correct_answer, explanation):
        self.id = question_id
        self.passage_id = passage_id
        self.type = question_type
        self.text = question_text
        self.options = options
        self.correct_answer = correct_answer
        self.explanation = explanation

    def check_answer(self, user_answer):
        """Check if the user's answer is correct"""
        return user_answer.upper() == self.correct_answer.upper()


class QuestionBank:
    """Database of comprehension questions for each passage"""

    QUESTIONS = {
        # Kindergarten - The Little Red Hen
        'k1': [
            {
                'id': 'k1_q1',
                'type': 'Main Idea',
                'question': 'What is this story mainly about?',
                'options': {
                    'A': 'A hen who plants wheat',
                    'B': 'A hen who does all the work herself',
                    'C': 'A cat and dog who are lazy',
                    'D': 'Making bread'
                },
                'answer': 'B',
                'explanation': 'The main idea is that the hen did all the work by herself because no one would help her.'
            },
            {
                'id': 'k1_q2',
                'type': 'Detail',
                'question': 'What did the hen find?',
                'options': {
                    'A': 'Bread',
                    'B': 'Seeds',
                    'C': 'Wheat',
                    'D': 'Flowers'
                },
                'answer': 'B',
                'explanation': 'At the beginning of the story, the hen found some seeds.'
            },
            {
                'id': 'k1_q3',
                'type': 'Sequence',
                'question': 'What did the hen do after she cut the wheat?',
                'options': {
                    'A': 'She planted more seeds',
                    'B': 'She made bread',
                    'C': 'She asked for help',
                    'D': 'She gave it to the cat'
                },
                'answer': 'B',
                'explanation': 'After cutting the wheat, the hen made bread from it.'
            }
        ],

        # Kindergarten - Colors in Nature
        'k2': [
            {
                'id': 'k2_q1',
                'type': 'Main Idea',
                'question': 'What is this passage mainly about?',
                'options': {
                    'A': 'Rainbows',
                    'B': 'The sky',
                    'C': 'Colors in nature',
                    'D': 'Flowers'
                },
                'answer': 'C',
                'explanation': 'The whole passage talks about different colors we see in nature.'
            },
            {
                'id': 'k2_q2',
                'type': 'Detail',
                'question': 'What color is the sun?',
                'options': {
                    'A': 'Blue',
                    'B': 'Green',
                    'C': 'Yellow',
                    'D': 'Red'
                },
                'answer': 'C',
                'explanation': 'The passage says "The sun is yellow."'
            }
        ],

        # Grade 1 - Sam and the Lost Puppy
        'g1_1': [
            {
                'id': 'g1_1_q1',
                'type': 'Main Idea',
                'question': 'What is the main idea of this story?',
                'options': {
                    'A': 'Sam found a lost puppy and helped find its owner',
                    'B': 'Sam got a new puppy',
                    'C': 'Sam walked home from school',
                    'D': 'A girl lost her puppy'
                },
                'answer': 'A',
                'explanation': 'The story is about Sam finding a lost puppy and doing the right thing by helping find its owner.'
            },
            {
                'id': 'g1_1_q2',
                'type': 'Character Traits',
                'question': 'Which word best describes Sam?',
                'options': {
                    'A': 'Mean',
                    'B': 'Helpful',
                    'C': 'Lazy',
                    'D': 'Silly'
                },
                'answer': 'B',
                'explanation': 'Sam was helpful because he took care of the puppy and helped find its owner.'
            },
            {
                'id': 'g1_1_q3',
                'type': 'Inference',
                'question': 'How did Sam probably feel when he had to give Sparky back?',
                'options': {
                    'A': 'Angry',
                    'B': 'Excited',
                    'C': 'Sad but happy to help',
                    'D': 'Scared'
                },
                'answer': 'C',
                'explanation': 'The story says Sam was sad to say goodbye, but he was happy Sparky found his home.'
            }
        ],

        # Grade 1 - How Plants Grow
        'g1_2': [
            {
                'id': 'g1_2_q1',
                'type': 'Main Idea',
                'question': 'What do plants need to grow?',
                'options': {
                    'A': 'Only water',
                    'B': 'Only sunlight',
                    'C': 'Water, sunlight, air, and soil',
                    'D': 'Just soil'
                },
                'answer': 'C',
                'explanation': 'The passage says plants need four things: water, sunlight, air, and soil.'
            },
            {
                'id': 'g1_2_q2',
                'type': 'Vocabulary',
                'question': 'What does photosynthesis mean in this passage?',
                'options': {
                    'A': 'How roots grow',
                    'B': 'How leaves use sunlight to make food',
                    'C': 'How plants drink water',
                    'D': 'How seeds start growing'
                },
                'answer': 'B',
                'explanation': 'The passage says "Leaves use sunlight to make food for the plant. This is called photosynthesis."'
            },
            {
                'id': 'g1_2_q3',
                'type': 'Sequence',
                'question': 'What happens first when a plant starts to grow?',
                'options': {
                    'A': 'Leaves grow',
                    'B': 'Flowers bloom',
                    'C': 'A seed is planted in soil',
                    'D': 'The stem grows up'
                },
                'answer': 'C',
                'explanation': 'The passage says first you plant a seed in the soil.'
            }
        ],

        # Grade 2 - The Friendship Garden
        'g2_1': [
            {
                'id': 'g2_1_q1',
                'type': 'Main Idea',
                'question': 'What is the main message of this story?',
                'options': {
                    'A': 'Gardens are hard to grow',
                    'B': 'Working together makes hard tasks easier',
                    'C': 'You should share vegetables',
                    'D': 'Summer is the best season'
                },
                'answer': 'B',
                'explanation': 'The story shows how Maya and Jake worked together despite challenges, and their friendship garden succeeded because they cooperated.'
            },
            {
                'id': 'g2_1_q2',
                'type': 'Detail',
                'question': 'What vegetables did Maya and Jake plant?',
                'options': {
                    'A': 'Tomatoes, carrots, and lettuce',
                    'B': 'Only sunflowers',
                    'C': 'Only tomatoes',
                    'D': 'Potatoes and beans'
                },
                'answer': 'A',
                'explanation': 'The story mentions tomatoes, carrots, lettuce, and sunflowers (which are flowers, not vegetables).'
            },
            {
                'id': 'g2_1_q3',
                'type': 'Cause and Effect',
                'question': 'Why did the neighbors decide to help start a community garden?',
                'options': {
                    'A': 'Because they were bored',
                    'B': 'Because Maya and Jake shared their vegetables',
                    'C': 'Because the teacher told them to',
                    'D': 'Because they didn\'t have food'
                },
                'answer': 'B',
                'explanation': 'The neighbors were grateful that Maya and Jake shared vegetables with them, which inspired the community garden idea.'
            }
        ],

        # Grade 2 - The Water Cycle
        'g2_2': [
            {
                'id': 'g2_2_q1',
                'type': 'Main Idea',
                'question': 'What is the main topic of this passage?',
                'options': {
                    'A': 'Different types of weather',
                    'B': 'How the water cycle works',
                    'C': 'Why it rains',
                    'D': 'How clouds are made'
                },
                'answer': 'B',
                'explanation': 'The passage explains the entire water cycle and how water moves in a continuous circle.'
            },
            {
                'id': 'g2_2_q2',
                'type': 'Vocabulary',
                'question': 'What does evaporation mean?',
                'options': {
                    'A': 'When water falls from clouds',
                    'B': 'When water turns into water vapor',
                    'C': 'When water vapor turns into drops',
                    'D': 'When water freezes'
                },
                'answer': 'B',
                'explanation': 'The passage explains that evaporation is when water turns into water vapor.'
            },
            {
                'id': 'g2_2_q3',
                'type': 'Sequence',
                'question': 'What happens after water vapor rises into the sky?',
                'options': {
                    'A': 'It falls as rain',
                    'B': 'It becomes condensation and forms clouds',
                    'C': 'It goes into the ocean',
                    'D': 'Plants use it'
                },
                'answer': 'B',
                'explanation': 'According to the passage, after water vapor rises, it cools down and condensation happens, forming clouds.'
            }
        ],

        # Grade 3 - The Mystery of the Missing Books
        'g3_1': [
            {
                'id': 'g3_1_q1',
                'type': 'Main Idea',
                'question': 'What is the central theme of this story?',
                'options': {
                    'A': 'Solving mysteries is fun',
                    'B': 'Understanding and helping others is important',
                    'C': 'Libraries should be more careful',
                    'D': 'Reading about animals is educational'
                },
                'answer': 'B',
                'explanation': 'The story emphasizes understanding Tommy\'s situation and helping him access books properly rather than just punishing him.'
            },
            {
                'id': 'g3_1_q2',
                'type': 'Inference',
                'question': 'Why did Tommy take the books instead of checking them out?',
                'options': {
                    'A': 'He wanted to steal them',
                    'B': 'He didn\'t know he could check books out',
                    'C': 'He didn\'t like Ms. Garcia',
                    'D': 'He wanted to hide them from Emma'
                },
                'answer': 'B',
                'explanation': 'When Emma explained he could check out books, Tommy said "Really? I didn\'t know that!" showing he was unaware of the library system.'
            },
            {
                'id': 'g3_1_q3',
                'type': 'Character Analysis',
                'question': 'How did Emma show good problem-solving skills?',
                'options': {
                    'A': 'She immediately told the teacher about Tommy',
                    'B': 'She noticed a pattern and investigated',
                    'C': 'She asked her friends for help',
                    'D': 'She used a computer to find the books'
                },
                'answer': 'B',
                'explanation': 'Emma noticed all missing books were about animals, made a list, and followed clues to solve the mystery.'
            }
        ],

        # Grade 3 - Honeybees
        'g3_2': [
            {
                'id': 'g3_2_q1',
                'type': 'Main Idea',
                'question': 'What is the author\'s main purpose in this passage?',
                'options': {
                    'A': 'To explain how honey is made',
                    'B': 'To show why honeybees are important to our food supply',
                    'C': 'To describe the queen bee',
                    'D': 'To teach about insect life cycles'
                },
                'answer': 'B',
                'explanation': 'While the passage covers many topics, the main purpose is explaining how crucial honeybees are for pollination and food production.'
            },
            {
                'id': 'g3_2_q2',
                'type': 'Supporting Details',
                'question': 'How many flowers must bees visit to make one pound of honey?',
                'options': {
                    'A': 'About 1,000',
                    'B': 'About 10,000',
                    'C': 'About 2 million',
                    'D': 'About 100 million'
                },
                'answer': 'C',
                'explanation': 'The passage states that to make one pound of honey, bees must visit about two million flowers.'
            },
            {
                'id': 'g3_2_q3',
                'type': 'Cause and Effect',
                'question': 'What happens when a bee visits a flower?',
                'options': {
                    'A': 'The flower makes honey',
                    'B': 'Pollen sticks to the bee and can pollinate other flowers',
                    'C': 'The bee builds a honeycomb',
                    'D': 'The flower dies'
                },
                'answer': 'B',
                'explanation': 'The passage explains that pollen sticks to the bee\'s fuzzy body and rubs off on other flowers, pollinating them.'
            }
        ],

        # Grade 4 - The Time Capsule Project
        'g4_1': [
            {
                'id': 'g4_1_q1',
                'type': 'Theme',
                'question': 'What is the deeper meaning behind the time capsule project?',
                'options': {
                    'A': 'Students learn what to put in boxes',
                    'B': 'Everyday objects and personal stories become meaningful when preserved for the future',
                    'C': 'Technology changes quickly',
                    'D': 'School projects are fun'
                },
                'answer': 'B',
                'explanation': 'Mrs. Richardson explains that everyday objects and personal stories become treasures when viewed through the lens of time.'
            },
            {
                'id': 'g4_1_q2',
                'type': 'Character Development',
                'question': 'How did the students\' thinking change during the project?',
                'options': {
                    'A': 'They started choosing items with deeper meaning instead of just cool objects',
                    'B': 'They stopped caring about the project',
                    'C': 'They all wanted to include technology',
                    'D': 'They became competitive with each other'
                },
                'answer': 'A',
                'explanation': 'The students moved from wanting to include phones and toys to choosing meaningful items like family recipes, soil from a historic garden, and personal letters.'
            },
            {
                'id': 'g4_1_q3',
                'type': 'Inference',
                'question': 'Why was Riley\'s contribution particularly meaningful?',
                'options': {
                    'A': 'Teddy bears are valuable',
                    'B': 'It preserved the memory of someone who had passed away',
                    'C': 'Riley was quiet and finally spoke up',
                    'D': 'It was the oldest item'
                },
                'answer': 'B',
                'explanation': 'Riley\'s teddy bear was meaningful because it honored her sister\'s memory and ensured she would be remembered in the future.'
            }
        ],

        # Grade 4 - The Science of Earthquakes
        'g4_2': [
            {
                'id': 'g4_2_q1',
                'type': 'Main Idea',
                'question': 'What is the main idea of this passage?',
                'options': {
                    'A': 'Earthquakes are dangerous',
                    'B': 'Tectonic plates cause earthquakes when they suddenly slip after pressure builds up',
                    'C': 'Japan has many earthquakes',
                    'D': 'Scientists use seismographs'
                },
                'answer': 'B',
                'explanation': 'The passage mainly explains how tectonic plate movement causes earthquakes.'
            },
            {
                'id': 'g4_2_q2',
                'type': 'Vocabulary in Context',
                'question': 'What does magnitude mean in this passage?',
                'options': {
                    'A': 'The location of an earthquake',
                    'B': 'The depth of an earthquake',
                    'C': 'The strength or size of an earthquake',
                    'D': 'The duration of an earthquake'
                },
                'answer': 'C',
                'explanation': 'The passage uses magnitude to describe an earthquake\'s strength, as measured on the Richter scale.'
            },
            {
                'id': 'g4_2_q3',
                'type': 'Compare and Contrast',
                'question': 'What is the difference between the focus and the epicenter?',
                'options': {
                    'A': 'The focus is underground where the earthquake starts; the epicenter is on the surface above it',
                    'B': 'They are the same thing',
                    'C': 'The epicenter is underground; the focus is on the surface',
                    'D': 'The focus measures strength; the epicenter measures location'
                },
                'answer': 'A',
                'explanation': 'The passage explains that the focus (hypocenter) is underground where the earthquake starts, while the epicenter is the point on the surface directly above it.'
            }
        ],

        # Grade 5 - The Art of Perseverance
        'g5_1': [
            {
                'id': 'g5_1_q1',
                'type': 'Theme Analysis',
                'question': 'What is the central theme of this story?',
                'options': {
                    'A': 'Art competitions are important',
                    'B': 'Perseverance means being authentic and learning from failures',
                    'C': 'Teachers always know best',
                    'D': 'Painting is easier than playing piano'
                },
                'answer': 'B',
                'explanation': 'The story explores how true perseverance involves authenticity, learning from mistakes, and continuing despite self-doubt.'
            },
            {
                'id': 'g5_1_q2',
                'type': 'Symbolism',
                'question': 'What do Kenji\'s crumpled sketches symbolize?',
                'options': {
                    'A': 'Failure and defeat',
                    'B': 'Waste of time',
                    'C': 'The learning process and growth',
                    'D': 'Bad art skills'
                },
                'answer': 'C',
                'explanation': 'Mrs. Chen explains that the sketches aren\'t failures but part of Kenji\'s process, teaching him something with each attempt.'
            },
            {
                'id': 'g5_1_q3',
                'type': 'Author\'s Craft',
                'question': 'Why does the author include Mrs. Chen\'s backstory about piano?',
                'options': {
                    'A': 'To show she is talented',
                    'B': 'To illustrate that sometimes you must stop forcing yourself to be something you\'re not',
                    'C': 'To prove piano is harder than painting',
                    'D': 'To make the story longer'
                },
                'answer': 'B',
                'explanation': 'Mrs. Chen\'s story about switching from piano to painting teaches Kenji that authenticity matters more than forcing yourself into a particular mold.'
            },
            {
                'id': 'g5_1_q4',
                'type': 'Making Connections',
                'question': 'What lesson from this story can be applied to any challenge in life?',
                'options': {
                    'A': 'Always stay up all night working',
                    'B': 'Copy what successful people do',
                    'C': 'Being honest and authentic is more valuable than appearing perfect',
                    'D': 'Art is the best skill to develop'
                },
                'answer': 'C',
                'explanation': 'The story\'s universal message is that authenticity and honesty are more valuable than perfection, which applies to any life challenge.'
            }
        ],

        # Grade 5 - Renewable Energy
        'g5_2': [
            {
                'id': 'g5_2_q1',
                'type': 'Main Idea and Supporting Details',
                'question': 'What is the author\'s main argument in this passage?',
                'options': {
                    'A': 'Fossil fuels are better than renewable energy',
                    'B': 'Renewable energy can replace fossil fuels and offers hope for a sustainable future',
                    'C': 'Solar energy is the only solution',
                    'D': 'Climate change is not a serious problem'
                },
                'answer': 'B',
                'explanation': 'The passage argues that renewable energy technologies can meet our needs sustainably and offers evidence from various sources and examples.'
            },
            {
                'id': 'g5_2_q2',
                'type': 'Text Structure',
                'question': 'How is this passage organized?',
                'options': {
                    'A': 'Chronologically, from past to present',
                    'B': 'By comparing only two energy sources',
                    'C': 'By introducing the problem, then describing different renewable solutions and their potential',
                    'D': 'As a personal narrative'
                },
                'answer': 'C',
                'explanation': 'The passage starts with the problems of fossil fuels, then systematically describes different renewable energy solutions, and concludes with their potential.'
            },
            {
                'id': 'g5_2_q3',
                'type': 'Critical Thinking',
                'question': 'According to the passage, what is one challenge of renewable energy?',
                'options': {
                    'A': 'It is always more expensive than fossil fuels',
                    'B': 'Different sources have limitations, like solar not working at night',
                    'C': 'No countries use renewable energy',
                    'D': 'It creates no jobs'
                },
                'answer': 'B',
                'explanation': 'The passage acknowledges that each renewable source has limitations, such as solar not working at night or wind turbines only working when wind blows.'
            },
            {
                'id': 'g5_2_q4',
                'type': 'Author\'s Purpose',
                'question': 'Why does the author mention that countries like Costa Rica generate nearly 100% renewable electricity?',
                'options': {
                    'A': 'To show those countries are wealthy',
                    'B': 'To provide evidence that full renewable energy is possible',
                    'C': 'To criticize other countries',
                    'D': 'To explain geography'
                },
                'answer': 'B',
                'explanation': 'The author uses these examples to counter the worry that renewable energy can\'t fully replace fossil fuels, showing it\'s already been achieved.'
            }
        ]
    }

    @classmethod
    def get_questions_for_passage(cls, passage_id):
        """Get all questions for a specific passage"""
        questions_data = cls.QUESTIONS.get(passage_id, [])
        questions = []
        for q_data in questions_data:
            question = Question(
                q_data['id'],
                passage_id,
                q_data['type'],
                q_data['question'],
                q_data['options'],
                q_data['answer'],
                q_data['explanation']
            )
            questions.append(question)
        return questions
