#!/usr/bin/bash

pyinstaller --onefile main.py

rm -f prod
mkdir prod
mkdir ./prod/final

cp ./dist/main ./prod/questionMaker
cp ./index_src.html ./prod/
cp -r ./sample_questions ./prod/questions

cp USAGE.md ./prod/README.md
