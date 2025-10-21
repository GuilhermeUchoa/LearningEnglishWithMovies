import json

data = {
  "firstName": "Sammy",
  "lastName": "Shark",
  "age": 30,
  "isStudent": False,
  "courses": [
    {"title": "Intro to JSON", "credits": 3},
    {"title": "Advanced Data", "credits": 4}
  ],
  "contact": {
    "email": "s.shark@example.com",
    "phone": None
  }
}

print(data)