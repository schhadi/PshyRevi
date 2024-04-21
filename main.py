import tkinter as tk
import random
import webbrowser

# List of questions extracted from the file
# questions =
    #"Explain one technique used to study the brain in relation to behavior",
    #"Outline localization of brain function using one relevant piece of research to support your answer.",
    #"Explain neuroplasticity using one relevant piece of research to support your answer",
    #"Describe neurotransmission using one relevant piece of research to support your answer",
    #"Describe synaptic pruning using one relevant piece of research to support your answer",
    #"Using a relevant example of research explain how one inhibitory neurotransmitter affects behavior",
    #"Using a relevant example of research explain how one excitatory neurotransmitter affects behavior",
    #"Explain neural networks by using one relevant piece of research",
    #"Explain the impact of agonists on human behavior by using a relevant piece of research",
    #"Explain the impact of antagonists on human behavior by using a relevant piece of research",
    #"Describe one research method used to investigate the relationship between brain and behavior using a relevant example of research",
    #"Using one or more examples outline the effects of hormones on human behavior.",
    #"Explain the effects of one or more pheromones on human behavior",
    #"Describe how genetic inheritance influences human behavior using one relevant example",
    #"Explain how a particular gene can influence human behavior using a relevant example",
    #"Explain one evolutionary explanation for behavior using relevant research",
    #"Outline one ethical consideration with research in the biological approach",
    #"Using a relevant example of research explain how one research method is used to explain human behavior in the biological approach"
#]

# Shuffle the list of questions
#random.shuffle(questions)

# Randomly select one question
# selected_question = random.choice(questions)
# selected_question

# print all randomly 
# print("Randomly selected questions:")
# for index, question in enumerate(questions, start=1):
    # print(f"{index}. {question}")

# Print one question at a time
# for question in questions:
    #input("Press Enter to see a random question...")
    #print("\nRandomly selected question:")
    #print(question)




#List of questions and corresponding study and concepts
questions_info = [
    {
        "question": "Explain one technique used to study the brain in relation to behavior",
        "study": "Maguire et al (2000) – Taxi Drivers",
        "concepts": "- Explain magnetic resonance imaging (MRI) – what is it and how it works - Present and explain the study (Maguire) - Conclusion"
    },
    {
        "question": "Outline localization of brain function using one relevant piece of research to support your answer.",
        "study": "Maguire et al (2000) – Taxi Drivers",
        "concepts": "- Explain the theory of localization of function - Structural and functional localization - Present and explain the study(Maguire) - Conclusion"
    },
    {
        "question": "Explain neuroplasticity using one relevant piece of research to support your answer",
        "study": "Maguire et al (2000) – Taxi Drivers",
        "concepts": "- Define the term neuroplasticity - Explain that it is an effect of environmental factors on brain structure or function (in case of the damage) - Present and explain the study (Luby) - conclusion"
    },
    {
        "question": "Describe neurotransmission using one relevant piece of research to support your answer",
        "study": "Fisher, Aron, and Brown (2005) – Dopamine & Attraction",
        "concepts": "- What is a neurotransmitter? - Explain the process of neurotransmission (how are the signals sent between the neurons) - Explain dopamine and its role in attraction - Present the study - Conclusion"
    },
    {
        "question": "Describe synaptic pruning using one relevant piece of research to support your answer",
        "study": "Luby et al (2013) – Preschool Depression Study",
        "concepts": "- Neuroplasticity - Neural circuits - Neurons - Neurons can lose connections - Can be result of stressors - Affected by environment (poverty) - Present the study - Children from low SEPs had less grey matter while the synapses had pruned."
    },
    {
        "question": "Using a relevant example of research explain how one inhibitory neurotransmitter affects behavior",
        "study": "Crockett et al (2010) – The Trolley problem",
        "concepts": "- Explain neurotransmission - Describe the role of neurotransmitters excitatory/inhibitory - Explain the role of serotonin - Define behavior (prosocial behavior) - Explain the study focusing of how serotonin promotes prosocial behavior"
    },
    {
        "question": "Using a relevant example of research explain how one excitatory neurotransmitter affects behavior",
        "study": "Fisher, Aron, and Brown (2005) – Dopamine & Attraction",
        "concepts": "- Explain neurotransmission - Describe the role of neurotransmitters excitatory/inhibitory - Give example of neurotransmitter - dopamine and explain that it is believed to be connected to romantic attachment - Define behavior (romantic attachment) - Allow impulse to pass More romantic attachment leads to more dopamine"
    },
    {
        "question": "Explain neural networks by using one relevant piece of research",
        "study": "Luby et al (2013) – Preschool Depression Study",
        "concepts": "- Explain neural networks and neural circuits - Explain neurons and neurotransmission - Explain how neurotransmitters work in neural networks: Dopamine (Fisher..) - or neuroplasticity (Maguire, Luby…) - Or synaptic pruning (Luby..) - Explain study"
    },
    {
        "question": "Explain the impact of agonists on human behavior by using a relevant piece of research",
        "study": "Devis et al (1978) – Agonist (Physostigmine)",
        "concepts": "-Explain neurotransmission and neurotransmitters - Explain how neurotransmitters are affected by antagonists and agonists: - Explain physostigmine more in detail and how it impacted memory in participants - Behaviour: Memory - Explain study - Conclusion, link back to the question"
    },
    {
        "question": "Explain the impact of antagonists on human behavior by using a relevant piece of research",
        "study": "Antonova et al (2011) – Antagonist (Scopolamine)",
        "concepts": "- Explain neurotransmission - Explain neurotransmitters - Agonists - Antagonists: Scopolamine - Behavior: Memory - Explain study - Link conclusion back to the question"
    },
    {
        "question": "Describe one research method used to investigate the relationship between brain and behavior using a relevant example of research",
        "study": "Maguire et al (2000) – Taxi Drivers",
        "concepts": "- Experiments - Hormones and behavior - Pheromones and behavior - Genes and behavio"
    },
    {
        "question": "Using one or more examples outline the effects of hormones on human behavior.",
        "study": "Schneiderman et al (2012) – Oxytocin during the initial stages of romantic attachment",
        "concepts": "- What are hormones - Explain how hormones function - Examples of hormones - Oxytocin believed to play a role in attachment - Explain attachment"
    },
    {
        "question": "Explain the effects of one or more pheromones on human behavior",
        "study": "Saxton et al (2008) - Evidence that androstadienone modulates women’s attributions of men’s attractiveness",
        "concepts": "- Define and explain pheromones - Explain sex pheromones (how they work by giving examples) - Explain the effect they have on individuals using study - Explain androstadienone and its role in attraction"
    },
    {
        "question": "Describe how genetic inheritance influences human behavior using one relevant example",
        "study": "Rushton and Bons (2005) - Similarity on a Genetic Level",
        "concepts": "- Describe genetics and inheritance and how they are situated in the human body - Explain how genetics affects behaviour - Explain that genetics can play role in attraction (the choice of a partner) - Twin study - explain what it is and how it is used in genetic studies (environment vs genes)"
    },
    {
        "question": "Explain how a particular gene can influence human behavior using a relevant example",
        "study": "Sadikajm Moskowitz and Bartz",
        "concepts": "Explain what molecular genetics method is about - Explain the gene CD38 and its connection to attraction - Explain what attraction is (as behavior) - Explain the study and link the conclusion back to the question"
    },
    {
        "question": "Explain one evolutionary explanation for behavior, using relevant research",
        "study": "Wedekind 1995",
        "concepts": "- Evolution and evolutionary development in the role of survival of the fittest - Natural selection - Evolutionary psychology - Biological origins of attraction - Present the study - Link back how the evolution played a role in the attraction"
    },
    {
        "question": "Outline one ethical consideration with research in the biological approach",
        "study": "Crocket et al",
        "concepts": "- Explain ethical consideration in psychological research and give examples - Outline one in particular e.g 'Protection of participants' and explain psychological or physical harm, consequences - Explain a study - e.g physostigmine, citalopram, scopolamine (infused) evaluate the issues this might cause for the study. → conclusion"
    },
    {
        "question": "Using a relevant example of research, explain how one research method is used to explain human behavior in the biological approach",
        "study": "Maguire et al",
        "concepts": "- Explain experiments - Explain quasi experiment - Present the study - Conclude, link back to question"
    }
]



# Shuffle questions
random.shuffle(questions_info)

class QuizApp:
    def __init__(self, master):
        self.master = master
        master.title("SAQ Psychology")
        master.config(bg="#dde")
        self.create_start_menu()

    def create_start_menu(self):
        self.start_frame = tk.Frame(self.master, bg="#dde")
        self.start_frame.pack(fill="both", expand=True)

        welcome_label = tk.Label(self.start_frame, text="Welcome to the Quiz App", bg="#dde", font=("Arial", 16))
        welcome_label.pack(pady=20)

        start_button = tk.Button(self.start_frame, text="Start Quiz", command=self.start_quiz, bg="#ffa")
        start_button.pack(pady=10)

        help_button = tk.Button(self.start_frame, text="Help", command=self.open_help_email, bg="#add8e6")
        help_button.pack(side="bottom", pady=10)

    def start_quiz(self):
        self.start_frame.destroy()
        self.setup_quiz()

    def setup_quiz(self):
        self.score = 0
        self.question_index = 0

        self.label = tk.Label(self.master, text="Press 'Next' to start the quiz", wraplength=300, bg="#dde", font=("Arial", 12))
        self.label.pack(pady=10)

        self.info_label = tk.Label(self.master, text="", wraplength=300, bg="#dde", font=("Arial", 12))
        self.info_label.pack(pady=10)

        self.buttons_frame = tk.Frame(self.master, bg="#dde")
        self.buttons_frame.pack()

        self.study_button = tk.Button(self.buttons_frame, text="Show Study", command=lambda: self.show_info("study"), bg="#aaf")
        self.study_button.grid(row=0, column=0, padx=10, pady=5)

        self.concept_button = tk.Button(self.buttons_frame, text="Show Concept", command=lambda: self.show_info("concept"), bg="#aaf")
        self.concept_button.grid(row=0, column=1, padx=10, pady=5)

        self.correct_button = tk.Button(self.buttons_frame, text="Correct", command=lambda: self.answer(True), bg="#8f8")
        self.correct_button.grid(row=1, column=0, padx=10, pady=5)

        self.incorrect_button = tk.Button(self.buttons_frame, text="Incorrect", command=lambda: self.answer(False), bg="#f88")
        self.incorrect_button.grid(row=1, column=1, padx=10, pady=5)

        self.next_button = tk.Button(self.master, text="Next Question", command=self.next_question, bg="#ffa")
        self.next_button.pack(pady=10)

        self.score_label = tk.Label(self.master, text=f"Score: {self.score}", bg="#dde", font=("Arial", 14, "bold"))
        self.score_label.pack(pady=10)

        self.next_question()

    def next_question(self):
        self.question_index += 1
        if self.question_index < len(questions_info):
            item = questions_info[self.question_index]
            self.label.config(text=item['question'])
            self.info_label.config(text="")
        else:
            self.label.config(text="Quiz completed!")
            self.next_button.config(state='disabled')

    def show_info(self, info_type):
        if self.question_index < len(questions_info):
            item = questions_info[self.question_index]
            if info_type == "study":
                self.info_label.config(text=f"Study: {item['study']}")
            else:
                self.info_label.config(text=f"Concepts: {item['concepts']}")
        else:
            self.info_label.config(text="")

    def answer(self, correct):
        if correct:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")

    def open_help_email(self):
        email_address = "elev.hadipaul.scharbrodt@skola.lund.se"
        subject = "Quiz App Help"
        webbrowser.open(f"mailto:{email_address}?subject={subject}")

root = tk.Tk()
root.geometry("500x400")
app = QuizApp(root)
root.mainloop()
