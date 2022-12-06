import time
import math

# Set the size of the globe
SIZE = 20

# Set the initial position of the sun
sun_x = 0
sun_y = 0

# Set the initial position and velocity of the earth
earth_x = 10
earth_y = 0
earth_vx = 0
earth_vy = 0.1

while True:
    # Clear the screen
    print("\033c", end="")

    # Compute the distance between the earth and the sun
    dx = sun_x - earth_x
    dy = sun_y - earth_y
    distance = math.sqrt(dx * dx + dy * dy)

    # Compute the gravitational force between the earth and the sun
    g = 0.01
    fx = g * dx / distance
    fy = g * dy / distance

    # Update the velocity of the earth based on the gravitational force
    earth_vx += fx
    earth_vy += fy

    # Update the position of the earth based on its velocity
    earth_x += earth_vx
    earth_y += earth_vy

    # Draw the sun at the center of the screen
    print("\033[33m@\033[0m")

    # Draw the earth at its current position
    earth_char = "\033[32mO\033[0m"
    for y in range(-SIZE, SIZE + 1):
        for x in range(-SIZE, SIZE + 1):
            # Compute the distance from the earth to the current position
            dx = x - earth_x
            dy = y - earth_y
            d = math.sqrt(dx * dx + dy * dy)

            # If the distance is less than the size of the earth,
            # draw the earth character at the current position
            if d <= SIZE:
                print(earth_char, end="")
            else:
                print(" ", end="")
        print()

    # Sleep for a short time before updating the screen again
    time.sleep(0.05)
