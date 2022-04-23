#email -  harofi5043@tourcc.com
#pass -  harofi5043@tourcc.com

from matplotlib.pyplot import flag
import pymysql as pm
from soupsieve import select
from sympy import false

class Database():
    
    def __init__(self):
        try:
            # self.conn = pm.connect(host="bh2dw0lkgcfngmubnokz-mysql.services.clever-cloud.com",user="ulscuhyrfehpdd9c",password="IePBkCqOIwskP84uueku",database="bh2dw0lkgcfngmubnokz")
            self.conn = pm.connect(host="127.0.0.1",user="root",password="",database="pharmacy_management")
            self.cursor = self.conn.cursor()
        except:
            print("Did not connect")


    def logincheck(self,uname,passw):
        sql = "select * from admin where email='%s' and password='%s';" % (uname,passw)
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            return True
        else:
            return False


    def getLoginData(self,uname):
        sql = "select * from admin where email='%s';" % (uname)
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            return self.cursor.fetchone()


    def changePassword(self,user,oldp,newp):
        sql = "UPDATE admin SET password='%s' WHERE email='%s' AND password='%s';" %(newp,user,oldp)
        self.cursor.execute(sql)
        
        try:
            self.conn.commit()
            flag = True
        except:
            self.conn.rollback()
            flag = False 
        finally:
            return flag


    def editProfile(self,user,name,email,image):
        sql = "UPDATE admin SET name='%s', email='%s', image='%s' WHERE email='%s';" % (name, email, image,user)
        self.cursor.execute(sql)

        try:
            self.conn.commit()
            flag = True
        except:
            self.conn.rollback()
            flag = False
        finally:
            return flag


    def getBillNumber(self):
        self.cursor.execute("SELECT * FROM patient_prescription")
        return self.cursor.rowcount


    def savePatientData(self,pname,age,pmob,drname,hospitalname,itemlist,quantitylist,expirylist,unitpricelist,totalamount,admin):
        # sql = "INSERT INTO patient_prescription(`name`, `age`, `mob`, `date`, `dr_name`, `hosp_name`, `description`, `qty`, `expiry`, `unit_price`, `total`, `admin`) VALUES (%s,%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%f)" % (pname,age,pmob,date,drname,hospitalname,itemlist,quantitylist,"this is not set","this is not set",totalammount)
        # sql = "INSERT INTO patient_prescription(name, age, mob, dr_name, hosp_name, description, qty, expiry, unit_prize, total, admin) VALUES (%s,%d,%s,%s,%s,%s,%s,%s,%s,%f,%s)" % (pname,age,pmob,drname,hospitalname,itemlist,quantitylist,"this is not set","this is not set",totalammount,admin)
        
        sql = "INSERT INTO patient_prescription (sr_no, name, age, mob, date, dr_name, hosp_name, description, qty, expiry, unit_price, total, admin) VALUES (NULL, '%s', '%d', '%s', CURRENT_TIMESTAMP, '%s', '%s', '%s', '%s', '%s', '%s', '%f', '%s');"  % (pname,age,pmob,drname,hospitalname,itemlist,quantitylist,expirylist,unitpricelist,totalamount,admin)

        self.cursor.execute(sql)
        try:
            self.conn.commit()
            flag = True
        except:
            self.conn.rollback()
            flag = False 
        finally:
            return flag


    def findExpPrize(self,sql):
        self.cursor.execute(sql)
        exp,unitprice = self.cursor.fetchone()
        return exp,unitprice


    def getMedicineStock(self):
        sql = "select * from medicine_stock"
        self.cursor.execute(sql)
        ls = self.cursor.fetchall()
        return ls


    def addMedicineStock(self,itemName,companyName,mfgDate,expDate,unitPrice,totalUnits):
        sql = "INSERT INTO medicine_stock (sr_no, medicine_name, company, mfg, expiry, unit_price, total_units) VALUES (NULL, '%s', '%s', '%s', '%s', '%f', '%d');" % (itemName, companyName, mfgDate, expDate, unitPrice, totalUnits)
        
        self.cursor.execute(sql)
        try:
            self.conn.commit()
            flag = True
        except:
            self.conn.rollback()
            flag = False
        finally:
            return flag


    def updateMedicineStock(self,srNo,itemName,companyName,mfgDate,expDate,unitPrice,totalUnits):
        sql = "UPDATE medicine_stock SET medicine_name = '%s', company = '%s', mfg = '%s', expiry = '%s', unit_price = '%f', total_units = '%d' WHERE sr_no = '%d';" % (itemName, companyName, mfgDate, expDate, unitPrice, totalUnits, srNo)
        self.cursor.execute(sql)

        try:
            self.conn.commit()
            flag = True 
        except:
            self.conn.rollback()
            flag = False 
        finally:
            return flag


    def printBill(self):
        row = self.cursor.rowcount
        sql = "select * from patient_prescription ORDER BY sr_no DESC LIMIT 1"
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        return data


    def findExpPrize(self,sql):
        self.cursor.execute(sql)
        exp,unitprice = self.cursor.fetchone()
        return exp,unitprice

    