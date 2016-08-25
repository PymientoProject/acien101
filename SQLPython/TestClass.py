import DATABASE
import SQLClass

obj = SQLClass.SQLClass(DATABASE.DB_HOST, DATABASE.DB_USER, DATABASE.DB_PASS, DATABASE.DB_NAME)
print(obj.getNumTweetsWithNum(1))