# RetriveGithubInfoAPI

This API is used for retrieve some user info from github API.
To use this API, firstly install the requests lib by: pip3 install requests
Then you can directly call the API with the function name and params.

get_github_followers(username, depth): accepts a GitHub ID and returns Follower GitHub ID’s (up to 5 Followers total) associated with the passed in GitHub ID.  Retrieve data up to 3 levels deep, repeating the process of retrieving Followers (up to 5 Followers total) for each Follower found
get_github_repos_and_stargazer(username, depth): accepts a GitHub ID and returns Follower GitHub ID’s (up to 5 Followers total) associated with the passed in GitHub ID.  Retrieve data up to 3 levels deep, repeating the process of retrieving Followers (up to 5 Followers total) for each Follower found
