import pymongo

db_connect_string = 'mongodb+srv://khanh051201:khanh051201@cluster0.kv1gu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
db_name = 'student_db'
client = pymongo.MongoClient(db_connect_string)

db = client[db_name]

collection = db["student_db"]

while (True):
    action = input("insert action: ")
    if action == 'show_all':
        results = collection.find()
        for result in results:
            print(result)
    if action == 'delete':
        student_id = input("insert student id: ")
        query = {"student_id": int(student_id)}
        result = collection.delete_one(query)
        if result.deleted_count == 1:
            print("Document deleted successfully")
        else:
            print("Document not found or could not be deleted")
    if action == 'find_name':
        student_name = input("insert student name: ")
        query = {"student_id": student_name}
        results = collection.find(query)
        for result in results:
            print(result)
    if action == 'find_score':
        subject = input("insert subject: ")
        score = input("input score")
        query = {
            "score": {
                "$elemMatch": {
                    "subject": subject,
                    "score": int(score)
                }
            }
        }
        results = collection.find(query)
        for result in results:
            print(result)
    if action == 'find_total_score':
        score = input("input score")
        query = {
            "$expr": {
                "$lt": [
                    {
                        "$sum": "$score.score"
                    },
                    int(score)
                ]
            }
        }
        results = collection.find(query)
        for result in results:
            print(result)
    if action == '0':
        break
client.close()