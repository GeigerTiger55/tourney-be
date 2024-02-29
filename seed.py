from app import app

from datetime import datetime

from models import (
    db,
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

with app.app_context():
    db.drop_all()
    db.create_all()

##################  users

user1 = User(
    email='user1@ilovesports.com',
    username='ilovesports',
    password='ilovesportspassword'
)

user2 = User(
    email='user2@sportsball.com',
    username='sportsball',
    password='sportsballpassword'
)

user3 = User(
    email='user3@sportsyay.com',
    username='sportsyay',
    password='sportsyaypassword'
)

user4 = User(
    email='user4@sportsisgood.com',
    username='sportsisgood',
    password='sportsisgoodpassword'
)

user5 = User(
    email='user5@iplaysports.com',
    username='iplaysports',
    password='iplaysportspassword'
)

user6 = User(
    email='user6@sportsarelife.com',
    username='sportsarelife',
    password='sportsarelifepassword'
)

user7 = User(
    email='user7@games.com',
    username='games',
    password='gamespassword'
)

user8 = User(
    email='user8@sports.com',
    username='sports',
    password='sports'
)

user9 = User(
    email='letsplaygames.com',
    username='letsplaygames',
    password='letsplaygamespassword'
)

################# teams

Team1 = Team(
    name="Red Monkeys"
)

Team2 = Team(
    name="Green Monkeys"
)

Team3 = Team(
    name="Blue Barracudas"
)


############## team members

tm1 = TeamMember(
    user_id=1,
    team_id=1,
    team_owner=True,
    team_admin_access=True,
)

tm2 = TeamMember(
    user_id=2,
    team_id=1,
    team_owner=False,
    team_admin_access=True,
)

tm3 = TeamMember(
    user_id=3,
    team_id=1,
    team_owner=False,
    team_admin_access=False,
)

tm4 = TeamMember(
    user_id=4,
    team_id=2,
    team_owner=True,
    team_admin_access=True,
)

tm5 = TeamMember(
    user_id=5,
    team_id=2,
    team_owner=False,
    team_admin_access=False,
)

tm6 = TeamMember(
    user_id=6,
    team_id=2,
    team_owner=False,
    team_admin_access=False,
)

tm7 = TeamMember(
    user_id=7,
    team_id=3,
    team_owner=True,
    team_admin_access=True,
)

tm8 = TeamMember(
    user_id=8,
    team_id=3,
    team_owner=False,
    team_admin_access=False,
)

tm9 = TeamMember(
    user_id=9,
    team_id=3,
    team_owner=False,
    team_admin_access=False,
)

################### locations

loc1 = Location(
    location_name="The Shire",
    address1="Middle Earth"
)

loc2 = Location(
    location_name="Mount Doom",
    address1="Mordor",
    address2="Middle Earth"
)


################## PlayType

pt1 = PlayType(
    name="Volleyball",
    thunderdome_type="turf"
)

pt2 = PlayType(
    name="Volleyball",
    thunderdome_type="sand"
)

pt3 = PlayType(
    name="Volleyball",
    thunderdome_type="court"
)


############### tournament formats

tf1 = TournamentFormat(
    name="Round Robin",
    total_teams=3,
    description="Team numbe not an issue. Each team plays every team. Elimination based on points"

)

tf2 = TournamentFormat(
    name="Heads up",
    total_teams=2,
    description=""
)

######################### Events

e1 = Event(
    tournament_name="Shire Showdown",
    date=datetime(2025,3,2,10,30,00,00),
    location_id=1,
    thunderdome_count=2,
    play_type_id=1,
    tournament_format_id=1
)

e2 = Event(
    tournament_name="Mt.Doom unfriendly",
    date=datetime(2025,6,6,12,00,00,00),
    location_id=2,
    thunderdome_count=1,
    play_type_id=2,
    tournament_format_id=2
)

e3 = Event(
    tournament_name="Sauron Slam",
    date=datetime(2026,7,7,12,00,00,00),
    location_id=2,
    thunderdome_count=1,
    play_type_id=3,
    tournament_format_id=2
)


##################### Arena details

ad1 = ArenaDetail(
    location_id=1,
    arena_name="Bag End",
    capacity=100
)

ad2 = ArenaDetail(
    location_id=1,
    arena_name="Green Dragon",
    capacity=75,
)

ad3 = ArenaDetail(
    location_id=2,
    arena_name="Mt. Doom",
    capacity=10
)


################## Game

game1 = Game(
    event_id=1,
    arena_id=1,
    home_team_id=1,
    away_team_id=2,
    tournament_type=1,
    home_team_score=2,
    away_team_score=3
)

game2 = Game(
    event_id=1,
    arena_id=2,
    home_team_id=1,
    away_team_id=3,
    tournament_type=1,
    home_team_score=3,
    away_team_score=0
)

game3 = Game(
    event_id=1,
    arena_id=1,
    home_team_id=2,
    away_team_id=3,
    tournament_type=1,
    home_team_score=1,
    away_team_score=3
)

game4 = Game(
    event_id=2,
    arena_id=3,
    home_team_id=1,
    away_team_id=2,
    tournament_type=2,
    home_team_score=1,
    away_team_score=1
)

game5 = Game(
    event_id=2,
    arena_id=3,
    home_team_id=1,
    away_team_id=2,
    tournament_type=2,
    home_team_score=None,
    away_team_score=None
)

with app.app_context():
    db.session.add_all([user1, user2, user3, user4, user5, user6, user7, user8, user9,])
    db.session.commit()
    db.session.add_all([Team1, Team2, Team3,])
    db.session.commit()
    db.session.add_all([tm1, tm2, tm3, tm4, tm5, tm6, tm7, tm8, tm9,])
    db.session.commit()
    db.session.add_all([loc1, loc2,])
    db.session.commit()
    db.session.add_all([pt1, pt2, pt3,])
    db.session.commit()
    db.session.add_all([tf1, tf2,]) 
    db.session.commit()
    db.session.add_all([e1, e2, e3,])
    db.session.commit()
    db.session.add_all([ad1, ad2, ad3,])
    db.session.commit() 
    db.session.add_all([game1, game2, game3, game4, game5])
    db.session.commit()