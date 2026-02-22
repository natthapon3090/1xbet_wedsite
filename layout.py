from flask import session

def css():
    return "<style>"+open("style.css").read()+"</style>"

def header():

    if "user" in session:

        menu=f"""

<a href='/profile'>โปรไฟล์ ({session['user']})</a>
<a href='/wallet'>กระเป๋าเงิน</a>
<a href='/game'>เกม</a>
<a href='/chat'>แชท</a>
<a href='/logout'>ออก</a>

"""

        if session["user"]=="admin":
            menu+="<a href='/admin'>แอดมิน</a>"

    else:

        menu="""

<a href='/login'>เข้าสู่ระบบ</a>
<a href='/register'>สมัคร</a>

"""

    return f"""

<div class='header'>

🛒 ร้านค้าออนไลน์

<span style='float:right'>

<a href='/'>หน้าแรก</a>
<a href='/shop'>สินค้า</a>

{menu}

</span>

</div>

<div class='container'>
"""
