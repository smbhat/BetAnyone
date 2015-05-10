import json
import sys
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BetAnyone.settings')
import django
django.setup()
from bets.models import Player

def main():
	users = []
	Player.objects.all().delete()
	jsonFile = open("students.json")
	studentList = json.loads(jsonFile.readline())
	for student in studentList:
		studentDict = {}
		name = student[0]
		year = student[1]
		email = student[2]
		netid = email[0:email.index("@")]
		Users.append(Student(netid=netid))

	for u in users:
		u.save()

main()