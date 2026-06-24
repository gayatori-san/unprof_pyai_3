# 📇 Contact Management CLI Tool (Day 3)

A Python-based command-line interface for managing contacts. This updated version incorporates robust error handling, custom exceptions, and system logging to ensure the application runs smoothly without crashing.

## ✨ Features

* **Input Validation:** Prevents saving contacts with missing critical information using custom error handling.
* **Safe Storage:** Automatically creates a fresh storage file if the existing one is missing or corrupted.
* **Activity Logging:** Silently records all user actions, warnings, and errors to a local `.log` file for easy debugging.
* **View Contacts:** Quickly display all saved contacts in a clean, formatted list.

## 🚀 Getting Started

Follow these instructions to run the application directly from your Ubuntu terminal.

### Installation & Usage
1. Clone the git repository
   ```bash
   git clone https://github.com/gayatori-san/unprof_pyai_3
   ```
2. Open your terminal and navigate to your project directory. 
   ```bash
   cd ~/Downloads/"UNPROF PROJECT"
   ```
3. Execute the code
   ```bash
   python3 "task 3.py"
   ```
📁 File Structure
task 3.py - The main Python script containing the application logic.

data.json - Auto-generated storage file for your contact data.

app.log - Auto-generated log file tracking application events and errors.

Concept,Implementation
try / except,Catching FileNotFoundError or JSONDecodeError to prevent the app from crashing on startup.
else / finally,Executing code only when file loading succeeds (else) and confirming startup completion (finally).
Custom Exceptions,Defining and raising a specific EmptyNameError to block blank name inputs.
Logging,"Utilizing Python's logging module to track INFO, WARNING, and ERROR events in the background."
