from sqlalchemy import Column, Integer, Text, Boolean

from repositories.config import Base


class UserTable(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    uuid = Column(Text, index=True, unique=True)
    email = Column(Text, index=True)
    password = Column(Text)

    def __repr__(self):
        return "repositories.UserTable: {}".format(self.email)
