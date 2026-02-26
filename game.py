from flask import Blueprint,render_template_string,session,redirect
from database import db
from layout import css,header
import random

game_bp=Blueprint("game",__name__)

@game_bp.route("/game")
def game():

    if "user" not in session:
        return redirect("/login")

    return render_template_string(css()+header()+"""
<h2>หมุนวงล้อ 10 บาท</h2>
<a href='/spin'>
<button>หมุน</button>
</a>
</div>
""")

@game_bp.route("/spin")
def spin():

    con=db()

    user=con.execute(
    "SELECT * FROM users WHERE username=?",
    (session["user"],)
    ).fetchone()

    if user[3]<10:
        return redirect("/wallet")

    reward=random.choice([0,5,10,20,50,100])

    newmoney=user[3]-10+reward

    con.execute(
    "UPDATE users SET money=? WHERE username=?",
    (newmoney,session["user"])
    )

    con.commit()

    return render_template_string(css()+header()+f"""

<h2>ได้ {reward} บาท</h2>

<a href='/game'>
<button>หมุนอีกครั้ง</button>
</a>

</div>

""")
