from flask import render_template
from app import app

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
  """
  View root page function that returns the index page and its data
  """
  title = 'Home - Welcome to the best Movie Review Website Online'
  return render_template('index.html',title = title)