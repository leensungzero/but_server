from app import create_app
from app.extension import db

from flask import Flask

app: Flask = create_app('develop')

if __name__ == '__main__':
    db.create_all(app=app)
    app.run(host='127.0.0.1', port=8080)
