from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

NOTES_FILE = 'notes.json'

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f)

@app.route('/')
def index():
    notes = load_notes()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    title = request.form.get('title')
    content = request.form.get('content')
    if title and content:
        notes = load_notes()
        notes.append({'title': title, 'content': content})
        save_notes(notes)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)