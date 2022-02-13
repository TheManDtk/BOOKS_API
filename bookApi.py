import os
from flask import Flask, jsonify, abort,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from sqlalchemy import *
load_dotenv()

passw=os.getenv("password")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:{}@localhost:5432/projet_iai'.format(passw)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Categorie(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    libelleCategorie = db.Column(db.String(50),nullable=False)
    livress = db.relationship("Livre", backref="categories", lazy=True)

    def __init__(self, libelleCategorie):
        self.libelleCategorie = libelleCategorie

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def formatage(self):
        return{
            "id": self.id,
            "libelle": self.libelleCategorie
        }


class Livre(db.Model):
    __tablename__ = "livres"
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(70), unique=True)
    titre = db.Column(db.String(150))
    date_publication = db.Column(db.Date)
    auteur = db.Column(db.String(150))
    editeur = db.Column(db.String(150))
    categories_id = db.Column(db.Integer, db.ForeignKey(
        "categories.id"), nullable=False)

    def __init__(self, isbn, titre, date_publication, auteur, editeur, categories_id):
        self.isbn = isbn
        self.titre = titre
        self.date_publication = date_publication
        self.auteur = auteur
        self.editeur = editeur
        self.categories_id = categories_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete()
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'isbn': self.isbn,
            'titre': self.titre,
            'date de publication': self.date_publication,
            'auteur': self.auteur,
            'l\'editeur': self.editeur,
            #'la categorie': self.libelleCategorie,
            'id de categorie': self.categories_id
        }


db.create_all()
###################################################################################################
##
##          POUR OBTENIR TOUS LES LIVRES DANS LA BASE DE DONNEES.
##
###################################################################################################
@app.route('/livres')
def get_all_books():
    try:
        books=Livre.query.all()
        books=[l.format() for l in books]
        return jsonify({
            'success':True,
            'Livres':books,
            'Compte':len(books)}
        )
    except:
        abort(400)

###################################################################################################
##
##          POUR OBTENIR UN LIVRE EN PARTICULIER DANS LA BASE DE DONNEES GRACE A SON ID
##
###################################################################################################
@app.route('/livre/<int:id>')
def get_one_book(id):
    try:
        book=Livre.query.get(id)
        if book is None:
            abort(404)
        else:
            return jsonify({
                'success':True,
                'id':id,
                'Livre':book.format()}
            )
    except:
        abort(400)

###################################################################################################
##
##          POUR OBTENIR TOUTES LES CATEGORIES DISPONIBLES DANS LA BASE DE DONNEES.
##
###################################################################################################
@app.route('/categories')
def get_all_categories():
    try:
        categoriAll=Categorie.query.all()
        categoriAll=[c.formatage() for c in categoriAll]
        return jsonify({
            'success':True,
            'Categories':categoriAll,
            'Count': len(categoriAll)}
        )
    except:
        abort(400)

###################################################################################################
##
##          POUR OBTENIR UNE CATEGORIE PARTICULIERE DANS LA BASE DE DONNEES GRACE A SON ID.
##
###################################################################################################
@app.route('/categorie/<int:id>')
def get_one_categorie(id):
    try:
        cat=Categorie.query.get(id)
        if cat is None:
            abort(400)
        else:
            return jsonify({
                'success':True,
                'id_cat':id,
                'libelleCat':cat.formatage()}
            )
    except:
        abort(400)

###################################################################################################
##
##          POUR SUPPRIMER UNE CATEGORIE EN PARTICULIER.
##
###################################################################################################
@app.route('/categorie/<int:id_cat>', methods=['DELETE'])
def delete_cat(id_cat):
    try:
        laCat=Categorie.query.get(id_cat)
        if laCat is None:
            abort(404)
        else:
            laCat.delete()
            return jsonify({
                "success":True,
                "deleted_cat_id":id_cat,
                "len_cat":len(Categorie.query.all())}
            )
    except:
        abort(400)


###################################################################################################
##
##          POUR SUPPPRIMER UN LIVRE EN PARTICULIER.
##
###################################################################################################
@app.route('/livre/<int:id_book>',methods=['DELETE'])
def delete_one_book(id_book):
   # try:
        bookSup=Livre.query.filter_by(id=id_book)
        if bookSup is None:
            abort(404)
        else:
            bookSup.delete()
            return jsonify({
                "success":True,
                "delete_book":id_book,
                "len_book":len(Livre.query.all())}
            )
   # except:
    #    abort(400)



###################################################################################################
##
##          POUR OBTENIR TOUS LES LIVRES APPARTENANT A UNE CATEGORIE DANS LA BASE DE DONNEES.
##
###################################################################################################
@app.route('/categorie/<int:id_cat>/livres')
def all_book_in_categorie(id_cat):
    nomcat=Categorie.query.get(id_cat)
    try:
        book_cat=Livre.query.filter_by(categories_id=id_cat)
        book_cat=[j.format() for j in book_cat]
        return jsonify({
            'success':True,
            'libelleCat':nomcat.libelleCategorie,
            'Livres':book_cat,
            'Compte':len(book_cat)}
        )
    except:
        abort(400)


###################################################################################################
##
##          POUR OBTENIR LA CATEGORIE A LAQUELLE APPARTIENT UN  LIVRE.
##
###################################################################################################
@app.route('/livre/<int:id_Book>/categorie')
def cat_of_Book(id_Book):
    try:
        livreCat=Categorie.query.get(id_Book)
        nomLivre=Livre.query.get(id_Book)
        return jsonify({
            'success':True,
            'nom du Livre':nomLivre.format(),
            'categorie du livre':livreCat.formatage()}
        )
    except:
        abort(400)


###################################################################################################
##
##          POUR EFFECTUER UNE MODIFICATION SUR UN LIVRE.
##
###################################################################################################
@app.route('/livre/<int:id_book>', methods=['PATCH'])
def update_book(id_book):
    recup=request.get_json()
    try:
        bookRec=Livre.query.filter_by(id=id_book).one_or_none()
        if recup is None:
            abort(404)
        else:
            if ('isbn' and 'titre' and 'date de publication' and 'auteur' and 'l\'editeur' ) in recup:
                bookRec.isbn=recup.get('isbn')
                bookRec.titre=recup.get('titre')
                bookRec.date_publication=recup.get('date de publication')
                bookRec.auteur=recup.get('auteur')
                bookRec.editeur=recup.get('l\'editeur')
                #bookRec.categories_id=recup.get('categories_id')
            bookRec.update()
            return jsonify({
                'success':True,
                'id':bookRec.id,
                'Livre':bookRec.format()}
            )
    except:
        abort(400)




###################################################################################################
##
##          POUR EFFECTUER UNE MODIFICATION SUR UNE CATEGORIE.
##
###################################################################################################
@app.route('/categorie/<int:id_cat>', methods=['PATCH'])
def update_categorie(id_cat):
    recup=request.get_json()
    try:
        cat=Categorie.query.filter_by(id=id_cat).one_or_none()
        if cat is None:
            abort(404)
        else:
            if 'libelle' in recup:
                cat.libelleCategorie=recup.get('libelle')
            cat.update()
            return jsonify({
                'success':True,
                'id':cat.id,
                'categorie':cat.formatage()
            })
    except:
        abort(400)


###################################################################################################
##
##          Pour Ajouter Un Livre aux livres déjà existants.
##
###################################################################################################
@app.route('/livre',methods=['POST'])
def add_book():
    aj=request.get_json()
    try:
        new_isbn=aj.get('isbn',None)
        new_datepublication=aj.get('date_de_publication',None)
        new_titre=aj.get('titre',None)
        new_editeur=aj.get('editeur',None)
        new_auteur=aj.get('auteur',None)
        new_categorie_id=aj.get('categorie_id',None)
        maxcat=Categorie.query.count()
        if new_categorie_id >  maxcat:
            abort(500)
        else:
            livvre=Livre(isbn=new_isbn, auteur=new_auteur, date_publication=new_datepublication,
            editeur=new_editeur,titre=new_titre,categories_id=new_categorie_id)
            livvre.insert()
            books=Livre.query.all()
            books=[l.format() for l in books]

        return jsonify({
            'success':True,
            'Livres':books,
            'Compte':len(books)}
        )
    except:
        abort(404)





###################################################################################################
##
##          Pour Ajouter Une nouvelle catégorie à celles déjà existantes.
##
###################################################################################################
@app.route('/categorie',methods=['POST'])
def add_catgeory():
    recup=request.get_json()
    try:
        newlibelle=recup.get('Libelle categorie',None)
        ca=Categorie(libelleCategorie=newlibelle)
        try:
            ca.insert()
            categories=Categorie.query.all()
            categories=[d.formatage() for d in categories]
            return jsonify({
                'success':True,
                'Categories':categories,
                'Count': len(categories)}
            )
        except:abort(404)
    except:abort(400)


###################################################################################################
##
##          Pour la gestion des erreurs.
##
###################################################################################################
@app.errorhandler(404)
def erreur_client1(error):
    return (jsonify({
        'success':False,
        'error':404,
        'success':False,
        'message':'Inexistant'
        }), 404)


@app.errorhandler(400)
def error_client(error):
    return (jsonify({
        'success': False,
        'error': 400,
        'message': 'Bad request'
        }), 400)
