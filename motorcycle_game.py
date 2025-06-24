
import random
import datetime

# ---------------------------
# Strategy interfaces (can be extended with classes if needed)
# ---------------------------

# Start behaviors
def default_start():
    print("🔑 The motorcycle starts with a key.")

def silent_start():
    print("🔇 The motorcycle starts silently.")

# Ride behaviors
def eco_ride(speed):
    print(f"🛵 Riding economically at {speed} km/h.")

def aggressive_ride(speed):
    print(f"🏍️ Zooming ahead at {speed} km/h!")

# Stop behaviors
def normal_stop():
    print("🛑 The motorcycle comes to a smooth stop.")

def emergency_stop():
    print("⚠️ Emergency braking!")


# ---------------------------
# Motorcycle Class (OOP Applied)
# ---------------------------
class Motorcycle:
    def __init__(self, start_behavior, ride_behavior, stop_behavior):
        self.start_behavior = start_behavior
        self.ride_behavior = ride_behavior
        self.stop_behavior = stop_behavior
        self.speed = 0
        self.running = False

    def start(self):
        try:
            self.start_behavior()
            self.running = True
            self.speed = 0
            self._log_action("Motorcycle started")
        except Exception as e:
            print(f"❌ Error while starting: {e}")

    def ride(self):
        try:
            if self.running:
                self.speed = random.randint(20, 120)
                self.ride_behavior(self.speed)
                self._log_action(f"Riding at {self.speed} km/h")
            else:
                print("⚠️ You need to start the motorcycle first!")
        except Exception as e:
            print(f"❌ Error while riding: {e}")

    def stop(self):
        try:
            if self.running:
                self.stop_behavior()
                self._log_action("Motorcycle stopped")
                self.running = False
                self.speed = 0
            else:
                print("⚠️ The motorcycle is already stopped.")
        except Exception as e:
            print(f"❌ Error while stopping: {e}")

    def measure_speed(self):
        try:
            if self.running:
                print(f"📏 Current speed: {self.speed} km/h")
            else:
                print("🛑 The motorcycle is off. Speed is 0 km/h.")
        except Exception as e:
            print(f"❌ Error while measuring speed: {e}")

    def set_start_behavior(self, behavior):
        self.start_behavior = behavior
        self._log_action("Changed start behavior")

    def set_ride_behavior(self, behavior):
        self.ride_behavior = behavior
        self._log_action("Changed ride behavior")

    def set_stop_behavior(self, behavior):
        self.stop_behavior = behavior
        self._log_action("Changed stop behavior")

    def _log_action(self, message):
        """Logs an action with timestamp to a text file"""
        try:
            with open("motorcycle_log.txt", "a") as file:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{timestamp}] {message}\n")
        except Exception as e:
            print(f"❌ Failed to write to log file: {e}")


# ---------------------------
# Game Loop Function
# ---------------------------
def game_loop():
    print("\n--- Welcome to: Motorbike Adventure ---")
    print("Commands: start, ride, speed, stop, change, quit\n")

    # Create the motorcycle instance
    bike = Motorcycle(default_start, eco_ride, normal_stop)

    while True:
        try:
            command = input("Enter a command: ").strip().lower()

            if command == "start":
                bike.start()

            elif command == "ride":
                bike.ride()

            elif command == "speed":
                bike.measure_speed()

            elif command == "stop":
                bike.stop()

            elif command == "change":
                print("\n-- Change riding style --")
                choice = input("Choose style (eco / aggressive): ").strip().lower()
                if choice == "eco":
                    bike.set_ride_behavior(eco_ride)
                    print("✅ Riding style set to: Eco.")
                elif choice == "aggressive":
                    bike.set_ride_behavior(aggressive_ride)
                    print("✅ Riding style set to: Aggressive.")
                else:
                    print("❌ Unknown style.")

            elif command == "quit":
                print("👋 Exiting the game. See you soon!")
                bike._log_action("Game ended by user.")
                break

            else:
                print("❓ Unknown command.")

        except KeyboardInterrupt:
            print("\n👋 Interrupted. Exiting safely.")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")


# ---------------------------
# Main Program Entry Point
# ---------------------------
if __name__ == "__main__":
    game_loop()
