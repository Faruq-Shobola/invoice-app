from invoice import create_app, db

app = create_app()

with app.app_context():
    # db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)