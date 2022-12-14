


class Database:
    exists = False

    def __init__(self, data):
        
        if (Database.exists is False):
            Database.instance = self
            Database.exists = True
            Database.data = data
  
    def getData(self):
        return self.data
  


mongo = Database('MongoDB')
print(mongo.getData())

mysql = Database('MySQL')
print(mysql.getData())

psql = Database('PostgreSQL')
print(mysql.getData())

# MongoDB
# MongoDB
# MongoDB