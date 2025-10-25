"""
Reading passages database with grade-appropriate content
"""

class ReadingPassage:
    """Represents a single reading passage"""

    def __init__(self, passage_id, title, content, grade, passage_type):
        self.id = passage_id
        self.title = title
        self.content = content
        self.grade = grade
        self.type = passage_type

    def __str__(self):
        return f"{self.title} (Grade {self.grade})"


class PassageDatabase:
    """Database of reading passages for different grade levels"""

    PASSAGES = [
        # Kindergarten passages
        {
            'id': 'k1',
            'title': 'The Little Red Hen',
            'grade': 'K',
            'type': 'story',
            'content': '''The little red hen found some seeds. "Who will help me plant?" she asked.
"Not I," said the cat.
"Not I," said the dog.
"Then I will," said the hen.
She planted the seeds all by herself. Soon they grew into wheat.
"Who will help me cut the wheat?" she asked.
"Not I," said the cat.
"Not I," said the dog.
"Then I will," said the hen.
She made bread from the wheat. It smelled so good!
"Who will help me eat the bread?" she asked.
"I will!" said the cat.
"I will!" said the dog.
"No," said the hen. "I will eat it myself!" And she did.'''
        },
        {
            'id': 'k2',
            'title': 'Colors in Nature',
            'grade': 'K',
            'type': 'informational',
            'content': '''Nature has many colors. The sky is blue. Grass is green.
The sun is yellow. Many flowers are red or pink.
At night, the sky turns dark. Sometimes we see a rainbow.
A rainbow has many colors: red, orange, yellow, green, blue, and purple.
Colors make our world beautiful!'''
        },

        # Grade 1 passages
        {
            'id': 'g1_1',
            'title': 'Sam and the Lost Puppy',
            'grade': '1',
            'type': 'story',
            'content': '''Sam was walking home from school. He heard a small cry. "Woof! Woof!"
A tiny puppy was sitting by a tree. It looked scared and alone.
"Are you lost?" Sam asked. The puppy wagged its tail.
Sam looked around but saw no one. He picked up the puppy and took it home.
"Mom, can we keep him?" Sam asked.
"First, we need to find his owner," Mom said.
They put up posters around the neighborhood. The next day, a girl called.
"That's my puppy, Sparky!" she cried happily.
Sam was sad to say goodbye, but he was happy Sparky found his home.
The girl thanked Sam for being kind and helpful.'''
        },
        {
            'id': 'g1_2',
            'title': 'How Plants Grow',
            'grade': '1',
            'type': 'informational',
            'content': '''Plants need four things to grow: water, sunlight, air, and soil.
First, you plant a seed in the soil. The seed needs water to start growing.
Roots grow down into the soil. They help the plant drink water.
A stem grows up toward the sun. Leaves grow on the stem.
Leaves use sunlight to make food for the plant. This is called photosynthesis.
With water, sunlight, air, and good soil, the plant grows big and strong.
Some plants grow flowers. Some grow fruits and vegetables.
Plants give us food and make our air clean!'''
        },

        # Grade 2 passages
        {
            'id': 'g2_1',
            'title': 'The Friendship Garden',
            'grade': '2',
            'type': 'story',
            'content': '''Maya and Jake were best friends who lived next door to each other. One spring day, they had an idea.
"Let's plant a garden together!" Maya said excitedly.
"Great idea! What should we plant?" asked Jake.
They decided to plant vegetables and flowers. Maya's grandmother gave them tomato seeds, and Jake's father gave them sunflower seeds. They also got carrot and lettuce seeds from the store.
Every day after school, Maya and Jake worked in their garden. They pulled weeds, watered the plants, and watched them grow. Sometimes it was hard work, especially on hot days.
"I'm tired," Jake said one afternoon.
"Me too," Maya agreed. "But look how big our tomatoes are getting!"
By summer, their garden was beautiful. Big yellow sunflowers stood tall. Red tomatoes hung from green vines. They had so many vegetables that they shared them with all their neighbors.
"Our friendship garden worked!" Maya said, smiling.
"Yes, because we worked together," Jake replied.
Their neighbors were so grateful that they decided to help Maya and Jake start a community garden the next year!'''
        },
        {
            'id': 'g2_2',
            'title': 'The Water Cycle',
            'grade': '2',
            'type': 'informational',
            'content': '''Water moves in a circle called the water cycle. This cycle happens over and over again.
The sun heats water in oceans, lakes, and rivers. The water turns into water vapor, which is like invisible steam. This is called evaporation. The water vapor rises up into the sky.
High in the sky, the air is cold. The water vapor turns back into tiny water drops. This is called condensation. The drops join together to make clouds.
When the drops get too heavy, they fall from the clouds. This is called precipitation. Precipitation can be rain, snow, sleet, or hail.
The water falls back to Earth. Some of it goes into oceans, lakes, and rivers. Some soaks into the ground. Plants and animals use this water.
Then the sun heats the water again, and the cycle starts over! The water cycle keeps going all the time. The same water has been moving around Earth for millions of years.'''
        },

        # Grade 3 passages
        {
            'id': 'g3_1',
            'title': 'The Mystery of the Missing Books',
            'grade': '3',
            'type': 'story',
            'content': '''Emma loved her school library more than any other place. Every week, she borrowed a new book to read. But recently, something strange was happening. Books were disappearing from the library!
Ms. Garcia, the librarian, looked worried. "Five books have vanished this month," she told Emma. "They were checked in, but now they're gone. If we can't find them, the library might lose funding."
Emma decided to investigate. She noticed that all the missing books were about animals. She made a list: "Wild Animals of Africa," "Ocean Creatures," "Birds of North America," "Jungle Adventures," and "The Secret Life of Insects."
During lunch, Emma explored the school. Behind the gym, she heard something unusual. Following the sound, she discovered a small reading nook that she never knew existed. And there sat Tommy, the shy new student, surrounded by all five missing books!
"Tommy, everyone is looking for these books!" Emma exclaimed.
Tommy's face turned red. "I'm sorry," he whispered. "I don't have any books at home. Reading about animals makes me happy, so I brought them here to read during lunch. I was going to return them, I promise!"
Emma understood. "Why don't you come to the library with me? Ms. Garcia can help you check out books properly. You can keep them for two whole weeks!"
Tommy's eyes lit up. "Really? I didn't know that!"
Emma and Tommy returned the books together. Ms. Garcia was so relieved that she gave Tommy his own library card and showed him how the system worked. She even started a lunch reading club so students like Tommy would always have a quiet place to read.
From that day on, Tommy became one of the library's best patrons, and he and Emma became good friends. The mystery was solved, and everyone was happy!'''
        },
        {
            'id': 'g3_2',
            'title': 'Honeybees: Nature\'s Helpers',
            'grade': '3',
            'type': 'informational',
            'content': '''Honeybees are amazing insects that play a crucial role in our world. These small creatures do much more than make honey – they help plants grow and provide food for people and animals.
A honeybee colony has three types of bees. The queen bee is the largest and lays all the eggs. Worker bees are females who collect nectar, make honey, and protect the hive. Drones are male bees whose job is to mate with the queen.
Honeybees are important pollinators. When a bee lands on a flower to drink nectar, pollen sticks to its fuzzy body. When the bee visits another flower, some pollen rubs off. This is how plants make seeds and fruit. Without bees, we wouldn't have apples, blueberries, almonds, and many other foods!
Inside the hive, worker bees have different jobs based on their age. Young bees clean the hive and feed baby bees. Older bees build honeycombs from wax they make in their bodies. The oldest bees leave the hive to collect nectar and pollen from flowers.
To make one pound of honey, bees must visit about two million flowers! They store honey in hexagonal cells in the honeycomb. The honey feeds the bees during winter when flowers aren't blooming.
Sadly, honeybee populations are declining. Pesticides, diseases, and loss of habitat threaten these important insects. We can help by planting bee-friendly flowers, avoiding pesticides, and supporting local beekeepers.
Next time you see a bee, remember how hard it works and how important it is to our food supply!'''
        },

        # Grade 4 passages
        {
            'id': 'g4_1',
            'title': 'The Time Capsule Project',
            'grade': '4',
            'type': 'story',
            'content': '''When Mrs. Richardson announced that their class would create a time capsule to be opened in 50 years, the students buzzed with excitement. Each student could contribute one item that represented their life in 2025.
"What should we include?" asked Marcus, twirling his pencil thoughtfully.
"I'm putting in my phone!" announced Sophia.
"But it won't work in 50 years," countered Alex. "Technology changes too fast."
The class debated for days. Some wanted to include toys, others suggested photos or letters. Mrs. Richardson encouraged them to think deeply about what would be meaningful decades into the future.
Sophia finally decided to include a handwritten letter to her future self instead of her phone. Marcus chose a small bottle of soil from his family's garden, where his great-grandmother had planted vegetables during World War II. Alex included a newspaper showing current events and a flash drive with videos of their daily life.
Other students added diverse items: Yuki contributed origami she had made using techniques passed down from her grandmother in Japan. Jamal included lyrics to his favorite song and a drawing of his neighborhood. Maria added a recipe book that her family had used for generations.
The most touching moment came when quiet Riley approached Mrs. Richardson privately. "Can I add something?" she asked, holding a small teddy bear. "This was my sister's. She passed away last year. I want people in the future to know she existed."
Mrs. Richardson hugged Riley gently. "That's beautiful, Riley. Your sister's memory will be preserved."
On the day they sealed the capsule, the entire school gathered. The principal gave a speech about how their lives would become history for future students. As they buried the metal container near the school's oldest oak tree, many students felt emotional.
"Fifty years is so long," Sophia said. "We'll be old!"
"Maybe we'll come back for the opening," Marcus suggested. "Imagine how different everything will be!"
Mrs. Richardson smiled. "That's the point. You're creating a connection between your present and someone else's future. You're teaching them about who you are and what matters to you. That's powerful."
As the class walked back inside, they looked at their school differently. They were now part of its history, their voices preserved for students not yet born. The project had taught them that everyday objects and personal stories could become treasures when viewed through the lens of time.'''
        },
        {
            'id': 'g4_2',
            'title': 'The Science of Earthquakes',
            'grade': '4',
            'type': 'informational',
            'content': '''The ground beneath our feet seems solid and still, but Earth's surface is actually moving constantly. Sometimes this movement is dramatic and frightening – we call it an earthquake.
Earth's outer layer, called the crust, is broken into large pieces called tectonic plates. These plates fit together like a giant jigsaw puzzle covering the entire planet. They float on a layer of hot, semi-liquid rock called the mantle. The plates move very slowly, usually just a few inches per year – about as fast as your fingernails grow.
Most of the time, this movement is so gradual that we don't notice it. But sometimes plates get stuck as they try to slide past each other. Pressure builds up over years or even centuries. Eventually, the pressure becomes too great, and the plates suddenly slip. This releases enormous amounts of energy, creating an earthquake.
The point underground where the earthquake starts is called the focus or hypocenter. The point directly above it on Earth's surface is called the epicenter. This is usually where the shaking is strongest. Energy from the earthquake travels outward in waves, like ripples when you drop a stone in water.
Scientists measure earthquakes using instruments called seismographs, which detect and record the shaking. The Richter scale describes an earthquake's magnitude, or strength. Each number on the scale represents about 32 times more energy than the previous number. An earthquake measuring 5.0 releases energy equal to a small nuclear weapon, while a 7.0 earthquake releases as much energy as 30 of those weapons!
Most earthquakes are too small for people to feel. Earth experiences about 500,000 earthquakes each year, but only about 100,000 are strong enough to feel, and only about 100 cause damage.
Certain regions are more prone to earthquakes. The "Ring of Fire" around the Pacific Ocean is especially active because several tectonic plates meet there. Countries like Japan, Chile, and the western United States experience frequent earthquakes.
While we cannot prevent earthquakes, we can prepare for them. Buildings in earthquake zones are designed with flexible materials and deep foundations. People practice "drop, cover, and hold on" drills. Early warning systems can provide precious seconds of advance notice.
Understanding earthquakes helps us respect the powerful forces that shape our planet and reminds us that Earth is dynamic and ever-changing.'''
        },

        # Grade 5 passages
        {
            'id': 'g5_1',
            'title': 'The Art of Perseverance',
            'grade': '5',
            'type': 'story',
            'content': '''Kenji stared at the blank canvas before him, his paintbrush trembling slightly. Tomorrow was the Young Artists Competition, and he had nothing to show. All around him in the community art studio, other students worked confidently on their masterpieces. His best friend Maria was putting finishing touches on a stunning landscape. Across the room, David's abstract piece drew admiring glances from everyone who passed by.
"Why can't I do this?" Kenji muttered, crumpling yet another sketch.
Mrs. Chen, the art instructor, appeared beside him. She had immigrated from Taiwan thirty years ago and had become one of the city's most respected art teachers. "You're thinking too much," she said gently. "What's blocking you?"
"Everyone else knows exactly what to paint," Kenji replied, frustrated. "I have too many ideas, and none of them feel right. I'm not good enough for this competition."
Mrs. Chen pulled up a stool. "Let me tell you a story. When I was your age, I wanted to be a concert pianist. I practiced eight hours a day. But no matter how hard I tried, I couldn't master certain pieces. I felt like a failure."
"But you became a famous artist," Kenji said, confused.
"Yes, but only after I stopped forcing myself to be something I wasn't. One day, frustrated with piano practice, I grabbed some paints my grandmother had given me. I painted what I heard in the music – the colors, the emotions, the stories. I wasn't trying to be perfect; I was trying to be honest."
She pointed to Kenji's crumpled sketches. "These aren't failures. They're your process. Each one teaches you something. The problem isn't that you're not good enough – it's that you're comparing your beginning to everyone else's middle."
Kenji looked at his rejected ideas with new eyes. There was the sketch of his grandfather's hands – weathered and wise. Another showed his neighborhood park at dawn when he walked his dog. A third captured his little sister's expression when she lost her first tooth.
"These are all parts of your life," Mrs. Chen observed. "What connects them?"
Kenji thought for a moment. "Moments that matter," he said slowly. "Ordinary times that feel special when you really look at them."
Something clicked. Kenji began to paint with new purpose, not worrying about technique or perfection. He created a collage-style piece showing fragments of daily life – his grandfather's hands planting seeds, morning light in the park, his sister's gap-toothed grin, his mother cooking dinner, his father reading the newspaper. The scenes overlapped and flowed into each other, connected by golden threads.
He worked through the night, losing track of time. When morning came, Kenji stepped back and truly saw what he had created. It wasn't technically perfect – some proportions were off, some colors bled together – but it was honest and heartfelt. It was his story.
At the competition, Kenji watched nervously as judges examined hundreds of paintings. Maria's landscape won second place, and she deserved it – it was breathtaking. David's abstract piece earned an honorable mention. When the judges announced first place, Kenji was stunned to hear his own name.
"This piece," the head judge explained, "demonstrates something we rarely see in young artists – the courage to be vulnerable and authentic. Technical skill can be learned, but the ability to capture truth in art is a gift."
As Kenji accepted his award, he caught Mrs. Chen's eye. She wasn't smiling proudly like the other teachers. Instead, she gave him a small, knowing nod – the kind that said she had always known he could do it, even when he hadn't known himself.
Later, as students celebrated with their families, Maria asked Kenji his secret. "How did you create something so amazing overnight?"
Kenji thought about Mrs. Chen's story, about all those crumpled sketches, about finally understanding that art wasn't about being perfect – it was about being real.
"I stopped trying to paint what I thought people wanted to see," he said. "I painted what I needed to say."
That evening, Kenji carefully hung his award ribbon next to his desk. But what he treasured more was what Mrs. Chen had written on the back of one of his crumpled sketches, which she'd rescued from the trash: "Every artist was first an amateur. Every master was first a student. Keep going."
Kenji realized that perseverance wasn't just about working hard. It was about continuing to learn, adapting when things didn't work, being honest about your struggles, and having the courage to be yourself even when it felt risky. These lessons would stay with him far longer than any trophy.'''
        },
        {
            'id': 'g5_2',
            'title': 'The Revolutionary World of Renewable Energy',
            'grade': '5',
            'type': 'informational',
            'content': '''For most of human history, people relied on renewable energy sources. They burned wood for warmth, used wind to sail boats, and harnessed water power to grind grain. Then came the Industrial Revolution, which introduced fossil fuels – coal, oil, and natural gas. These fuels seemed like magic: they were energy-dense, portable, and abundant. They powered factories, vehicles, and eventually, modern civilization.
However, we now understand that fossil fuels come with serious problems. When burned, they release carbon dioxide and other greenhouse gases that trap heat in Earth's atmosphere, causing climate change. Extracting fossil fuels damages ecosystems. And most importantly, they're finite – eventually, they will run out.
This is why scientists and engineers are developing renewable energy technologies that can meet our needs without depleting resources or harming the environment. Let's explore the main types.
Solar power captures energy from the sun using photovoltaic cells, commonly called solar panels. These cells contain special materials that convert sunlight directly into electricity. When photons from the sun hit the cell, they knock electrons loose from atoms, creating an electrical current. Solar energy is incredibly abundant – the sun provides more energy to Earth in one hour than humanity uses in an entire year! The challenge is capturing and storing it efficiently.
Wind power uses turbines to convert wind's kinetic energy into electricity. Modern wind turbines are technological marvels, with blades as long as football fields and towers taller than 20-story buildings. As wind flows past the blades, it causes them to rotate. This rotation spins a generator that produces electricity. Wind farms, both on land and offshore in the ocean, can generate enormous amounts of power. Some countries, like Denmark, generate more than 40% of their electricity from wind.
Hydroelectric power harnesses the energy of moving water. Most hydroelectric systems use dams to create reservoirs. When water flows through turbines in the dam, it generates electricity. Hydroelectric power is reliable and can be controlled by adjusting water flow. However, large dams can disrupt ecosystems and displace communities, so engineers are developing smaller, less invasive systems.
Geothermal energy taps into Earth's internal heat. Deep underground, temperatures reach thousands of degrees. In certain locations, this heat is accessible near the surface. Geothermal power plants pump water underground where it's heated by hot rocks, then use the resulting steam to spin turbines and generate electricity. Iceland, which sits on active volcanic zones, generates most of its power this way.
Biomass energy comes from organic materials like plants, wood, and waste. When these materials are burned or decomposed by bacteria, they release energy that can generate electricity or create biofuels for vehicles. Unlike fossil fuels, biomass is renewable because we can grow more plants. However, it still produces emissions, so it's not as clean as solar or wind.
Each renewable energy source has advantages and limitations. Solar doesn't work at night or during cloudy weather. Wind turbines only generate power when the wind blows. Hydroelectric requires specific geography. This is why energy experts advocate for a diverse energy portfolio that combines multiple renewable sources.
Recent innovations are making renewable energy more practical. Better batteries can store solar and wind energy for use when the sun isn't shining or wind isn't blowing. Smart grids use computer technology to distribute electricity more efficiently. Floating solar farms utilize reservoirs and oceans. Offshore wind turbines access stronger, more consistent ocean winds.
The transition to renewable energy isn't just about technology – it's about economics and policy too. Renewable energy costs have dropped dramatically. In many places, solar and wind are now cheaper than coal or natural gas. Governments worldwide are setting renewable energy targets and providing incentives for clean energy development.
This transition is creating millions of new jobs. Solar panel installers, wind turbine technicians, energy efficiency specialists, and sustainability engineers are in high demand. Students today will likely work in careers that involve renewable energy, whether directly or indirectly.
Some people worry that renewable energy can't fully replace fossil fuels, but countries like Costa Rica, Iceland, and Norway prove otherwise – they generate nearly 100% of their electricity from renewable sources. As technology improves and costs decrease, renewable energy becomes increasingly practical for all nations.
The shift to renewable energy represents one of humanity's greatest challenges and opportunities. It requires innovation, investment, and international cooperation. But it also offers hope: we can power our civilization while protecting the planet for future generations. The question isn't whether we'll transition to renewable energy, but how quickly we can accomplish it. Every solar panel installed, every wind turbine erected, and every electric vehicle purchased moves us closer to a sustainable future.'''
        }
    ]

    @classmethod
    def get_passages_by_grade(cls, grade):
        """Get all passages for a specific grade"""
        return [p for p in cls.PASSAGES if p['grade'] == grade.upper()]

    @classmethod
    def get_passage_by_id(cls, passage_id):
        """Get a specific passage by ID"""
        for passage in cls.PASSAGES:
            if passage['id'] == passage_id:
                return ReadingPassage(
                    passage['id'],
                    passage['title'],
                    passage['content'],
                    passage['grade'],
                    passage['type']
                )
        return None

    @classmethod
    def get_all_passages(cls):
        """Get all passages"""
        return cls.PASSAGES
