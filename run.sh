#!/bin/bash
FILES=./data/*.in
for f in $FILES
do
	python3.5 main.py < $f > "${f%.*}.out"
done