from flask import Blueprint,render_template_string,session,request,redirect
from database import db
from layout import css,header

auth_bp=Blueprint("auth",__name__)

@auth_bp.route("/login",methods=["GET","POST"])
def login():

    if request.method=="POST":

        con=db()

        u=con.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (request.form["u"],request.form["p"])
        ).fetchone()

        if u:
            session["user"]=u[1]
            return redirect("/")

    return render_template_string(css()+header()+"""

<style>

body{

background:linear-gradient(135deg,#141e30,#243b55);
color:white;
font-family:Arial;

}

/* กล่อง login */

.box{

width:350px;
margin:auto;
margin-top:60px;
padding:40px;
border-radius:25px;
background:rgba(255,255,255,0.1);
backdrop-filter:blur(15px);
box-shadow:0px 0px 40px black;
text-align:center;
animation:fade 1s;

}

@keyframes fade{

from{opacity:0;transform:translateY(40px)}
to{opacity:1}

}

.title{

font-size:32px;
margin-bottom:20px;
text-shadow:0px 0px 20px gold;

}

input{

width:90%;
padding:12px;
margin:10px;
border-radius:10px;
border:none;
font-size:16px;

}

button{

padding:12px 25px;
border:none;
border-radius:12px;
background:gold;
cursor:pointer;
font-size:18px;
margin-top:10px;

}

button:hover{

background:orange;
transform:scale(1.05);

}

.link{

margin-top:15px;
display:block;
color:#00ffcc;
font-size:16px;

}

</style>



<div class="box">

<div class="title">

🔐 LOGIN VIP

</div>


<form method=post>

<input name=u placeholder="Username">

<input name=p placeholder="Password" type=password>

<button>

Login

</button>

</form>


<a class="link" href="/register">

สมัครสมาชิก

</a>

</div>


</div>

""")



@auth_bp.route("/register",methods=["GET","POST"])
def register():

    if request.method=="POST":

        con=db()

        con.execute(
        "INSERT INTO users(username,password,money) VALUES(?,?,0)",
        (request.form["u"],request.form["p"])
        )

        con.commit()

        return redirect("/login")

    return render_template_string(css()+header()+"""

<style>

body{

background:linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
font-family:Arial;

}

.box{

width:350px;
margin:auto;
margin-top:60px;
padding:40px;
border-radius:25px;
background:rgba(255,255,255,0.1);
backdrop-filter:blur(15px);
box-shadow:0px 0px 40px black;
text-align:center;
animation:fade 1s;

}

@keyframes fade{

from{opacity:0;transform:translateY(40px)}
to{opacity:1}

}

.title{

font-size:32px;
margin-bottom:20px;
text-shadow:0px 0px cyan;

}

input{

width:90%;
padding:12px;
margin:10px;
border-radius:10px;
border:none;
font-size:16px;

}

button{

padding:12px 25px;
border:none;
border-radius:12px;
background:#00ffcc;
cursor:pointer;
font-size:18px;
margin-top:10px;

}

button:hover{

background:#00ccaa;
transform:scale(1.05);

}

.link{

margin-top:15px;
display:block;
color:gold;
font-size:16px;

}

</style>



<div class="box">

<div class="title">

👑 REGISTER VIP

</div>


<form method=post>

<input name=u placeholder="Username">

<input name=p placeholder="Password" type=password>

<button>

Register

</button>

</form>


<a class="link" href="/login">

กลับไป Login

</a>

</div>


</div>

""")



@auth_bp.route("/logout")
def logout():

    session.clear()

    return redirect("/")
