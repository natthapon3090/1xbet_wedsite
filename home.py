from flask import Blueprint,render_template_string
from layout import css,header

home_bp=Blueprint("home",__name__)

@home_bp.route("/")
def home():

    from database import db
    from flask import session

    con=db()

    user=session.get("user")

    # โค้ด user มีแล้ว
    mycoupon=[]

    if user:

        rows=con.execute(
        "SELECT code FROM user_coupons WHERE username=?",
        (user,)
        ).fetchall()

        for r in rows:
            mycoupon.append(r[0])


    # ดึง coupon จาก admin
    coupons=con.execute(
    "SELECT * FROM coupons"
    ).fetchall()


    # ดึงสินค้าหน้า Home

    recommend=con.execute(
    "SELECT * FROM home_products WHERE type='recommend'"
    ).fetchall()


    sale=con.execute(
    "SELECT * FROM home_products WHERE type='sale'"
    ).fetchall()



    return render_template_string(css()+header()+f"""

<style>

body{{
background: linear-gradient(135deg,#141e30,#243b55);
font-family:Arial;
color:white;
}}

.coupon-box{{
display:flex;
flex-wrap:wrap;
justify-content:center;
}}

.coupon{{
width:220px;
margin:10px;
padding:20px;
border-radius:20px;
background:rgba(255,255,255,0.1);
text-align:center;
box-shadow:0px 0px 20px black;
transition:0.3s;
}}

.coupon:hover{{
transform:scale(1.05);
box-shadow:0px 0px 30px cyan;
}}

.btn{{
padding:8px 15px;
border:none;
border-radius:10px;
background:#00ffcc;
cursor:pointer;
}}

.section-title{{
font-size:32px;
text-align:center;
margin-top:50px;
margin-bottom:20px;
text-shadow:0px 0px 20px gold;
}}

.grid{{
display:flex;
flex-wrap:wrap;
justify-content:center;
gap:20px;
}}

.card{{
width:240px;
background:linear-gradient(145deg,#1c2735,#2a3f57);
border-radius:20px;
padding:15px;
text-align:center;
box-shadow:0px 0px 20px black;
transition:0.4s;
}}

.card:hover{{
transform:translateY(-10px);
box-shadow:0px 0px 30px cyan;
}}

.card img{{
width:100%;
border-radius:15px;
}}

.price{{
color:#00ff88;
font-size:22px;
font-weight:bold;
}}

.oldprice{{
text-decoration:line-through;
color:gray;
}}

.sale{{
background:red;
padding:5px 10px;
border-radius:10px;
display:inline-block;
margin-bottom:10px;
}}

.buy{{
margin-top:10px;
padding:10px 20px;
border-radius:10px;
border:none;
background:gold;
cursor:pointer;
}}

.recommend{{
margin-top:40px;
padding:20px;
border-radius:20px;
background:rgba(0,0,0,0.4);
box-shadow:0px 0px 20px cyan;
}}

</style>


<h2 align=center>🎁 โค้ดส่วนลด</h2>

<div class="coupon-box">

""" + "".join(f"""

<div class="coupon">

ลด {c[2]}

<br>

{c[1]}

<br><br>

<a href="/getcoupon/{c[1]}">

<button class="btn">

เก็บโค้ด

</button>

</a>

</div>

""" for c in coupons if c[1] not in mycoupon)+"""

</div>



<div class="recommend">

<div class="section-title">

🔥 สินค้าแนะนำ

</div>


<div class="grid">

""" + "".join(f"""

<div class="card">

<img src="{x[3]}">

<h3>{x[1]}</h3>

<div class="price">

{x[2]} บาท

</div>

<a href="/buyhome/{x[0]}">

<button class="buy">

ซื้อเลย

</button>

</a>

</div>

""" for x in recommend)+"""

</div>

</div>



<div class="recommend">


<div class="section-title">

💰 สินค้าลดราคา

</div>


<div class="grid">

""" + "".join(f"""

<div class="card">

<div class="sale">

SALE

</div>

<img src="{x[3]}">

<h3>{x[1]}</h3>

<div class="price">

{x[2]} บาท

</div>

<a href="/buyhome/{x[0]}">

<button class="buy">

ซื้อสินค้า

</button>

</a>

</div>

""" for x in sale)+"""

</div>

</div>



</div>

""")
