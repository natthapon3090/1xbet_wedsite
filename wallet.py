from flask import Blueprint,render_template_string,session,request,redirect
from database import db
from layout import css,header

wallet_bp=Blueprint("wallet",__name__)

@wallet_bp.route("/wallet",methods=["GET","POST"])
def wallet():

    if "user" not in session:
        return redirect("/login")

    con=db()

    if request.method=="POST":

        # ⭐ แก้ Error เติมเงิน
        try:
            m=int(request.form.get("money",0))
        except:
            m=0

        u=con.execute(
        "SELECT * FROM users WHERE username=?",
        (session["user"],)
        ).fetchone()

        con.execute(
        "UPDATE users SET money=? WHERE username=?",
        (u[3]+m,session["user"])
        )

        con.commit()

    u=con.execute(
    "SELECT * FROM users WHERE username=?",
    (session["user"],)
    ).fetchone()


    html=f"""

<style>

body{{
background:linear-gradient(135deg,#141e30,#243b55);
font-family:Arial;
color:white;
}}

.walletbox{{

width:450px;
margin:auto;
margin-top:50px;
padding:40px;
border-radius:20px;
background:rgba(255,255,255,0.1);
text-align:center;
box-shadow:0px 0px 30px black;

}}

.money{{

font-size:40px;
color:#00ff88;
margin:20px;

}}

.title{{

font-size:30px;
margin-bottom:20px;

}}

input{{

width:80%;
padding:12px;
margin:10px;
border-radius:10px;
border:none;
text-align:center;
font-size:18px;

}}

button{{

padding:10px 25px;
border:none;
border-radius:10px;
background:gold;
font-size:18px;
cursor:pointer;

}}

button:hover{{
background:orange;
}}

.quick button{{

background:#00ffcc;
margin:5px;

}}

</style>


<div class="walletbox">

<div class="title">
💰 WALLET
</div>


<div class="money">
{u[3]} บาท
</div>


<form method=post>

<input name=money placeholder="จำนวนเงิน">

<br>

<button>
เติมเงิน
</button>

</form>



<h3>เติมเร็ว</h3>

<div class="quick">

<button onclick="add(10)">10</button>

<button onclick="add(50)">50</button>

<button onclick="add(100)">100</button>

<button onclick="add(500)">500</button>

<button onclick="add(1000)">1000</button>

</div>


</div>


<script>

function add(m){{
document.querySelector("input[name=money]").value=m
}}

</script>


</div>

"""

    return render_template_string(css()+header()+html)
