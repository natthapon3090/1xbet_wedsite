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

<form method=post>

<input name=u>
<input name=p>

<button>login</button>

</form>

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

<form method=post>

<input name=u>
<input name=p>

<button>register</button>

</form>

</div>

""")

@auth_bp.route("/logout")
def logout():

    session.clear()

    return redirect("/")
