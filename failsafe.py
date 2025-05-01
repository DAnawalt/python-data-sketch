from flask import Flask
from helper import pets

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
        for i3 in z.items():
          if i3[0] == "name":
            html += f'<li><a href="{pet_type}/{i3[1]}">{i3[1]}</a></li>'
  html += '</ul>'
  return html
#@app.route('/animals/<string:pet_type>/{i3{1}}')
"""
@app.route('/animals/<string:pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  for x, y in pets.items():
    if x == pet_type:
        for z in y:
            print(z)
"""