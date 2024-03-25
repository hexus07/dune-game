import random
import time
import threading
import pygame
from colorama import Fore, Style

def survival_challenge(water, distance_to_safety):
    print("Welcome to the Desert Survival Challenge!")
    print("You find yourself stranded in the vast desert of Arrakis. Your goal is to survive and find your way to safety.")

    while water > 0 and distance_to_safety > 0:
        print("\nYou have", water, "units of water left.")
        print("Distance to safety:", distance_to_safety, "kilometers.")

        # Random events  
        event_chance = random.randint(1, 10)
        if event_chance <= 3:  # 30% chance of a sandstorm
            print("A sandstorm approaches!")

            water -= 1
        elif event_chance <= 6:  # 30% chance of finding water
            found_water = random.randint(1, 3)
            print("You found", found_water, "units of water!")
            water += found_water
        else:  # 40% chance of nothing happening
            print("The desert is quiet for now.")

        # Player choices
        print("\nWhat will you do?")
        print("1. Keep walking towards safety.")
        print("2. Rest to conserve energy.")
        print("3. Search for water.")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            distance_to_safety -= random.randint(2, 4)  # Progress towards safety
            if event_chance <= 3:
                water -= 7
            else:
                water -= 2  # Water consumption while walking
        elif choice == '2':
            water -= 1  # Water consumption while resting
        elif choice == '3':
            if event_chance <= 3:
                water -= 7
            else:
                water -= 1  # Water consumption while searching for water
                found_water = random.randint(0, 5)  
                water += found_water
                print("You found", found_water, "units of water")
        else:
            print("Invalid choice. Try again.")
            water += found_water

        


    if water <= 0:
        print("\nYou ran out of water and perished in the desert. Game over!")
    elif distance_to_safety <= 0:
        print("\nCongratulations! You've reached safety and survived the desert.")
        return True
    else:
        print("\nUnexpected error occurred.")

def quizz(file_name):
    def load_questions(file_name):
        questions = []
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 4):
                question = lines[i].strip()
                answers = [line.strip() for line in lines[i + 1:i + 4]]
                questions.append((question, answers))
        return questions

    def display_question(question, answers):
        print(question)
        for i, answer in enumerate(answers):
            print(f"{chr(65 + i)}. {answer}")

    def quiz(questions):
        score = 0
        for i, (question, answers) in enumerate(questions, 1):
            display_question(question, answers)
            user_answer = input("Your answer: ").upper()
            correct_answer = correct_answers[i-1]


            if user_answer == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Sorry, the correct answer is {correct_answer}.")
            print()
        return score

    # Load questions from file
    correct_answers = ['A','B','B','C']
    return(quiz(load_questions(file_name)))


class VisionGame:
    def __init__(self):
        self.vision = "You have a vision of an ancient temple hidden deep within the jungle, guarded by mystical traps and puzzles."
        self.historical_info = {
            "ancient temple": "The ancient temple was built by an ancient civilization known for their advanced knowledge of astronomy and architecture.",
            "mystical traps": "The temple is protected by mystical traps designed to test the wisdom and courage of those who seek its secrets.",
            "puzzles": "To unlock the temple's inner chamber, one must solve a series of puzzles based on celestial patterns and ancient symbols."
        }
        self.time_limit = 60  # Set the time limit for solving the puzzle (in seconds)
    
    def play(self):
        print("Welcome to the Vision Game.")
        print("In this game, you will explore the mysteries of an ancient temple and uncover its secrets.")
        print("Let's begin...\n")
        
        print("Vision:")
        print(self.vision)
        print()
        
        print("You awaken from your vision and decide to search for historical information about the temple.")
        search_term = input("Enter a keyword to search for historical information (e.g., 'ancient temple', 'mystical traps', 'puzzles'): ")
        print()
        
        if search_term.lower() in self.historical_info:
            print("Historical Information:")
            print(self.historical_info[search_term.lower()])
            print()
            print("You continue your exploration and come across a locked door.")
            print("To open the door, you must solve the following puzzle:")
            self.solve_puzzle()
        else:
            print("Sorry, historical information about that keyword is not available.")
    
    def solve_puzzle(self):
        print("Puzzle: Identify the missing letter in the sequence to unlock the door.")
        sequences = {
            "ABCD": "E",
            "FGHI": "J",
            "JKLM": "N",
            "OPQR": "S",
            "UVWX": "Y"
        }
        sequence, missing_letter = random.choice(list(sequences.items()))
        print("Sequence:", sequence)
        print()
        
        # Start the timer thread
        timer_thread = threading.Thread(target=self.timer_thread)
        timer_thread.start()
        
        user_answer = input("Enter the missing letter in the sequence: ").strip().upper()
        print()
        
        # Stop the timer thread
        timer_thread.join()
        
        if user_answer == missing_letter:
            print(Fore.RED + "Congratulations! You have successfully solved the puzzle and opened the door.")
        else:
            print(Fore.RED + "Sorry, that is incorrect. Try again.")
    
    def timer_thread(self):
        elapsed_time = 0
        pygame.mixer.init()
        clock_sound = pygame.mixer.Sound("clock-ticking.wav")  # Replace "clock_tick.wav" with the path to your clock ticking sound file
        clock_sound.play()
        while elapsed_time < self.time_limit:
            print(Fore.RED + Style.BRIGHT + f"\rTime left: {self.time_limit - elapsed_time} seconds", end="")
            elapsed_time += 1
            time.sleep(1)
        print()
