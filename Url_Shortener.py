import pyshorteners

# initialize the shortener object
shortener = pyshorteners.Shortener()

# get input URL from user
url = input("Enter the URL to shorten: ")

# generate the shortened URL
short_url = shortener.tinyurl.short(url)

# print the shortened URL
print("Shortened URL:", short_url)
