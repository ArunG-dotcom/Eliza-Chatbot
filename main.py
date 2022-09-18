# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 15:33:43 2020

@author: reach
"""


print("Welcome to which Hello World instructor is your spirit animal")

quiz_Lines = open("Quiz.txt").readlines()

#"Quiz.txt".close()



score = {}
answers ={}
results = {}
people = {}
Q1 ={}
Q2 = {}
Q3 = {}

for line in quiz_Lines:
		line = line.replace("\n","")
		line = line.split(":")
		
		if line[0] == 'q1':
			Q1['question'] = line[1]
		
		if line[0] == 'q2':
			Q2['question'] = line[1]
		
		if line[0] == 'q3':
			Q3['question'] = line[1]
		
		if 'a1' in line[0]:
			Q1[line[0]] = line[1:]
		if 'a2' in line[0]:
				Q2[line[0]] = line[1:]
		if 'a3' in line[0]:
					Q3[line[0]] = line[1:]

		
		#if "result_" in line[0]:
			#print(line[0][7:])
			
		#print(Q1)			

print(Q1['question'])

# what is your favorite color and  red
print("1. " + Q1['a11'][0])  # print question, answer 1
print("2. " + Q1['a12'][0]) # print question, answer 2
print("3. " + Q1['a13'][0]) # print question, answer 3
print("4. " + Q1['a14'][0]) # print question, answer 4
answers['q1'] = input("Type your answer here:")	
new_key = 'a1'+ answers['q1']
print(Q1[new_key][1])

#print(Q1)



#print(people[answers['q1']])
# corrospond answer by user to person.



print(Q2['question'])
print("1. " + Q2['a21'][0])
print("2. " + Q2['a22'][0])
print("3. " + Q2['a23'][0])
print("4. " + Q2['a24'][0])
answers['q2'] = input("Type your answer here:")	
new_key = 'a2'+ answers['q1']
print(Q2[new_key][1])

print(Q3['question'])
print("1. " + Q3['a31'][0])
print("2. " + Q3['a32'][0])
print("3. " + Q3['a33'][0])
print("4. " + Q3['a34'][0])
answers['q3'] = input("Type your answer here:")	
new_key = 'a3'+ answers['q2']
print(Q3[new_key][1])

key_string = 'a3' + answers['q3'] 
print(Q3[key_string])
print(answers)
#print(Q3[key_string] + answers[0][2:])
print(results)
#full_name = first_name + ' ' + last_name )
# answer 3 and input for Q3
for results in answers:
	print(str(results))

print(results)
