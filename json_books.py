import json

books = { "book1": {
                    "title": "The Green Lantern",
                    "author" : "Someone old",
                    "year": "1962",
                    "pages": "34"
                    },
          "book2":{ 
                    "title": "The Shed",
                    "author": "Someone new",
                    "year": "1998",
                    "pages": "22",
                    },
          "book3":{
                    "title": "Teletubbies",
                    "author": "Someone young",
                    "year": "2002",
                    "pages": "3"
                    },
          "book4":{
                    "title": "The Lion King",
                    "author": "Some icon",
                    "year": "1972",
                    "pages": "101",
                    },
          "book5":{
                    "title": "The Hulk",
                    "author": "Someome interesting",
                    "year": "1923",
                    "pages": "89",
                    },
          "book6":{
                    "title": "Lord of the Rings",
                    "author": "A Legend",
                    "year": "1962",
                    "pages": "34"
                    }
        }

with open('books.json','w') as b:
    json.dump(books, b, sort_keys = True, indent = 4)