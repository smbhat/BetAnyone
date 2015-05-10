import json
import sys
import os

def main():
	users = []
	d = {}
	jsonFile = open("students.json")
	studentList = json.loads(jsonFile.readline())
	for student in studentList:
		name = student[0]
		year = student[1]
		email = student[2]
		netid = email[0:email.index("@")]
		users.append(netid)

	for i in range(0, len(users)):
		print str(users[i]),
		print ','

main()