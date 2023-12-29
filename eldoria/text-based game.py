import time
import gender_guesser.detector as gender


def start_game():
    d=gender.Detector()

    title="""
   ___________.__       .___           .__        
\_   _____/|  |    __| _/___________|__|____   
 |    __)_ |  |   / __ |/  _ \_  __ \  \__  \  
 |        \|  |__/ /_/ (  <_> )  | \/  |/ __ \_
/_______  /|____/\____ |\____/|__|  |__(____  /
        \/            \/                    \/ 
    """
    for line in title.split('\n'):
        print(line)
        time.sleep(0.5) #delay for half a second

    #nPlayer name and pronoun
    player_name= input("Enter your name: ")
    player_gender= d.get_gender(player_name)

    if player_gender in ['male','mostly_male']:
        pronoun = 'he'
        possessive_pronoun = 'his'
        reflexive_pronoun = 'himself'
    elif player_gender in ['female','mostly_female']:
        pronoun = 'she'
        possessive_pronoun = 'her'
        reflexive_pronoun = 'herself'
    else:
        pronoun = 'they'
        possessive_pronoun = 'their'
        reflexive_pronoun = 'themself'




    print(f"Once upon a time, in the mystical realm of Eldoria where Dragons sore high above the clouds, a courageous adventurer named {player_name} embarked on a journey to find a hidden treasure of unimaginable power.")
    time.sleep(1)
    print(f"{player_name}'s heart thumped with excitement and trepidation as {pronoun} set foot into the Enchanted Grove, guided by the tales of {possessive_pronoun} late mentor, a legendary explorer.")
    time.sleep(1)
    print(f"But beneath {player_name}'s brave facade lay a deep motivation - a burning desire to prove {reflexive_pronoun} worthy and honor {possessive_pronoun} mentor's legacy.")
    time.sleep(1)
    print(f"As {pronoun} ventured deeper into the Grove, {pronoun} encountered a mischievous fairy named Luna. Luna presented a riddle that guarded the path to the treasure.")
    time.sleep(1)
    print("\"Two sisters I have, united yet apart,")
    print("One brings light, the other darkness.")
    print("Through the whispering wind, their voices ring,")
    print("Find the answer, and treasures you shall bring.\"")
    time.sleep(1)
    riddle_choice = input("Can you solve the riddle and proceed? (y/n): ",)

    if riddle_choice.lower() != "y":
        print("Unsure of the answer, you retreat from the Enchanted Grove.")
        time.sleep(1)
        print("Your quest ends here, and the treasure remains forever hidden.")
        restart_game()
        return

    print("Impressed by your wisdom, Luna opens a hidden passageway.")
    time.sleep(1)
    print("You find yourself in the heart of the Enchanted Grove, surrounded by ancient trees and shimmering lights.")
    time.sleep(1)
    def get_user_input(prompt, valid_responses):
        while True:
            response = input(prompt).lower()
            if response in valid_responses:
                return response
            else:
                print("Invalid response. Please try again.")

    # Usage:
    path_choice = get_user_input("A pathway splits into two directions: the Path of Illumination and the Path of Shadows. Which path will you choose? ", ["illumination", "shadows"])

    if path_choice.lower() == "illumination":
        print("You walk along the Path of Illumination, where beams of sunlight guide your way.")
        time.sleep(1)
        fish_choice = input("As you proceed, you encounter a shimmering pool with a golden fish swimming within. The fish speaks with a melodious voice, offering you a cryptic choice. \"To reach the treasure's embrace, answer me this: In Eldoria, what creature soars high above the clouds?\" What is your answer? (bird/fish/dragon): ")

        if fish_choice.lower() == "bird":
            print("The golden fish nods in approval and grants you passage.")
            time.sleep(1)
            treasure_chamber()
        else:
            print("The water ripples in disappointment, and you find yourself back at the crossroads.")
            time.sleep(1)
            restart_game()
            return
    else:
        print("You navigate the treacherous Path of Shadows, shrouded in darkness.")
        time.sleep(1)
        voice_choice = input("Glowing eyes watch you from the depths, and an eerie whisper fills the air. A mysterious voice poses a riddle that guards the path ahead. \"I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?\" What is your answer? (wind/fire/water): ")

        if voice_choice.lower() == "wind":
            print("The shadows part, and the path clears before you.")
            time.sleep(1)
            treasure_chamber()
        else:
            print("The whisper fades into silence, and you find yourself back at the crossroads.")
            time.sleep(1)
            restart_game()
            return

def treasure_chamber():
    print("You arrive in the ancient chamber that houses the Eldorian treasure.")
    time.sleep(1)
    acceptance_choice = input("Before you lies a magnificent chest, radiating with an otherworldly glow. The chest demands a final decision to unlock its secrets. \"What is the true essence of an adventurer? Will you accept the responsibility that comes with this power?\" Do you accept? (y/n): ")

    if acceptance_choice.lower() == "y":
        print("As you affirm your acceptance, the chest opens with a blinding light.")
        time.sleep(1)
        print("You have proven your worth, and the power of the Eldorian treasure is bestowed upon you.")
        time.sleep(1)
        print("Congratulations! You have triumphed in your quest and unlocked a new destiny in Eldoria.")
    else:
        print("Hesitant to bear the burden, you step back from the chest.")
        time.sleep(1)
        print("The treasure fades away, leaving you with a sense of longing and unfinished business.")
    
    restart_game()

def restart_game():
    restart_choice = input("Do you want to play again? (y/n): ")
    if restart_choice.lower() == "y":
        print("Restarting the game...")
        time.sleep(1)
        start_game()
    else:
        print("Exiting the game...")
        time.sleep(1)
        print("Thank you for playing!")

# Start the game
start_game()
