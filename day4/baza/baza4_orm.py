# Mapowanie obiektowo-relacyjne
# (ang. Object-Relational Mapping – ORM) – sposób odwzorowania obiektowej architektury systemu
# informatycznego na bazę danych (lub inny element systemu) o relacyjnym charakterze.

# orm w pythonie -> peewe, sqlalchemy

# pip install sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine('sqlite:///moja_baza.db', echo=True)
Base = declarative_base()


# model, encja
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)

    def __repr__(self):
        return f"{self.name}"


Base.metadata.create_all(engine)
# 2026-03-26 13:13:34,425 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2026-03-26 13:13:34,425 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("person")
# 2026-03-26 13:13:34,425 INFO sqlalchemy.engine.Engine [raw sql] ()
# 2026-03-26 13:13:34,426 INFO sqlalchemy.engine.Engine COMMIT

Session = sessionmaker(bind=engine)
session = Session()

person = Person(name="Radek", age="23")
session.add(person)
session.commit()
# INSERT INTO person (name, age) VALUES (?, ?), ('Radek', '23')

# SELECT person.id AS person_id, person.name AS person_name, person.age AS person_age
# FROM person
persons = session.query(Person).all()
print(persons)
# [Radek, Radek]

for p in persons:
    print(p.name, p.age)
# Radek 23
# Radek 23
# Radek 23