import os
# Any import from taskmanager package launches __init__.py file but only once
from taskmanager import app

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
