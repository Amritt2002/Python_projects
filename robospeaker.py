import pyttsx3

def pronounce_name(name):
    engine = pyttsx3.init()
    engine.say(name)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        name_to_pronounce = input("Enter a name to pronounce (type 'exit' to end): ")
        
        if name_to_pronounce.lower() == 'exit':
            print("Exiting the program.")
            break  # Exit the while loop if the user types 'exit'
        
        pronounce_name(name_to_pronounce)
