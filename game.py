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

<style>

body{
background:linear-gradient(135deg,#141e30,#243b55);
color:white;
text-align:center;
font-family:Arial;
}

.wheel{

width:320px;
height:320px;
border-radius:50%;
margin:auto;
margin-top:20px;
border:10px solid gold;

background:
conic-gradient(
red 0deg 60deg,
orange 60deg 120deg,
yellow 120deg 180deg,
green 180deg 240deg,
blue 240deg 300deg,
purple 300deg 360deg
);

transition:3s;

}

.pointer{

font-size:40px;

}

.legend{

margin-top:20px;
width:300px;
margin:auto;
padding:15px;
background:rgba(0,0,0,0.5);
border-radius:15px;
box-shadow:0px 0px 20px cyan;

}

.row{

margin:5px;

}

.colorbox{

display:inline-block;
width:20px;
height:20px;
margin-right:10px;

}

button{

padding:15px 30px;
border:none;
border-radius:10px;
background:gold;
font-size:20px;
cursor:pointer;
margin-top:20px;

}

button:hover{
background:orange;
}

</style>


<h1>🎰 วงล้อเสี่ยงโชค</h1>

<h3>หมุนครั้งละ 10 บาท</h3>


<div class="pointer">
⬇
</div>


<div id="wheel" class="wheel">
</div>


<button onclick="spin()">
หมุนวงล้อ
</button>


<div class="legend">

<h3>🎯 รางวัล</h3>

<div class="row">
<span class="colorbox" style="background:red"></span>
แดง = 0 บาท
</div>

<div class="row">
<span class="colorbox" style="background:orange"></span>
ส้ม = 5 บาท
</div>

<div class="row">
<span class="colorbox" style="background:yellow"></span>
เหลือง = 10 บาท
</div>

<div class="row">
<span class="colorbox" style="background:green"></span>
เขียว = 20 บาท
</div>

<div class="row">
<span class="colorbox" style="background:blue"></span>
น้ำเงิน = 50 บาท
</div>

<div class="row">
<span class="colorbox" style="background:purple"></span>
ม่วง = 100 บาท
</div>

</div>



<script>

function spin(){

let deg=Math.floor(Math.random()*360)+1080

document.getElementById("wheel").style.transform="rotate("+deg+"deg)"

setTimeout(function(){

window.location="/spin"

},3000)

}

</script>

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

<style>

body{{
background:black;
color:white;
text-align:center;
font-family:Arial;
}}

.box{{
margin-top:50px;
padding:40px;
background:rgba(255,255,255,0.1);
border-radius:20px;
width:400px;
margin:auto;
box-shadow:0px 0px 40px gold;
}}

.win{{
font-size:40px;
color:#00ff88;
}}

button{{
padding:12px 25px;
border:none;
border-radius:10px;
background:gold;
font-size:20px;
cursor:pointer;
}}

</style>


<div class="box">

<h2>🎉 ผลการหมุน</h2>

<div class="win">

ได้ {reward} บาท

</div>

<br>

<a href="/game">

<button>

หมุนอีกครั้ง

</button>

</a>

</div>

</div>

""")
