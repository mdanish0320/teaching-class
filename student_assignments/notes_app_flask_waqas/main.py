from flask import Flask

from controller.api_blueprint import auth_bp,notes_bp,category_bp
from route import auth_route,notes_route,category_route

def create_app():
  app = Flask(__name__)
  app.register_blueprint(auth_bp, url_prefix='/api')
  app.register_blueprint(notes_bp, url_prefix='/api')
  app.register_blueprint(category_bp, url_prefix='/api')
    
  
  return app

myapp = create_app()
# print(myapp.url_map)
# for rule in myapp.url_map.iter_rules():
#     print(rule)

@myapp.route('/', methods=['GET'])
def root_api():
  print('helo')
  return 'server is running'

if __name__ == "__main__":
   myapp.run(
    debug=True,
    port=5000
)


    