from flask import Blueprint,render_template_string,session,request,redirect
from database import db
from layout import css,header

chat_bp=Blueprint("chat",__name__)

@chat_bp.route("/chat",methods=["GET","POST"])
def chat():

    if "user" not in session:
        return redirect("/login")

    con=db()

    if request.method=="POST":

        msg=request.form.get("msg","")

        if msg!="":

            con.execute(
            "INSERT INTO chat(user,msg) VALUES(?,?)",
            (session["user"],msg)
            )

            con.commit()

            return redirect("/chat")

    c=con.execute("SELECT * FROM chat").fetchall()

    html=""

    for x in c:
        html+=f"{x[1]} : {x[2]}<br>"

    return render_template_string(css()+header()+f"""

<h2>แชท</h2>

{html}

<form method=post>

<input name=msg>

<button>ส่ง</button>

</form>

</div>

""")
