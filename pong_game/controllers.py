from __future__ import annotations

import random

import pygame
from pygame.constants import K_1, K_2, K_DOWN, K_ESCAPE, K_UP, K_s, K_w

from pong_game.models import GameModel, HEIGHT, WIDTH
from pong_game.views import PongView


class PongController:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()
        self.model = GameModel()
        self.view = PongView(self.screen, self.model)
        self.running = True
        self.state = "menu"
        self.mode: str | None = None
        self.winner: str | None = None

    def run(self) -> None:
        while self.running:
            delta_time = self.clock.tick(60) / 1000.0
            self.handle_events()
            self.update(delta_time)
            self.render()
            pygame.display.flip()

        pygame.quit()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == K_ESCAPE:
                self.running = False
                return

            if self.state == "menu":
                if event.key == K_1:
                    self.mode = "single"
                    self.state = "playing"
                    self.model.reset_match()
                    self.model.ball.reset(1)
                    return

                if event.key == K_2:
                    self.mode = "two_player"
                    self.state = "playing"
                    self.model.reset_match()
                    self.model.ball.reset(random.choice([-1, 1]))
                    return

            elif self.state == "game_over":
                if event.key == K_1:
                    self.mode = "single"
                    self.state = "playing"
                    self.model.reset_match()
                    self.model.ball.reset(1)
                    self.winner = None
                    return

                if event.key == K_2:
                    self.mode = "two_player"
                    self.state = "playing"
                    self.model.reset_match()
                    self.model.ball.reset(random.choice([-1, 1]))
                    self.winner = None
                    return

    def update(self, delta_time: float) -> None:
        if self.state != "playing":
            return

        keys = pygame.key.get_pressed()

        if self.mode == "single":
            if keys[K_w]:
                self.model.left_paddle.move(-1, delta_time)
            if keys[K_s]:
                self.model.left_paddle.move(1, delta_time)

            self.model.right_paddle.move_towards_ball(self.model.ball, delta_time, difficulty=0.82)

        elif self.mode == "two_player":
            if keys[K_w]:
                self.model.left_paddle.move(-1, delta_time)
            if keys[K_s]:
                self.model.left_paddle.move(1, delta_time)
            if keys[K_UP]:
                self.model.right_paddle.move(-1, delta_time)
            if keys[K_DOWN]:
                self.model.right_paddle.move(1, delta_time)

        self.model.update(delta_time)

        winner = self.model.get_winner()
        if winner is not None:
            self.winner = winner
            self.state = "game_over"
            self.mode = None

    def render(self) -> None:
        if self.state == "menu":
            self.view.draw_menu()
            return

        if self.state == "game_over":
            self.view.draw_game_over(self.winner or "Player")
            return

        self.view.draw_game()


def main() -> None:
    game = PongController()
    game.run()


if __name__ == "__main__":
    main()
