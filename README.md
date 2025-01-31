# ecommerce26-11-24

This is a django app I am making for college, it needs login logout functionality, along with a functional
product database which will store a couple products.

---

### Guide for setup

### 1.

```
virtualenv -v python -p python3.13
```

This command initialises the venv which is necessary for development

---

### 2.

```
pip3 install django
django-admin startproject myProject
```

This creates the main project folder

---

### 3.

```
source bin/activate
```

Sometimes this could be `source python/bin/activate`

This runs the venv

---

### 4.

```
python3 manage.py runserver
```

This command runs the site, which we can access on`https://localhost:8000` or `https://127.0.0.1:8000`

---

### 5.

```
python3 manage.py startapp myapp
```

This generates the /myapp folder

---

### 6.

Create `urls.py` folder in myapp.py
Copy the python from myProject/urls.py to myapp/urls.py
