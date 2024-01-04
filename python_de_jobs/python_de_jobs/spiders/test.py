from urllib.parse import urlencode

parameters = {"q": "Python", "l": "Deutschland", "fromage": 14, "filter": 0, "start": "offset"}
print("https://www.de.indeed.com/jobs?" + urlencode(parameters))