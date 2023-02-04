import json
import sqlalchemy
import sqlalchemy.dialects.postgresql as psql


# create engine and connect to a postgresql database

engine = sqlalchemy.create_engine(
    "postgresql://postgres:W9waGDlNONcom0BSJmXJ8OCy68LS@localhost:5432/postgres"
)

# test connection
try:
    connection = engine.connect()
    print("Connection established")
except:
    print("Connection failed")
    exit()


meta = sqlalchemy.MetaData()

# create a table quotes
quotes: sqlalchemy.Table = sqlalchemy.Table(
    "quotes",
    meta,
    sqlalchemy.Column("id", psql.UUID, primary_key=True),
    sqlalchemy.Column("quote", sqlalchemy.String),
    sqlalchemy.Column("author", sqlalchemy.String),
)

# create a table tags
tags: sqlalchemy.Table = sqlalchemy.Table(
    "tags",
    meta,
    sqlalchemy.Column("id", psql.UUID, primary_key=True),
    sqlalchemy.Column("tag", sqlalchemy.String),
)

# create a table tags_quotes with foreign keys and unique constraint
tags_quotes: sqlalchemy.Table = sqlalchemy.Table(
    "tags_quotes",
    meta,
    sqlalchemy.Column("id", psql.UUID, primary_key=True, unique=True),
    sqlalchemy.Column("tag_id", None, sqlalchemy.ForeignKey("tags.id")),
    sqlalchemy.Column("quote_id", None, sqlalchemy.ForeignKey("quotes.id")),
    sqlalchemy.UniqueConstraint("tag_id", "quote_id", name="unique_tag_quote"),
)
