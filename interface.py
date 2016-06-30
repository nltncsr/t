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


# Send a direct message
def dm(user, message):
	if type(user) == str and type(message) == str:
		if user[0] == '@': user = user[1:]
		api.send_direct_message(user, None, None, message)
	else:
		print('Both username and message must be a text.')


# Reply my last tweet
def continuing(status):
	if type(status) == str:
		api.update_status(status, api.me().status.id)


# Print a number of tweets of a user, default is own user, including theirs id's
def status(user=myself.screen_name, count=10):
	if user[0] == '@': user = user[1:]

	tweets = api.user_timeline(screen_name=user, count=count)

	if user == myself.screen_name:
		print('\n' + myself.name + '\n' + '@' + myself.screen_name + '\n')
	else:
		print('\n' + tweets[0].author.name + '\n' + '@' + tweets[0].author.screen_name + '\n')

	for tweet in tweets:
		print(tweet.text)
		print('ID: ' + tweet.id_str + '\n\n')


# Delete your own tweet
def delete(id):
	api.destroy_status(id)


# Retweet someone status
def retweet(id):
	api.retweet(id)

