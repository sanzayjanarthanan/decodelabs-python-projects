def main():
    print("General Knowledge Quiz")
    print("-----------------------\n")

    questions = [
        {"question": "What is the capital of France?", "answer": "paris"},
        {"question": "Which planet is known as the Red Planet?", "answer": "mars"},
        {"question": "What is 5 + 7?", "answer": "12"}
    ]

    score = 0

    for q in questions:
        user_answer = input(q["question"] + " ").strip().lower()
        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.\n")

    print("--- QUIZ OVER ---")
    print(f"Your final score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()