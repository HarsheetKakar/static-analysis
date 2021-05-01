from static_analyzer import create_app

if __name__ == '__main__':
    app, db = create_app()
    app.run(debug=True)
