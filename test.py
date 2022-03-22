from importlib.machinery import all_suffixes
from model import db,User

all=User.query.all()
p=User(user_id=101,
user_name="unnni",
email="unnni@example.com",
password="pasnnnsword@example.com")
db.session.add(p)
db.session.commit()