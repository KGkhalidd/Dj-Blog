Developed a Django-based personal blog project with CRUD functionalities for creating, editing, and deleting blog posts. Implemented robust search and filtering features by author, category, and publication date. Included a user session feature for adding posts to a 'Read Later' list and removing from the stored posts. Users can engage through comments by providing username, email, and comments on each post.

u can see it deployed from here :
https://kgkhalidd.pythonanywhere.com/

### Installation

1. Clone the Repo

```sh
git clone https://github.com/KGkhalidd/Dj-Blog.git
```

2. Create Python Enviornment

```sh
python -m venv ENV
```

3. Install Requirements Libs

```sh
pip install -r requirements.txt
```
### Running Server 

1. Migrate the Database 
```sh
manage.py migrate
```

2. Run Server 
```sh
manage.py runserver
```
