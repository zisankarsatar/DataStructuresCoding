#!/bin/zsh

cd /Users/zisan/Desktop/workingPython/simpleProjects

simdi=$(date +%d.%m.%Y)
git commit --allow-empty -m "Autocommit ${simdi}"
git push