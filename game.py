
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
