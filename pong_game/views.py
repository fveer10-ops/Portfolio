from __future__ import annotations

# This module is responsible for drawing all visible game elements.
# The view receives the model state and renders it to the screen.
import pygame

from pong_game.models import GameModel, HEIGHT, WIDTH


class PongView:
    # The view handles all screen rendering and text presentation.
    def __init__(self, screen: pygame.Surface, game_model: GameModel):
        self.screen = screen
        self.game_model = game_model

        # Fonts are loaded once so text can be drawn consistently throughout the game.
        self.font = pygame.font.Font(None, 72)
        self.medium_font = pygame.font.Font(None, 42)
        self.small_font = pygame.font.Font(None, 28)

    def draw_background(self) -> None:
        # Fill the screen with a dark background and draw the center line.
        self.screen.fill((15, 20, 35))

        midpoint = WIDTH // 2
        for y in range(0, HEIGHT, 22):
            pygame.draw.rect(self.screen, (255, 255, 255), (midpoint - 2, y, 4, 14))

    def draw_scores(self) -> None:
        # Render the current score for both players at the top of the screen.
        left_text = self.font.render(str(self.game_model.left_score), True, (255, 255, 255))
        right_text = self.font.render(str(self.game_model.right_score), True, (255, 255, 255))

        left_rect = left_text.get_rect(midleft=(WIDTH // 2 - 90, 55))
        right_rect = right_text.get_rect(midright=(WIDTH // 2 + 90, 55))

        self.screen.blit(left_text, left_rect)
        self.screen.blit(right_text, right_rect)

    def draw_paddles_and_ball(self) -> None:
        # Draw the left paddle, right paddle, and ball in their current positions.
        pygame.draw.rect(self.screen, (255, 255, 255), self.game_model.left_paddle.rect)
        pygame.draw.rect(self.screen, (255, 255, 255), self.game_model.right_paddle.rect)
        pygame.draw.ellipse(self.screen, (255, 255, 255), self.game_model.ball.rect)

    def draw_menu(self) -> None:
        # Display the title screen and mode-selection instructions.
        self.draw_background()

        title = self.font.render("PONG", True, (255, 255, 255))
        title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 120))
        self.screen.blit(title, title_rect)

        menu_text = self.medium_font.render(
            "Press 1 for 1 Player or 2 for 2 Players",
            True,
            (235, 235, 235),
        )
        menu_rect = menu_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(menu_text, menu_rect)

        controls_text = self.small_font.render(
            "Player 1: W / S   Player 2: Up / Down   Esc: Quit",
            True,
            (190, 190, 190),
        )
        controls_rect = controls_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
        self.screen.blit(controls_text, controls_rect)

    def draw_game(self) -> None:
        # Draw the active game state: the background, scores, and moving objects.
        self.draw_background()
        self.draw_scores()
        self.draw_paddles_and_ball()

    def draw_game_over(self, winner: str) -> None:
        # Display the winner message after a match ends.
        self.draw_background()
        self.draw_scores()

        win_text = self.font.render(f"{winner} Wins!", True, (255, 255, 255))
        win_rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
        self.screen.blit(win_text, win_rect)

        prompt_text = self.small_font.render(
            "Press 1 or 2 to play again, or Esc to quit",
            True,
            (220, 220, 220),
        )
        prompt_rect = prompt_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
        self.screen.blit(prompt_text, prompt_rect)


__all__ = ["PongView"]
