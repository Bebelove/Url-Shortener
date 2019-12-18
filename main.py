def userPrompt(text):
    return input(text)


def generateShortUrl(length):
    ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def main():
    while True:
        urlsSet = dict()
        url = userPrompt('Input your url please: ')
		shortUrl = generateShortUrl(7)
		print('Your url is: ' + 'shurl.com/' + shortUrl)


if __name__ == '__main__':
    main()
