import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "


def parse_input(input_string):
    """Return `input_string` as an integer between 1 and 6

    Check if `input_string` is an integer number between 1 and 6.
    If so, return an integer with the same value. Otherwise, tell 
    the user to enter a valid number and quit the program.
    """

    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)


def roll_dice(num_dice):
    """Return a list of integers with length `num_dice`.

    Each integer in the returned list is a random number between
    1 and 6, inclusive 
    """
    roll_results = [random.randint(1, 6) for _ in range(num_dice)]
    return roll_results


def generate_face_diagram(dice_values):
    """Return an ASCII diagram of dice faces from `dice_values`

    The string returned contains an ASCII representation of each die.
    For example, if `dice_values = [4, 1, 3, 2]` then the string 
    returned looks like this:

    ~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~
    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
    │  ●   ●  │ │         │ │  ●      │ │  ●      │
    │         │ │    ●    │ │    ●    │ │         │
    │  ●   ●  │ │         │ │      ●  │ │      ●  │
    └─────────┘ └─────────┘ └─────────┘ └─────────┘
    """
    # Generate a list of dice faces from DICE_ART
    dice_faces = _get_dice_faces(dice_values)

    # Generate a list containing the dice face rows
    dice_faces_rows = _generate_dice_faces_rows(dice_faces)

    # Generate header with the word "RESULTS" centered
    header = " RESULTS ".center(len(dice_faces_rows[0]), "~")

    # Combine header and rows to return output as a singe string
    dice_faces_diagram = "\n".join([header] + dice_faces_rows)
    return dice_faces_diagram


def _get_dice_faces(dice_values):
    dice_faces = [DICE_ART[value] for value in dice_values]
    return dice_faces


def _generate_dice_faces_rows(dice_faces):
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for dice in dice_faces:
            row_components.append(dice[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)
    return dice_faces_rows


# App's main code block
# 1. Get and validate user's input
num_dice_input = input("How many dice do you want to roll? [1-6] ")
num_dice = parse_input(num_dice_input)

# 2. Roll the dice
roll_results = roll_dice(num_dice)

# 3. Generate the ASCII art
dice_face_diagram = generate_face_diagram(roll_results)
print(f"\n{dice_face_diagram}")
