# Match case statement in Python

def day_of_week(day):
    match day:
        case "Sunday":
            return "It's Sunday!"
        case "Monday":
            return "It's Monday!"
        case "Tuesday":
            return "It's Tuesday!"
        case "Wednesday":
            return "It's Wednesday!"
        case "Thursday":
            return "It's Thursday!"
        case "Friday":
            return "It's Friday!"
        case "Saturday":
            return "It's Saturday!"
        case _:
            return "Invalid day!"
        
print(day_of_week("Monday"))
