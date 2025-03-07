import pyttsx3
import time

class HomeVoyager:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.lights_on = False
        self.door_locked = True

    def speak(self, text):
        """Convert text to speech."""
        print(f"🤖 Home Voyager: {text}")  # Display text in the console
        self.engine.say(text)
        self.engine.runAndWait()

    def get_command(self):
        """Get user input instead of voice recognition."""
        return input("Enter command: ").lower()

    def control_lights(self, status):
        """Turn lights on or off."""
        if status == "on":
            self.lights_on = True
            self.speak("Turning lights on.")
        elif status == "off":
            self.lights_on = False
            self.speak("Turning lights off.")

    def control_door(self, status):
        """Lock or unlock the door."""
        if status == "lock":
            self.door_locked = True
            self.speak("Locking the door.")
        elif status == "unlock":
            self.door_locked = False
            self.speak("Unlocking the door.")

    def process_command(self, command):
        """Process the given command."""
        actions = {
            "lights on": lambda: self.control_lights("on"),
            "lights off": lambda: self.control_lights("off"),
            "lock door": lambda: self.control_door("lock"),
            "unlock door": lambda: self.control_door("unlock"),
            "exit": lambda: self.speak("Shutting down Home Voyager.") or exit()
        }

        if command in actions:
            actions[command]()
        else:
            self.speak("Invalid command. Try again.")

    def run(self):
        """Main loop for listening and responding to text commands."""
        self.speak("Welcome to Home Voyager System. Type your command below.")
        while True:
            command = self.get_command()
            if command:
                self.process_command(command)
            time.sleep(1)

if __name__ == "__main__":
    home_voyager = HomeVoyager()
    home_voyager.run()
