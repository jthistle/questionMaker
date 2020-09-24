@echo off

pyinstaller --onefile main.py

rmdir /S /Q prod
mkdir prod
mkdir prod\final\

copy dist\main.exe prod\questionMaker.exe
copy index_src.html prod\
xcopy /Y /E /I sample_questions prod\questions

copy USAGE.md prod\README.md
