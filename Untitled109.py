#!/usr/bin/env python
# coding: utf-8
Question 1. What is MongoDB? Explain non-relational databases in short. In which scenarios it is preferred to use MongoDB over SQL databases? Answer :MongoDB is a document-oriented, NoSQL database that uses a JSON-like format for storing and querying data. Unlike traditional SQL databases, MongoDB does not use tables and rows, but instead uses collections and documents. Each document can have a unique schema, which means that the structure of the data can vary from one document to another within the same collection.

Non-relational databases, also known as NoSQL databases, are databases that do not use the traditional relational data model used in SQL databases. Instead of tables, non-relational databases use different data models, such as key-value, document, column-family, or graph. These databases are often designed to handle large volumes of unstructured or semi-structured data, and they provide high scalability and flexibility.

There are several scenarios where MongoDB may be preferred over SQL databases:

Agile development: MongoDB's flexibility allows developers to quickly change the schema as needed, making it ideal for agile development environments.

High-volume data: MongoDB's scalability allows it to handle large volumes of data and high-velocity data streams, making it a good choice for applications that require real-time data processing.

Complex data structures: MongoDB's document-oriented data model allows it to handle complex data structures, making it well-suited for applications that deal with unstructured or semi-structured data.

Cloud-based applications: MongoDB's ability to scale horizontally and its cloud-friendly architecture make it a popular choice for cloud-based applications.

Mobile and web applications: MongoDB's flexible schema and native support for JSON make it a good choice for mobile and web applications that require a lightweight, scalable database.

Overall, MongoDB is a powerful and flexible database that can handle a wide range of data models and workloads, making it an attractive choice for many applications.Question 2. State and Explain the features of MongoDB. Answer :MongoDB is a popular NoSQL document-oriented database that offers a wide range of features to developers and users. Here are some of the key features of MongoDB:

1.Document-Oriented: MongoDB is a document-oriented database, which means that data is stored in flexible JSON-like documents, rather than tables and rows like in SQL databases. Each document can have a unique schema, making it easy to store and retrieve complex data.

2.Schema-less: MongoDB is schema-less, which means that the data structure can be changed dynamically, making it easy to work with evolving data.

3.Scalability: MongoDB is highly scalable, making it a good choice for large-scale applications. It can be easily scaled horizontally across multiple servers or nodes, and can handle large volumes of data.

4.High Availability: MongoDB offers automatic failover and replica sets, which ensures that data is always available even in the event of a hardware failure or network outage.

5.Performance: MongoDB offers high performance with features like indexing, query optimization, and support for parallel queries.

6.Flexibility: MongoDB provides a flexible data model that can be used to store and process various types of data, including unstructured, semi-structured, and structured data.

7.Aggregation Framework: MongoDB has a powerful aggregation framework that allows users to perform complex analytics on the data.

8.MapReduce: MongoDB supports MapReduce for processing large volumes of data and performing complex data analysis.

9.Multi-platform: MongoDB supports multiple platforms, including Windows, Linux, and macOS, making it accessible to a wide range of users.Question 3. Write a code to connect MongoDB to Python. Also, create a database and a collection in MongoDB. Answer :In this example, we first import the pymongo module, which is a Python driver for MongoDB. We then connect to the MongoDB server using the MongoClient() method and specifying the connection string.

Next, we create a new database called "mydatabase" using the client["mydatabase"] syntax. We then create a new collection called "customers" within the database using the mydb["customers"] syntax.

Finally, we add a document to the collection using the insert_one() method and print the ID of the inserted document using the inserted_id property.

Note that in this example, we are assuming that MongoDB is running on the local machine on the default port of 27017. If your MongoDB server is running on a different host or port, you'll need to adjust the connection string accordingly.
# In[2]:


pip install pymongo


# In[3]:


import pymongo

# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb+srv://oyerahul:Rahulmongo2023@cluster0.dobkzwl.mongodb.net/?retryWrites=true&w=majority")

# Create a new database
mydb = client["mydatabase"]

# Create a new collection in the database
mycol = mydb["customers"]

# Add a document to the collection
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)

# Print the ID of the inserted document
print(x.inserted_id)

Q4. Using the database and the collection created in question number 3, write a code to insert one record, and insert many records. Use the find() and find_one() methods to print the inserted record. Answer:
# In[4]:


# Insert many records into the collection
mylist = [
  { "name": "Peter", "address": "Lowstreet 27" },
  { "name": "Amy", "address": "Apple st 652" },
  { "name": "Hannah", "address": "Mountain 21" },
  { "name": "Michael", "address": "Valley 345" },
  { "name": "Sandy", "address": "Ocean blvd 2" },
  { "name": "Betty", "address": "Green Grass 1" },
  { "name": "Richard", "address": "Sky st 331" },
  { "name": "Susan", "address": "One way 98" },
  { "name": "Vicky", "address": "Yellow Garden 2" },
  { "name": "Ben", "address": "Park Lane 38" },
  { "name": "William", "address": "Central st 954" },
  { "name": "Chuck", "address": "Main Road 989" },
  { "name": "Viola", "address": "Sideway 1633" }
]
x = mycol.insert_many(mylist)

# Find one record in the collection
result = mycol.find_one()
print(result)

# Find all records in the collection and print them
results = mycol.find()
for result in results:
    print(result)

Question 5. Explain how you can use the find() method to query the MongoDB database. Write a simple code to demonstrate this. Answer:The find() method is used to query the MongoDB database and retrieve documents that match a given set of criteria. The find() method takes one or more query parameters and returns a cursor object that can be used to iterate over the matching documents.

Here's an example code that demonstrates how to use the find() method to query the "customers" collection in the "mydatabase" database created in Question 3:
# In[5]:


# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb+srv://oyerahul:Rahulmongo2023@cluster0.dobkzwl.mongodb.net/?retryWrites=true&w=majority")

# Get a reference to the "mydatabase" database and the "customers" collection
mydb = client["mydatabase"]
mycol = mydb["customers"]

# Find all records in the collection where the name is "John"
query = { "name": "John" }
results = mycol.find(query)

# Print the matching records
for result in results:
    print(result)

Question 6. Explain the sort() method. Give an example to demonstrate sorting in MongoDB. Answer :The sort() method in MongoDB is used to sort the results of a query in either ascending or descending order based on one or more fields in the documents. The sort() method takes a dictionary as its parameter, where the keys represent the field or fields to sort by, and the values represent the sort order (1 for ascending order and -1 for descending order).

Here's an example code that demonstrates how to use the sort() method to sort the "customers" collection in the "mydatabase" database created in Question 3
# In[6]:


# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb+srv://oyerahul:Rahulmongo2023@cluster0.dobkzwl.mongodb.net/?retryWrites=true&w=majority")

# Get a reference to the "mydatabase" database and the "customers" collection
mydb = client["mydatabase"]
mycol = mydb["customers"]

# Sort the collection by name in ascending order
results = mycol.find().sort("name", 1)

# Print the sorted results
for result in results:
    print(result)


# In[7]:


results2 = mycol.find().sort([("name", 1), ("address", -1)])
# Print the sorted results
for result in results2:
    print(result)

Question 7. Explain why delete_one(), delete_many(), and drop() is used. Answer: In MongoDB, the delete_one() and delete_many() methods are used to remove one or many documents from a collection, respectively. The drop() method is used to remove an entire collection from a database.

1.delete_one(filter): This method is used to remove a single document that matches the given filter criteria. For example, if we wanted to remove a customer with the name "John" and the address "Highway 37", we could use the following code: This would remove the first document that matches the query criteria from the "customers" collection.

myquery
mycol.delete_one(myquery)```

2.`delete_many(filter)`: This method is used to remove all documents that match the given filter criteria. For example, if we wanted to remove all customers with the last name "Doe", we could use the following code:

```myquery = { "lastname": "Doe" }
mycol.delete_many(myquery)```

3.`drop()`: This method is used to remove an entire collection from a database. For example, if we wanted to remove the "customers" collection from the "mydatabase" database, we could use the following code:

```mycol.drop()```