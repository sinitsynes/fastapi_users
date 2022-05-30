from datetime import date

from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    department_id = Column(Integer, ForeignKey('departments.id'))
    username = Column(String(200))
    password = Column(String(128))
    email = Column(String(120))
    roles = relationship(
        'UserRoles',
        cascade='all, delete-orphan')


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))


class UserRoles(Base):
    __tablename__ = 'user_roles'

    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('role.id'), primary_key=True)
    is_active = Column(Boolean)
    date_created = Column(Date, default=date.today())


class Department_Level(Base):
    __tablename__ = 'dep_level'

    id = Column(Integer, primary_key=True, autoincrement=True)


class Departments(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(20))
    department_level = Column(Integer, ForeignKey('dep_level.id'))
