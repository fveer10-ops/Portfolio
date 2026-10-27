from __future__ import annotations

import random

import pygame

WIDTH = 900
HEIGHT = 600
PADDLE_WIDTH = 18
PADDLE_HEIGHT = 110
PADDLE_SPEED = 430
BALL_RADIUS = 10
INITIAL_BALL_SPEED = 280
WIN_SCORE = 7


class Paddle:
    def __init__(self, x: float, y: float, width: float, height: float, speed: float):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def move(self, direction: int, delta_time: float) -> None:
        self.rect.y += direction * self.speed * delta_time
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))

    def move_towards_ball(self, ball: "Ball", delta_time: float, difficulty: float = 0.8) -> None:
        if ball.rect.centery > self.rect.centery:
            self.rect.y += self.speed * difficulty * delta_time
        elif ball.rect.centery < self.rect.centery:
            self.rect.y -= self.speed * difficulty * delta_time
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))


class Ball:
    def __init__(self, x: float, y: float, radius: float, speed_x: float, speed_y: float):
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self, delta_time: float) -> None:
        self.rect.x += self.speed_x * delta_time
        self.rect.y += self.speed_y * delta_time

    def reset(self, direction: int) -> None:
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x = direction * INITIAL_BALL_SPEED
        self.speed_y = random.uniform(-INITIAL_BALL_SPEED * 0.75, INITIAL_BALL_SPEED * 0.75)


class GameModel:
    def __init__(self):
        self.left_score = 0
        self.right_score = 0
        self.left_paddle = Paddle(28, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED)
        self.right_paddle = Paddle(WIDTH - 28 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED)
        self.ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, 0, 0)
        self.reset_match()

    def reset_match(self) -> None:
        self.left_score = 0
        self.right_score = 0
        self.left_paddle.rect.y = HEIGHT // 2 - PADDLE_HEIGHT // 2
        self.right_paddle.rect.y = HEIGHT // 2 - PADDLE_HEIGHT // 2
        self.ball.reset(random.choice([-1, 1]))

    def reset_ball(self, direction: int) -> None:
        self.ball.reset(direction)

    def award_point(self, left_scored: bool) -> None:
        if left_scored:
            self.left_score += 1
            self.reset_ball(1)
        else:
            self.right_score += 1
            self.reset_ball(-1)

    def clamp_ball(self) -> None:
        if self.ball.rect.top <= 0:
            self.ball.rect.top = 0
            self.ball.speed_y *= -1
        if self.ball.rect.bottom >= HEIGHT:
            self.ball.rect.bottom = HEIGHT
            self.ball.speed_y *= -1

    def handle_paddle_collision(self, paddle: Paddle, is_left_paddle: bool) -> None:
        if not self.ball.rect.colliderect(paddle.rect):
            return

        if is_left_paddle and self.ball.speed_x < 0:
            self.ball.rect.left = paddle.rect.right
        elif not is_left_paddle and self.ball.speed_x > 0:
            self.ball.rect.right = paddle.rect.left

        relative_hit = (self.ball.rect.centery - paddle.rect.centery) / (paddle.rect.height / 2)
        self.ball.speed_x *= -1.06
        self.ball.speed_y = relative_hit * 310

        self.ball.speed_x = max(-720, min(720, self.ball.speed_x))
        self.ball.speed_y = max(-720, min(720, self.ball.speed_y))

    def update(self, delta_time: float) -> None:
        self.ball.update(delta_time)
        self.clamp_ball()

        if self.ball.rect.left <= 0:
            self.award_point(False)
            return
        if self.ball.rect.right >= WIDTH:
            self.award_point(True)
            return

        self.handle_paddle_collision(self.left_paddle, True)
        self.handle_paddle_collision(self.right_paddle, False)

    def get_winner(self) -> str | None:
        if self.left_score >= WIN_SCORE:
            return "Player 1"
        if self.right_score >= WIN_SCORE:
            return "Player 2"
        return None


__all__ = ["WIDTH", "HEIGHT", "PADDLE_WIDTH", "PADDLE_HEIGHT", "BALL_RADIUS", "WIN_SCORE", "Paddle", "Ball", "GameModel"]
