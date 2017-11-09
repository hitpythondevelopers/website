# this file runs the application and allows you to view the application from the web browser 

from website import app
import os

if __name__ == '__main__':
    app.run(debug=True, port=8000)   