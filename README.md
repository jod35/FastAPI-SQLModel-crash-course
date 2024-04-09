# FastAPI + SQLModel Crash Course
This is code for how to build a REST API with FastAPI and SQLModel. SQLModel is a library for interacting with SQL databases from Python code, with Python objects. It is designed to be intuitive, easy to use, highly compatible, and robust.

This code shows you how to build a REST API using FastAPI and SQLmodel

For a more updated guide to building such a project, check this video out [here](https://youtu.be/I8WiIXMDydw?si=LSJ7Tb6iETjg8IPy)

Also, the updated project source code will be found [here](https://github.com/jod35/lib-api)

## How to run the project
- Install the requirements 
```
pip freeze > requirements.txt
```

- Create the database
```
python create_db.py

```

- Finally run the project
```
uvicorn main:app
```

