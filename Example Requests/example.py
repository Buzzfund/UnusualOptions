# example request from Tradier API

import http.client

# Request: Market Quotes (https://sandbox.tradier.com/v1/markets/quotes?symbols=spy)

connection = http.client.HTTPSConnection('sandbox.tradier.com', 443, timeout = 30)

# Headers

headers = {"Accept":"application/json",
           "Authorization":"Bearer VRJviCo0AQNLEpZOeUvrC2WbqHAC"}

# Send synchronously

connection.request('GET', '/v1/markets/quotes?symbols=spy', None, headers)
try:
  response = connection.getresponse()
  content = response.read()
  print(content)
  # Success
  print('Response status ' + str(response.status))
except http.client.HTTPException as e:
  # Exception
  print('Exception during request')