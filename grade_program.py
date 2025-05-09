#!/usr/bin/env python3
# Created by: Gustav I
# Created on: May 9, 2025
# This program defines a function to convert grade levels to percentages (middle percentages)


def main():
    level = input("Enter a level (e.g. 4+, 3, 2-, R, I): ")
    result = calc_mark(level)
    if result == -1:
        print("Invalid level entered. Please retry")
    else:
        print(f"The middle percentage mark for level {level} is {result}%.")


def calc_mark(level):
    mark = -1  # Default to invalid

    if level == "4+":
        mark = 95
    elif level == "4":
        mark = 87
    elif level == "4-":
        mark = 82
    elif level == "3+":
        mark = 78
    elif level == "3":
        mark = 75
    elif level == "3-":
        mark = 71
    elif level == "2+":
        mark = 68
    elif level == "2":
        mark = 65
    elif level == "2-":
        mark = 61
    elif level == "1+":
        mark = 57
    elif level == "1":
        mark = 52
    elif level == "1-":
        mark = 51
    elif level == "R":
        mark = 30
    elif level == "I":
        mark = 0

    return mark


# This runs main() only if this file is run directly
if __name__ == "__main__":
    main()
