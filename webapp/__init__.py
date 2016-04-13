from flask import Flask

app = Flask(__name__)

import webapp.views

def page_not_found(e):
    return("Request not permitted")

@app.errorhandler(500)
def page_not_found(e):
    return("five hundred")

if __name__ == "__main__":
    app.run()
