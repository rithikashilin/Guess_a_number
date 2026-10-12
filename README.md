This Python program is a simple interactive game where the computer randomly selects a number between 1 and 100, and the player tries to guess it.The program provides hints (Too Low or Too High) until the correct number is guessed.

How It Works:
  Step1: The program generates a random number between 1 and 100 using random.randint().
  Step2: The player is prompted to guess the number.
  Step3: The program checks:
          ~If the guess is equal to the number → prints Correct Guess and ends the game.
          ~If the guess is lower → prints Too Low.
          ~If the guess is higher → prints Too High.
  Step4: The loop continues until the correct guess is made.

Sample output:

  Guess a number between 1 to 100: 50
  Too Low
  Guess a number between 1 to 100: 75
  Too High
  Guess a number between 1 to 100: 63
  Correct Guess
