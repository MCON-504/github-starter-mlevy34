import requests
'''
# GET
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
post = response.json()

# POST
new_post = {"title": "Hello", "body": "World", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)

# PUT
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=updated_post)

# DELETE
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
'''
# EXERCISE 1.1
response = requests.get("https://jsonplaceholder.typicode.com/posts")
post = response.json()

# EXERCISE 1.2
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
post = response.json()

# EXERCISE 1.3
response = requests.get("https://jsonplaceholder.typicode.com/posts?userId=1")
post = response.json()

# EXERCISE 1.4
response = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")
post = response.json()

# EXERCISE 2.1
new_post = {
    "title": "My New Post",
    "body": "This is the content of my post.",
    "userId": 1
}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)

# EXERCISE 3.1
updated_post = {
    "id": 1,
    "title": "Updated Title",
    "body": "Completely new content.",
    "userId": 1
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json=updated_post
)

# EXERCISE 4.1
updated_post = {
    "title": "Only the Title Changed"
}

response = requests.patch(
    "https://jsonplaceholder.typicode.com/posts/1",
    json=updated_post
)

# EXERCISE 5.1

response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

# EXERCISE 6.1
new_post = {
    "username": "emilys",
    "password": "emilyspass"
}
response = requests.post("https://dummyjson.com/auth/login", json=new_post)

# EXERCISE 6.2
login_response = response.json()
access_token = login_response["accessToken"]
headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get(
    "https://dummyjson.com/auth/me",
    headers = headers
)

post = response.json()

# EXERCISE 7.1
response = requests.get("https://dummyjson.com/products?limit=5")
post = response.json()

# EXERCISE 7.2
response = requests.get("https://dummyjson.com/products/1")
post = response.json()

# EXERCISE 7.3
new_product = {
    "title": "New Product",
    "price": 99.99,
    "description": "A test product",
    "category": "electronics"
}

response = requests.post(
    "https://dummyjson.com/products/add",
    json=new_product
)

# EXERCISE 7.4
updated_post = {
    "title": "Updated Product Name",
    "price": 149.99
}
response = requests.put("https://dummyjson.com/products/1", json=updated_post)

# EXERCISE 7.5
response = requests.delete("https://dummyjson.com/products/1")