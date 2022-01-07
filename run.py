import project
import os

if __name__ == '__main__':

    app = project.create_app()
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')