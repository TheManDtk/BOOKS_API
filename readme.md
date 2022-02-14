"# BOOKS_API" 
# BOOKS_API

## Getting Started

### Installing Dependencies

#### Python 3.10.0
#### pip 22.0.3 from /Python310/lib/site-packages/pip (python 3.10)

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/projet api flask` directory and running:

```bash
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 



## Database Setup
With Postgres running, restore a database using the plants_database.sql file provided. From the backend folder in terminal run:
```bash
psql projet_iai < projet api flask.sql
```

## Running the server

From within the `projet api flask` directory first ensure you are working using your created virtual environment.

To run the server on Linux or Mac, execute:

```bash
export FLASK_APP=bookApi
export FLASK_ENV=development
flask run
```
To run the server on Windows, execute:

```bash
set FLASK_APP=bookApi
set FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

## API REFERENCE

Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

## Error Handling
Errors are retourned as JSON objects in the following format:
{
    "success":False
    "error": 400
    "message":"Bad request
}

The API will return 2 error types when requests fail:
. 400: Bad request
. 404: Not found

## Endpoints
In the bookApi.py you will see the code and in comment, what is their purpose.
## Endpoints

#
#          1) THIS PART CONCERNS THE BOOKS
#
## GET/livres

    GENERAL:
        This endpoints returns a list of book object, success value, total number of the books.


    SAMPLE: curl http://localhost:5000/livres
    {
    "Compte": 12,
    "Livres": [
        {
            "auteur": "Olivier Liron",
            "date de publication": "Thu, 10 Feb 2022 00:00:00 GMT",
            "id": 2,
            "id de categorie": 1,
            "isbn": "2072876656",
            "l'editeur": "Gallimard",
            "titre": "Le livre de Neige"
        },
        {
            "auteur": "Laurent Gaudé",
            "date de publication": "Wed, 09 Feb 2022 00:00:00 GMT",
            "id": 3,
            "id de categorie": 1,
            "isbn": "2330161743",
            "l'editeur": "Actes Sud-Papiers",
            "titre": "Le grand menteur"
        },
        {
            "auteur": "Nicolas Juncker",
            "date de publication": "Fri, 04 Feb 2022 00:00:00 GMT",
            "id": 4,
            "id de categorie": 1,
            "isbn": "2808201222",
            "l'editeur": "Le Lombard Eds",
            "titre": "Un général, des généraux"
        },
        {
            "auteur": "Melissa Da Costa",
            "date de publication": "Wed, 26 Jan 2022 00:00:00 GMT",
            "id": 5,
            "id de categorie": 2,
            "isbn": "2253936138",
            "l'editeur": "Lgf",
            "titre": "je revenais des autres"
        },
        {
            "auteur": "Maud Ankaoua",
            "date de publication": "Wed, 02 Oct 2019 00:00:00 GMT",
            "id": 6,
            "id de categorie": 2,
            "isbn": "229021051X",
            "l'editeur": "j'ai lu",
            "titre": "Kilometre zéro"
        },
        {
            "auteur": "Michel Bussi",
            "date de publication": "Mon, 03 Feb 2020 00:00:00 GMT",
            "id": 7,
            "id de categorie": 3,
            "isbn": "226632084X",
            "l'editeur": "Pocket",
            "titre": "Plus rien ne t'efface."
        },
        {
            "auteur": "Rupi kaur",
            "date de publication": "Thu, 21 Mar 2019 00:00:00 GMT",
            "id": 8,
            "id de categorie": 3,
            "isbn": "2266282802",
            "l'editeur": "Pocket",
            "titre": "lait et miel"
        },
        {
            "auteur": "J K Rowling",
            "date de publication": "Thu, 12 Oct 2017 00:00:00 GMT",
            "id": 9,
            "id de categorie": 4,
            "isbn": "2070584623",
            "l'editeur": "gallimard",
            "titre": "harry potter"
        },
        {
            "auteur": "Michael Morpurgo",
            "date de publication": "Thu, 17 May 2018 00:00:00 GMT",
            "id": 10,
            "id de categorie": 4,
            "isbn": "2075103828",
            "l'editeur": "gallimard",
            "titre": "le roi arthur"
        },
        {
            "auteur": "Viktor Vincent",
            "date de publication": "Thu, 10 Feb 2022 00:00:00 GMT",
            "id": 1,
            "id de categorie": 1,
            "isbn": "ViK-02-22-FlEds",
            "l'editeur": "Fleuve Eds",
            "titre": "Apparition"
        },
        {
            "auteur": "joe",
            "date de publication": "Sat, 10 Mar 2012 00:00:00 GMT",
            "id": 11,
            "id de categorie": 3,
            "isbn": "20123201",
            "l'editeur": "maison bruce",
            "titre": "au dessus de la loi"
        },
        {
            "auteur": "joe",
            "date de publication": "Sat, 10 Mar 2012 00:00:00 GMT",
            "id": 14,
            "id de categorie": 3,
            "isbn": "201232p1",
            "l'editeur": "maison bruce",
            "titre": "mars à la lunn e"
        }
    ],
    "success": true
    }


## DELETE/livre (livre_id)
 GENERAL:
        Delete the book of the given ID if it exists. Return the id of the deleted book, success value, total of books remaining.
        {
            "delete_book": 2,
            "len_book": 11,
            "success": true
        }

## PATCH/livre(livre_id)
  GENERAL:
  This endpoint is used to update a book
  We return a book which we update

  SAMPLE.....For Patch
   curl -X PATCH http://localhost:5000/livre/1 -H "Content-Type:application/json" -d "{
        "auteur": "Viktor Vocent",
        "date de publication": "Thu, 10 Feb 2022 00:00:00 GMT",
        "isbn": "ViK-02-22-FlEds",
        "l'editeur": "Fleuve Eds",
        "titre": "Apparition"
        }"

     {
    "Livre": {
        "auteur": "Viktor Vocent",
        "date de publication": "Thu, 10 Feb 2022 00:00:00 GMT",
        "id": 1,
        "id de categorie": 1,
        "isbn": "ViK-02-22-FlEds",
        "l'editeur": "Fleuve Eds",
        "titre": "Apparition"
    },
    "id": 1,
    "success": true
    }


## POST/livre

    GENERAL:
    This endpoint is used to create a new book.
    In the case of the creation of a new question.
    We return the ID of the new book created, the book that was created, the list of book and the number of books.

    SAMPLE.....For create

    curl -X POST http://localhost:5000/livre -H "Content-Type:application/json" -d "{
    "isbn":"201456",
    "date_de_publication":"2012-03-10",
    "titre":"jeune et fier",
    "editeur":"maison bruce",
    "auteur":"joeg",
    "categorie_id":3
    }"

    The result after the sample:
    {
    "Compte": 13,
    "Livres": [
        {
            "auteur": "Olivier Liron",
            "date de publication": "Thu, 10 Feb 2022 00:00:00 GMT",
            "id": 2,
            "id de categorie": 1,
            "isbn": "2072876656",
            "l'editeur": "Gallimard",
            "titre": "Le livre de Neige"
        },
        {
            "auteur": "Laurent Gaudé",
            "date de publication": "Wed, 09 Feb 2022 00:00:00 GMT",
            "id": 3,
            "id de categorie": 1,
            "isbn": "2330161743",
            "l'editeur": "Actes Sud-Papiers",
            "titre": "Le grand menteur"
        },
        {
            "auteur": "Nicolas Juncker",
            "date de publication": "Fri, 04 Feb 2022 00:00:00 GMT",
            "id": 4,
            "id de categorie": 1,
            "isbn": "2808201222",
            "l'editeur": "Le Lombard Eds",
            "titre": "Un général, des généraux"
        },
        {
            "auteur": "Melissa Da Costa",
            "date de publication": "Wed, 26 Jan 2022 00:00:00 GMT",
            "id": 5,
            "id de categorie": 2,
            "isbn": "2253936138",
            "l'editeur": "Lgf",
            "titre": "je revenais des autres"
        },
        {
            "auteur": "Maud Ankaoua",
            "date de publication": "Wed, 02 Oct 2019 00:00:00 GMT",
            "id": 6,
            "id de categorie": 2,
            "isbn": "229021051X",
            "l'editeur": "j'ai lu",
            "titre": "Kilometre zéro"
        },
        {
            "auteur": "Michel Bussi",
            "date de publication": "Mon, 03 Feb 2020 00:00:00 GMT",
            "id": 7,
            "id de categorie": 3,
            "isbn": "226632084X",
            "l'editeur": "Pocket",
            "titre": "Plus rien ne t'efface."
        },
        {
            "auteur": "Rupi kaur",
            "date de publication": "Thu, 21 Mar 2019 00:00:00 GMT",
            "id": 8,
            "id de categorie": 3,
            "isbn": "2266282802",
            "l'editeur": "Pocket",
            "titre": "lait et miel"
        },
        {
            "auteur": "J K Rowling",
            "date de publication": "Thu, 12 Oct 2017 00:00:00 GMT",
            "id": 9,
            "id de categorie": 4,
            "isbn": "2070584623",
            "l'editeur": "gallimard",
            "titre": "harry potter"
        },
        {
            "auteur": "Michael Morpurgo",
            "date de publication": "Thu, 17 May 2018 00:00:00 GMT",
            "id": 10,
            "id de categorie": 4,
            "isbn": "2075103828",
            "l'editeur": "gallimard",
            "titre": "le roi arthur"
        },
        {
            "auteur": "Viktor Vincent",
            "date de publication": "Thu, 10 Feb 2022 00:00:00 GMT",
            "id": 1,
            "id de categorie": 1,
            "isbn": "ViK-02-22-FlEds",
            "l'editeur": "Fleuve Eds",
            "titre": "Apparition"
        },
        {
            "auteur": "joe",
            "date de publication": "Sat, 10 Mar 2012 00:00:00 GMT",
            "id": 11,
            "id de categorie": 3,
            "isbn": "20123201",
            "l'editeur": "maison bruce",
            "titre": "au dessus de la loi"
        },
        {
            "auteur": "joe",
            "date de publication": "Sat, 10 Mar 2012 00:00:00 GMT",
            "id": 14,
            "id de categorie": 3,
            "isbn": "201232p1",
            "l'editeur": "maison bruce",
            "titre": "mars à la lunn e"
        },
        {
            "auteur": "joeg",
            "date de publication": "Sat, 10 Mar 2012 00:00:00 GMT",
            "id": 17,
            "id de categorie": 3,
            "isbn": "201456",
            "l'editeur": "maison bruce",
            "titre": "jeune et fier"
        }
    ],
    "success": true
    }


#
#          2) THIS PART CONCERNS THE CATEGORIES
#
###     we will proceed in the same way as for books. the change for the "category" part 
###             will just concern the modification and addition.

##
#       MODIFICATION OF  CATEGORY
##

## PATCH/categorie(categorie_id)
    this endpoint is use to modify a category.

   curl -X PATCH http://localhost:5000/livre/1 -H "Content-Type:application/json" -d "{
        "libelle":"Policière"
    }"

    the result the sample returns:
    {
    "categorie": {
        "id": 3,
        "libelle": "Policière"
    },
    "id": 3,
    "success": true
    }


##
#       ADD A NEW CATEGORY
##

## POST/categorie

    GENERAL:
    This endpoint is used to create a new category.
    We return the ID of the new category created, the category that was created, the list of category and the number of categories.

    SAMPLE.....For create

    curl -X POST http://localhost:5000/categorie -H "Content-Type:application/json" -d "{{
    "Libelle categorie":"théatre"
    "}"
    the returns of the sample:
    {
    "Categories": [
        {
            "id": 1,
            "libelle": "Fiction"
        },
        {
            "id": 2,
            "libelle": "Conte"
        },
        {
            "id": 4,
            "libelle": "Science"
        },
        {
            "id": 3,
            "libelle": "Policière"
        },
        {
            "id": 8,
            "libelle": "théatre"
        }
    ],
    "Count": 5,
    "success": true
    }"
