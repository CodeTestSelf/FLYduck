import pymongo
# Replace the uri string with your MongoDB deployment's connection string.
conn_str = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000"
                                    #"mongodb+srv://<username>:<password>@<cluster-address>/test?retryWrites=true&w=majority"  (default)
           
# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
try:
    print(client.server_info())
except Exception:
    print("Unable to connect to the server.")