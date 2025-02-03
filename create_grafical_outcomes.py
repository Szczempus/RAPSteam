import os
import subprocess
import time

import pyautogui
from pyvirtualdisplay import Display

pyautogui.FAILSAFE = False
pyautogui._pyautogui_x11._display = ":8"


# Function to run a Python file in xterm
def run_task(file_path):
    try:
        # Uruchomienie skryptu Python bezpośrednio
        print(f"Running {file_path}...")
        env = os.environ.copy()
        env["DISPLAY"] = ":8"

        subprocess.run(['python3', file_path], env=env, check=True)

        # Krótkie opóźnienie na renderowanie (jeśli potrzebne)
        time.sleep(2)

        # Wykonanie zrzutu ekranu
        screenshot_path = f"/home/outcome/{file_path.split('/')[-1]}_screenshot.png"
        print(f"Capturing screenshot: {screenshot_path}")

        pyautogui.screenshot(screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

    except Exception as e:
        print(f"Error running {file_path}: {e}")


# Function to capture a screenshot
def capture_screenshot(filename):
    try:
        print(f"Capturing screenshot: {filename}")
        time.sleep(2)  # Increase delay to 2 seconds
        pyautogui.moveTo(640, 512)
        pyautogui.click()

        screenshot = pyautogui.screenshot()
        screenshot.save(filename + ".png")
        print(f"Screenshot saved to {filename}")
    except Exception as e:
        print(f"Error capturing screenshot: {e}")


# Function to process tasks and take screenshots
def run_tasks_and_capture_screenshots(folder_path, outcome_folder):
    if not os.path.exists(folder_path):
        print(f"Error: Input folder does not exist: {folder_path}")
        return
    if not os.path.exists(outcome_folder):
        os.makedirs(outcome_folder)

    files = [f for f in os.listdir(folder_path) if f.endswith('.py')]
    for file in files:
        file_path = os.path.join(folder_path, file)
        run_task(file_path)

        # Save screenshot after running task
        screenshot_filename = os.path.join(outcome_folder, f"{file}_screenshot.png")
        capture_screenshot(screenshot_filename)


# Main function
def main():
    folder_path = '/home/files'  # Path to Python scripts
    outcome_folder = '/home/outcome'  # Path to save screenshots

    screenshot = pyautogui.screenshot()
    screenshot.save('/home/outcome/A.png')  # Zmień ścieżkę na odpowiednią

    # Start the virtual display
    display = Display(visible=False, size=(1366, 768))
    try:
        display.start()
        screenshot.save('/home/outcome/B.png')  # Zmień ścieżkę na odpowiednią

        print(f"Virtual display started on DISPLAY={display.display}")
        run_tasks_and_capture_screenshots(folder_path, outcome_folder)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        display.stop()
        print("Virtual display stopped.")


if __name__ == "__main__":
    main()
