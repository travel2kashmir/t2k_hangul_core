from ...utils.config import ConfigStore
from config import config
from credentials import credentials

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

store = ConfigStore.get_instance()
store.load({**config, **credentials})


class DBConnection(object):
    """Database connection"""

    def __init__(self):
        self.connection_string = f"postgresql://{store.get('db.credentials.username')}:{store.get('db.credentials.password')}@{store.get('db.server.url')}:{store.get('db.server.port')}/{store.get('db.name')}"
        self.session = None

    def __enter__(self):
        engine = create_engine(self.connection_string)

        Session = sessionmaker(autocommit=True, autoflush=False)
        self.session = Session(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
