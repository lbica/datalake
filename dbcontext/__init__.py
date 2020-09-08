from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Column, String, Integer, Date
from config import Config
from marshmallow_sqlalchemy import SQLAlchemySchema


# __all__ = [
#     "engine",
#     "get_session",
#     "Base"
#     "Apps",
# ]


cfg = Config()
# engine = None
# _session = None


engine = create_engine(cfg.MYSQL_DATABASE_URI)

Base = declarative_base(bind=engine)
session = sessionmaker(bind=engine)

# _session = None

# def get_session(is_new = False):

#     global _session

#     if (_session is None or is_new):
#         _session = sessionmaker(bind=engine)
#         _session = _session()
    
#     return _session


def setup_database(database_uri):


    # cfg = Config()

    try:
        global engine

        engine = create_engine(database_uri)


        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        
    except Exception as ex:
        raise


# def setup_database(database_uri):


#     # cfg = Config()

#     try:
#         global engine

#         engine = create_engine(database_uri)

#         # Base.metadata.create_all(engine)
        
#         # session = get_session()

#         # Session = sessionmaker(bind=engine)

#         Base.metadata.drop_all(engine)
#         Base.metadata.create_all(engine)
        
#     except Exception as ex:
#         raise



# class ETLLogMessages(Base):
    
#     __tablename__ = 'ETL_LOG_MESSAGES'
#     log_id = Column(Integer, primary_key=True, autoincrement=False)
#     log_effective_date = Column(Date)
#     module_name = Column(String(255))
#     task_name = Column(String(255))
#     detail_type = Column(String(1024))
#     error_message = Column(String(4028))
#     insert_count = Column(Integer)
#     update_count = Column(Integer)
#     delete_count = Column(Integer)

#     def __init__(self, log_effective_date, module_name, task_name, detail_type, error_message, insert_count, update_count, delete_count):
#         self.log_effective_date = log_effective_date
#         self.module_name = module_name
#         self.task_name = task_name
#         self.detail_type = detail_type
#         self.error_message = error_message
#         self.insert_count = insert_count
#         self.update_count = update_count
#         self.delete_count = delete_count


# class ETLLogMessagesSchema(SQLAlchemySchema):
#         class Meta:
#             model = ETLLogMessages
#             # sqla_session = Base.session