from flask import Flask
from helper import pets

#This is the real main file.
if __name__ == "__main__":
  app.run()

app = Flask(__name__)

@app.route('/')
def index():
  return '''
    <h1>Adopt a Pet!</h1>
    <p>Browse through the links to below to find your new furry friend:</p>
    <ul>
    <li><a href="/animals/dogs">Dogs</a></li>
    <li><a href="/animals/cats">Cats</a></li>
    <li><a href="/animals/rabbits">Rabbits</a></li>
    </ul>
  '''
 
@app.route('/animals/<string:pet_type>')
def animals(pet_type):
  html = f'<h1>List of {pet_type}</h1>'
  html += '<ul>'
  for x, y in pets.items():
    if x == pet_type:
      for z in y:
        html += f'<>\n</>'
        for i3 in z.values():
          html += f'<li>{i3}</li>'
  html += '</ul>'
  return html

@app.route('/animals/<string:pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  for x, y in pets.items():
    if x == pet_type:
        for z in y:
            print(z)