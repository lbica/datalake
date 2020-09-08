from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from dbcontext import Base


# Base = declarative_base()

class ETLLogMessages(Base):
    
    __tablename__ = 'ETL_LOG_MESSAGES'
    log_id = Column(Integer, primary_key=True, autoincrement=False)
    log_effective_date = Column(Date)
    module_name = Column(String(255))
    task_name = Column(String(255))
    detail_type = Column(String(1024))
    error_message = Column(String(4028))
    insert_count = Column(Integer)
    update_count = Column(Integer)
    delete_count = Column(Integer)

    def __init__(self, log_effective_date, module_name, task_name, detail_type, error_message, insert_count, update_count, delete_count):
        self.log_effective_date = log_effective_date
        self.module_name = module_name
        self.task_name = task_name
        self.detail_type = detail_type
        self.error_message = error_message
        self.insert_count = insert_count
        self.update_count = update_count
        self.delete_count = delete_count


class ETLLogMessagesSchema(SQLAlchemySchema):
        class Meta:
            model = ETLLogMessages
            # sqla_session = Base.session