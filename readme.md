# FastAPI

Now that we have a solid understanding of Django and DRF, it's time to delve into one of the fastest-growing web frameworks in the Python ecosystem — FastAPI. Let's get started!

##### Dt. 25 Apr, 2025.

I will be exploring the FastAPI [Docs](https://fastapi.tiangolo.com/tutorial/) to cover the fundamental concepts.

### Introduction to FastAPI

- **FastAPI** is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- It is built on top of Starlette for the web parts and Pydantic for the data parts.
- FastAPI is designed to be easy to use and learn, and to provide high performance.
- It is one of the fastest Python frameworks available, rivaling NodeJS and Go in speed.

#### Project Structure

A well-organized FastAPI project typically follows this structure:

```plaintext
my_fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── users.py
│   │   │   │   ├── items.py
│   │   │   ├── models/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── user.py
│   │   │   │   ├── item.py
│   │   │   ├── schemas/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── user.py
│   │   │   │   ├── item.py
│   │   │   └── services/
│   │   │       ├── __init__.py
│   │   │       ├── user_service.py
│   │   │       ├── item_service.py
│   ├── config.py
│   ├── database.py
│   └── middleware.py
├── tests/
│   ├── __init__.py
│   ├── test_users.py
│   └── test_items.py
├── requirements.txt
└── README.md
```

#### Key Components

**`main.py`**

- The entry point of the application where the FastAPI app instance is created.

  ```python
  from fastapi import FastAPI
  from app.api.v1.endpoints import users, items

  app = FastAPI()

  app.include_router(users.router)
  app.include_router(items.router)
  ```

**`api/`**

- Contains versioned APIs (`v1`, `v2`, etc.) to accommodate future changes without breaking existing implementations.
- **endpoints/**: Holds separate files for each endpoint, facilitating modular development.
- **models/**: Contains the data models, which usually correspond to database tables or external data structures.
- **schemas/**: Includes Pydantic models used for request and response validation.
- **services/**: Houses business logic related to each feature (e.g., retrieving data from a database).

**`config.py`**

- Stores configuration settings such as database connection information and environment variables.

**`database.py`**

- Manages database connections and ORM session configurations.

**`middleware.py`**

- Defines custom middleware for handling requests or responses.

**`tests/`**

- This directory includes all test cases utilizing a framework like pytest, ensuring that your API endpoints work as expected.

#### Install and Uninstall FastAPI

**Installation**

- Install using pip: `pip install fastapi`
- Install an ASGI server (e.g., Uvicorn): `pip install uvicorn`
- Verify installation: `uvicorn --version`

**Uninstallation**

- Use `pip uninstall fastapi`
- Remove project dependencies using `pip freeze | grep fastapi` before uninstalling.

#### Create FastAPI Project

- **`app/`**: Create the main application directory.
- **`main.py`**: Create the entry point of the application.
- **`api/`**: Create versioned APIs.
- **`models/`**: Create database models.
- **`schemas/`**: Create Pydantic models.
- **`services/`**: Create business logic.
- **`config.py`**: Create configuration settings.
- **`database.py`**: Create database connections.
- **`middleware.py`**: Create custom middleware.

#### FastAPI Architecture

- FastAPI follows a modular architecture, allowing for easy scaling and maintenance.
- **APIRouter**: Used to define routes and group them logically.
- **Pydantic Models**: Used for data validation and serialization.
- **Dependency Injection**: Allows for reusable components like database connections or authentication mechanisms.
- **Middleware**: Used to process requests and responses globally before reaching routes.
- **ASGI Server**: FastAPI applications are served using ASGI servers like Uvicorn or Daphne.

#### Example: Function-Based Views (FBVs)

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}
```

#### Example: Class-Based Views (CBVs)

```python
from fastapi import FastAPI
from fastapi.views import View

app = FastAPI()

class HomeView(View):
    async def get(self, request):
        return {"message": "Hello, FastAPI!"}

app.add_route("/", HomeView.as_view())
```

#### URL Dispatcher

- FastAPI uses path operations to map URLs to functions.
- **Basic URL Configuration:**

  ```python
  from fastapi import FastAPI

  app = FastAPI()

  @app.get("/")
  async def read_root():
      return {"message": "Hello, FastAPI!"}
  ```

- Supports including multiple application URLs using `include_router()`.
- URL parameters can be captured using path parameters like `{id}`.

#### Testing FastAPI

- FastAPI provides a `TestClient` for testing endpoints.

  ```python
  from fastapi.testclient import TestClient
  from app.main import app

  client = TestClient(app)

  def test_read_root():
      response = client.get("/")
      assert response.status_code == 200
      assert response.json() == {"message": "Hello, FastAPI!"}
  ```

- Use `pytest` for writing and running tests.

Along with this, I explained SQL queries, joins and normalization in database to one of my co-trainees.

Later our whole python department had Ghughara Party (Specialty of Rajkot) and cutthroat foosball and table-tennis match.

So that's it for today. See you on Monday. Bye!

##### Dt. 28 Apr, 2025.

Today, I skimmed through FastAPI documentation, later I started watching [BitFumes FastAPI](https://www.youtube.com/watch?v=7t2alSnE2-I) video tutorial, recommended by my mentor.

I have discovered about Path and Query parameters along with Swagger UI provided by FastAPI. I have practised all this in [HelloWorld](/HelloWorld/) directory.

I will follow this documentation alongside - [Tiangolo](https://fastapi.tiangolo.com/python-types/#more-motivation) | [devdocs](https://devdocs.io/fastapi/tutorial/background-tasks/index#add-the-background-task)

So that's it for today. See you tomorrow. Bye!

##### Dt. 29 Apr, 2025.

Today, we will cover request body, pydantic schema and database connection from BitFumes Tutorial video.

Before that, I wanted to work on my problem solving skills in python, so I started solving problems on Hackerrank and I have successfully achieved 5 star.

Have a look - [Hackerrank Python 5 Star Gold badge](/images/Hackerrank_Python_Gold_badge.png)

Now I will continue with my FastAPI module.

I have covered request body, pydantic schema as well as creating database connection and Recipe model in it. I have implemented create operation and rest of CRUD I will perform tomorrow along with that I will add some notes for these topics.

I have practised them in [HelloWorld](/HelloWorld/) and [Recipe_CRUD](/Recipe_CRUD/) direcories.

Along with this, I helped one of the trainee with [Symmetric Tree Leetcode problem](https://leetcode.com/problems/symmetric-tree/) and few others with today's [POTD](https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/?envType=daily-question&envId=2025-04-29) on LeetCode.

So that's it for today. See you tomorrow. Bye!

##### Dt. 30 Apr, 2025.

Today, I have covered CRUD operations for Recipe model in SQLite, along with exceptions and status codes. Later I created User model using passlib library to hash passwords. I have also created response models and doc tags to partite Swagger doc routes. You can track my progress here - [Recipe_CRUD](/Recipe_CRUD/)

### Path Operations (Endpoints)

FastAPI allows defining endpoints using Python functions. Path parameters are specified in curly braces within the URL, while query parameters are declared with default or optional values in the function signature.

```python
@app.get("/items/{item_id}")
def read_item(item_id: int, name: str = None):
    return {"item_id": item_id, "name": name}
```

Supported HTTP methods include GET, POST, PUT, DELETE, and PATCH, each represented by decorators like `@app.get()`, `@app.post()`, etc.

```python
@app.post("/items/")
def create_item(item: dict):
    return item
```

To validate and serialize request and response data, FastAPI integrates Pydantic models.

```python
class Item(BaseModel):
    name: str
    description: str = None
    price: float

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    return item
```

### Data Validation with Pydantic

#### Data Modeling

Pydantic models are used to define and enforce data structures. Each model inherits from `BaseModel`.

```python
class User(BaseModel):
    id: int
    name: str
    email: str
```

#### Nested Models and Data Types

Nested models enable modeling of complex data structures using types like `List`, `Dict`, and `Optional`.

```python
class Address(BaseModel):
    city: str
    zip_code: str

class UserWithAddress(BaseModel):
    name: str
    addresses: List[Address]
```

#### Field Validation

Fields can be validated using `Field()` constraints and custom validation logic via `@validator`.

```python
class Product(BaseModel):
    name: str
    price: float = Field(gt=0)

    @validator('name')
    def not_empty(cls, v):
        if not v.strip():
            raise ValueError("Name cannot be empty")
        return v
```

### Database Integration

#### Database Options

FastAPI supports ORMs such as SQLAlchemy (sync) and Tortoise ORM (async). SQLAlchemy is widely used for production-grade applications.

#### Database CRUD Operations

CRUD operations are implemented using an ORM and the dependency injection system.

```python
@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserModel(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
```

#### Database Dependency

Database sessions are handled using dependencies that yield and close the session.

```python
engine = create_engine("sqlite:///./test.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### Error Handling and Responses

#### Custom Error Responses

Custom error messages can be defined in endpoint decorators using the `responses` parameter.

```python
@app.get("/items/{item_id}", responses={404: {"description": "Item not found"}})
def read_item(item_id: int):
    if item_id != 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}
```

#### HTTPException

The `HTTPException` class is used to raise HTTP errors explicitly.

```python
@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id}
```

#### Global Exception Handling

Global exception handlers allow central management of application-wide exceptions.

```python
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "An internal error occurred"},
    )
```

One key note - To create standalone application for fast development use FastAPI but in case of whole end-to-end setup use Django instead.
Mostly Data and ML departments make use of FastAPI and Azure services.

So that's it for today, I will be on academic leave tomorrow as I have external viva and submission at my college, wish me luck.
See you day after tomorrow. Bye!

##### Dt. 2 May, 2025.

I have completed the [Bitfumes Tutorial](https://www.youtube.com/watch?v=7t2alSnE2-I) at last. It has covered, Relationships, API Routers, JWT tokens and Authentication. Although I haven't implemented it yet.

#### Dependency Injection

FastAPI's dependency injection system enables the modular reuse of functionality across endpoints. Dependencies are declared as function parameters and are injected automatically.

```python
from fastapi import Depends

def get_token_header(token: str = ""):
    if token != "secret":
        raise HTTPException(status_code=403)
    return token

@app.get("/protected/")
def read_protected(token: str = Depends(get_token_header)):
    return {"message": "Access granted"}
```

Dependencies can encapsulate logic such as authentication, database sessions, and settings loading, promoting DRY principles.

##### Defining and Using Dependencies

Reusable functions are defined with optional logic, such as query parsing or validation. These are injected using `Depends`.

```python
def query_limit(limit: int = 10):
    return min(limit, 100)

@app.get("/items/")
def read_items(limit: int = Depends(query_limit)):
    return {"limit_used": limit}
```

##### Sub-dependencies

Dependencies can themselves rely on other dependencies. FastAPI resolves them recursively, supporting complex workflows.

```python
def get_db():
    db = "fake_db_connection"
    return db

def get_current_user(db=Depends(get_db)):
    return {"user": "admin", "db": db}

@app.get("/profile/")
def read_profile(user=Depends(get_current_user)):
    return user
```

#### Synchronous vs. Asynchronous

Synchronous functions block the server during I/O operations. Asynchronous (`async def`) functions allow the server to continue handling other requests, improving scalability. Use async for I/O-bound tasks (e.g., database, APIs), and sync for CPU-bound logic.

##### Async Endpoints

FastAPI supports native `async def` endpoints. Use them for non-blocking I/O operations.

```python
@app.get("/async-data/")
async def fetch_data():
    await asyncio.sleep(1)
    return {"message": "Non-blocking response"}
```

Async endpoints require using async-compatible libraries (e.g., HTTPX, async ORMs).

##### Performance and Concurrency

FastAPI is built on ASGI, allowing high concurrency using asynchronous I/O. Combined with Uvicorn or Hypercorn, FastAPI can handle thousands of simultaneous connections efficiently.

#### OAuth2 with Password (JWT)

FastAPI provides built-in support for OAuth2 and JWT authentication. Tokens are issued after successful login and used in the Authorization header of protected endpoints.

```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/users/me/")
def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"token": token}
```

A full implementation includes token generation and validation using libraries like `python-jose`.

##### Role-Based Access Control

Dependencies can restrict access based on user roles. A common pattern is to inject a user and check their role before proceeding.

```python
def get_admin_user(user=Depends(get_current_user)):
    if user["user"] != "admin":
        raise HTTPException(status_code=403)
    return user

@app.get("/admin/")
def read_admin_data(admin=Depends(get_admin_user)):
    return {"data": "Secret admin data"}
```

##### Security Best Practices

Security practices include:

- Hash passwords using `bcrypt` or `passlib`.
- Store only hashed passwords in the database.
- Use HTTPS to protect tokens in transit.
- Set short token expirations and implement refresh tokens.
- Never expose sensitive info in exceptions or logs.

```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def hash_password(password):
    return pwd_context.hash(password)
```

Later I read a few blogs to extend my knowledge sphere -

- [GFG - FastAPI Intro](https://www.geeksforgeeks.org/fastapi-introduction/)
- [Medium - FastAPI 101](https://medium.com/the-modern-scientist/fastapi-101-a-comprehensive-tutorial-for-building-lightning-fast-apis-90832b45579d)
- [GFG - Coroutine in python](https://www.geeksforgeeks.org/coroutine-in-python/)
- [Medium - FastAPI with MongoDB](https://medium.com/analytics-vidhya/fastapi-the-modern-age-api-framework-for-pythonista-4b2cd1e6652)
- [Medium - FastAPI Creator's Take](https://tiangolo.medium.com/introducing-fastapi-fdc1206d453f)
- [Medium - SQLAlchemy and Declarative_base](https://python.plainenglish.io/understanding-sqlalchemys-declarative-base-and-metadata-in-python-8eb0946b0eff)

_But Ramírez’s original ambition for the framework was much simpler: “I made it to please myself,” he says._ - [Sebastian Ramirez - Creator of FastAPI](https://www.sequoiacap.com/article/sebastian-ramirez-spotlight/)

##### Points to Note -

- **Relationships in FastAPI**: In FastAPI, relationships refer to how models (often SQLAlchemy models) are linked, such as **one-to-many** or **many-to-many** associations, which can be managed using foreign keys and ORM relationships.

* **JWT (JSON Web Token)** is commonly used for securely transmitting information between client and server, enabling stateless authentication.
* Authentication typically involves validating the JWT token to grant access to protected API endpoints.

* **API Router** in FastAPI allows for routing HTTP requests to specific functions, enabling cleaner and more maintainable code by organizing endpoints.

* **python-jose** is a library for working with JSON Web Tokens (JWT) in Python, providing encoding and decoding functionality for JWTs.

* **Motor** is an asynchronous MongoDB driver for Python, enabling non-blocking database interactions in async applications like FastAPI.

* **Uvicorn** is a fast ASGI server for Python that serves web applications built with frameworks like FastAPI and Starlette, supporting asynchronous features.

* **Starlette** is a lightweight ASGI framework used for building web applications and microservices, providing routing, middleware, and other components for asynchronous systems.

* **asyncio** is a Python module for writing concurrent code using the async/await syntax, enabling asynchronous programming for I/O-bound tasks.

* **UUID** is a 128-bit identifier used to uniquely identify information without relying on a central authority, ensuring uniqueness across distributed systems.

* **Alembic** is a lightweight database migration tool used with SQLAlchemy in FastAPI, helping to manage schema changes and migrations for databases.

I will be learning from ChatGPT from now on, here is the [link.](https://chatgpt.com/share/6814c713-84f8-8008-9730-b34d6798c90c)

I also had my project review done by my mentor, for [SimFood](https://github.com/Tanishqua-Simform/SimFood) Application, his feedback was positive and overall the review went great.

I wanted to have a change of mind, so i solved a LeetCode question on DFS - [PathSum](https://leetcode.com/problems/path-sum/description/)

So that's it for today. See you on Monday. Bye!
