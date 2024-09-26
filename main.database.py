from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

# Replace the uri string with your MongoDB deployment's connection string.
uri = "mongodb+srv://amjadegbaria:amjadegbaria123@dev.q9log.mongodb.net/?retryWrites=true&w=majority&appName=dev"

client = MongoClient(uri)


def check_mongo_connection():
    try:
        # Create a MongoDB client instance
        client = MongoClient(uri, serverSelectionTimeoutMS=200000)  # 5-second timeout

        # Attempt to retrieve server info (this will raise an exception if the connection fails)
        client.server_info()
        print("MongoDB connection successful")

        # Optionally, print the server version
        print("MongoDB Server Version:", client.server_info()['version'])

    except ServerSelectionTimeoutError:
        print("Failed to connect to MongoDB: Server selection timeout.")
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")


# Run the connection check
if __name__ == "__main__":
    check_mongo_connection()
