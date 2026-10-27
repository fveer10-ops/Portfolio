# Pong Game

This project includes a simple 2D Pong game built with Python and Pygame CE.

Features:
- Single-player mode against a CPU-controlled opponent
- Local two-player mode with one keyboard
- Score tracking and win condition
- Clean MVC-style architecture for easier maintenance

Installation:
1. Open a terminal in the repository root.
2. Install the dependency:
   python -m pip install -r requirements.txt
3. Start the game:
   python -m pong_game.main

Controls:
- Single-player mode: W / S move the left paddle; the right paddle is controlled by the CPU.
- Two-player mode: Player 1 uses W / S, Player 2 uses Up / Down.
- Escape exits the game.

Project Structure:
- pong_game/models.py: ball, paddle, and game state logic
- pong_game/views.py: rendering and screen presentation
- pong_game/controllers.py: input handling, game loop, AI, and state transitions
- pong_game/main.py: application entry point
