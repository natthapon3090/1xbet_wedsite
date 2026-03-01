from flask import Blueprint,render_template_string,session,request,redirect
from database import db
from layout import css,header

admin_bp=Blueprint("admin",__name__)

@admin_bp.route("/admin",methods=["GET","POST"])
def admin():

    if session.get("user")!="admin":
        return redirect("/")

    con=db()

    # เพิ่มสินค้า (ของเดิม)
    if request.method=="POST":

        con.execute(
        "INSERT INTO products(name,price,detail,image) VALUES(?,?,?,?)",
        (request.form["name"],
         request.form["price"],
         request.form["detail"],
         request.form["image"])
        )

        con.commit()

        return redirect("/admin")


    p=con.execute("SELECT * FROM products").fetchall()

    coupons=con.execute(
    "SELECT * FROM coupons"
    ).fetchall()

    homeproducts=con.execute(
    "SELECT * FROM home_products"
    ).fetchall()



    html="""


<h1>⚙ ADMIN PANEL</h1>

<h2>เพิ่มสินค้า</h2>

<form method=post>

ชื่อสินค้า<br>
<input name=name><br>

ราคา<br>
<input name=price><br>

รายละเอียด<br>
<input name=detail><br>

รูป<br>
<input name=image><br>

<br>

<button>เพิ่มสินค้า</button>

</form>


<hr>

<h2>เพิ่มโค้ดส่วนลด</h2>

<form method=post action="/addcoupon">

Code<br>
<input name=code><br>

Discount<br>
<input name=discount><br>

<br>

<button>เพิ่มโค้ด</button>

</form>

<hr>

<h2>สินค้า</h2>

"""

    # ⭐ แก้ตรงนี้ → เพิ่มปุ่มลบสินค้า

    for x in p:

        html+=f"""

{x[1]} - {x[2]} บาท

<a href="/deleteproduct/{x[0]}">

<button>

ลบสินค้า

</button>

</a>

<br><br>

"""


    html+="""


<hr>

<h2>🎁 โค้ดทั้งหมด</h2>

"""


    for c in coupons:

        html+=f"""

Code {c[1]}

ลด {c[2]} บาท

<a href='/deletecoupon/{c[0]}'>

<button>

ลบโค้ด

</button>

</a>

<br><br>

"""


    html+="""


<hr>

<h2>🔥 สินค้าหน้า Home</h2>

<form method=post action="/addhome">

ชื่อสินค้า<br>
<input name=name><br>

ราคา<br>
<input name=price><br>

รูป<br>
<input name=image><br>

ประเภท<br>

<select name=type>

<option value="recommend">
สินค้าแนะนำ
</option>

<option value="sale">
สินค้าลดราคา
</option>

</select>

<br><br>

<button>

เพิ่มสินค้า Home

</button>

</form>

<br>

"""


    for h in homeproducts:

        html+=f"""

{h[1]} - {h[2]} บาท ({h[4]})

<a href="/deletehome/{h[0]}">

<button>

ลบ

</button>

</a>

<br><br>

"""


    return render_template_string(css()+header()+html+"</div>")



# เพิ่มโค้ด
@admin_bp.route("/addcoupon",methods=["POST"])
def addcoupon():

    if session.get("user")!="admin":
        return redirect("/")

    con=db()

    con.execute(
    "INSERT INTO coupons(code,discount) VALUES(?,?)",
    (request.form["code"],
     request.form["discount"])
    )

    con.commit()

    return redirect("/admin")



# ลบโค้ด
@admin_bp.route("/deletecoupon/<id>")
def deletecoupon(id):

    if session.get("user")!="admin":
        return redirect("/")

    con=db()

    con.execute(
    "DELETE FROM coupons WHERE id=?",
    (id,)
    )

    con.commit()

    return redirect("/admin")



# เพิ่มสินค้า Home
@admin_bp.route("/addhome",methods=["POST"])
def addhome():

    if session.get("user")!="admin":
        return redirect("/")

    con=db()

    con.execute(
    "INSERT INTO home_products(name,price,image,type) VALUES(?,?,?,?)",
    (
    request.form["name"],
    request.form["price"],
    request.form["image"],
    request.form["type"]
    )
    )

    con.commit()

    return redirect("/admin")



# ลบสินค้า Home
@admin_bp.route("/deletehome/<id>")
def deletehome(id):

    if session.get("user")!="admin":
        return redirect("/")

    con=db()

    con.execute(
    "DELETE FROM home_products WHERE id=?",
    (id,)
    )

    con.commit()

    return redirect("/admin")



# ⭐ ลบสินค้า Shop
@admin_bp.route("/deleteproduct/<id>")
def deleteproduct(id):

    if session.get("user")!="admin":
        return redirect("/")

    con=db()

    con.execute(
    "DELETE FROM products WHERE id=?",
    (id,)
    )

    con.commit()

    return redirect("/admin")
