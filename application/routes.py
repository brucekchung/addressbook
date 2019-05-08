from application import app


@app.route("/")

@app.route("/home")
def home():
  return '<h1>Address Book</h1>' 
