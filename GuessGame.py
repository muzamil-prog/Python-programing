import random


class GuessingGame:

    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

    def play(self):
        print("🎮 Welcome to the Guessing Game!")
        print("I have selected a number between 1 and 100.")

        while True:
            try:
                guess = int(input("Enter your guess: "))
                self.attempts += 1

                if guess < self.secret_number:
                    print("📉 Too Low! Try again.")

                elif guess > self.secret_number:
                    print("📈 Too High! Try again.")

                else:
                    print("🎉 Congratulations!")
                    print(f"You guessed the number in {self.attempts} attempts.")
                    break

            except ValueError:
                print("❌ Please enter a valid number.")


# Create object
game = GuessingGame()

# Start game
game.play()