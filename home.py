from flask import Blueprint,render_template_string
from layout import css,header

home_bp=Blueprint("home",__name__)

@home_bp.route("/")
def home():

    return render_template_string(css()+header()+"""

<h2>หน้าแรก</h2>

ยินดีต้อนรับร้านค้าออนไลน์

</div>

""")
