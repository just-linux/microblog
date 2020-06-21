from app import app

@app.route("/")
@app.route("/index")
def index():
    user = ['username': 'Miguel']
    return '''
    
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        
    </body>
</html>'''