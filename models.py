"""SQLAlchemy models for Tourney app"""

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
import bcrypt

db = SQLAlchemy()


class User(db.Model):
    """Users"""

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    email = db.Column(
        db.Text,
        nullable=False,
        unique=True
    )

    username = db.Column(
        db.Text,
        nullable=False,
        unique=True
    )

    password = db.Column(
        db.Text,
        nullable=False
    )

    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}>"
    
    @classmethod
    def signup(cls, username, email, password):
        """Sign up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('utf8')

        user = User(
            username=username,
            email=email,
            password=hashed_pwd
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.

        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.

        If this can't find matching user (or if password is wrong), returns
        False.
        """

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False
    
class Team(db.Model):
    """Team"""

    __tablename__ = 'teams'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String,
        nullable=False
    )

class TeamMember(db.Model):
    """TeamMember"""

    ___tablename__ = 'team_members'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False
    )
    
    team_id = db.Column(
        db.Integer,
        db.ForeignKey('teams.id', ondelete='CASCADE'),
        nullable=False
    )

class Location(db.Model):
    """Location"""

    __tablename__ = 'locations'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    location_name = db.Column(
        db.String,
        nullable=False
    )

    address1 = db.Column(
        db.Text
    )

    address2 = db.Column(
        db.Text
    )

class PlayType(db.Model):
    """Type of activity"""

    __tablename__ = 'play_types'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String,
        nullable=False
    )

    thunderdome_type = db.Column(
        db.String,
        nullable=False
    )

class TournamentFormat(db.Model):
    """Type of tournament"""

    __tablename__ = 'tournament_formats'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String,
        nullable=False,
        unique=True
    )

    total_teams = db.Column(
        db.Integer,
        nullable=False
    )

    description = db.Column(
        db.Text
    )

class Event(db.Model):
    """Event"""

    __tablename__ = 'events'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    tournament_name = db.Column(
        db.String,
        nullable=False
    )

    date = db.Column(
        db.Datetime,
        nullable=False,
    )

    location_id = db.Column(
        db.Integer,
        nullable=False
    )

    thunderdome_count = db.Column(
        db.Integer,
        nullable=False
    )

    play_type_id = db.Column(
        db.Integer,
        db.ForeignKey('play_types.id', ondelete="CASCADE"), 
    )

    tournament_format_id = db.Column(
        db.Integer,
        db.ForeignKey('tournament_formats.id', ondelete="CASCADE")
    )

class ArenaDetail(db.Model):
    """Arena Details"""

    __tablename__ = 'arena_details'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    location_id = db.Column(
        db.Interger,
        db.ForeignKey('locations.id', ondelete="CASCADE")
    )

    arena_name = db.Column(
        db.String,
        nullable=False
    )

    capacity = db.Column(
        db.Text
    )

class Game(db.Model):
    """Games"""

    __tablename__ = 'games'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    event_id = db.Column(
        db.Integer,
        db.ForeignKey('events.id', ondelete="CASCADE"),
    )

    team1_id = db.Column(
        db.Integer,
        db.ForeignKey('teams.id', ondelete="CASCADE")
    )

    team2_id = db.Column(
        db.Integer,
        db.ForeignKey('teams.id', ondelete="CASCADE"),
    )

    game_type = db.Column(
        db.Integer,
        db.ForeignKey('tournament_formats.id', ondelete="CASCADE")
    )

    team1_score = db.Column(
        db.Integer
    )

    team2_score = db.Column(
        db.Integer
    )

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)