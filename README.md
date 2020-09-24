# QuestionMaker

A tool for making portable webpages to randomly choose practice questions.

## Building for distribution

Requires `pyinstaller` and python3:

```
pip install pyinstaller
```

### Linux

To make this into a form distributable to end users on Linux, run `make_prod.sh` and share the contents of the `prod` directory.

### Windows

Run `make_prod.bat` and share the contents of the `prod` directory. You may have to go into Windows Defender a couple of times
to tell it that, no, you're not trying to install malware.

## Dev

### Setup

1. `cp sample_questions questions`
2. `python3 main.py`
3. `firefox ./final/index.html` (replacing `firefox` with the browser of your choice)

### Testing

Every time you make a change, you'll have to run `python3 main.py` and then reload the webpage at `./final/index.html` in your browser.

