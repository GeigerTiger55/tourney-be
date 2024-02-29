import os
import bcrypt
from dotenv import load_dotenv

from flask import Flask

from models import (
    db,
    connect_db,
    User,
    Team,
    TeamMember,
    Location,
    PlayType,
    TournamentFormat,
    Event,
    ArenaDetail,
    Game
)

load_dotenv()
CURR_USER_KEY = "curr_user"

app = Flask(__name__)

# Get DB_URI from environ variable (useful for production/testing) or,
# if not set there, use development local db.
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"].replace(
    "postgres://", "postgresql://"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]

connect_db(app)