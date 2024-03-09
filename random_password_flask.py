from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return '<a href="/random_password">Zobacz losowe hasło tutaj!</a>'


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>AaBbCcDdEeFfGgHhQqWwRrTtYyUuIiOoPpSsJjKkLlZzXxVvNnMm"
    password = ""
    for i in range(pass_length):
      password += random.choice(elements)
    return password
@app.route("/random_password")
def random_password():
   return f'<p>{gen_pass(pass_length=10)}</p>'

app.run(debug=True)
