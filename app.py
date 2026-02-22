from flask import Flask
from database import init

from home import home_bp
from shop import shop_bp
from wallet import wallet_bp
from profile import profile_bp
from admin import admin_bp
from auth import auth_bp
from game import game_bp
from chat import chat_bp

app = Flask(__name__)
app.secret_key = "1234"

init()

app.register_blueprint(home_bp)
app.register_blueprint(shop_bp)
app.register_blueprint(wallet_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(game_bp)
app.register_blueprint(chat_bp)

if __name__ == "__main__":
    app.run(debug=True)
