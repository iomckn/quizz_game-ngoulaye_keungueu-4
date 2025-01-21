def quiz():
    #Liste des questions et réponses
    questions = [
        {
            "question": "What is the name of the main character?",
            "choices": ["Erik", "T'Challa", "Nakia"],
            "answer": "T'Challa"
        },
        {
            "question": "What is T'Challa's sister's name?",
            "choices": ["Nakia", "Okoye", "Shuri", "Christalle"],
            "answer": "Shuri"
        },
        {
            "question": "Which actor plays Erik Killmonger?",
            "choices": ["Michel Jordan", "Michel B.Jordan", "Chadwick Boseman"],
            "answer": "Michel B.Jordan"
        },
        {
            "question": "Which Marvel does Klaue appear in?",
            "choices": ["Thor Ragnarok", "Avengers: Inifinity War", "Avengers: L'Ere d'Ultron"],
            "answer": "Avengers: L'Ere d'Ultron"
        },
        {
            "question": "Who is T'Challa's cousin?",
            "choices": ["Klaue", "Erik Killmonger", "W'Kabi"],
            "answer": "Erik Killmonger"
        },
        {
            "question": "Who is the director?",
            "choices": ["Anthony Russo", "Joe Russo", "Ryan Coogler"],
            "answer": "Ryan Coogler"
        },
        {
            "question": "In which American city did Erik Stevens aka Killmonger grow up?",
            "choices": ["Cleveland", "JOakland", "Detroit", "Memphis"],
            "answer": "Oakland"
        },
        {
            "question": "What is Erik Stevens' real name?",
            "choices": ["N'Kabi", "N'Jadaka", "N'Tchaka", "N'Jobu"],
            "answer": "N'Jadaka"
        },
        {
            "question": "The post-credits scene shows Bucky being cryogenically frozen in Shuri's lab.",
            "choices": ["True", "False"],
            "answer": "False"
        },
        {
            "question": "What does T'Challa plan to do with the old building where Killmonger and his father lived?",
            "choices": ["A shelter for disadvantaged youth", "A place paying tribute to the memory of his cousin","Wakanda's first international aid center", "The first Wakanda embassy"],
            "answer": "Wakanda's first international aid center"
        }
    ]

    score = 0

    print("Welcome to the quiz about the movie Black Panther! :) \n")

    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {question['question']}")
        for j, choice in enumerate(question['choices'], 1):
            print(f"{j}. {choice}")

        while True:
            replay = input("Do you want to play again? (yes/no): ").strip().lower()
            if replay == 'yes':
                quiz()
                break
            elif replay == 'no':
                print("Thanks for playing!")
                break
            else:
                print("Please enter 'yes' or 'no'.")

                user_input = input("Your answer (enter number or text): ").strip()
                # Vérification si l'utilisateur entre un nombre ou du texte
                
                if user_input.isdigit():
                    user_choice = int(user_input)
                    if 1 <= user_choice <= len(question['choices']):
                        selected_answer = question['choices'][user_choice - 1]
                        break
                else:
                    print("Please enter a valid number.")
            else:
                selected_answer = user_input
                if selected_answer in question['choices']:
                    break
                else:
                    print("Please enter a valid choice.")

        if selected_answer == question['answer']:
            print("Correct! You earn 1 point.\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {question['answer']}.\n")

    print(f"Quiz complete! Your final score is : {score}/{len(questions)}.")

if __name__ == "__main__":
    quiz()
