from app import app
import view
from db import db
import admin

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()