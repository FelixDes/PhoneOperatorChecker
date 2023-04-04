import os
import secrets

from flask import Flask

import PhoneControllers
from MainContainer import MainContainer

container = MainContainer()

app = Flask(__name__)
app.container = container
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
app.add_url_rule("/", "index", PhoneControllers.index)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
