from app import create_app,db


app = create_app()

with app.app_context():
    # Crea las tablas en la base de datos
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)