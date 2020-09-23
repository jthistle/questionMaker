# QuestionMaker

A tool for making portable webpages to randomly choose practice questions.

## Building for distribution

### Linux

To make this into a form distributable to end users, run `make_prod.sh` and share the contents of the `prod` directory.

Requires `pyinstaller`.

### Windows

Once I work out how tf batch files work I'll do something for this.

## Dev

### Setup

1. `cp sample_questions questions`
2. `python3 main.py`
3. `firefox ./final/index.html` (replacing `firefox` with the browser of your choice)

### Testing

Every time you make a change, you'll have to run `python3 main.py` and then reload the webpage at `./final/index.html` in your browser.

