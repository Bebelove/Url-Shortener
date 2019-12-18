def userPrompt(text):
    return input(text)
	
def generateShortUrl(length):
    return ''.join(
        random.choice(string.ascii_lowercase) for i in range(length))

def main():
    while True:
        urlsSet = dict()
        url = userPrompt('Input your url please: ')
		shortUrl = generateShortUrl(7)
		print('Your url is: ' + 'shurl.com/' + shortUrl)


if __name__ == '__main__':
    main()
