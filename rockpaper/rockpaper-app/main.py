import streamlit as st
import random

# Set page title
st.set_page_config(page_title="Rock, Paper, Scissors Game", page_icon="🪐")

# Title and description
st.title("🪐 Rock, Paper, Scissors Game")
st.markdown("""
Welcome to the **Rock, Paper, Scissors** game!  
Choose one of the options below and see if you can beat the computer.
""")

# User choice
user_choice = st.radio("Choose your move:", ["Rock", "Paper", "Scissors"])

# Display user's choice
st.write(f"Your choice: {user_choice}")

# Computer's choice
options = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(options)
st.write(f"Computer's choice: {computer_choice}")

# Game logic to determine the winner
def game_result(user, computer):
    if user == computer:
        return "It's a tie! 😐"
    elif (user == "Rock" and computer == "Scissors") or (user == "Paper" and computer == "Rock") or (user == "Scissors" and computer == "Paper"):
        return "You win! 🎉"
    else:
        return "You lose! 😞"

# Display the result of the game
result = game_result(user_choice, computer_choice)
st.write(result)

# Play again button
if st.button("Play Again"):
    st.experimental_rerun()  # this might still trigger the error, so we'll remove this part
