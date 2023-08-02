import random

def roll_dice():
    # Function to simulate rolling a standard 6-sided dice
    return random.randint(1, 6)

def print_dice(dice_value):
    # Function to display ASCII art for the dice roll result
    dice_art = [
        " ------- ",
        "|       |",
        "|   O   |",
        "|       |",
        " ------- "
    ]
    
    # Update the ASCII art based on the dice_value
    if dice_value == 1:
        dice_art[2] = "|       |"
    elif dice_value == 2:
        dice_art[1] = "| O     |"
        dice_art[3] = "|     O |"
    elif dice_value == 3:
        dice_art[1] = "| O     |"
        dice_art[2] = "|   O   |"
        dice_art[3] = "|     O |"
    elif dice_value == 4:
        dice_art[1] = "| O   O |"
        dice_art[3] = "| O   O |"
    elif dice_value == 5:
        dice_art[1] = "| O   O |"
        dice_art[2] = "|   O   |"
        dice_art[3] = "| O   O |"
    else:
        dice_art[1] = "| O   O |"
        dice_art[2] = "| O   O |"
        dice_art[3] = "| O   O |"

    # Print the dice ASCII art
    for line in dice_art:
        print(line)

def main():
    # Main function to run the dice simulator
    print("Welcome to the Dice Simulator made in Python!")
    while True:
        # Wait for the user to press Enter to roll the dice
        input("Press Enter to roll the dice...")
        
        # Roll the dice and get the result
        dice_value = roll_dice()
        
        # Display the dice result as ASCII art
        print("\nDice Result:")
        print_dice(dice_value)
        
        # Ask the user if they want to roll again
        repeat = input("Roll again? (y/n): ")
        if repeat.lower() != 'y':
            # If the user enters 'n', exit the loop and end the program
            print("Thank you for using the Dice Simulator made in Python!")
            break

if __name__ == "__main__":
    # Call the main function when the script is executed
    main()