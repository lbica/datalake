from os import environ
from os import path
from logger import logger
from dotenv import load_dotenv, find_dotenv


# config_data = None
# config_filepath = path.join(path.dirname(path.abspath(__file__)), 'config.json')

# with open(config_filepath) as config_file:
#     config_data = json.load(config_file)

try:

    env_file = path.join(path.dirname(path.abspath(__file__)), 'config\\.env')

    # env_file = find_dotenv(raise_error_if_not_found=True)

    load_dotenv(dotenv_path=env_file)


except Exception as es:
    logger.error(es)
    raise


# OR, explicitly providing path to '.env'
# from pathlib import Path  # python3 only
# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)


class Config:

        

    # General Config
    DEBUG = False
    TESTING = False
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    MYSQL_URL = environ.get('MYSQL_URL')

    MYSQL_HOSTNAME = environ.get('MYSQL_HOSTNAME')
    MYSQL_USER=environ.get('MYSQL_USER')
    MYSQL_PASSWORD=environ.get('MYSQL_PASSWORD')
    MYSQL_DB=environ.get('MYSQL_DB')

    # Flask-Assets
    LESS_BIN = environ.get('LESS_BIN')
    ASSETS_DEBUG = environ.get('ASSETS_DEBUG')
    LESS_RUN_IN_DEBUG = environ.get('LESS_RUN_IN_DEBUG')

    GENERATOR_NUMROWS = environ.get('GENERATOR_NUMROWS')
    CSV_FILE_NAME = environ.get('CSV_FILE_NAME')

    # Redshift params
    REDSHIFT_HOSTNAME = environ.get('REDSHIFT_HOSTNAME')
    REDSHIFT_USER = environ.get('REDSHIFT_USER')
    REDSHIFT_PASSWORD = environ.get('REDSHIFT_PASSWORD')
    REDSHIFT_PORT = environ.get('REDSHIFT_PORT')
    REDSHIFT_DB = environ.get('REDSHIFT_DB')

    # @property
    # def MYSQL_DATABASE_URI(self):
    #     return 'mysql://{}:{}@{}/{}'.format(self.MYSQL_USER, self.MYSQL_PASSWORD, self.MYSQL_HOSTNAME, self.MYSQL_DB)

    @property
    def MYSQL_DATABASE_URI(self):
        return 'mysql+pymysql://{}:{}@{}/{}'.format(self.MYSQL_USER, self.MYSQL_PASSWORD, self.MYSQL_HOSTNAME, self.MYSQL_DB)

    @property
    def REDSHIFT_DATABASE_URI(self):
        return 'postgresql://{}:{}@{}:{}/{}'.format(self.REDSHIFT_USER, self.REDSHIFT_PASSWORD, 
            self.REDSHIFT_HOSTNAME, self.REDSHIFT_PORT, self.REDSHIFT_DB)

 

class ProductionConfig(Config):
    
    DB_SERVER = '192.168.19.32'


class DevelopmentConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True


class TestingConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True
    DATABASE_URI = 'sqlite:///:memory:'
