#!/usr/bin/python
#Author : Anthony Minerva
#Date: September 12th, 2018
#Desc: Class Exercise 1: Counting Student Questions

studentGrades  = [
	["A", "B", "A", "C", "C", "D", "E", "E", "A", "D"],
	["D", "B", "A", "B", "C", "A", "E", "E", "A", "D"],
	["E", "D", "D", "A", "C", "B", "E", "E", "A", "D"],
	["C", "B", "A", "E", "D", "C", "E", "E", "A", "D"],
	["A", "B", "D", "C", "C", "D", "E", "E", "A", "D"],
	["B", "B", "E", "C", "C", "D", "E", "E", "A", "D"],
	["B", "B", "A", "C", "C", "D", "E", "E", "A", "D"],
	["E", "B", "E", "C", "C", "D", "E", "E", "A", "D"]
]
answerKey = ["D", "B", "D", "C", "C", "D", "A", "E", "A", "D"]
for i in range(len(studentGrades)):
	score = 0
	for j in range(len(answerKey)):
		if(studentGrades[i][j] == answerKey[j]):
			score = score + 1
	print 'Student ' + str(i) + ' Correct Count is: ' + str(score)
	
