import random

ticket1 = []
while len(ticket1) < 5:
    n = int(random.random() * 90) + 1
    if n not in ticket1:
        ticket1.append(n)

print("Your Ticket 1:", ticket1)


ticket2 = []
while len(ticket2) < 5:
    n = int(random.random() * 90) + 1
    if n not in ticket2:
        ticket2.append(n)

print("Your Ticket 2:", ticket2)


ticket3 = []
while len(ticket3) < 5:
    n = int(random.random() * 90) + 1
    if n not in ticket3:
        ticket3.append(n)

print("Your Ticket 3:", ticket3)

drawn = []

attempts = 0
max_attempts = 15

while attempts < max_attempts:
    input("\nPress Enter to draw number...")

    # Draw unique number
    while True:
        num = int(random.random() * 90) + 1
        if num not in drawn:
            drawn.append(num)
            break

    attempts += 1
    print("Number Drawn:", num)
    print("Attempt:", attempts)

    
    if all(n in drawn for n in ticket1):
        print("\n Ticket 1 Wins! ")
        break

    if all(n in drawn for n in ticket2):
        print("\n Ticket 2 Wins! ")
        break

    if all(n in drawn for n in ticket3):
        print("\n Ticket 3 Wins! ")
        break

if attempts == max_attempts:
    print("\nGame Over! No ticket completed in 15 attempts.")
