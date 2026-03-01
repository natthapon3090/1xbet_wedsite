from flask import Blueprint,render_template_string,session,redirect
from database import db
from layout import css,header

shop_bp=Blueprint("shop",__name__)


# ⭐ หน้า Shop ใส่รูปได้

@shop_bp.route("/shop")
def shop():

    con=db()

    p=con.execute(
    "SELECT * FROM products"
    ).fetchall()

    html="""

<style>

.grid{
display:flex;
flex-wrap:wrap;
justify-content:center;
gap:20px;
}

.card{
width:250px;
padding:15px;
background:black;
border-radius:15px;
text-align:center;
box-shadow:0px 0px 20px gray;
}

.card img{
width:100%;
height:200px;
object-fit:cover;
border-radius:10px;
}

.price{
color:#00ff88;
font-size:22px;
}

.buy{
margin-top:10px;
padding:10px 20px;
border:none;
border-radius:10px;
background:gold;
cursor:pointer;
}

.buy:hover{
background:orange;
}

</style>


<h2 align=center>🛒 สินค้าทั้งหมด</h2>

<div class="grid">

"""

    for x in p:

        html+=f"""

<div class="card">

<img src="{x[4]}">

<h3>{x[1]}</h3>

<div class="price">
{x[2]} บาท
</div>

<a href="/buy/{x[0]}">
<button class="buy">
ซื้อสินค้า
</button>
</a>

</div>

"""

    html+="</div>"

    return render_template_string(css()+header()+html+"</div>")



@shop_bp.route("/getcoupon/<code>")
def getcoupon(code):

    if "user" not in session:
        return redirect("/login")

    con=db()

    exist=con.execute(
    "SELECT * FROM user_coupons WHERE username=? AND code=?",
    (session["user"],code)
    ).fetchone()

    if not exist:

        con.execute(
        "INSERT INTO user_coupons(username,code) VALUES(?,?)",
        (session["user"],code)
        )

        con.commit()

    return render_template_string(css()+header()+"""

<h2>เก็บโค้ดสำเร็จ</h2>

<a href="/">
<button>กลับหน้าแรก</button>
</a>

</div>

""")


# ⭐⭐⭐ ซื้อสินค้า (อลังการ)

@shop_bp.route("/buy/<id>")
def buy(id):

    if "user" not in session:
        return redirect("/login")

    con=db()

    product=con.execute(
    "SELECT * FROM products WHERE id=?",
    (id,)
    ).fetchone()

    user=con.execute(
    "SELECT * FROM users WHERE username=?",
    (session["user"],)
    ).fetchone()

    discount=0

    coupon=con.execute(
    "SELECT * FROM user_coupons WHERE username=? LIMIT 1",
    (session["user"],)
    ).fetchone()

    if coupon:

        c=con.execute(
        "SELECT * FROM coupons WHERE code=?",
        (coupon[2],)
        ).fetchone()

        if c:
            discount=c[2]

    price=product[2]-discount

    if price<0:
        price=0

    if user[3] < price:
        return redirect("/wallet")

    newmoney=user[3]-price

    con.execute(
    "UPDATE users SET money=? WHERE username=?",
    (newmoney,session["user"])
    )

    con.commit()


    return render_template_string(css()+header()+f"""

<style>

body{{
background:linear-gradient(135deg,#141e30,#243b55);
color:white;
font-family:Arial;
text-align:center;
}}

.box{{
margin:auto;
margin-top:60px;
width:450px;
padding:40px;
border-radius:25px;
background:rgba(255,255,255,0.1);
backdrop-filter:blur(10px);
box-shadow:0px 0px 40px gold;
animation:fade 1s;
}}

@keyframes fade{{
from{{opacity:0;transform:translateY(30px)}}
to{{opacity:1}}
}}

.title{{
font-size:40px;
color:#00ff88;
margin-bottom:20px;
text-shadow:0px 0px 20px #00ff88;
}}

.detail{{
font-size:20px;
margin:10px;
}}

.money{{
font-size:25px;
color:gold;
margin-top:20px;
}}

button{{
padding:12px 25px;
border:none;
border-radius:10px;
background:gold;
font-size:18px;
cursor:pointer;
}}

button:hover{{
background:orange;
transform:scale(1.1);
}}

</style>


<div class="box">

<div class="title">
✅ ซื้อสำเร็จ
</div>

<div class="detail">
สินค้า : {product[1]}
</div>

<div class="detail">
ส่วนลด : {discount} บาท
</div>

<div class="detail">
จ่ายจริง : {price} บาท
</div>

<div class="money">
💰 เงินเหลือ {newmoney} บาท
</div>

<br>

<a href="/shop">
<button>
กลับร้านค้า
</button>
</a>

</div>

</div>

""")


# ⭐ ซื้อจากหน้า Home (อลังการ)

@shop_bp.route("/buyhome/<id>")
def buyhome(id):

    if "user" not in session:
        return redirect("/login")

    con=db()

    product=con.execute(
    "SELECT * FROM home_products WHERE id=?",
    (id,)
    ).fetchone()

    user=con.execute(
    "SELECT * FROM users WHERE username=?",
    (session["user"],)
    ).fetchone()

    price=product[2]

    if user[3] < price:
        return redirect("/wallet")

    newmoney=user[3]-price

    con.execute(
    "UPDATE users SET money=? WHERE username=?",
    (newmoney,session["user"])
    )

    con.commit()


    return render_template_string(css()+header()+f"""

<style>

.box{{
margin:auto;
margin-top:60px;
width:450px;
padding:40px;
border-radius:25px;
background:rgba(255,255,255,0.1);
text-align:center;
box-shadow:0px 0px 40px cyan;
}}

.title{{
font-size:35px;
color:#00ff88;
}}

.money{{
font-size:25px;
margin-top:20px;
color:gold;
}}

button{{
padding:10px 25px;
border:none;
border-radius:10px;
background:gold;
font-size:18px;
cursor:pointer;
}}

</style>

<div class="box">

<div class="title">
🎉 ซื้อสำเร็จ
</div>

<br>

สินค้า {product[1]}

<br><br>

ราคา {price}

<div class="money">
เงินเหลือ {newmoney}
</div>

<br>

<a href="/">
<button>
กลับหน้าแรก
</button>
</a>

</div>

</div>

""")
