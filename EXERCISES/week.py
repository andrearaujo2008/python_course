day = "Monday"

# Match the day to predifined patterns

match day:
    case "Satuday" | "Sunday":
        print(f"{day}is a weekend")  # Match weekends
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print(f"{day} is weekday")  # Match weekdays
    case _:
        print("That's not a valid day of the weekdays")
