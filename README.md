# 🛳️ Battleship Game

A simple terminal-based implementation of the classic Battleship game using Python.

Players have 10 turns to guess the hidden location of 5 enemy ships on an 8x8 grid. Guessing is done by entering row (1–8) and column (A–H) coordinates. The goal is to sink all ships before you run out of turns!


## 🎮 How to Play

- The game board is an 8x8 grid labeled with **rows (1–8)** and **columns (A–H)**.
- There are **5 hidden ships** randomly placed on the grid.
- You will be prompted to guess a ship's location by entering the row and column.
- You have **10 turns** to try and sink all 5 ships.
- Hits are marked with `X`, and misses are marked with `O`.
- Try not to repeat guesses!


## 📁 Project Structure

## 🚀 Running the Game Locally and on Heroku

Follow these steps to start playing Battleship directly in your browser via the Heroku app:

### 1. **Visit the Heroku App**  
   Click on the link below to open the Battleship game in your browser:
   
   [Play Battleship on Heroku](https://battleship-danivgiulia-199c33dc989b.herokuapp.com/)

   - This will open the game in a web-based terminal.

### 2. Clone the repository
```bash
git clone https://github.com/Danivgiulia/battleship-game.git
```

## 🌐 Deployment

To deploy this project, I used [Heroku](https://www.heroku.com/)

Here’s how I set it up:


1. **Pushed the code to GitHub**  
   I uploaded the full project to a new GitHub repository.

2. **Created a new Heroku app**  
   I logged into Heroku and created a new app from the dashboard. Then I connected my GitHub repo to the app under the **"Deploy"** tab.

3. **Set the buildpack to Python**  
   Heroku didn’t show buildpacks at first, but I manually added the Python buildpack under **"Settings" → "Buildpacks"** by selecting `heroku/python` and then `heroku/nodejs` in the order.

4. **Set a config variable for the port**  
   I went to **"Settings" → "Config Vars"** and added a new variable:
   - Key: `PORT`
   - Value: `8000`

5. **Deployed the app**  
   Back in the **"Deploy"** tab, I selected my GitHub branch (usually `main`) and clicked **"Deploy Branch"**. After it built and deployed, I opened the app using the "Open App" button.

> ✅ Note: Since this is a terminal-based game, it won’t render as an interactive game in a web browser. It's designed to run in a Python environment (like locally or through a terminal), but I deployed it to demonstrate cloud deployment with Heroku.

## 🐞 Bugs I Encountered

While building the game, I ran into a few bugs. One of the first issues was:

### 🔹 Empty User Input Caused a Crash

**What happened:**  
When the user was prompted to enter a row or column and just pressed Enter without typing anything, the game would crash with an error (like a `KeyError` or `IndexError`), since the input wasn’t validated properly.

**How I fixed it:**  
I added input validation loops that check:
- If the input is actually present
- If the value is within the expected range (1–8 for rows, A–H for columns)
- If not, the game displays a message and asks the user to try again

Example of the updated input check:
```python
row = input("Please enter a ship row (1–8): ")
while row not in '12345678':
    print("Please enter a valid row.")
    row = input("Please enter a ship row (1–8): ")
```

Throughout development, I also encountered several smaller issues, such as:

- **Blank spaces around `=` in function arguments**  
  These were flagged by linters (like `flake8`) and caused style warnings. I corrected them by removing the spaces:
  ```python
  # Before
  def print_board(board, start = 1)

  # After
  def print_board(board, start=1)
  ```

## PEP8 Compliance

To ensure clean, readable, and professional-quality code, I followed the [Code Institute's PEP8 Python Style Guide](https://pep8ci.herokuapp.com/) throughout development.

### ✅ What I Checked

- **Consistent indentation** (4 spaces per level)
- **Proper spacing** around operators and assignment statements  
  Example: `x = 5` instead of `x=5`
- **Function and variable naming** using `snake_case`
- **Two blank lines** before function and class definitions
- **No lines longer than 79 characters** (where possible)
- **No trailing whitespace** or unused imports

### 🔧 Tool Used

I used the [Code Institute's PEP8 CI Validator](https://pep8ci.herokuapp.com/) to check my code. This tool automatically detects:

- Syntax and indentation issues  
- Style violations like extra spaces or missing blank lines  

## 🚀 Future Features

While the current version of the game is fully functional, I plan to add more exciting features to enhance the gameplay experience. Some of the future improvements include:

### 🔹 Dynamic Ship Sizes

This will require adjusting the logic for ship placement to ensure that ships are randomly placed in a way that respects their lengths and the boundaries of the 8x8 grid.

### 🔹 Multiplayer Functionality

I would love to expand the game to allow for **multiplayer** so that users can play against each other. This feature could include:
- **Turn-based gameplay**, where players take turns guessing each other’s ship locations.

## 💡 Credits & Acknowledgments

This project was built with inspiration from various online sources and tutorials that helped guide the development process. 

- **[Python Documentation](https://docs.python.org/3/)**
- **[W3Schools](https://www.w3schools.com/python/)**
- **[Real Python](https://realpython.com/)**
- **[Stack Overflow](https://stackoverflow.com/)**
- **[GitHub](https://github.com/)**

### Inspiration from Online Battleship Python Projects:
- **[Python Battleship Game by "codeit"](https://www.codeitbro.com/python-battleship-game-project/)**: This tutorial provided great insights on implementing a simple Battleship game in Python, which helped me understand the basic logic for ship placement and turn-based gameplay.
- **[Real Python Battleship Tutorial](https://realpython.com/python-battleship-game/)**: A step-by-step tutorial on how to build a Python Battleship game. It was particularly useful for understanding how to handle the game logic and user input validation.
- **[GitHub Repository: Python Battleship Game](https://github.com/abhishekchandan/python-battleship)**: A fantastic open-source Python Battleship game repository that I referred to for understanding how to implement ship placement, randomization, and board display.
- **[GeeksforGeeks Python Battleship Game](https://www.geeksforgeeks.org/python-project-battleship-game/)**: This tutorial helped me with basic Python game logic, such as using loops, conditional statements, and managing the game flow.