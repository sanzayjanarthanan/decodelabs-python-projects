def main():
    total = 0.0
    count = 0

    print("Expense Tracker")
    print("Enter expense amounts one by one.")
    print("Type 'done' when finished.\n")

    while True:
        user_input = input("Enter expense (or 'done' to finish): ").strip()

        if user_input.lower() == "done":
            break

        try:
            expense = float(user_input)
            total += expense
            count += 1
            print(f"✅ Added ₹{expense}. Running total: ₹{total}\n")
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.\n")

    print("\n--- SUMMARY ---")
    print(f"Total expenses entered: {count}")
    print(f"Total Spent: ₹{total}")

if __name__ == "__main__":
    main()