from base import Session, engine, Base
from log import logger
from apps import Apps





def main():

    try:
        # 2 - generate database schema
        logger.info(f"Started application")

        Base.metadata.create_all(engine)

        logger.info(f"Successfully created apps table in Postgres database")

        # 3 - create a new session
        session = Session()

        logger.info(f"Finished application")

    except Exception as ex:
        logger.exception(ex)
        raise


if __name__ == '__main__':
    main()
