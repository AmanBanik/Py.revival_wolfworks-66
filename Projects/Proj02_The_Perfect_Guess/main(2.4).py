# ==============================================================================
# ADVANCED PYTHON NUMBER GUESSING GAME
# Demonstrates: OOP, Inheritance, Abstract Classes, Decorators, Enums, Dataclasses
# ==============================================================================

import random
from abc import ABC, abstractmethod  # For creating abstract base classes
from typing import Optional, List    # For type hints - helps with code clarity
from functools import wraps          # Preserves function metadata in decorators
from dataclasses import dataclass, field  # Creates classes with less boilerplate
from enum import Enum               # For creating enumerated constants


# ==============================================================================
# ENUM DEMONSTRATION
# Enums provide a way to create named constants that are more readable than magic numbers
# ==============================================================================

class Difficulty(Enum):
    """
    ENUM CONCEPT: Creates a set of named constants
    - More readable than using raw numbers (1, 100, 7)
    - Type-safe - prevents invalid values
    - Each enum member has multiple values (min, max, attempts)
    """
    EASY = (1, 50, 10)     # Range 1-50, 10 attempts allowed
    MEDIUM = (1, 100, 7)   # Range 1-100, 7 attempts allowed  
    HARD = (1, 200, 5)     # Range 1-200, 5 attempts allowed
    
    def __init__(self, min_val: int, max_val: int, max_attempts: int):
        """
        ENUM INITIALIZATION: Custom constructor to unpack tuple values
        This allows each enum member to have multiple associated values
        """
        self.min_val = min_val
        self.max_val = max_val
        self.max_attempts = max_attempts


# ==============================================================================
# DATACLASS DEMONSTRATION  
# Dataclasses automatically generate __init__, __repr__, __eq__ methods
# ==============================================================================

@dataclass
class Stats:
    """
    DATACLASS CONCEPT: Reduces boilerplate code for data-holding classes
    - Automatically generates __init__, __repr__, __eq__ methods
    - Type hints make the structure clear
    - field(default_factory=list) creates a new list for each instance (avoids mutable default)
    """
    attempts: int = 0                                    # Current game attempts
    games_played: int = 0                               # Total games played  
    games_won: int = 0                                  # Total games won
    best_score: Optional[int] = None                    # Best score (fewest attempts)
    guess_history: List[int] = field(default_factory=list)  # List of guesses made


# ==============================================================================
# DECORATOR DEMONSTRATIONS
# Decorators modify or extend function behavior without changing the function itself
# ==============================================================================

def attempt_counter(func):
    """
    DECORATOR CONCEPT #1: Function wrapper that adds functionality
    - Automatically counts attempts when a guess is made
    - Logs each guess to history
    - Uses @wraps to preserve original function metadata
    """
    @wraps(func)  # Preserves original function's name, docstring, etc.
    def wrapper(self, guess: int):
        # DECORATOR LOGIC: Execute before the original function
        self.stats.attempts += 1
        self.stats.guess_history.append(guess)
        
        # Call the original function
        return func(self, guess)
    return wrapper


def game_tracker(func):
    """
    DECORATOR CONCEPT #2: Tracks game statistics automatically
    - Runs after each game completes
    - Updates win/loss statistics
    - Tracks best scores
    """
    @wraps(func)
    def wrapper(self):
        # Call the original function first
        result = func(self)
        
        # DECORATOR LOGIC: Execute after the original function
        self.stats.games_played += 1
        if result:  # If game was won
            self.stats.games_won += 1
            # Update best score if this is better
            if not self.stats.best_score or self.stats.attempts < self.stats.best_score:
                self.stats.best_score = self.stats.attempts
        return result
    return wrapper


# ==============================================================================
# ABSTRACT BASE CLASS DEMONSTRATION
# Defines a contract that all subclasses must follow
# ==============================================================================

class Game(ABC):
    """
    ABSTRACT BASE CLASS CONCEPT: Defines interface that subclasses must implement
    - Cannot be instantiated directly
    - Forces subclasses to implement abstract methods
    - Provides common initialization and shared behavior
    - Demonstrates POLYMORPHISM - different games can be used interchangeably
    """
    
    def __init__(self):
        """
        CONSTRUCTOR: Initialize common attributes for all game types
        Every subclass will have these same basic components
        """
        self.stats = Stats()  # Each game instance gets its own stats
    
    @abstractmethod
    def generate_number(self) -> int:
        """
        ABSTRACT METHOD: Must be implemented by subclasses
        Defines the contract - every game must be able to generate a number
        """
        pass
    
    @abstractmethod
    def check_guess(self, guess: int) -> str:
        """
        ABSTRACT METHOD: Must be implemented by subclasses  
        Defines the contract - every game must be able to check guesses
        """
        pass
    
    @abstractmethod
    def play(self) -> bool:
        """
        ABSTRACT METHOD: Must be implemented by subclasses
        Defines the contract - every game must have a play method
        """
        pass


# ==============================================================================
# INHERITANCE DEMONSTRATION - BASE CLASS
# Inherits from abstract Game class and implements required methods
# ==============================================================================

class NumberGuessingGame(Game):
    """
    INHERITANCE CONCEPT: Inherits from Game abstract base class
    - Must implement all abstract methods from parent
    - Gets Stats object automatically from parent constructor
    - Demonstrates basic implementation of the game contract
    """
    
    def __init__(self, difficulty: Difficulty = Difficulty.MEDIUM):
        """
        CONSTRUCTOR WITH INHERITANCE:
        - Calls parent constructor with super()
        - Adds its own specific attributes
        - Uses Enum for type-safe difficulty setting
        """
        super().__init__()  # Call parent constructor to get self.stats
        self.difficulty = difficulty        # Store difficulty settings
        self.secret_number: Optional[int] = None  # Will hold the target number
    
    def generate_number(self) -> int:
        """
        ABSTRACT METHOD IMPLEMENTATION: Generate random number using difficulty settings
        - Uses random module as required
        - Range determined by difficulty enum values
        """
        self.secret_number = random.randint(self.difficulty.min_val, self.difficulty.max_val)
        return self.secret_number
    
    @attempt_counter  # DECORATOR APPLIED: Automatically counts attempts and logs guesses
    def check_guess(self, guess: int) -> str:
        """
        ABSTRACT METHOD IMPLEMENTATION with DECORATOR:
        - @attempt_counter decorator automatically increments attempts
        - Returns exact strings as specified in requirements
        """
        if guess == self.secret_number:
            return "correct"
        elif guess < self.secret_number:
            return "higher"  # "Higher number please" will be added in play()
        else:
            return "lower"   # "Lower number please" will be added in play()
    
    def reset_game(self):
        """
        HELPER METHOD: Reset stats for new game
        - Resets attempt counter
        - Clears guess history
        """
        self.stats.attempts = 0
        self.stats.guess_history.clear()
    
    def display_game_rules(self):
        """
        GAME RULES DISPLAY: Shows complete game information before starting
        - Clear explanation of objective
        - Range and attempt limits
        - How scoring/feedback works
        """
        print("\n" + "="*60)
        print("🎯 GAME RULES - NUMBER GUESSING GAME")
        print("="*60)
        print("📋 OBJECTIVE:")
        print(f"   Guess the secret number I'm thinking of!")
        print(f"\n📊 GAME SETTINGS:")
        print(f"   • Number Range: {self.difficulty.min_val} to {self.difficulty.max_val}")
        print(f"   • Maximum Attempts: {self.difficulty.max_attempts}")
        print(f"   • Difficulty Level: {self.difficulty.name}")
        print(f"\n💡 HOW TO PLAY:")
        print(f"   • I'll tell you if your guess is too high or too low")
        print(f"   • Keep guessing until you find the number or run out of attempts")
        print(f"   • Try to guess in as few attempts as possible!")
        print(f"\n🏆 WINNING:")
        print(f"   • Guess the correct number within {self.difficulty.max_attempts} attempts")
        print(f"   • The fewer attempts you use, the better your score!")
        print("="*60)

    def display_attempt_status(self):
        """
        ATTEMPT STATUS: Shows current progress during game
        - Current attempt number
        - Remaining attempts
        - Previous guesses made
        """
        remaining = self.difficulty.max_attempts - self.stats.attempts
        print(f"\n📊 ATTEMPT STATUS:")
        print(f"   Current Attempt: {self.stats.attempts + 1} of {self.difficulty.max_attempts}")
        print(f"   Remaining Attempts: {remaining}")
        if self.stats.guess_history:
            recent_guesses = self.stats.guess_history[-3:]  # Show last 3 guesses
            print(f"   Recent Guesses: {recent_guesses}")
        print(f"   Range: {self.difficulty.min_val} - {self.difficulty.max_val}")

    @game_tracker  # DECORATOR APPLIED: Automatically tracks game statistics
    def play(self) -> bool:
        """
        ABSTRACT METHOD IMPLEMENTATION with DECORATOR:
        - @game_tracker decorator automatically updates game statistics
        - Implements the main game loop as specified in requirements
        - Returns True if won, False if lost
        """
        # STEP 1: Initialize new game
        self.reset_game()
        target = self.generate_number()
        
        # STEP 2: Display game rules and setup
        self.display_game_rules()
        print("\n🎮 GAME STARTING...")
        print(f"I have picked a number between {self.difficulty.min_val} and {self.difficulty.max_val}. Try to guess it!")
        
        # STEP 3: Main game loop - continue until max attempts reached
        while self.stats.attempts < self.difficulty.max_attempts:
            # Show current status before each guess
            self.display_attempt_status()
            
            # Get user input
            guess = int(input(f"\n🎯 Enter your guess: "))
            
            # Check the guess (decorator automatically counts attempts)
            result = self.check_guess(guess)
            
            # STEP 4: Provide feedback based on result
            if result == "correct":
                print(f"\n🎉 CONGRATULATIONS! 🎉")
                print(f"You guessed the number {target} correctly in {self.stats.attempts} attempts!")
                print(f"🏆 Final Score: {self.difficulty.max_attempts - self.stats.attempts + 1} points")
                return True  # Game won
            elif result == "higher":
                print(f"📈 Higher number please")  # Exact message as specified
            else:  # result == "lower"
                print(f"📉 Lower number please")   # Exact message as specified
        
        # STEP 5: Game lost - show the answer and summary
        print(f"\n💔 GAME OVER!")
        print(f"The number was {target}")
        print(f"You used all {self.difficulty.max_attempts} attempts.")
        print(f"📊 Your guesses were: {self.stats.guess_history}")
        return False  # Game lost


# ==============================================================================
# INHERITANCE DEMONSTRATION - DERIVED CLASS
# Shows how inheritance allows extending and modifying behavior
# ==============================================================================

class AdvancedGame(NumberGuessingGame):
    """
    INHERITANCE CONCEPT - DERIVED CLASS:
    - Inherits ALL functionality from NumberGuessingGame
    - Extends behavior by adding hints
    - Overrides methods to provide enhanced functionality
    - Demonstrates METHOD OVERRIDING and EXTENSION
    """
    
    def __init__(self, difficulty: Difficulty = Difficulty.MEDIUM):
        """
        INHERITED CONSTRUCTOR: Calls parent constructor
        - Gets all parent functionality automatically
        - Could add additional attributes if needed
        """
        super().__init__(difficulty)  # Get all parent initialization
    
    def get_hint(self, guess: int) -> str:
        """
        NEW METHOD: Adds functionality not in parent class
        - Calculates proximity hint based on guess
        - Uses difficulty settings to scale hints appropriately
        """
        if not self.secret_number:
            return ""
        
        # Calculate how close the guess is
        difference = abs(guess - self.secret_number)
        range_size = self.difficulty.max_val - self.difficulty.min_val
        
        # Provide contextual hints based on proximity
        if difference <= range_size * 0.1:      # Within 10% of range
            return " (Very close!)"
        elif difference <= range_size * 0.25:   # Within 25% of range
            return " (Close!)"
        else:                                   # Far away
            return " (Far!)"
    
    @attempt_counter  # INHERITED DECORATOR: Same functionality as parent
    def check_guess(self, guess: int) -> str:
        """
        METHOD OVERRIDE: Same logic as parent but kept for clarity
        - Could modify behavior here if needed
        - Decorator still applies automatically
        """
        if guess == self.secret_number:
            return "correct"
        elif guess < self.secret_number:
            return "higher"
        else:
            return "lower"
    
    def display_advanced_rules(self):
        """
        ADVANCED GAME RULES: Enhanced rules display with hint information
        - Includes all basic rules plus hint system explanation
        """
        print("\n" + "="*70)
        print("🎯 ADVANCED GAME RULES - NUMBER GUESSING WITH HINTS")
        print("="*70)
        print("📋 OBJECTIVE:")
        print(f"   Guess the secret number I'm thinking of!")
        print(f"\n📊 GAME SETTINGS:")
        print(f"   • Number Range: {self.difficulty.min_val} to {self.difficulty.max_val}")
        print(f"   • Maximum Attempts: {self.difficulty.max_attempts}")
        print(f"   • Difficulty Level: {self.difficulty.name}")
        print(f"\n💡 HOW TO PLAY:")
        print(f"   • I'll tell you if your guess is too high or too low")
        print(f"   • BONUS: I'll give you proximity hints!")
        print(f"   • 'Very close!' means within 10% of the range")
        print(f"   • 'Close!' means within 25% of the range")  
        print(f"   • 'Far!' means you're quite far from the target")
        print(f"\n🏆 WINNING:")
        print(f"   • Guess the correct number within {self.difficulty.max_attempts} attempts")
        print(f"   • Use the hints to narrow down your guesses efficiently!")
        print("="*70)

    def display_enhanced_status(self):
        """
        ENHANCED ATTEMPT STATUS: Shows current progress with additional details
        - All basic status info plus advanced features
        """
        remaining = self.difficulty.max_attempts - self.stats.attempts
        progress_percent = (self.stats.attempts / self.difficulty.max_attempts) * 100
        
        print(f"\n📊 GAME PROGRESS:")
        print(f"   Current Attempt: {self.stats.attempts + 1} of {self.difficulty.max_attempts}")
        print(f"   Remaining Attempts: {remaining}")
        print(f"   Progress: {progress_percent:.1f}% of attempts used")
        if self.stats.guess_history:
            recent_guesses = self.stats.guess_history[-3:]  # Show last 3 guesses
            print(f"   Recent Guesses: {recent_guesses}")
            print(f"   Total Guesses So Far: {len(self.stats.guess_history)}")
        print(f"   Valid Range: {self.difficulty.min_val} - {self.difficulty.max_val}")

    @game_tracker  # INHERITED DECORATOR: Same functionality as parent
    def play(self) -> bool:
        """
        METHOD OVERRIDE: Enhanced version of parent's play method
        - Adds hint functionality to the basic game loop
        - Shows how inheritance allows customization while reusing code
        """
        # STEP 1: Initialize new game (same as parent)
        self.reset_game()
        target = self.generate_number()
        
        # STEP 2: Display enhanced rules and setup
        self.display_advanced_rules()
        print("\n🎮 ADVANCED GAME STARTING...")
        print(f"I have picked a number between {self.difficulty.min_val} and {self.difficulty.max_val}. Try to guess it!")
        
        # STEP 3: Enhanced game loop with hints
        while self.stats.attempts < self.difficulty.max_attempts:
            # Show enhanced status before each guess
            self.display_enhanced_status()
            
            # Get user input
            guess = int(input(f"\n🎯 Enter your guess: "))
            
            # Check the guess (decorator automatically counts attempts)
            result = self.check_guess(guess)
            
            # STEP 4: Enhanced feedback with hints
            if result == "correct":
                print(f"\n🎉 OUTSTANDING! 🎉")
                print(f"You guessed the number {target} correctly in {self.stats.attempts} attempts!")
                
                # Calculate and display score
                base_score = self.difficulty.max_attempts - self.stats.attempts + 1
                bonus_multiplier = {"EASY": 1.0, "MEDIUM": 1.5, "HARD": 2.0}
                final_score = int(base_score * 100 * bonus_multiplier.get(self.difficulty.name, 1.0))
                
                print(f"🏆 Final Score: {final_score} points")
                print(f"📊 Efficiency: {(self.stats.attempts/self.difficulty.max_attempts)*100:.1f}% of attempts used")
                return True
            elif result == "higher":
                hint = self.get_hint(guess)  # NEW FEATURE: Add hint
                print(f"📈 Higher number please{hint}")
            else:  # result == "lower" 
                hint = self.get_hint(guess)  # NEW FEATURE: Add hint  
                print(f"📉 Lower number please{hint}")
        
        # STEP 5: Enhanced game over summary
        print(f"\n💔 GAME OVER!")
        print(f"The secret number was: {target}")
        print(f"You used all {self.difficulty.max_attempts} attempts.")
        print(f"📊 Complete guess history: {self.stats.guess_history}")
        
        # Show some analysis
        if self.stats.guess_history:
            closest_guess = min(self.stats.guess_history, key=lambda x: abs(x - target))
            closest_diff = abs(closest_guess - target)
            print(f"🎯 Your closest guess was {closest_guess} (off by {closest_diff})")
        
        return False
    
    def show_stats(self):
        """
        NEW METHOD: Additional functionality not in parent
        - Demonstrates how derived classes can add new capabilities
        - Uses inherited stats object
        """
        print(f"\n" + "="*50)
        print("📈 DETAILED GAME STATISTICS")
        print("="*50)
        print(f"🎮 Games Played: {self.stats.games_played}")
        print(f"🏆 Games Won: {self.stats.games_won}")
        print(f"💔 Games Lost: {self.stats.games_played - self.stats.games_won}")
        
        if self.stats.games_played > 0:
            win_rate = (self.stats.games_won / self.stats.games_played) * 100
            print(f"📊 Win Rate: {win_rate:.1f}%")
            
        if self.stats.best_score:
            print(f"⭐ Best Score: {self.stats.best_score} attempts")
            
        if self.stats.games_won > 0:
            print(f"🎯 Current Difficulty: {self.difficulty.name}")
            print(f"📋 Range Setting: {self.difficulty.min_val}-{self.difficulty.max_val}")
            
        print("="*50)


# ==============================================================================
# FACTORY PATTERN DEMONSTRATION  
# Provides a way to create objects without specifying their exact class
# ==============================================================================

class GameFactory:
    """
    FACTORY PATTERN CONCEPT: Creates objects based on parameters
    - Encapsulates object creation logic
    - Allows adding new game types without changing client code
    - Demonstrates POLYMORPHISM - returns different types that share same interface
    """
    
    @staticmethod  # No need for instance, this is a utility method
    def create_game(game_type: str, difficulty: Difficulty = Difficulty.MEDIUM) -> Game:
        """
        FACTORY METHOD: Creates appropriate game instance based on type
        - Returns Game interface (polymorphism)
        - Client code doesn't need to know specific class names
        - Easy to extend with new game types
        """
        if game_type == "basic":
            return NumberGuessingGame(difficulty)
        elif game_type == "advanced":
            return AdvancedGame(difficulty)
        else:
            # Default fallback
            return NumberGuessingGame(difficulty)


# ==============================================================================
# DEMONSTRATION OF ALL CONCEPTS
# Shows how all the advanced Python features work together
# ==============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("ADVANCED PYTHON CONCEPTS DEMONSTRATION")
    print("=" * 80)
    
    # DEMONSTRATION 1: Basic inheritance and abstract class implementation
    print("\n1. BASIC GAME (Inheritance + Abstract Classes + Decorators)")
    print("-" * 60)
    basic_game = NumberGuessingGame(Difficulty.EASY)  # Uses enum
    basic_game.play()  # Uses decorators automatically
    
    # DEMONSTRATION 2: Enhanced inheritance with method overriding
    print("\n2. ADVANCED GAME (Method Overriding + Enhanced Functionality)")  
    print("-" * 60)
    advanced_game = AdvancedGame(Difficulty.MEDIUM)  # Uses enum
    advanced_game.play()  # Overridden method with hints
    advanced_game.show_stats()  # New method not in parent
    
    # DEMONSTRATION 3: Factory pattern and polymorphism
    print("\n3. FACTORY PATTERN (Polymorphism + Object Creation)")
    print("-" * 60) 
    factory_game = GameFactory.create_game("advanced", Difficulty.HARD)  # Factory creation
    # factory_game is of type Game (polymorphism), actual type is AdvancedGame
    factory_game.play()  # Same interface, different implementation
    
    print("\n" + "=" * 80)
    print("DEMONSTRATION COMPLETE - All concepts successfully used!")
    print("=" * 80)