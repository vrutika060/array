def main():
    scores = input("Enter scores separated by spaces: ")

    scores = [float(score) for score in scores.split()]

    if not scores:
        print("No scores entered.")
        return

    total = sum(scores)
    average = total / len(scores)

    print("Scores:", scores)
    print("Sum:", total)
    print("Average:", average)


if __name__ == "__main__":
    main()