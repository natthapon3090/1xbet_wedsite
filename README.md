🛒 Flask Online Shop System

ระบบร้านค้าออนไลน์พัฒนาโดยใช้ Python Flask + SQLite สามารถสมัครสมาชิก ซื้อสินค้า เติมเงิน เล่นเกม และแชทได้ พร้อมระบบ Admin จัดการสินค้า

📌 โครงสร้างระบบ

ระบบถูกสร้างด้วย Flask โดยแบ่งเป็นหลายส่วน (Blueprint)

ไฟล์	หน้าที่
app.py	ไฟล์หลักใช้รันระบบ
database.py	จัดการฐานข้อมูล
auth.py	สมัครสมาชิก / Login
home.py	หน้าแรก
shop.py	ร้านค้า
wallet.py	กระเป๋าเงิน
profile.py	โปรไฟล์
game.py	เกมวงล้อ
chat.py	แชท
admin.py	จัดการระบบ
layout.py	Header และ CSS
style.css	ตกแต่งเว็บไซต์
⚙ การทำงานของระบบ
1. app.py (ไฟล์หลัก)

ไฟล์นี้ใช้รันโปรแกรมและเชื่อมทุกหน้าเข้าด้วยกัน 

app

app = Flask(__name__)
app.secret_key = "1234"

ใช้สร้าง Flask Application และ session

init()

ใช้สร้างฐานข้อมูลอัตโนมัติ

app.register_blueprint(home_bp)
app.register_blueprint(shop_bp)

ใช้เชื่อมหน้าต่าง ๆ ของระบบ

app.run(debug=True)

ใช้รันเว็บเซิร์ฟเวอร์

2. database.py (ฐานข้อมูล)

ใช้สร้างฐานข้อมูล SQLite 

database

ตารางที่มี:

users

เก็บข้อมูลผู้ใช้

id
username
password
money
products

เก็บสินค้า

id
name
price
detail
image
coupons

เก็บโค้ดส่วนลด

code
discount
home_products

เก็บสินค้าในหน้าแรก

name
price
image
type
chat

เก็บข้อความแชท

user
msg

ระบบจะสร้าง admin อัตโนมัติ

username = admin
password = 1234
3. auth.py (ระบบ Login)

ใช้สมัครสมาชิกและเข้าสู่ระบบ 

auth

Login
/login

ตรวจสอบ username และ password จากฐานข้อมูล

ถ้าถูกต้อง:

session["user"]=username
Register
/register

เพิ่ม user ลงฐานข้อมูล

INSERT INTO users
Logout
/logout

ลบ session

4. home.py (หน้าแรก)

แสดง:

โค้ดส่วนลด

สินค้าแนะนำ

สินค้าลดราคา

ดึงข้อมูลจากฐานข้อมูล 

home

SELECT * FROM coupons
SELECT * FROM home_products
5. shop.py (ร้านค้า)

แสดงสินค้าทั้งหมด 

shop

SELECT * FROM products

ผู้ใช้สามารถ:

ซื้อสินค้า

ใช้โค้ดส่วนลด

ระบบจะหักเงิน:

UPDATE users SET money=?
6. wallet.py (กระเป๋าเงิน)

ใช้เติมเงิน 

wallet

ผู้ใช้กรอกจำนวนเงิน:

UPDATE users SET money=money+จำนวนเงิน
7. profile.py (โปรไฟล์)

แสดง:

Username

เงิน

คูปอง

ดึงข้อมูล:

SELECT * FROM users

profile

8. game.py (เกมวงล้อ)

ผู้ใช้หมุนวงล้อราคา 10 บาท 

game

สุ่มรางวัล:

random.choice([0,5,10,20,50,100])

อัพเดทเงิน:

UPDATE users SET money=?
9. chat.py (แชท)

ผู้ใช้ส่งข้อความได้ 

chat

INSERT INTO chat

และแสดงข้อความทั้งหมด

SELECT * FROM chat
10. admin.py (Admin Panel)

ใช้จัดการระบบ 

admin

Admin สามารถ:

เพิ่มสินค้า

ลบสินค้า

เพิ่มโค้ด

ลบโค้ด

เพิ่มสินค้า Home

ลบสินค้า Home

เข้าได้ที่:

/admin

Login:

admin
1234
11. layout.py

สร้าง Header และ CSS 

layout

แสดงเมนูตาม user เช่น:

Profile

Wallet

Game

Chat

Admin

▶ วิธีรันโปรแกรม
1. ติดตั้ง Python

ต้องมี Python 3

ตรวจสอบ:

python --version
2. ติดตั้ง Flask
pip install flask
3. เปิดโฟลเดอร์โปรเจค

เช่น

cd shop
4. รันโปรแกรม
python app.py

จะได้

Running on http://127.0.0.1:5000

เปิดเว็บ:

http://127.0.0.1:5000
👤 Username เริ่มต้น

Admin:

username: admin
password: 1234
⭐ ฟีเจอร์ระบบ

สมัครสมาชิก

Login

ร้านค้าออนไลน์

เติมเงิน

ซื้อสินค้า

โค้ดส่วนลด

แชท

เกม

Admin panel
