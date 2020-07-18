![MIT License](https://img.shields.io/github/license/zeborg/HASHirama)
# HASHirama
HASHirama is a web application for hashing texts as well as binary files.\
[Try HASHirama](https://zeborg.pythonanywhere.com/) (hosted on PythonAnywhere)
### Algorithms Supported

- BLAKE2b
- BLAKE2s
- MD5
- SHA-1
- SHA-224
- SHA3-224
- SHA-256
- SHA3-256
- SHA-384
- SHA-512
- SHA3-512

### Installation
HASHirama uses [Flask](https://flask.palletsprojects.com/en/1.1.x/) as the backend framework and utilizes [Bootstrap 4.5](https://getbootstrap.com/docs/4.5/getting-started/introduction/) for styles.

#### Using HASHirama in a virtual environment:
Create and activate a virtual environment (`myvirtualenv` in the example below) and install the dependencies provided in `requirements.txt` by executing the following command:
```sh
(myvirutalenv) $ pip install -r requirements.txt
```
\
*(Linux)* For production environment:
```sh
$ export FLASK_ENV=production
```
*(Linux)* For development environment:
```sh
$ export FLASK_ENV=development
```
*(Windows)* For production environment:
```sh
$ set FLASK_ENV=production
```
*(Windows)* For development environment:
```sh
$ set FLASK_ENV=development
```

### Running the app
Once the installation steps are done, CD to the directory where `app.py` is located and execute the following command:
```sh
(myvirtualenv) $ flask run
```
\
Default maximum file upload size is 50 MB, however you can change it in `__init__.py`
\
\
**NOTE:** Use a proper WSGI instead of using the Flask production environment to avoid unusual behavior such as connection reset upon error handling

### Contributions and Improvements
Always welcome!
