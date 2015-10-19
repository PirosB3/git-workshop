#!/usr/bin/env python

def calculate_bmi(weight, height):
    """
    Calculates BMI given the weight and height as float
    """
    bmi = (weight / (height * height)) * 703.0
    return bmi

def main():
    print "Welcome to our BMI calculator"

    # raw_input() waits to a line of input from the terminal.
    # Let user input height and weight and store them into their
    # correspondent variables as a string
    height_string = raw_input("Insert height in inches: ")
    weight_string = raw_input("Insert weight in pounds: ")

    # Convert height string representation into a float
    try:
        height = float(height_string)
    except ValueError:
        # We end up here if height_string is not a valid float.
        # We print a nice error message and then exit
        print "ERROR: height did not convert. Please try again"
        return

    # Convert weight string representation into a float
    try:
        weight = float(weight_string)
    except ValueError:
        # We end up here if weight_string is not a valid float.
        # We print a nice error message and then exit
        print "ERROR: weight did not convert. Please try again"
        return

    bmi = calculate_bmi(height, weight)
    print "Your BMI is %s" % bmi


if __name__ == '__main__':
    main()
