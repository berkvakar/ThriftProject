from flask import Flask
from routes import routes  # Import the routes blueprint

def create_app():
    app = Flask(__name__)

    
    app.register_blueprint(routes, url_prefix='/')  # Base route (home page)
    app.register_blueprint(routes, url_prefix='/about')
    app.register_blueprint(routes, url_prefix='/login')  # login page
    app.register_blueprint(routes, url_prefix='/register')  # Register page

    return app

# Initialize the app when running the script
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
