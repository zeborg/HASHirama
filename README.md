![MIT License](https://img.shields.io/github/license/zeborg/HASHirama)
\
\
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Mlh-logo-color.svg/1200px-Mlh-logo-color.svg.png" width=150px/>
<img src="https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/challenge_photos/001/306/326/datas/full_width.png"/>
## [MLH New Year New Hack Submission](https://devpost.com/software/hashirama)
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
HASHirama uses [Flask](https://flask.palletsprojects.com/en/1.1.x/) at the backend and utilizes [Bootstrap 4.5](https://getbootstrap.com/docs/4.5/getting-started/introduction/) for styles.

#### Using HASHirama in a virtual environment:
Create and activate a virtual environment (`myvirtualenv` in the example below) and install the dependencies provided in `requirements.txt` by executing the following command:
```sh
(myvirutalenv) $ pip install -r requirements.txt
```
*(Linux)* For production environment without debug mode:
```sh
$ export FLASK_ENV=production
$ export FLASK_DEBUG=0
```
*(Linux)* For development environment with debug mode:
```sh
$ export FLASK_ENV=development
$ export FLASK_DEBUG=1
```
*(Windows)* For production environment without debug mode:
```sh
$ set FLASK_ENV=production
$ set FLASK_DEBUG=0
```
*(Windows)* For development environment with debug mode:
```sh
$ set FLASK_ENV=development
$ set FLASK_DEBUG=1
```

### Running the app
Once the installation steps are done, CD to the directory where `app.py` is located and execute the following command:
```sh
(myvirtualenv) $ python3 app.py
```
Default maximum file upload size is 100 MB, however you can change it in `__init__.py`
\
**NOTE:** Use a proper WSGI instead of using the Flask production environment for better security and to avoid unusual behavior such as connection reset upon error handling. [Here are a few deployment options as suggested by Flask itself](https://flask.palletsprojects.com/en/1.1.x/deploying/).

### Contributions and Improvements
They're always welcome!
