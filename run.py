from application import app


#not working run with FLASK_DEBUG=1
if __name__ == '__main__':
  print('run.py!!!')
  app.run(debug=True)
else:
  print('run.py not __main__')

