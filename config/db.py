from sqlalchemy import create_engine, MetaData
from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from models.modelos import DataBaseModel 






#---LOCAL DATABASE ----

# _hostname ='localhost'
# _username ='basedatos'
# _password ='basedatos'
# _database ='notario'

#---HEROKU DATABASE ----

_hostname = 'jtb9ia3h1pgevwb1.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
_username = 'vl0v51r0t6ald9dh'
_password = 'nq5d3dq46cc551cj'
_database = 'u67qxne0bs0uujx8' 


# SQLALCHEMY 
engine = create_async_engine("mysql+asyncmy://"+_username + ":"+ _password +"@"+ _hostname +":3306/" + _database)
SessionLocal = async_sessionmaker(engine)



async def get_db():
    async with engine.begin() as conn:
        await conn.run_sync(DataBaseModel.metadata.create_all)

    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()







# Connect to the database MODO ANTIGUO 
# conn = pymysql.connect(host=_hostname ,
#                              user=_username,
#                              password=_password,
#                              database=_database,
#                              cursorclass=pymysql.cursors.DictCursor)

