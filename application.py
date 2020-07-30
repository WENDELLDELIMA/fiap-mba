from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>OPA FIAP!</h1>\nMBA!  - WENDELL LIMA"

if __name__ == '__main__':
    application.run()
