import os
import datetime
from sqlitedict import SqliteDict


class DatabaseClient:

    DB_NAME = "truenative_db.sqlite"

    def __init__(self, source:str):
        self.table_name = f"{source}_requests"
        self.audit_table_name = f"{source}_audit"

    def save(self, key: str, data: dict) -> None:
        db = SqliteDict(self.DB_NAME, tablename=self.table_name, autocommit=True)
        db[key] = data
        db.close()

    def get(self, key: str) -> dict:
        db = SqliteDict(self.DB_NAME, tablename=self.table_name)
        if key not in db:
            db.close()
            return None
        else:
            data = db[key]
            db.close()
            return data

    def get_all(self) -> list:
        db = SqliteDict(self.DB_NAME, tablename=self.table_name)
        items = []
        for key, item in db.items():
            print("%s=%s" % (key, item))
            items.append(item)
        db.close()
        return items

    def get_rows_len(self) -> int:
        return len(self.get_all())

    def clean(self) -> None:
        if os.path.exists(self.DB_NAME):
            os.unlink(self.DB_NAME)

    def audit(self, key: str, event:str) -> None:
        db = SqliteDict(self.DB_NAME, tablename=self.audit_table_name, autocommit=True)
        date_event = f"{datetime.datetime.now()}: {event}"
        if key not in db:
            db[key] = [date_event]
        else:
            items = db[key]
            items.append(date_event)
            db[key] = items
        db.close()

    def get_audit(self, key: str) -> dict:
        db = SqliteDict(self.DB_NAME, tablename=self.audit_table_name)
        if key not in db:
            db.close()
            return None
        else:
            data = db[key]
            db.close()
            return data
