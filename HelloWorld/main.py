from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/')
def hello_world():
    data = {
        'message': 'Hello World, From FastAPI!', 
        'status': 'success'
    }
    return data

# Path Parameter along with type hints
@app.get('/print-hello/{times}')
def print_hello(times: int):
    msg = ['Hello' for i in range(times)]
    data = {
        'message': msg, 
        'length': times,
        'status': 'success'
    }
    return data


# Query Parameter along with type hints and default value
@app.get('/get-blogs')
def print_hello(limit: int = 10):
    msg = ['Hello' for i in range(limit)]
    data = {
        'message': msg, 
        'length': limit,
        'status': 'success'
    }
    return data

# Path and Query Parameter along with type hints and default value
@app.get('/details/{id}/comments')
def print_hello(id: int, limit: int = 5, format: Optional[bool] = True):
    msg = [f'Comment - {i}' for i in range(limit)]
    if format:
        msg += ['FORMATTED']
    data = {
        'id': id,
        'comments': msg, 
        'total comments': limit,
        'status': 'success'
    }
    return data