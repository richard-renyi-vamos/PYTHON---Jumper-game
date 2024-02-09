import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_game_area(area):
    clear_screen()
    print(''.join(area))

def game_loop():
    game_width = 30
    player_pos = 2
    ground = ['=' if i != player_pos else 'A' for i in range(game_width)]
    obstacle_pos = random.randint(20, 29)
    ground[obstacle_pos] = 'X'
    score = 0

    try:
        while True:
            display_game_area(ground)
            print(f"Score: {score}")
            move = input("Press Enter to jump (or 'q' to quit): ").strip().lower()

            if move == 'q':
                break

            if player_pos == obstacle_pos - 1:  # Simple jump mechanism
                ground[player_pos] = '='
                player_pos += 1
                ground[player_pos] = 'A'
            elif player_pos < obstacle_pos - 1:  # Move obstacle closer
                ground[obstacle_pos] = '='
                obstacle_pos -= 1
                ground[obstacle_pos] = 'X'
            else:  # Reset obstacle position after jump
                score += 1
                ground[obstacle_pos] = '='
                obstacle_pos = random.randint(20, 29)
                ground[obstacle_pos] = 'X'
                
            time.sleep(0.5)  # Adjust game speed here

    except KeyboardInterrupt:
        print("\nGame Over")
        print(f"Final Score: {score}")

if __name__ == '__main__':
    game_loop()
