#!flask/bin/python
from app import app
import os, sys

if (os.environ.get("DEBUG", False) == "True"):
    app.config["DEBUG"] = True

    port = int(os.environ.get("PORT", 5000))
    print >> sys.stderr, "DEBUG Mode! Port: " + str(port) 
    app.run()

    #app.run(debug=True)
else:
    app.run()

