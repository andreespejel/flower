from database import SessionLocal

# define get_db, 
def get_db():
    # create a session
    session = SessionLocal()
    try:
        # give the session to the endpoint
        yield session
    finally:
        # close the session
        session.close()