#DoggyQuiz Simple Version

class Question:
    
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        
class DoggyQuiz:        
    def __init__(self):
        self.username = ""
    
    def startup(self):        
        
        # print the greeting at startup
        self.greeting()

        # ask the user for their name
        self.username = input("What is your name? ")
        print(f"Welcome, {self.username}!")
        print()
    
    def greeting(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print("----- Welcome to DoggyQuiz! -----")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print()

   
def run_quiz(questions):
    score = 0
    for question in questions:
        user_answer = input(question.prompt)
        if user_answer.lower() == question.answer.lower():
            score += 1
    print("You got", score, "out of", len(questions), "correct!")
    
# Create an instance of DoggyQuiz
doggy_quiz = DoggyQuiz()

# Call the startup method to initialize the quiz
doggy_quiz.startup()


# Define your quiz questions here
question1 = Question("What is the television series named after a male collie? ", "Lassie")
question2 = Question("What breed of dog is Snoopy from the Peanuts comic strip? ", "Beagle")
question3 = Question("What is Mickey Mouse's pet dog named? ", "Pluto")

# Create a list of questions
quiz_questions = [question1, question2, question3]

# Run the quiz
run_quiz(quiz_questions)