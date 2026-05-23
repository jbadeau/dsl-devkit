#!/usr/bin/env python3
"""Initialize BuildGrid database schema (PostgreSQL or SQLite)."""

import sys
import time
from buildgrid.server.sql.models import Base
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

def main():
    if len(sys.argv) < 2:
        print("Usage: init-db.py <connection-string>")
        print("Examples:")
        print("  init-db.py sqlite:////var/lib/buildgrid/buildgrid.db")
        print("  init-db.py postgresql://bgd:insecure@postgres:5432/bgd")
        sys.exit(1)

    connection_string = sys.argv[1]
    print(f"Initializing database: {connection_string}")

    # Retry connection for PostgreSQL (may take time to start)
    max_retries = 10
    for i in range(max_retries):
        try:
            engine = create_engine(connection_string)
            # Test connection
            with engine.connect() as conn:
                pass
            break
        except OperationalError as e:
            if i < max_retries - 1:
                print(f"Database not ready, retrying in 2s... ({i+1}/{max_retries})")
                time.sleep(2)
            else:
                print(f"Failed to connect to database: {e}")
                sys.exit(1)

    Base.metadata.create_all(engine)
    print("Database schema created successfully")

if __name__ == "__main__":
    main()
