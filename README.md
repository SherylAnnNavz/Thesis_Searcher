# Thesis_Searcher

This is a Django-based web application for searching and browsing academic theses. It allows users to search for theses by title and abstract, view detailed information about each thesis, and add comments.



Features
Search for theses by title and abstract
View detailed information about each thesis
Add comments to theses
Pagination



Installation
To install and run the Thesis Searcher locally, follow these steps:

Clone the repository:
git clone (repository-url)

Navigate to the project directory:
cd Thesis_Searcher

Create a virtual environment:
python3 -m venv env


Activate the virtual environment:
On Windows:
.\env\Scripts\activate

On macOS and Linux:
source env/bin/activate


Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Create a superuser (admin):
python manage.py createsuperuser

Start the development server:
python manage.py runserver

Access the application:
Open a web browser and go to http://localhost:8000 to access the Thesis Searcher.



Usage
Navigate to http://localhost:8000 in your web browser to access the homepage.
Use the search bar to search for theses by title and abstract.
Click on a thesis title to view detailed information about that thesis.
Add comments to theses using the comment form.
Use pagination controls to navigate.