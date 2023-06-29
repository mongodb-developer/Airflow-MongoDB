def my_task():
    # Connect to MongoDB
    client = MongoClient('mongodb://your_mongodb_host:your_mongodb_port')
    db = client.your_database
    collection = db.your_collection
    
    # Perform operations on the MongoDB data
    # Example: Fetch documents from the collection
    documents = collection.find({})
    for document in documents:
        print(document)
Create a DAG object and define its parameters:
with DAG(
    dag_id='my_dag',
    schedule_interval=None,  # Set the schedule as per your requirement
    start_date=datetime.datetime(2023, 6, 29),  # Set the start date
) as dag:
