# Q1: Moringa School Career Fair sign-up

FILENAME = r"C:\Users\User\Desktop\Moringa-School-Labs\Python_Functions\attendees.txt"

# Count existing records (0 if the file doesn't exist yet)
try:
    with open(FILENAME, "r") as file:
        ticket_number = len(file.readlines()) + 1
except FileNotFoundError:
    ticket_number = 1

# Collect details
name = input("Enter your name: ")
course = input("Enter your course: ")
mode = input("Mode of learning (part-time or full-time): ")

# Append the new record
with open(FILENAME, "a") as file:
    file.write(f"{name},{course},{mode}\n")

# Confirmation
print("\nThanks for signing up for the Moringa School Career Fair!")
print(f"Ticket No: {ticket_number}")
print(f"Name: {name}")
print(f"Course: {course} - {mode.title()}")