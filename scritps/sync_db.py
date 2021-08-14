"""
syncing database schema and tables

"""

from utils.database import connect
from utils.models import Base

SCHEMA_NAME = "identity_management"

db_conn = connect(SCHEMA_NAME)
Base.metadata.create_all(db_conn)
