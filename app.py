from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


books = [
    {"id": 1, "title": "Harry Potter and the Sorcere's Stone","author":"J.K.Rowling","year":1997},
    {"id": 2, "title": "The Great Gatsby","author":"F.Scott Fitzgerald","year":1925},
    {"id": 3, "title": "1984","author":"George Orwell","year":1949},
    {"id": 4, "title": "To Kill a Mockingbird","author":"Harper Lee","year":1960},
    {"id": 5, "title": "A Promised Land","author":"Barrack Obama","year":2020}
]
@app.route('/', methods=("GET","POST"))
def index():
    return render_template("index.html")

# @app.route('/search', methods=["GET"])
# def search():
#     query = request.args.get('query')
#     date = request.args.get('date')
#     return f'Recherche : {query}'

@app.route('/books', methods=["GET"])
def book():

    author = request.args.get('author')
    exist = False

    for livre in books:
        if livre['author'] == author:
            exist = True
            return f"livre : {livre['title']} ( {livre['year']})"

    if exist == False:
        return "cherche mieux"
    
@app.route('/add_book', methods=["POST"])
def add_book():
    titre = request.form.get('title')
    auteur = request.form.get('author')
    annee = request.form.get('year')

    books.append(
        {"id": len (books) + 1, "title": titre,"author":auteur,"year":annee}
    )
    return f'titre: {titre} | auteur : {auteur} | annee : {annee}'



# @app.route('/login', methods=["POST"])
# def login():
#     nom = request.form.get('username')
#     motdepasse = request.form.get('motdepasse')
#     return f'Nom : {nom} / Mot de passe = {motdepasse}'

if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=8080)