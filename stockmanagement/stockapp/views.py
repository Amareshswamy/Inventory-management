from django.shortcuts import render
import mysql.connector
from django.core.files.storage import FileSystemStorage
# Create your views here.

mydb=mysql.connector.connect (
host="localhost",
user="root",
password="root",
database="stock",
charset="utf8"
)

mycur = mydb.cursor()

def login(request):
    return render(request,'login.html')
    
def panal(request):
    return render(request,'panal.html')

def verify(request):
    if request.method=="POST":
        user=request.POST.get("username")
        psw=request.POST.get("password")
        sql="select * from login where username='"+user+"' and password='"+psw+"'"
        mycur.execute(sql);
        if len(mycur.fetchall())>0:
            return render(request,"panal.html")
        else:
            return render(request,"login.html",{"status":"invalid username or password"})    
            
def add(request):
    return render(request,'add.html')            
    
def addproduct(request):
            if request.method=="POST" and request.FILES['upload']:
                p_name = request.POST.get("pname")
                p_id = request.POST.get("pid")
                hsn_code = request.POST.get("hsn")
                qty = request.POST.get("qty")
                price = request.POST.get("price")
                date = request.POST.get("date")
                
                sql= "insert into import(p_name,p_id,hsn_code,qty,price,date) values(%s,%s,%s,%s,%s,%s)"
                val=(p_name,p_id,hsn_code,qty,price,date)
                mycur.execute(sql,val)
                mydb.commit()
                
                
                upload = request.FILES['upload']
                fss = FileSystemStorage()
                file = fss.save(upload.name, upload)
                print(file);
                file_url = fss.url(file)
                return render(request, 'panal.html', {'file_url': file_url})
               
def sales(request):
    return render(request,'sales.html') 
    
def cart(request):
    return render(request,'cart.html')  
    
def salesproduct(request):
            if request.method=="POST":
                c_name = request.POST.get("cname")
                p_id = request.POST.get("pid")
                qtys = request.POST.get("qty")
                price = request.POST.get("price")
                gst = request.POST.get("gst")               
                sql= "insert into sales(c_name,p_id,qty,price,gst) values(%s,%s,%s,%s,%s)"
                val=(c_name,p_id,qtys,price,gst)
                mycur.execute(sql,val)
                mydb.commit()
                
                p_id = request.POST.get("pid") 
                sql="select * from sales where p_id='"+p_id+"'"
                mycur.execute(sql)
                result=mycur.fetchall()
                
                p_id = request.POST.get("pid")                
                sql= "update import set qty=(qty-'"+qtys+"') where p_id ='"+p_id+"'"
                mycur.execute(sql)
                mydb.commit()
                return render(request,'cart.html',{"res":result})


def order(request):
    return render(request,'order.html')  
           


def viewstock(request):
    sql="select * from import"
    mycur.execute(sql)
    result=mycur.fetchall()
    return render(request,"viewstock.html",{"res":result})	

def report(request):
    return render(request,'report.html')    
            
def report(request):
    sql="select * from sales"
    mycur.execute(sql)
    result=mycur.fetchall()
    return render(request,"report.html",{"res":result})            