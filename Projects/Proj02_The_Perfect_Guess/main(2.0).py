# The gussing game (Multiplayer)



import random
from abc import ABC, abstractmethod
from typing import Optional, List
from functools import wraps
from dataclasses import dataclass, field
from enum import Enum


class Difficulty(Enum):
    EASY = (1, 50, 10)
    MEDIUM = (1, 100, 7)
    HARD = (1, 200, 5)
    
    def __init__(self, min_val: int, max_val: int, max_attempts: int):
        self.min_val = min_val
        self.max_val = max_val
        self.max_attempts = max_attempts


@dataclass
class Stats:
    attempts: int = 0
    games_played: int = 0
    games_won: int = 0
    best_score: Optional[int] = None
    guess_history: List[int] = field(default_factory=list)


def attempt_counter(func):
    @wraps(func)
    def wrapper(self, guess: int):
        self.stats.attempts += 1
        self.stats.guess_history.append(guess)
        return func(self, guess)
    return wrapper


def game_tracker(func):
    @wraps(func)
    def wrapper(self):
        result = func(self)
        self.stats.games_played += 1
        if result:
            self.stats.games_won += 1
            if not self.stats.best_score or self.stats.attempts < self.stats.best_score:
                self.stats.best_score = self.stats.attempts
        return result
    return wrapper


class Game(ABC):
    def __init__(self):
        self.stats = Stats()
    
    @abstractmethod
    def generate_number(self) -> int:
        pass
    
    @abstractmethod
    def check_guess(self, guess: int) -> str:
        pass
    
    @abstractmethod
    def play(self) -> bool:
        pass


class NumberGuessingGame(Game):
    def __init__(self, difficulty: Difficulty = Difficulty.MEDIUM):
        super().__init__()
        self.difficulty = difficulty
        self.secret_number: Optional[int] = None
    
    def generate_number(self) -> int:
        self.secret_number = random.randint(self.difficulty.min_val, self.difficulty.max_val)
        return self.secret_number
    
    @attempt_counter
    def check_guess(self, guess: int) -> str:
        if guess == self.secret_number:
            return "correct"
        elif guess < self.secret_number:
            return "higher"
        else:
            return "lower"
    
    def reset_game(self):
        self.stats.attempts = 0
        self.stats.guess_history.clear()
    
    @game_tracker
    def play(self) -> bool:
        self.reset_game()
        target = self.generate_number()
        
        print("Welcome to the Number Guessing Game!")
        print(f"I have picked a number between {self.difficulty.min_val} and {self.difficulty.max_val}. Try to guess it!")
        
        while self.stats.attempts < self.difficulty.max_attempts:
            guess = int(input(f"Attempt {self.stats.attempts + 1}: Enter your guess: "))
            result = self.check_guess(guess)
            
            if result == "correct":
                print(f"Congratulations! You guessed the number {target} correctly in {self.stats.attempts} attempts.")
                return True
            elif result == "higher":
                print("Higher number please")
            else:
                print("Lower number please")
        
        print(f"Game over! The number was {target}")
        return False


class AdvancedGame(NumberGuessingGame):
    def __init__(self, difficulty: Difficulty = Difficulty.MEDIUM):
        super().__init__(difficulty)
    
    def get_hint(self, guess: int) -> str:
        if not self.secret_number:
            return ""
        
        difference = abs(guess - self.secret_number)
        range_size = self.difficulty.max_val - self.difficulty.min_val
        
        if difference <= range_size * 0.1:
            return " (Very close!)"
        elif difference <= range_size * 0.25:
            return " (Close!)"
        else:
            return " (Far!)"
    
    @attempt_counter
    def check_guess(self, guess: int) -> str:
        if guess == self.secret_number:
            return "correct"
        elif guess < self.secret_number:
            return "higher"
        else:
            return "lower"
    
    @game_tracker
    def play(self) -> bool:
        self.reset_game()
        target = self.generate_number()
        
        print("Welcome to the Advanced Number Guessing Game!")
        print(f"I have picked a number between {self.difficulty.min_val} and {self.difficulty.max_val}. Try to guess it!")
        
        while self.stats.attempts < self.difficulty.max_attempts:
            guess = int(input(f"Attempt {self.stats.attempts + 1}: Enter your guess: "))
            result = self.check_guess(guess)
            
            if result == "correct":
                print(f"Congratulations! You guessed the number {target} correctly in {self.stats.attempts} attempts.")
                return True
            elif result == "higher":
                hint = self.get_hint(guess)
                print(f"Higher number please{hint}")
            else:
                hint = self.get_hint(guess)
                print(f"Lower number please{hint}")
        
        print(f"Game over! The number was {target}")
        return False
    
    def show_stats(self):
        print(f"\nGame Statistics:")
        print(f"Games played: {self.stats.games_played}")
        print(f"Games won: {self.stats.games_won}")
        if self.stats.games_played > 0:
            win_rate = (self.stats.games_won / self.stats.games_played) * 100
            print(f"Win rate: {win_rate:.1f}%")
        if self.stats.best_score:
            print(f"Best score: {self.stats.best_score} attempts")


class GameFactory:
    @staticmethod
    def create_game(game_type: str, difficulty: Difficulty = Difficulty.MEDIUM) -> Game:
        if game_type == "basic":
            return NumberGuessingGame(difficulty)
        elif game_type == "advanced":
            return AdvancedGame(difficulty)
        else:
            return NumberGuessingGame(difficulty)


# Usage
if __name__ == "__main__":
    # Basic game
    basic_game = NumberGuessingGame(Difficulty.EASY)
    basic_game.play()
    
    # Advanced game with hints
    advanced_game = AdvancedGame(Difficulty.MEDIUM)
    advanced_game.play()
    advanced_game.show_stats()
    
    # Factory pattern
    factory_game = GameFactory.create_game("advanced", Difficulty.HARD)
    factory_game.play()


