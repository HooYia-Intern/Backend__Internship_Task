import http.client

# Create an HTTP connection
conn = http.client.HTTPConnection('www.udemy.com')
conn.request('GET', '/')

# Get the response
response = conn.getresponse()
print("Response Status:", response.status)
print("Response Data:", response.read().decode())
