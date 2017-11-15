from sqlalchemy.orm import sessionmaker

from maketables import *

engine = create_engine('sqlite:///user.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

user = User("test_user", 'password')
session.add(user)

session.commit()

session.commit()
