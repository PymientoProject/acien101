import MySQLdb

class SQLClass:

    def __init__(self, DB_HOST, DB_USER, DB_PASS, DB_NAME):
        datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
        self.conn = MySQLdb.connect(*datos)  # Conectar a la base de datos



    def getNumTweets(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM TweeterData")
        data = cursor.fetchall()
        cursor.close

        return data

    def getNumTweetsWithNum(self, num):
        query = "SELECT VALUE FROM TweeterData WHERE Planta=" + str(num)

        cursor = self.conn.cursor()
        cursor.execute(query)

        data = cursor.fetchone()

        desc = cursor.description

        dict = {}

        for (name, value) in zip(desc, data):
            dict[name[0]] = value

        cursor.close
        return dict['VALUE']

    def insertNumTweets(self, planta):
        query = "UPDATE TweeterData SET Value=1 WHERE Planta=" + str(planta)
        print(query)

        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()  # Hacer efectiva la escritura de datos
        cursor.close


