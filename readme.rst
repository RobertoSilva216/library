Library system
============

System for book management and favorites books

Features
--------

Books
* GET /books - Retrieve a list of all books.
* GET /books/:id - Retrieve a specific book by ID.
* POST /books - Create a new book (protected).
* PUT /books/:id - Update an existing book (protected).
* DELETE /books/:id - Delete a book (protected).

Authors
* GET /authors - Retrieve a list of all authors.
* GET /authors/:id - Retrieve a specific author by ID.
* POST /authors - Create a new author (protected).
* PUT /authors/:id - Update an existing author (protected).
* DELETE /authors/:id - Delete an author (protected).

Authentication
* JWT for user authentication.
* Registration (POST /register) and login (POST /login) endpoints.


Search Functionality
* Query string params to filter books and authors

Prerequisites
-------------
Use the requirements file to install

* Python 3.x
* asgiref==3.8.1
* Django==5.1.1
* djangorestframework==3.15.2
* djangorestframework-simplejwt==5.3.1
* joblib==1.4.2
* numpy==2.1.1
* PyJWT==2.9.0
* scikit-learn==1.5.2
* scipy==1.14.1
* sqlparse==0.5.1
* threadpoolctl==3.5.0
* tzdata==2024.2


Installation
------------

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/yourusername/projectname.git
      cd projectname

2. Create and activate a virtual environment:

   .. code-block:: bash

      python3 -m venv dev
      source dev/bin/activate  # For Windows: dev\Scripts\activate

3. Install dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

4. Apply migrations:

   .. code-block:: bash

      python manage.py makemigrations
      python manage.py migrate

5. Run the development server:

   .. code-block:: bash

      python manage.py runserver

Usage
-----
Try the endpoints of books and authors
* /api/books
* /api/authors


Contributing
------------

- Feel free to improve this project
- Maybe starting with a pagination for the endpoints

License
-------

MIT License
