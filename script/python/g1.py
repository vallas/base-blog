import time

def render_globe():
    # Initialize the globe
    globe = [
        "     o ",
        "     o ",
        "     o ",
        " ooooo ",
        " o   o ",
        " o   o ",
        " o   o ",
        " ooooo "
    ]

    # Rotate the globe 10 times
    for i in range(10):
        # Clear the terminal
        print("\033[2J")

        # Print the globe in its current orientation
        for line in globe:
            print(line)

        # Rotate the globe 90 degrees clockwise
        globe = ["".join(x) for x in zip(*globe[::-1])]

        # Sleep for a short time to animate the rotation
        time.sleep(0.25)

# Render the spinning globe
render_globe()
