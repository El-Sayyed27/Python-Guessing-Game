# 🎯 Python-Guessing-Game

A simple Python number guessing game where the user has **6 attempts** to guess a randomly generated number between 1 and 100. The program provides feedback for each guess and handles invalid input gracefully.

## 🚀 Features
- Random number generation using Python's `random` module  
- Limited attempts (6 tries) for increased difficulty  
- Input validation with error handling  
- Interactive feedback (too high / too low)  
- Game ends when the player wins or runs out of attempts  

## 🛠️ Technologies Used
- Python 3  

## ⚙️ How to Run
- Ensure Python is installed on your system
- Clone the repository to your local computer `git clone https://github.com/El-Sayyed27/number-guessing-game.git`
- Install the 2 packages `pip install colorama playsound==1.2.2`  
- Navigate into downloaded folder `guessing_game`

## 🔊 Sound Effects
- The game also plays audio feedback for guesses:
  - **Correct guess:** plays `sounds/correct-answer.wav`  
  - **Wrong guess:** plays `sounds/wrong-answer.wav`

### Run the script:
```bash
python guessing_game.py
