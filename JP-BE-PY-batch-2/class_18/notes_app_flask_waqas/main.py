from flask import Flask

from route.auth import auth_bp
from route.category import category_bp
# from route.notes import notes_bp

def create_app():
  app = Flask(__name__)
  app.register_blueprint(auth_bp, url_prefix='/api')
  # app.register_blueprint(notes_bp, url_prefix='/api')
  app.register_blueprint(category_bp, url_prefix='/api')
    
  
  return app

myapp = create_app()

@myapp.route('/', methods=['GET'])
def root_api():
  print('helo')
  return 'server is running'

if __name__ == "__main__":
   myapp.run(
    debug=True,
    port=3000
)


    