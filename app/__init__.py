"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq3382qv2dcb92g7dg-a.oregon-postgres.render.com",
        database="todo_ym72",
        user="root",
        password="845Hz7bQvZcvdzsqPdFR2GqzWYDohBGU")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
