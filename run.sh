#!/bin/bash

if [ ! -d "VenvPython1" ] 
then
	echo "The virtual environnement does not exist"
	python3 -m venv VenvPython1
fi
echo "Virtual environnement exists"
pip install -r requirements.txt
source VenvPython1/bin/activate
python main.py
