while True:
    # Enter three quiz marks.
    quiz1 = float(input("Quiz 1: "))
    quiz2 = float(input("Quiz 2: "))
    quiz3 = float(input("Quiz 3: "))

    # Calculate the average.
    average = (quiz1 + quiz2 + quiz3) / 3
    print("Average mark:", round(average, 2))

    # Check pass or fail.
    if average >= 50:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    # Ask if another student should be entered.
    again = input("Enter another student's marks? (y/n): ").lower()
    if again != "y":
        break
