#!/bin/bash
FILES=./data/**
for f in $FILES
do
	python3.5 main.py < $f > "${f%.*}.out"
done