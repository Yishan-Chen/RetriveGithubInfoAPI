import requests

def get_github_followers(username, depth=3, cuzDepth=1, num_of_followers=5):
	url = "https://api.github.com/users/%s/followers" % (username)
	response = requests.get(url)
	if response.status_code == 200:
		data = response.json()
		if cuzDepth == depth:
			res = []
			for i in range(num_of_followers):
				if i > len(data)-1: break
				res.append(str(data[i]["id"]))
		else:
			res = {}
			for i in range(num_of_followers):
				if i > len(data)-1: break
				res[str(data[i]["id"])] = get_github_followers(data[i]["login"], depth, cuzDepth+1)
		return res
	else:
		print ("%i:%s, fail to retrieve %s's followers" % (response.status_code, response.reason, username))
		return None

def get_github_repos_and_stargazer(username, depth=3, cuzDepth=1, num_of_repos=3):
	url = "https://api.github.com/users/%s/repos" % (username)
	response = requests.get(url)
	if response.status_code == 200:
		data = response.json()
		if cuzDepth == depth:
			res = []
			for i in range(num_of_repos):
				if i > len(data)-1: break
				res.append(data[i]["name"])
		else:
			res = {}
			for i in range(num_of_repos):
				if i > len(data)-1: break
				owner = data[i]["owner"]["login"]
				repoName = data[i]["name"]
				res[repoName] = {}
				stargazers = get_github_stargazer(owner,repoName)
				if stargazers:
					for stargazer in stargazers:
						res[repoName][stargazer] = get_github_repos_and_stargazer(stargazer, depth, cuzDepth+1)
		return res
	else:
		print ("%i:%s, fail to retrieve %s's repos" % (response.status_code, response.reason, username))
		return None

def get_github_stargazer(username, repoName, num_of_stargazer=3):
	url = "https://api.github.com/repos/%s/%s/stargazers" % (username,repoName)
	response = requests.get(url)
	if response.status_code == 200:
		res = []
		data = response.json()
		for i in range(num_of_stargazer):
			if i > len(data)-1: break
			else:
				res.append(data[i]["login"])
		return res
	else:
		print ("%i:%s, fail to retrieve %s's repo %s's stargazer" % (response.status_code, response.reason, username, repoName))
		return None

username = "yongtang"
print(get_github_followers(username))
print(get_github_repos_and_stargazer(username))

