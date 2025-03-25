
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://nandan4118006ex:Nandan8850@cluster0.wd7wp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)