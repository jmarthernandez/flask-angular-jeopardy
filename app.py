from flask import Flask, json, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bower import Bower
from sqlalchemy import create_engine
import os



app = Flask(__name__)
Bower(app)
app.config.from_object(os.environ['APP_SETTINGS'])
db = create_engine(os.environ['DATABASE_URL'])

@app.route('/')
def index():
  return render_template('index.html')

def alchemyencoder(obj):
  """JSON encoder function for SQLAlchemy special classes."""
  if isinstance(obj, datetime.date):
    return obj.isoformat()
  elif isinstance(obj, decimal.Decimal):
    return float(obj)

@app.route('/api/question', methods=['GET'])
def getQuestion():
  result = db.execute('SELECT * FROM questions WHERE question NOT LIKE %s ORDER BY RANDOM() LIMIT 1', '%<a%')
  return json.dumps([dict(r) for r in result], default=alchemyencoder)

if __name__ == '__main__':
  app.run()