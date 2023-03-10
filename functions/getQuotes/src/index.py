import pprint
from appwrite.client import Client

from appwrite.services.account import Account
from appwrite.services.avatars import Avatars
from appwrite.services.databases import Databases
from appwrite.services.functions import Functions
from appwrite.services.health import Health
from appwrite.services.locale import Locale
from appwrite.services.storage import Storage
from appwrite.services.teams import Teams
from appwrite.services.users import Users
# import db
# from db import connection, quotes, tags, tags_quotes

"""
  'req' variable has:
    'headers' - object with request headers
    'payload' - request body data as a string
    'variables' - object with function variables

  'res' variable has:
    'send(text, status)' - function to return text response. Status code defaults to 200
    'json(obj, status)' - function to return JSON response. Status code defaults to 200

  If an error is thrown, a response with code 500 will be returned.
"""


def main(req, res):
    client = Client()

    account = Account(client)
    avatars = Avatars(client)
    database = Databases(client)
    functions = Functions(client)
    health = Health(client)
    locale = Locale(client)
    storage = Storage(client)
    teams = Teams(client)
    users = Users(client)

    if not req.variables.get("APPWRITE_FUNCTION_ENDPOINT") or not req.variables.get(
        "APPWRITE_FUNCTION_API_KEY"
    ):
        print("Environment variables are not set. Function cannot use Appwrite SDK.")
    else:
        (
            client.set_endpoint(req.variables.get("APPWRITE_FUNCTION_ENDPOINT", None))
            .set_project(req.variables.get("APPWRITE_FUNCTION_PROJECT_ID", None))
            .set_key(req.variables.get("APPWRITE_FUNCTION_API_KEY", None))
            .set_self_signed(True)
        )
        # if req.get("payload").get("tag") is not None:

        #     tags = req.get("payload").get("tag")
        #     if isinstance(tags, str):
        #         tags = [tags]

        #     stmt = f"""
        #     SELECT quotes.quote FROM tags_quotes 
        #         join quotes on tags_quotes.quote_id = quotes.id
        #         join tags on tags_quotes.tag_id = tags.id
        #         where tags.tag in ({str([i for i in tags])[1:-1]})
        #     """
        #     result = connection.execute(stmt).fetchall()

        #     if len(result) > 0:
        #         return res.json({"quotes": [i[0] for i in result]})

        # else:
        #     return res.json({"error": "tag not found"}, 400)

    return res.json(
        {
            "areDevelopersAwesome": True,
            "hello": "apwrite",
        }
    )


# main({"payload": {"tag": ['happy','happiness','joy']}}, None)
