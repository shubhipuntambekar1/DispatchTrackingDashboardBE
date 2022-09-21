from simple_settings import settings

from configurations.config import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='localhost', port=settings.PORT)


@app.route("/")
def hello_world():
    return 'Hello World!'


@app.route("/ping")
def ping():
    return "pong"

