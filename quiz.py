print("Welcome to the Computer Science Quiz!")
playing = input("Do you want to play? (yes/no) ").lower()

if playing != "yes":
    print("Maybe next time!")
    quit()

print("Great! Let's begin :)")
score = 0

# Question 1
answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The answer is Central Processing Unit.")

# Question 2
answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The answer is Random Access Memory.")

# Question 3
answer = input("What does HTML stand for? ").lower()
if answer == "hypertext markup language":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The answer is HyperText Markup Language.")

# Show final score
print(f"\nYou got {score} out of 3 questions correct!")
print(f"Your score: { (score / 3) * 100 }%")