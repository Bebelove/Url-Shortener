import random
import string


def generateShortUrl(length):
    return ''.join(
        random.choices(string.ascii_lowercase + string.digits, k=length))


def main():

    urlsSet = dict()

    while True:
        url = input('Input your url please: ')

        if url in urlsSet:
            print('Url already shortened! Here it is: '+ 'shurl.com/' + urlsSet.get(url))
            print(' ')
        else:
            shortUrl = generateShortUrl(7)
            urlsSet[url] = shortUrl
            print('Your url is: ' + 'shurl.com/' + shortUrl)
            print(' ')


if __name__ == '__main__':
    main()
