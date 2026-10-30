from __future__ import annotations

import random

import pygame
from pygame.constants import K_1, K_2, K_3, K_4, K_DOWN, K_ESCAPE, K_UP, K_s, K_w

from pong_game.models import GameModel, HEIGHT, WIDTH, PADDLE_COLORS
from pong_game.views import PongView


class PongController:
    # The controller owns the game loop and manages the current game state.
    def __init__(self) -> None:
        # Initialize pygame and create the window used for drawing the game.
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()

        # Create the data model and the view that renders it.
        self.model = GameModel()
        self.view = PongView(self.screen, self.model)

        # Track whether the game should keep running and what screen is active.
        self.running = True
        self.state = "menu"
        self.mode: str | None = None
        self.winner: str | None = None

    def cycle_paddle_color(self, direction: int) -> None:
        unlocked = list(self.model.unlocked_paddle_colors)
        unlocked.sort(key=lambda item: list(PADDLE_COLORS.keys()).index(item))

        current_index = unlocked.index(self.model.selected_paddle_color)
        next_index = (current_index + direction) % len(unlocked)
        self.model.set_selected_paddle_color(unlocked[next_index])

    def start_single_player_match(self) -> None:
        self.mode = "single"
        self.state = "playing"
        self.model.reset_match()
        self.model.single_player_run_time = 0.0
        self.model.ball.reset(1)
        self.model.set_selected_paddle_color(self.model.selected_paddle_color)

    def start_two_player_match(self) -> None:
        self.mode = "two_player"
        self.state = "playing"
        self.model.reset_match()
        self.model.ball.reset(random.choice([-1, 1]))

    def run(self) -> None:
        # Main game loop: process input, update logic, redraw the screen,
        # and keep the frame rate consistent.
        while self.running:
            delta_time = self.clock.tick(60) / 1000.0
            self.handle_events()
            self.update(delta_time)
            self.render()
            pygame.display.flip()

        pygame.quit()

    def handle_events(self) -> None:
        # Read all queued pygame events and react to user input.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == K_ESCAPE:
                self.running = False
                return

            # When in the menu screen, pressing 1 or 2 starts a new match.
            if self.state == "menu":
                if event.key == K_1:
                    self.start_single_player_match()
                    return

                if event.key == K_2:
                    self.start_two_player_match()
                    return

                if event.key == K_3:
                    self.cycle_paddle_color(-1)
                    return

                if event.key == K_4:
                    self.cycle_paddle_color(1)
                    return

                if event.key == K_5:
                    self.model.selected_paddle_color = "classic"
                    self.model.left_paddle.color = PADDLE_COLORS["classic"]
                    return

            # After a match ends, the player can restart in either mode.
            elif self.state == "game_over":
                if event.key == K_1:
                    self.start_single_player_match()
                    self.winner = None
                    return

                if event.key == K_2:
                    self.start_two_player_match()
                    self.winner = None
                    return

    def update(self, delta_time: float) -> None:
        # Ignore updates when the game is not currently active.
        if self.state != "playing":
            return

        keys = pygame.key.get_pressed()

        # In single-player mode, the left paddle is controlled by the user
        # and the right paddle follows the ball automatically.
        if self.mode == "single":
            if keys[K_w]:
                self.model.left_paddle.move(-1, delta_time)
            if keys[K_s]:
                self.model.left_paddle.move(1, delta_time)

            self.model.right_paddle.move_towards_ball(self.model.ball, delta_time, difficulty=0.82)

        # In two-player mode, both paddles are controlled by keyboard input.
        elif self.mode == "two_player":
            if keys[K_w]:
                self.model.left_paddle.move(-1, delta_time)
            if keys[K_s]:
                self.model.left_paddle.move(1, delta_time)
            if keys[K_UP]:
                self.model.right_paddle.move(-1, delta_time)
            if keys[K_DOWN]:
                self.model.right_paddle.move(1, delta_time)

        # Update the model after the players have moved.
        self.model.update(delta_time)

        if self.mode == "single":
            self.model.update_single_player_countdown(delta_time)

        # Check whether someone reached the win condition and switch states.
        winner = self.model.get_winner()
        if winner is not None:
            self.winner = winner
            self.state = "game_over"
            self.mode = None

    def render(self) -> None:
        # Draw the correct screen depending on the current game state.
        if self.state == "menu":
            self.view.draw_menu()
            return

        if self.state == "game_over":
            self.view.draw_game_over(self.winner or "Player")
            return

        self.view.draw_game()


def main() -> None:
    # Construct the controller and start the game loop.
    game = PongController()
    game.run()


if __name__ == "__main__":
    main()

