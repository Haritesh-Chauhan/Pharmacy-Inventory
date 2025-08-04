import mysql.connector

# connection with database
Info = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    db="medi"
)
cursor = Info.cursor()

def registerUser(data):
    try:
        cursor.execute('INSERT INTO `emp` (`name`,`email`,`phone number`,`username`,`password`) VALUES (%s,%s,%s,%s, %s)', data)
        Info.commit()
        return True
    except Exception as e:
        print('exception is ', e)
        return False
    
def insertdata(data):
    try:
        cursor.execute('INSERT INTO `med` (`Ref ID`,`Medicine name`,`Price`,`Quantity`) VALUES (%s,%s,%s,%s)', data)
        Info.commit()
        return True
    except Exception as e:
        print('exception is ', e)
        return False
    
def fetch_data():
    try:
        cursor.execute('SELECT * FROM `med` where Quantity > 0')
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return False
   
def loginUser(data):
    try:
        cursor.execute('SELECT * FROM `emp` WHERE `username` = %s AND `password` = %s', data)
        return cursor.fetchone()
    except Exception as e:
        print(e)
        return False
    

def deleteUser(id):
    try:
        cursor.execute('DELETE FROM `emp` WHERE `id` = %s', id)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def deleteUser1(id):
    try:
        cursor.execute('DELETE FROM `med` WHERE `id` = %s', id)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
  
def fetch1_data():
    try:
        cursor.execute('SELECT * FROM `med`')
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return False
    
    
def fetchnew_data():
    try:
        cursor.execute('SELECT * FROM `emp`')
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return False
    

def updateMedQuantity(data):
    print("to quantity = ", data[1], "of id = ", data[0])
    try:
        cursor.execute('UPDATE `med` SET `Quantity` = %s WHERE `id` = %s', data)
        Info.commit()
        return True
    except Exception as e:
        print("Error in updateMedQuantity", e)
        return False
    
def placeOrder(data):
    try:
        cursor.execute('INSERT INTO `place_order` (`name`,`phone_no`,`date`,`total_price`) VALUES (%s,%s,%s,%s)', data)
        Info.commit()
        return True
    except Exception as e:
        print("Error in placeOrder", e)
        return False
    
def fetchbill_data():
    try:
        cursor.execute('SELECT * FROM `place_order`')
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return False
    