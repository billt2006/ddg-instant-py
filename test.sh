#!/bin/bash

printf "Topic Summary\n=============\n"
python ./ddg-instant.py "valley forge national park"

printf "\nCategory\n========\n"
python ./ddg-instant.py "simpsons characters"

printf "\nDisambiguation\n==============\n"
python ./ddg-instant.py "apple"

printf "\n!Bang Redirect\n==============\n"
python ./ddg-instant.py "\!imdb rushmore"

printf "\nAnswer\n======\n"
python ./ddg-instant.py "1 + 1"
