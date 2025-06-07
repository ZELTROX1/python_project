import random

class NumberSequenceGame:
    """
    A game where players take turns adding 1-3 consecutive numbers.
    The player who reaches exactly 21 loses.
    """
    
    def __init__(self):
        self.current_count = 0
        self.target = 21
        self.current_player = ""
        self.game_over = False
        self.winner = ""
    
    def display_rules(self):
        """Show game rules to the player"""
        print("\n" + "="*50)
        print("🎮 WELCOME TO THE NUMBER SEQUENCE GAME! 🎮")
        print("="*50)
        print("Rules:")
        print("1. Players take turns adding 1-3 consecutive numbers")
        print("2. You must continue from where the last player left off")
        print("3. The player who reaches exactly 21 LOSES!")
        print("4. Enter your numbers separated by commas (e.g., 1,2,3)")
        print("="*50 + "\n")
    
    def get_starting_player(self):
        """Let user choose who goes first"""
        while True:
            try:
                print("Who should go first?")
                print("1. Computer goes first")
                print("2. You go first")
                choice = int(input("Enter 1 or 2: "))
                
                if choice == 1:
                    self.current_player = "computer"
                    print("🤖 Computer will go first!\n")
                    break
                elif choice == 2:
                    self.current_player = "user"
                    print("👤 You will go first!\n")
                    break
                else:
                    print("❌ Please enter 1 or 2 only!")
                    
            except ValueError:
                print("❌ Please enter a valid number!")
    
    def display_current_state(self):
        """Show the current game state"""
        print(f"Current count: {self.current_count}")
        print(f"Target: {self.target}")
        print(f"Next player: {'You' if self.current_player == 'user' else 'Computer'}")
        print("-" * 30)
    
    def validate_user_input(self, user_numbers):
        """
        Validate if user's input follows the game rules
        Returns: (is_valid, error_message)
        """
        # Check if 1-3 numbers
        if len(user_numbers) < 1 or len(user_numbers) > 3:
            return False, "You must enter 1-3 numbers!"
        
        # Check if numbers are consecutive and start from current_count + 1
        expected_start = self.current_count + 1
        for i, num in enumerate(user_numbers):
            if num != expected_start + i:
                return False, f"Numbers must be consecutive starting from {expected_start}!"
        
        # Check if it doesn't exceed target
        if user_numbers[-1] > self.target:
            return False, f"Cannot go beyond {self.target}!"
        
        return True, ""
    
    def user_turn(self):
        """Handle user's turn"""
        print(f"\n👤 Your turn! Current count: {self.current_count}")
        print(f"You can choose {min(3, self.target - self.current_count)} number(s) starting from {self.current_count + 1}")
        
        while True:
            try:
                user_input = input("Enter your numbers (comma-separated): ")
                user_numbers = [int(x.strip()) for x in user_input.split(",")]
                
                is_valid, error_msg = self.validate_user_input(user_numbers)
                
                if is_valid:
                    self.current_count = user_numbers[-1]
                    print(f"✅ You chose: {user_numbers}")
                    print(f"New count: {self.current_count}")
                    
                    if self.current_count == self.target:
                        self.game_over = True
                        self.winner = "computer"
                        return
                    
                    self.current_player = "computer"
                    return
                else:
                    print(f"❌ {error_msg}")
                    
            except ValueError:
                print("❌ Please enter valid numbers separated by commas!")
    
    def computer_turn(self):
        """Handle computer's turn with smart strategy"""
        print(f"\n🤖 Computer's turn! Current count: {self.current_count}")
        
        remaining = self.target - self.current_count
        max_can_take = min(3, remaining)
        
        if remaining <= 3:
            numbers_to_take = remaining
        else:
            optimal_remainder = (remaining - 1) % 4
            if optimal_remainder == 0:
                numbers_to_take = random.randint(1, min(3, remaining))
            else:
                numbers_to_take = optimal_remainder
        
        # Generate the sequence
        computer_numbers = []
        for i in range(numbers_to_take):
            computer_numbers.append(self.current_count + i + 1)
        
        self.current_count = computer_numbers[-1]
        print(f"🤖 Computer chose: {computer_numbers}")
        print(f"New count: {self.current_count}")
        
        if self.current_count == self.target:
            self.game_over = True
            self.winner = "user"
            return
        
        self.current_player = "user"
    
    def play_game(self):
        """Main game loop"""
        self.display_rules()
        self.get_starting_player()
        
        print("🎯 Game starting...")
        
        while not self.game_over:
            self.display_current_state()
            
            if self.current_player == "user":
                self.user_turn()
            else:
                self.computer_turn()
            
            print()  # Add spacing
        
        # Game over - announce winner
        print("\n" + "="*50)
        print("🎉 GAME OVER! 🎉")
        print("="*50)
        
        if self.winner == "user":
            print("🎊 Congratulations! You WON! 🎊")
            print("The computer reached 21 and lost!")
        else:
            print("😢 You lost! Better luck next time!")
            print("You reached 21 and lost!")
        
        print(f"Final count: {self.current_count}")
        print("="*50)
    
    def play_again(self):
        """Ask if player wants to play again"""
        while True:
            choice = input("\nDo you want to play again? (y/n): ").lower().strip()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")


def main():
    """Main function to run the game"""
    print("Welcome to the Number Sequence Game!")
    
    while True:
        game = NumberSequenceGame()
        game.play_game()
        
        if not game.play_again():
            print("\nThanks for playing! Goodbye! 👋")
            break


if __name__ == "__main__":
    main()