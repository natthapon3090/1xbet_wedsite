from flask import Blueprint,render_template_string,session,request,redirect
from database import db
from layout import css,header

admin_bp=Blueprint("admin",__name__)

@admin_bp.route("/admin",methods=["GET","POST"])
def admin():

    if session.get("user")!="admin":
        return redirect("/")

    con=db()

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

    html="<h2>แอดมิน</h2>"

    html+="""<form method=post>
ชื่อ<input name=name><br>
ราคา<input name=price><br>
รายละเอียด<input name=detail><br>
รูป<input name=image><br>
<button>เพิ่มสินค้า</button>
</form><br>"""

    for x in p:
        html+=f"{x[1]} {x[2]} บาท<br>"

    return render_template_string(css()+header()+html+"</div>")
