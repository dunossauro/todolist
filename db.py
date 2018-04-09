from sqlalchemy import (create_engine, MetaData, Column,
                        Table, Integer, String, DateTime)

engine = create_engine('sqlite:///teste.db',
                       echo=False)

metadata = MetaData(bind=engine)

task_table = Table('tasks', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('task', String(40), index=True),
                   Column('date', DateTime))

metadata.create_all()
