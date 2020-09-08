from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config
from logger import logger


# Init app
app = Flask(__name__)

# init config object
cfg = Config()

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = cfg.MYSQL_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Init Db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)


class ETLLogMessages(db.Model):
    
    __tablename__ = 'ETL_LOG_MESSAGES'
    log_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    log_effective_date = db.Column(db.Date)
    module_name = db.Column(db.String(32))
    task_name = db.Column(db.String(32))
    detail_type = db.Column(db.String(255))
    error_message = db.Column(db.String(1024))
    insert_count = db.Column(db.Integer)
    update_count = db.Column(db.Integer)
    delete_count = db.Column(db.Integer)

    def __init__(self, log_effective_date, module_name, task_name, detail_type, error_message, insert_count, update_count, delete_count):
        self.log_effective_date = log_effective_date
        self.module_name = module_name
        self.task_name = task_name
        self.detail_type = detail_type
        self.error_message = error_message
        self.insert_count = insert_count
        self.update_count = update_count
        self.delete_count = delete_count


# class ETLLogMessagesSchema(Base):
#     #


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
