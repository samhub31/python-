import psycopg2
from collections import Counter
import random
import logging

# Define the table data as a dictionary
table_data = {
    "MONDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "TUESDAY": "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE",
    "WEDNESDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE",
    "THURSDAY": "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "FRIDAY": "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"
}

# Combine all the colors into a single list
all_colors = [color.strip() for colors in table_data.values() for color in colors.split(",")]

# Count the occurrences of each color
color_counts = Counter(all_colors)

# Find the color with the highest count (mean color)
mean_color = color_counts.most_common(1)[0][0]

# Print the mean color
print("The mean color of shirts is:", mean_color)

###########################################################################################################################

# Create a dictionary to store color counts for each day
color_counts_per_day = {day: Counter(colors.split(', ')) for day, colors in table_data.items()}

# Combine all the color counts from each day
all_color_counts = Counter()
for counts in color_counts_per_day.values():
    all_color_counts += counts

# Find the color with the highest total count (most worn color throughout the week)
most_worn_color = all_color_counts.most_common(1)[0][0]

print("The color mostly worn throughout the week is:", most_worn_color)

############################################################################################################################

# Sort the colors by their counts
sorted_colors = sorted(color_counts.items(), key=lambda x: x[1])

# Find the median color(s)
total_colors = len(sorted_colors)
if total_colors % 2 == 1:
    median_color = sorted_colors[total_colors // 2][0]
else:
    middle1 = sorted_colors[total_colors // 2 - 1]
    middle2 = sorted_colors[total_colors // 2]
    median_color = (middle1[0], middle2[0])

print("The median color(s) is/are:", median_color)

################################################################################################################################

# Count of red
red_count = color_counts.get("RED", 0)

# Total count of colors
total_count = sum(color_counts.values())

# Probability of choosing red at random
probability_red = red_count / total_count

print("The probability of choosing red at random is:", probability_red)

#############################################################################################################################

def recursive_search(numbers, target, index=0):
    if index == len(numbers):
        return -1  # Number not found in the list
    if numbers[index] == target:
        return index  # Number found at this index
    return recursive_search(numbers, target, index + 1)

# Example usage:
numbers = [1, 3, 5, 7, 9, 11, 13, 15]
target = int(input("Enter a number to search for: "))
result = recursive_search(numbers, target)

if result != -1:
    print(f"{target} found at index {result}")
else:
    print(f"{target} not found in the list")

##################################################################################################################################


# Generate a random 4-digit binary number
random_binary = ''.join(random.choice('01') for _ in range(4))

# Convert the binary number to base 10
decimal_number = int(random_binary, 2)

print(f"Random Binary: {random_binary}")
print(f"Decimal Equivalent: {decimal_number}")

############################################################################################################################################

def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Initialize with the first two Fibonacci numbers

    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

# Generate the first 50 Fibonacci numbers
n = 50
fibonacci_sequence = generate_fibonacci(n)

# Calculate and print the sum of the first 50 Fibonacci numbers
fibonacci_sum = sum(fibonacci_sequence)
print(f"Sum of the first {n} Fibonacci numbers: {fibonacci_sum}")



