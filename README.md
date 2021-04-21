# ArtWayNN

Python3 module for image recognision in ArtWay project. Implemented with ```FastAPI``` and ```TensorFlow```.

**Contents:**
* [Setup](#setup)
* [Running the app](#run)
* [Docs](#docs)


# Setup 
<a name="first"></a>
Clone the repo. It is recommended to create a python3 virtual environment for your system and work in it:

```
python3 -m venv venv
```
Activate ```venv``` for Windows system:
```
venv\Scripts\activate
```
or for Linux:
```
source venv/bin/activate
```
Install requirements:
```
(venv) python3 -m pip install --upgrade pip
(venv) pip install -r requirements.txt
```

# Running the app
<a name="first"></a>
```
(venv) uvicorn main:app
```

The app runs on ```http://127.0.0.1:8000```

# Docs
<a name="docs"></a>
Swagger is available by ```http://127.0.0.1:8000/docs```

Alternative API - ```http://127.0.0.1:8000/redoc```

