from application import app


@app.route("/")
def main():
  return '<h1>Address Book Main</h1>' 
