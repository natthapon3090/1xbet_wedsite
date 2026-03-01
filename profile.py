
from flask import Blueprint,render_template_string,session,redirect,request
from database import db
from layout import css,header

profile_bp=Blueprint("profile",__name__)

@profile_bp.route("/profile")
def profile():

    if "user" not in session:
        return redirect("/login")

    con=db()

    u=con.execute(
    "SELECT * FROM users WHERE username=?",
    (session["user"],)
    ).fetchone()


    # โค้ดที่ user มี
    coupons=con.execute(
    "SELECT code FROM user_coupons WHERE username=?",
    (session["user"],)
    ).fetchall()


    return render_template_string(css()+header()+f"""

<style>

body {{
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
font-family: Arial;
}}

.profile-box{{
width:500px;
margin:auto;
margin-top:40px;
padding:30px;
border-radius:20px;
background:rgba(255,255,255,0.1);
backdrop-filter: blur(10px);
box-shadow:0px 0px 30px black;
text-align:center;
animation: fade 1s;
}}

@keyframes fade{{
from{{opacity:0;transform:translateY(30px)}}
to{{opacity:1;transform:translateY(0)}}
}}

.avatar{{
width:120px;
height:120px;
border-radius:50%;
background:white;
margin:auto;
margin-bottom:15px;
background-image:url('https://cdn-icons-png.flaticon.com/512/149/149071.png');
background-size:cover;
border:4px solid gold;
}}

.name{{
font-size:28px;
font-weight:bold;
margin-bottom:10px;
}}

.money{{
font-size:26px;
color:#00ff88;
margin:20px;
}}

.card{{
background:rgba(0,0,0,0.4);
padding:15px;
margin:10px;
border-radius:15px;
}}

.badge{{
background:gold;
color:black;
padding:5px 10px;
border-radius:10px;
font-size:14px;
}}

.btn{{
padding:10px 20px;
border-radius:10px;
border:none;
background:#00ffcc;
margin:10px;
cursor:pointer;
font-size:16px;
}}

.btn:hover{{
background:#00ccaa;
transform:scale(1.1);
}}

.coupon-box{{
margin-top:20px;
}}

.coupon{{
background:black;
padding:10px;
margin:8px;
border-radius:10px;
box-shadow:0px 0px 10px gold;
}}

</style>


<div class="profile-box">

<div class="avatar"></div>

<div class="name">{u[1]}</div>

<div class="badge">
VIP USER
</div>

<div class="money">
💰 เงิน {u[3]} บาท
</div>


<div class="card">
📊 Level : 5
</div>

<div class="card">
⭐ Experience : 1200 XP
</div>

<div class="card">
🔥 Status : Online
</div>


<a href="/editprofile">
<button class="btn">
Edit Profile
</button>
</a>


<a href="/logout">
<button class="btn">
Logout
</button>
</a>


<div class="card">

<h3>🎁 โค้ดของฉัน</h3>

<div class="coupon-box">

{ "".join(f"<div class='coupon'>{c[0]}</div>" for c in coupons) if coupons else "ยังไม่มีโค้ด"}

</div>

</div>


</div>

</div>

""")


# ⭐ Edit Profile

@profile_bp.route("/editprofile",methods=["GET","POST"])
def editprofile():

    if "user" not in session:
        return redirect("/login")

    con=db()

    if request.method=="POST":

        con.execute(
        "UPDATE users SET password=? WHERE username=?",
        (
        request.form["password"],
        session["user"]
        )
        )

        con.commit()

        return redirect("/profile")


    return render_template_string(css()+header()+"""

<h2>แก้ไขโปรไฟล์</h2>

<form method=post>

รหัสผ่านใหม่<br>

<input name=password>

<br><br>

<button>

บันทึก

</button>

</form>

</div>

""")


# ⭐ Logout

@profile_bp.route("/logout")
def logout():

    session.clear()

    return redirect("/")
