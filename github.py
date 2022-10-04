import requests 
import json 

class GitHub: 
	def __init__(self): 
		self.api_url = 'https://api.github.com'

	def getUser(self, username):
		response = requests.get(self.api_url + '/users/' + username)
		return response.json()

	def getRepositories(self, username):
		response = requests.get(self.api_url + '/users/' + username + '/repos')
		return response.json()

github = GitHub()

while True: 
	secim = input('1- Find User\n2- Get Repository\n3- Create Repository\n4- Exit\nSeçim: ')

	if secim == '4':
		break 

	elif secim == '1':
		username = input("username: ")
		result = github.getUser(username)
		print(f"name: {result['name']} public repos: {result['public_repos']} followers: {result['followers']}")

	elif secim == '2':
		username = input("username: ")
		result = github.getRepositories(username)
		for repo in result: 
			print(repo["name"])

	elif secim == '3':
		pass 

	else: 
		pass 