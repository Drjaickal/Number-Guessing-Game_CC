import random

def get_guess(lower_bound, upper_bound):
  """
  Prompts the user for a guess within the specified range and validates the input.

  Args:
      lower_bound: The lower bound of the guessing range.
      upper_bound: The upper bound of the guessing range.

  Returns:
      A valid integer guess within the range.
  """
  while True:
    try:
      guess_str = input(f"Guess a number between {lower_bound} and {upper_bound}: ")
      guess = int(guess_str)
      if lower_bound <= guess <= upper_bound:
        return guess
      else:
        print("Invalid input. Please enter a number within the specified range.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def play_game():
  """
  Runs a single round of the number guessing game.
  """
  # Set the difficulty level (optional)
  difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
  if difficulty == "easy":
    lower_bound = 1
    upper_bound = 10
  elif difficulty == "medium":
    lower_bound = 1
    upper_bound = 100
  else:
    lower_bound = 1
    upper_bound = 1000

  # Generate the secret number
  secret_number = random.randint(lower_bound, upper_bound)

  # Initialize number of guesses
  num_guesses = 0

  # Main game loop
  print("Welcome to the Number Guessing Game!")
  while True:
    guess = get_guess(lower_bound, upper_bound)
    num_guesses += 1

    if guess == secret_number:
      print(f"Congratulations! You guessed the number {secret_number} in {num_guesses} attempts.")
      break
    elif guess < secret_number:
      print("Too low, try again.")
    else:
      print("Too high, try again.")

if __name__ == "__main__":
  play_game()

  while True:
    play_again = input("Play again? (y/n): ").lower()
    if play_again == 'y':
      play_game()
    else:
      print("Thanks for playing!")
      break
