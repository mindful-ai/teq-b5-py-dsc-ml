# Program to calculate the height of the building
# given the distance from the building and angle of sight

import math

# Input

dist = float(input('Enter the distance in mts: '))
ang  = float(input('Enter the angle of sight in degrees : '))

#dist = float(dist)

# Process

height = dist * math.tan(math.radians(ang))


# Output

print('Height is %.2f mts' % height)
