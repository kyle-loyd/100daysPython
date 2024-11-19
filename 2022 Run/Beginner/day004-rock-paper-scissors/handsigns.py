rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

handsign_names = {
  0: "rock",
  1: "paper",
  2: "scissors"
}

outcomes = {
  "01": "Paper beats rock. You lose!",
  "02": "Rock beats scissors. You win!",
  "10": "Paper beats rock. You win!",
  "12": "Scissors beats paper. You lose!",
  "20": "Rock beats scissors. You lose!",
  "21": "Scissors beats paper. You win!"
}