#!/usr/bin/bash

pyinstaller --onefile main.py

rm -f prod
mkdir prod

cp ./dist/main ./prod/questionMaker
cp ./index_src.html ./prod/
cp -r ./sample_questions ./prod/questions


