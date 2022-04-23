from flask import Flask, render_template, request, redirect, session
import os

from requests import Session

from model import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "123"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

app.config['UPLOAD_FOLDER'] = 'uploads/'

# ***************************Billing Operations Start*****************************
# ********************************************************************************

# Billing Page
@app.route("/billing")
def billing():
    db = Database()
    billno= db.getBillNumber()
    medstock = db.getMedicineStock()
    return render_template("billing.html",billno=billno,medstock=medstock)


@app.route("/handlebill", methods=["POST","GET"])
def handleBill():
    if request.method == "POST":
        pname = request.form["pname"]
        age = int(request.form["age"])
        pmob = request.form["pmob"]
        drname = request.form["drname"]
        hospitalname = request.form["hospitalname"]
        
        itemlist = request.form["itemlist"]
        quantitylist = request.form["quantitylist"]
        totalammount = float(request.form["totalammount"])

        admin = session["user"]

        unitpricelist = []
        expirylist = []


        # taking expry date and unit prize from database
        tempItemList = itemlist.split(",")
        for i in tempItemList:
            sql = 'select expiry, unit_price from medicine_stock where medicine_name="%s";' % (i.strip());
            db = Database()
            try:
                tempExp,tempUnit = db.findExpPrize(sql)
            except:
                tempExp,tempUnit=0,0
            
            unitpricelist.append(str(tempUnit))
            expirylist.append(str(tempExp))

        unitpricelist = ",".join(unitpricelist)
        expirylist = ",".join(expirylist)

        db = Database()
        flag = db.savePatientData(pname,age,pmob,drname,hospitalname,itemlist,quantitylist,expirylist,unitpricelist,totalammount,admin)
        
        if flag:
            return redirect("/printbill")

        # else:
        #     return "failed"
        #     # session["alert"] == "patientDetails_failed"

    return redirect("/billing")


@app.route("/printbill")
def printBill():
    db = Database()
    data = db.printBill()
    billno = data[0]
    name = data[1]
    age = data[2]
    mob = data[3]

    date = str(data[4]).split()[0]
    date = date.split("-")
    date= date[2]+"/"+date[1]+"/"+date[0]

    dr = data[5]
    hosp = data[6]
    medicines = data[7].split(",")
    expiry = data[9].split(",")
    
    qty = data[8].split(",")
    qty = list(map(int,qty))
    unitprice = data[10].split(",")
    unitprice = list(map(float,unitprice))  

    total = data[11]

    return render_template("billlayout.html",name=name,age=age,mob=mob,date=date,dr=dr,hosp=hosp,billno=billno,total=total,medicines=medicines,qty=qty,expiry=expiry,unitprice=unitprice)
    

# *****************************Billing Operations End *****************************
# *********************************************************************************


# *******************************Check Stock Start*********************************
# *********************************************************************************

# Checkstock Page
@app.route("/checkstock")
def checkstock():
    db = Database()
    ls = db.getMedicineStock()
    return render_template("checkstock.html",ls=ls)


# *******************************Check Stock End***********************************
# *********************************************************************************


# *******************************Edit Stock Start**********************************
# *********************************************************************************

# editstock Page
@app.route("/editstock")
def editstock():
    db = Database()
    medStock = db.getMedicineStock()
    return render_template("editstock.html",medStock=medStock)


# additem handle
@app.route("/additem",methods=["POST","GET"])
def additem():
    if request.method == "POST":
        itemName = request.form["itemname"]
        companyName = request.form["companyname"]
        mfgDate = request.form["mfgdate"]
        expDate = request.form["expdate"]
        unitPrice = float(request.form["unitprice"])
        totalUnits = int(request.form["totalunits"])

        db = Database()
        flag = db.addMedicineStock(itemName,companyName,mfgDate,expDate,unitPrice,totalUnits)

        if flag:
            return redirect("/editstock")

    # send alert message for fail 
    return redirect("/editstock")
    

# update handle 
@app.route("/updateitem", methods=["post","get"])
def updateItem():
    if request.method == "POST":
        srNo = int(request.form["sr"])
        itemName = request.form["itemname"]
        companyName = request.form["companyname"]
        mfgDate = request.form["mfgdate"]
        expDate = request.form["expdate"]
        unitPrice = float(request.form["unitprice"])
        totalUnits = int(request.form["totalunits"])

        db = Database()
        flag = db.updateMedicineStock(srNo,itemName,companyName,mfgDate,expDate,unitPrice,totalUnits)

        if flag:
            return redirect("/editstock")
            
    # send alert message for fail 
    return redirect("/editstock")


# *******************************Edit Stock End************************************
# *********************************************************************************


# ***************************Admin Operations Start********************************
# *********************************************************************************

# Login Page
@app.route("/")
def login():
    if session.get("login") == None:
        return render_template("index.html")
    
    elif session.get("login") == True:
        return redirect("/home")
    
    else:
        session.clear()
        return render_template("index.html", msg="1")


# Login Handle
@app.route("/handlelogin", methods=["GET", "POST"])
def handlelogin():
    if request.method == "POST":
        uname = request.form["username"]    
        passw = request.form["passw"]

        db = Database()
        flag = db.logincheck(uname, passw)

        if flag:
            session["login"] = True
            session["user"] = uname
            return redirect("/home")
    session["login"] = False
    return redirect('/')
    

# Changing Admin Password
@app.route("/changepassword", methods=["GET", "POST"])
def changePassword():
    if request.method == "POST":
        oldp = request.form["oldpassword"]
        newp = request.form["newpassword"]
        conp = request.form["confirmpassword"]

        # checking if new password and confirm password are same
        if newp==conp:
            db = Database()
            flag = db.changePassword(session["user"], oldp, newp)

            if flag:
                # if changes are made successfully
                session["alert"] = "password_success"
                return redirect("/home")
            else:
                # if changes are failed
                session["alert"] = "password_failed"
                return redirect("/home")

        # error if new and confirm password are not same
        else:
            session["alert"] = "password_failed"
            return redirect("/")   
   
    # error if user tries access this page with get method
    else:
        return redirect("/")


# Edit Admin Profile
@app.route("/editprofile",methods=["GET","POST"])
def editProfile():
    if request.method == "POST":
        name = request.form["name"].title()
        email = request.form["email"]

        # if user does not enters image then some error will be created hence to prevent this we are using try-except
        try:
            f = request.files['image']
            image = f.filename
            f.save('static/uploads/'+f.filename)

            # first we store file in system and then rename that file so that we can sort images according to username

            newimagename = session["user"].split(".")[0] + ".jpg"

            # it deletes the existing file with this name so that rename operation can take place successfully otherwise file will not change
            try:
                os.remove("static/uploads/"+newimagename)
            except:
                pass

            # renaming file name to username.jpg name
            os.rename("static/uploads/"+image, "static/uploads/"+newimagename)

            db = Database()
            flag = db.editProfile(session['user'], name, email, newimagename)

        # if image is not entered in input
        except:
            image = session["image"]
            db = Database()
            flag = db.editProfile(session['user'], name, email, image)

        if flag:
            # if changes are successful
            session["user"] = email
            return redirect("/")
        else:
            # if changes are failed
            return redirect("/")

    # if user calls this page with get method
    return redirect("/")


# Home Redirect Page i.e. Admin Page
@app.route("/home")
def home():
    if(session.get("user")!=None):
        uname = session["user"]
        db = Database()
        data = db.getLoginData(uname)
        session["image"] = data[-1]#we need this session in editprofile method
        session["name"] = data[1] 
        return render_template("home.html", msg=data)

    # if user is not logged in then session['user'] will be None and hence home page will not load and will redirect to login page
    else:
        return redirect("/")


# Logout account
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ***************************Admin Operations Start********************************
# *********************************************************************************


if __name__ == "__main__":
    app.run(debug=True)