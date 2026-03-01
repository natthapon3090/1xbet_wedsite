import sqlite3

def db():
    return sqlite3.connect("database.db")

def init():

    con=db()


    # USERS (ของเดิม)
    con.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    money INTEGER)
    """)



    # PRODUCTS (ของเดิม)
    con.execute("""
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER,
    detail TEXT,
    image TEXT)
    """)



    # CHAT (ของเดิม)
    con.execute("""
    CREATE TABLE IF NOT EXISTS chat(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    msg TEXT)
    """)



    # COUPONS (ของเดิม)
    con.execute("""
    CREATE TABLE IF NOT EXISTS coupons(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT,
    discount INTEGER)
    """)



    # USER COUPONS (ของเดิม)
    con.execute("""
    CREATE TABLE IF NOT EXISTS user_coupons(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    code TEXT)
    """)



    # ⭐ NEW — สินค้าหน้า Home (Admin คุมได้)

    con.execute("""
    CREATE TABLE IF NOT EXISTS home_products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER,
    image TEXT,
    type TEXT)
    """)


    con.commit()



    # ADMIN (ของเดิม)

    admin=con.execute(
    "SELECT * FROM users WHERE username='admin'"
    ).fetchone()

    if not admin:

        con.execute(
        "INSERT INTO users(username,password,money) VALUES('admin','1234',1000)"
        )

        con.commit()



    # COUPON เริ่มต้น (ของเดิม)

    default=[

    ("SAVE10",10),
    ("SALE50",50),
    ("VIP20",20),
    ("FREE",0)

    ]


    for c in default:

        exist=con.execute(
        "SELECT * FROM coupons WHERE code=?",
        (c[0],)
        ).fetchone()

        if not exist:

            con.execute(
            "INSERT INTO coupons(code,discount) VALUES(?,?)",
            c
            )


    # ⭐ NEW เพิ่มสินค้า Home เริ่มต้น

    default_home=[

    ("หูฟัง Gaming Pro",590,
    "https://via.placeholder.com/200",
    "recommend"),

    ("เมาส์ RGB Pro",350,
    "https://via.placeholder.com/200",
    "recommend"),

    ("คีย์บอร์ด Mechanical",890,
    "https://via.placeholder.com/200",
    "recommend"),

    ("เสื้อ Gamer",299,
    "https://via.placeholder.com/200",
    "sale")

    ]


    for p in default_home:

        exist=con.execute(
        "SELECT * FROM home_products WHERE name=?",
        (p[0],)
        ).fetchone()

        if not exist:

            con.execute(
            "INSERT INTO home_products(name,price,image,type) VALUES(?,?,?,?)",
            p
            )


    con.commit()
