from django.shortcuts import render
import sqlite3 as sql
conn = sql.connect('db.sqlite3')

# Create your views here.
def ulogin(request):
    res = ""
    if request.method=="POST":
        conn = sql.connect('db.sqlite3')
        cur = conn.cursor()
        met=request.POST
        fid = met['fid']
        pas = met['pas']
        inp = (fid, pas)
        cur.execute('''SELECT * from farmer where FID=? and pas=?''', inp)
        if len(cur.fetchall()) == 1:
            return render(request, 'chatbot.html')
        else:
            res = "Unable to Signin Password or Admin Id entered is incorrect"
    return render(request,'farmer.html')
def admin(request):
    return render(request,'admin.html')
def home(request):
    return render(request,'home.html')
def farmer(request):
    res = ""
    if request.method == "POST":
        conn = sql.connect('db.sqlite3')
        cur = conn.cursor()
        met = request.POST
        fid=met['fid']
        fname=met['fname']
        pas=met['pas']
        phone=met['phone']
        cur.execute('insert into farmer values(?,?,?,?)',(fid,fname,pas,phone))
        print(len(cur.fetchall()))
        conn.commit()
        conn.close()
        if len(cur.fetchall()) == 1:
            return render(request, 'chatbot.html')
        else:
            res = "Unable to Signin Password or farmer Id entered is incorrect"
            return render(request, 'farmer.html', {"res": res})

    return render(request,'farmer.html')
def signin(request):
    res=""
    conn = sql.connect('db.sqlite3')
    cur = conn.cursor()
    if request.method=="POST":
        met=request.POST
        aid=met['aid']
        pas=met['pas']
        inp=(aid,pas)
        cur.execute('''SELECT * from admin where AID=? and pas=?''',inp)
        if len(cur.fetchall())==1:
            return render(request,'chatbot.html')
        else:
            res = "Unable to Signin Password or Admin Id entered is incorrect"
    return render(request,'admin.html',{"res":res})
def signup(request):
    res = ""
    conn = sql.connect('db.sqlite3')
    try:
        cur=conn.cursor()
        print(True)
    except Exception as ex:
        print(False)
    if request.method == "POST":
        met = request.POST
        aid = met['aid']
        email=met['email']
        pas = met['pas']
        inp = (aid,email,pas)
        cur.execute('insert into admin values(?,?,?)', inp)
        print(len(cur.fetchall()))
        conn.commit()
        conn.close()
        if len(cur.fetchall()) == 1:
            return render(request, 'chatbot.html')
        else:
            res = "Unable to Signin Password or Admin Id entered is incorrect"
            return render(request, 'admin.html', {"res": res})

    return render(request,'admin.html')