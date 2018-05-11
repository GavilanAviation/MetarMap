#!/bin/bash
#Runs metar scripts in special python environment
#Change mode before using - chmod +x metarscript
#How to use metarscript pythonscriptname
#written by Herb Spenner
#rev. 05/10/2018
string1='sudo PYTHONPATH=".:./" python '
cmd=$string1$1
$cmd
