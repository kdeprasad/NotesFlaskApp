# Notes App

A basic Flask web application for saving and storing notes.

## Setup

1. Ensure you have Python installed.
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment: `.venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`

## Running the App

Run the application with:

```
python app.py
```

The app will start on http://127.0.0.1:5000/

## Features

- View all saved notes on the home page.
- Add new notes with title and content.
- Notes are stored in a JSON file (`notes.json`) for persistence.

## Usage

- Navigate to the home page to see existing notes.
- Use the form at the bottom to add a new note.