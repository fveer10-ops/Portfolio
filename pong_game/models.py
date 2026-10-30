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

PADDLE_COLORS = {
    "classic": (255, 255, 255),
    "red": (255, 92, 92),
    "blue": (79, 153, 255),
    "green": (96, 221, 145),
    "purple": (176, 128, 255),
}

PADDLE_COLOR_UNLOCKS = {
    "classic": 0.0,
    "red": 8.0,
    "blue": 16.0,
    "green": 28.0,
    "purple": 45.0,
}


class Paddle:
    # A paddle is a rectangular object that moves vertically on the left or right side.
    def __init__(self, x: float, y: float, width: float, height: float, speed: float, color: tuple[int, int, int] = PADDLE_COLORS["classic"]):
        # A pygame Rect makes it easy to position and detect collisions.
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.color = color

    def move(self, direction: int, delta_time: float) -> None:
        # Move the paddle up or down while keeping it inside the game area.
        self.rect.y += direction * self.speed * delta_time
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))

    def move_towards_ball(self, ball: "Ball", delta_time: float, difficulty: float = 0.8) -> None:
        # AI paddle moves toward the ball's vertical position.
        if ball.rect.centery > self.rect.centery:
            self.rect.y += self.speed * difficulty * delta_time
        elif ball.rect.centery < self.rect.centery:
            self.rect.y -= self.speed * difficulty * delta_time
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))


class Ball:
    # The ball is what players hit back and forth.
    def __init__(self, x: float, y: float, radius: float, speed_x: float, speed_y: float):
        # The ball's rectangle is centered around the x/y position.
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self, delta_time: float) -> None:
        # Update the ball's position based on its current velocity.
        self.rect.x += self.speed_x * delta_time
        self.rect.y += self.speed_y * delta_time

    def reset(self, direction: int) -> None:
        # Reset the ball to the center and choose a starting direction.
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x = direction * INITIAL_BALL_SPEED
        self.speed_y = random.uniform(-INITIAL_BALL_SPEED * 0.75, INITIAL_BALL_SPEED * 0.75)


class GameModel:
    # The model holds the current game state and enforces the Pong rules.
    def __init__(self):
        # Scores start at zero and paddles are placed in the center of each side.
        self.left_score = 0
        self.right_score = 0
        self.single_player_high_score = 0.0
        self.single_player_run_time = 0.0
        self.selected_paddle_color = "classic"
        self.unlocked_paddle_colors = {"classic"}
        self.last_point_conceded = False

        self.left_paddle = Paddle(
            28,
            HEIGHT // 2 - PADDLE_HEIGHT // 2,
            PADDLE_WIDTH,
            PADDLE_HEIGHT,
            PADDLE_SPEED,
            PADDLE_COLORS[self.selected_paddle_color],
        )
        self.right_paddle = Paddle(
            WIDTH - 28 - PADDLE_WIDTH,
            HEIGHT // 2 - PADDLE_HEIGHT // 2,
            PADDLE_WIDTH,
            PADDLE_HEIGHT,
            PADDLE_SPEED,
            (255, 255, 255),
        )
        self.ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, 0, 0)
        self.reset_match()

    def reset_match(self) -> None:
        # Start a fresh round with both paddles centered and a random serve.
        self.left_score = 0
        self.right_score = 0
        self.last_point_conceded = False
        self.single_player_run_time = 0.0
        self.left_paddle.rect.y = HEIGHT // 2 - PADDLE_HEIGHT // 2
        self.right_paddle.rect.y = HEIGHT // 2 - PADDLE_HEIGHT // 2
        self.ball.reset(random.choice([-1, 1]))

    def reset_ball(self, direction: int) -> None:
        # Put the ball back in the center after a point is scored.
        self.ball.reset(direction)

    def set_selected_paddle_color(self, color_name: str) -> None:
        if color_name in self.unlocked_paddle_colors:
            self.selected_paddle_color = color_name
            self.left_paddle.color = PADDLE_COLORS[color_name]

    def update_unlocked_paddle_colors(self) -> None:
        for color_name, threshold in PADDLE_COLOR_UNLOCKS.items():
            if self.single_player_high_score >= threshold:
                self.unlocked_paddle_colors.add(color_name)

        if self.selected_paddle_color not in self.unlocked_paddle_colors:
            self.selected_paddle_color = "classic"
        self.left_paddle.color = PADDLE_COLORS[self.selected_paddle_color]

    def award_point(self, left_scored: bool) -> None:
        # Give the point to the correct player and reset the ball for the next serve.
        if left_scored:
            self.left_score += 1
            self.last_point_conceded = False
            self.reset_ball(1)
        else:
            self.right_score += 1
            self.last_point_conceded = True
            self.reset_ball(-1)

    def update_single_player_countdown(self, delta_time: float) -> None:
        # Record seconds survived without conceding a point.
        if self.last_point_conceded:
            self.single_player_run_time = 0.0
            self.last_point_conceded = False
            return

        self.single_player_run_time += delta_time
        if self.single_player_run_time > self.single_player_high_score:
            self.single_player_high_score = self.single_player_run_time
        self.update_unlocked_paddle_colors()

    def clamp_ball(self) -> None:
        # Keep the ball inside the top and bottom walls of the game field.
        if self.ball.rect.top <= 0:
            self.ball.rect.top = 0
            self.ball.speed_y *= -1
        if self.ball.rect.bottom >= HEIGHT:
            self.ball.rect.bottom = HEIGHT
            self.ball.speed_y *= -1

    def handle_paddle_collision(self, paddle: Paddle, is_left_paddle: bool) -> None:
        # Bounce the ball whenever it collides with a paddle.
        if not self.ball.rect.colliderect(paddle.rect):
            return

        # Prevent the ball from getting stuck inside the paddle when it hits.
        if is_left_paddle and self.ball.speed_x < 0:
            self.ball.rect.left = paddle.rect.right
        elif not is_left_paddle and self.ball.speed_x > 0:
            self.ball.rect.right = paddle.rect.left

        # Adjust the ball's angle based on where it hits the paddle.
        relative_hit = (self.ball.rect.centery - paddle.rect.centery) / (paddle.rect.height / 2)
        self.ball.speed_x *= -1.06
        self.ball.speed_y = relative_hit * 310

        # Keep the ball speed within a reasonable range so the game remains fair.
        self.ball.speed_x = max(-720, min(720, self.ball.speed_x))
        self.ball.speed_y = max(-720, min(720, self.ball.speed_y))

    def update(self, delta_time: float) -> None:
        # Update the ball's movement and test for wall, paddle, and scoring events.
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
        # Return the player name when one player reaches the win target.
        if self.left_score >= WIN_SCORE:
            return "Player 1"
        if self.right_score >= WIN_SCORE:
            return "Player 2"
        return None


__all__ = [
    "WIDTH",
    "HEIGHT",
    "PADDLE_WIDTH",
    "PADDLE_HEIGHT",
    "BALL_RADIUS",
    "WIN_SCORE",
    "PADDLE_COLORS",
    "PADDLE_COLOR_UNLOCKS",
    "Paddle",
    "Ball",
    "GameModel",
]

