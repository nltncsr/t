from t import api


# Instance object of User containing the token's owner user data
myself = api.me()


# Returns own name's user
def get_name():
	return myself.name


# Returns own username
def get_username():
	return myself.screen_name


# Returns user bio
def get_description():
	return myself.description


# Displays tweets from home timeline
def timeline(count=10):
	tl = api.home_timeline(None, None, count)
	for tweet in tl:
		print('\n@' + tweet.author.screen_name, tweet.author.name)
		print(tweet.text + '\n\n')


# Tweet
def tweet(status):
	if type(status) == str or type(status) == int:
		if len(status) <= 140:
			api.update_status(status)
		else:
			print('This tweet is too long!')
	else:
		print('This is not a valid status to tweet. Try to be human.')
