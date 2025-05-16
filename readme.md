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

### Dependency Injection

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

#### Sub-dependencies

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

### Synchronous vs. Asynchronous

Synchronous functions block the server during I/O operations. Asynchronous (`async def`) functions allow the server to continue handling other requests, improving scalability. Use async for I/O-bound tasks (e.g., database, APIs), and sync for CPU-bound logic.

#### Async Endpoints

FastAPI supports native `async def` endpoints. Use them for non-blocking I/O operations.

```python
@app.get("/async-data/")
async def fetch_data():
    await asyncio.sleep(1)
    return {"message": "Non-blocking response"}
```

Async endpoints require using async-compatible libraries (e.g., HTTPX, async ORMs).

#### Performance and Concurrency

FastAPI is built on ASGI, allowing high concurrency using asynchronous I/O. Combined with Uvicorn or Hypercorn, FastAPI can handle thousands of simultaneous connections efficiently.

### OAuth2 with Password (JWT)

FastAPI provides built-in support for OAuth2 and JWT authentication. Tokens are issued after successful login and used in the Authorization header of protected endpoints.

```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/users/me/")
def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"token": token}
```

A full implementation includes token generation and validation using libraries like `python-jose`.

#### Role-Based Access Control

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

#### Security Best Practices

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

#### Points to Note -

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

##### Dt. 5 May, 2025.

Today, I have completed brief overview for all topics given on LMS. You can find the link to [ChatGPT](https://chatgpt.com/share/6814c713-84f8-8008-9730-b34d6798c90c) here.

Later, I implemented JWT authentication and authorization as well as password hashing for security. [JWT-Auth](/JWT_Auth/)

I have also solved a problem on DP on Leetcode - [House Robber](https://leetcode.com/problems/house-robber/description/)

It was quite stormy today, such a lovely atmosphere. It saved us from the scorching heat of May.

That's it for today. See you tomorrow. Bye!

##### Dt. 6 May, 2025.

Today, I have started watching a video tutorial on youtube [FastAPI - Ssali Jonathan](https://www.youtube.com/watch?v=TO4aQ3ghFOc)

I have completed 3 hours and notes of the Video are as follows -

- `pip install fastapi[standard]` installs FastAPI with CLI and common extras like `uvicorn`, `httpx`, and `jinja2`.
- `fastapi run` or `fastapi dev` starts the development server using CLI from FastAPI’s standard installation.
- HTTP clients like **Postman** and **Restfox** are used to test and send HTTP requests to FastAPI endpoints.

#### Introduction and Project Setup

- **Installation**: Use `pip install fastapi[standard]` and `pip install uvicorn` (if needed) to set up FastAPI.

- **Path parameter**: Passed directly in the URL, e.g., `/items/{id}`.

- **Query parameter**: Passed after `?` in URL, e.g., `/items?limit=10`; optional with default values.

- **Request Body**: Use Pydantic models to accept structured JSON data in the request body.

- **Path handler function**: Python function mapped to HTTP methods using decorators like `@app.get()`.

- **Type hints**: Specify expected types for FastAPI to auto-validate and document (e.g., `name: str`).

- **Annotated, Union, Optional, Depends**:

  - `Annotated`: Adds metadata to type hints.
  - `Union`: Accepts multiple types.
  - `Optional`: Allows `None` as a valid value.
  - `Depends`: Injects dependencies into routes/functions.

- **Serialization module / schema / Pydantic model**: Used to validate request/response data and serialize models.

- **Header function**: Use `Header` class to read header values from incoming requests.

- **Status code**: Set using `status_code=...` or `from fastapi import status`.

#### Building CRUD in REST API

- **Return type**: Declare with type hints (e.g., `-> dict`, `-> List[Item]`) for clarity and docs.

- **Response model**: Use `response_model=Model` to define the shape of the response data.

- **Typing module**: Use `List`, `Dict`, `Optional`, etc., from `typing` for type annotations.

- **Validation using Pydantic model**: Ensures data shape and constraints before processing request.

- **HTTPException**: Raise with `status_code` and `detail` to return custom error responses.

#### File Structure and Routers

- **Make modular by creating modules**: Separate logic into reusable files (models, schemas, services).

- **Make Python folders as packages with `__init__.py`**: Allows module imports and proper packaging.

- **schemas - Pydantic models**: Define request and response data shapes.

- **models - SQLAlchemy ORM models**: Define database table structure and relationships.

- **routes - API Endpoints**: Define API paths and connect them with handlers.

- **Use `include_router`, `tags`, and `prefix`**: Organize endpoints and group by function/version.

- **Do proper versioning**: e.g., `/api/v1/users` for maintainable APIs.

#### Databases with SQLModel

- **ORM**: Object Relational Mapping; interacts with DB using Python objects.

- **`.env` for secret keys**: Store DB URLs, JWT secrets, etc., securely.

- **`pip install asyncpg`**: Required for async PostgreSQL drivers.

- **`pip install pydantic-settings`**: Manage and load `.env` into Pydantic settings.

- **config.py**: Central location to load and access environment variables.

- **AsyncEngine of SQLAlchemy**: Enables non-blocking DB communication using `create_async_engine`.

- **Lifespan**: Manages startup/shutdown events with FastAPI’s app lifecycle.

- **contextlib, asynccontextmanager, coroutine**: Handle async resource setup/teardown using `@asynccontextmanager`.

- **uuid**: Use `uuid4()` for generating unique identifiers.

- **Field**: Customize column defaults, constraints, and metadata in SQLModel.

#### Finishing Up CRUD

- **service.py - function handler of API endpoints**: Business logic layer separating routes and DB operations.

- **AsyncSession**: Non-blocking DB session used with SQLAlchemy’s async engine.

- **Select(), order_by(), where(), session.exec(statement), first(), session.add(), session.commit(), setattr(), session.delete()**: SQLModel query and mutation methods for async CRUD operations.

Later, I solved a question on strings on LeetCode - [Length of last word](https://leetcode.com/problems/length-of-last-word/description/)

Watching the video got very monotonous, so i challenged myself by giving a quiz - [FastAPI Quiz](https://chatgpt.com/share/681a0f7a-4588-8008-9c1c-0696c60ae662)

Ahh, it started raining here, gotta reach home safe now. Alright, that's it for today, see you tomorrow. Bye!

##### Dt. 8 May, 2025.

I reached home safely that night, although it rained heavily yesterday, due to which roads were clogged with water, so we trainees were provided a leave for the day.

Today, I continued with doing those quiz rounds - [FastAPI Quiz](https://chatgpt.com/share/681a0f7a-4588-8008-9c1c-0696c60ae662)

Later, I watched the video by [Ssali Jonathan](https://www.youtube.com/watch?v=TO4aQ3ghFOc) for 30 mins but I felt more like implementing rather than watching, so I started working on 1st POC - To Do List Api, given on LMS. -> [FastAPI-POC](https://github.com/Tanishqua-Simform/FastAPI-POC)

One of my co-trainee was facing issue with circular import error, when initializing the package. So we discussed a work-around for that and solved the error together.

So that's it for today. See you tomorrow. Bye!

##### Dt. 9 May, 2025.

I have some news, so yesterday at 9 PM war has been initiated between India and its Neighbouring Country. As of now India has been victorious in intercepting the enemy's drone attacks. Let's see what the future holds for us.

So, today I have completed the POC-1 task -> [FastAPI-POC](https://github.com/Tanishqua-Simform/FastAPI-POC)

Later I did pair-programming with one of my co-trainee which helped us share our insights of FastAPI mutually. I have learnt about Newly added execute method in sqlachemy and that what I had been using - query method, is now just a legacy method.

We gave in a lot of time in understanding of 'orm_mode = True' configuration of pydantic schema, but it bear us no fruit. We concluded that it may have been resolved in newer releases of Pydantic but we'll still inquire with our mentor about the same.

Also, I was given the feedback of evaluation-2 by my mentor. He said that feedback is positive and we just need to broaden our knowledge on ORM and SQL, rest everything was perfect.

So that's it for today, I will complete POC-2 on Monday. Bye.

##### Dt. 12 May, 2025.

Today, I have completed the required tasks for POC-2 given on LMS -> [FastAPI-POC](https://github.com/Tanishqua-Simform/FastAPI-POC)

But I wish to implement few more concepts just to practice, which I will complete tomorrow.

During today's meet, my mentor advised us to keep following things in mind while coding in any framework -

- Add Docstring in every function -> Information, Arguments, Returns, Raises
- Add try and except blocks to handle breaking of code.
- Add as many comments as possible
- `# TODO: Description of task to be done later in code` -> Mark this in code as a good practice [Very imp]

I found these resources helpful -

- [Solving Circular Import Error in Pydantic Relationships](https://stackoverflow.com/questions/69042316/defining-fastapi-pydantic-many-to-many-relationships)
- [Video - Sqlalchemy Relationships](https://www.youtube.com/watch?v=3N9JqtpkFJI)

So that's it for today, see you tomorrow. Bye!

##### Dt. 13 May, 2025.

Today, I have created [InstaClone](/InstaClone/) to implement image uploading and alembic for migrations.

I have configured alembic and Postgres db, but alembic was not creating tables in db although it was changing versions, so I will solve this issue tomorrow.

I found these resources helpful while development -

- [Sqlalchemy Driver Error](https://stackoverflow.com/questions/15648814/sqlalchemy-exc-argumenterror-cant-load-plugin-sqlalchemy-dialectsdriver)
- [Medium - Alembic + FastAPI](https://medium.com/@alonskii44/using-alembic-with-fastapi-python-application-and-mysql-database-for-data-migration-e356bea9285)
- [Medium - Alembic in FastAPI Configuration detailed](https://medium.com/@hasanmahira/fastapi-with-sqlalchemy-postgresql-and-alembic-1ccaba79572e)
- [Medium - Amazon S3 Bucket Setup](https://medium.com/@thilinawaks/setup-aws-s3-bucket-for-storing-files-images-90cbcc7558d7)

Also, I am going to box cricket match with our Python team.

So, that's it for today, see you tomorrow. Bye!

##### Dt. 14 May, 2025.

The issue in alembic that I am facing is, when I autogenerate migrations it does not modify upgrade function inside version file. I got to know about this issue by reading the docs - [Alembic Auto generate migrations](https://alembic.sqlalchemy.org/en/latest/autogenerate.html)

Yippee, we have solved the error, so the problem was arising from Base.metadata which i was importing in env file. Somehow when I declared Base inside models file, it started detecting the changes. [Stackoverflow - Alembic Quick Overview](https://stackoverflow.com/questions/30425214/what-is-the-difference-between-creating-db-tables-using-alembic-and-defining-mod)

I wanted to integrate Amazon S3 bucket, but did not want to add billing information in registration so finding a workaround now.

I have found MinIO, which mocks Amazon S3 API but in local server. Boto3 is an AWS SDK for python, which we have used to create S3 client for uploading files on MinIO server.

We need to install minIO with following commands -

- Installation - wget https://dl.min.io/server/minio/release/linux-amd64/minio
- Making command executable - chmod +x minio
- Moving minio to global environment - sudo mv minio /usr/local/bin/
- Changing minio user - export MINIO_ROOT_USER=admin
- Changing minio password - export MINIO_ROOT_PASSWORD=admin
- Running the MinIO Server - minio server directory-name

Later, I installed python-multipart package, for uploading files from APIs, with help of docs - [Fastapi - File upload](https://fastapi.tiangolo.com/tutorial/request-forms-and-files/)

In [InstaClone](/InstaClone/), I have integrated alembic and image/video uploading feature. Tomorrow I will work on relationship between user and posts.

So that's it for today, see you tomorrow. Bye!

##### Dt. 15 May, 2025.

Today, I started by going through Regular expressions as I needed to validate email id, I found this article concise and easy to understand - [GFG - Regex](https://www.geeksforgeeks.org/write-regular-expressions/)

While migrating to postgres, I faced an issue regarding Enums, where Alembic was throwing type error. I made a silly mistake I was using snake casing in Enum Class when I should have used Pascal Case instead, so it was causing some error internally for Alembic. I don't know how, but I case it solved the issue.

I have watched a tutorial [Video - Sqlalchemy ORM](https://www.youtube.com/watch?v=XWtj4zLl_tg) for 35 mins and started implementing relationships for User, Post and Comments in my [InstaClone](/InstaClone/).

I have faced lots of recurring issues in Alembic, but with every error solved I feel like I am understanding more about How it works.

Note - Alembic has a certain down points that it cannot detect renaming of columns and tables, rather it performs addition with new_name and deletion of column with old_name, so instead it is recommended to do so manually in the database.

Later, I learnt about Background Tasks, Email sending and Jinja Templates, the notes are as follows -

### Background Tasks for sending Email with Jinja2 template

Using background tasks, the email will be sent asynchronously in the background without blocking the response to the user.

1. **Install Dependencies**

```bash
pip install fastapi jinja2 aiosmtplib email-validator python-multipart
```

2. **Folder Structure**

```
.
├── main.py
└── templates
    └── email.html
```

3. **`templates/email.html`**

```html
<!DOCTYPE html>
<html>
  <body>
    <h2>Hello {{ user_name }}!</h2>
    <p>Welcome to our service.</p>
  </body>
</html>
```

4. **`main.py` with BackgroundTask**

```python
from fastapi import FastAPI, BackgroundTasks, Form
from jinja2 import Environment, FileSystemLoader
from email.message import EmailMessage
import aiosmtplib

app = FastAPI()

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader("templates"))

async def send_email_background(user_email: str, user_name: str):
    # Render the Jinja2 template
    template = env.get_template("email.html")
    html_content = template.render(user_name=user_name)

    # Create email message
    message = EmailMessage()
    message["From"] = "your_email@example.com"
    message["To"] = user_email
    message["Subject"] = "Welcome!"
    message.set_content("This is a fallback plain text.")
    message.add_alternative(html_content, subtype="html")

    # Send the email (via SMTP)
    await aiosmtplib.send(
        message,
        hostname="smtp.example.com",  # Your SMTP server
        port=587,
        start_tls=True,
        username="your_email@example.com",  # Your email
        password="your_password",  # Your password
    )

@app.post("/send-email/")
async def send_email(user_email: str = Form(...), user_name: str = Form(...), background_tasks: BackgroundTasks):
    # Add the send_email_background task to be run in the background
    background_tasks.add_task(send_email_background, user_email, user_name)

    return {"message": "Email will be sent in the background!"}
```

5. **Explanation**

- **`send_email_background`**: This is the background function that sends the email. It uses **Jinja2** to render the HTML content and **aiosmtplib** to send the email asynchronously.

- **`background_tasks.add_task(...)`**: This adds the `send_email_background` function to the background tasks. It won't block the main thread while sending the email.

- **`BackgroundTasks`**: FastAPI's built-in `BackgroundTasks` allows you to execute code in the background while returning a response to the client immediately.

7. **Test the Background Task**

You can test this via a **POST request** (using Postman or curl):

- **URL**: `http://localhost:8000/send-email/`
- **Form Data**:

  - `user_email`: `recipient@example.com`
  - `user_name`: `John Doe`

FastAPI will respond immediately with a message saying the email is being sent in the background.

#### Miscellaneous Topics -

**CORS**:

- FastAPI provides built-in support for **Cross-Origin Resource Sharing (CORS)**. Use the `CORSMiddleware` to enable CORS for your FastAPI application, allowing cross-origin requests from specified domains.

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins or specify a list
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
```

**State**:

- The `state` object in FastAPI allows you to store application-level variables or objects that can be accessed globally throughout the lifecycle of the app. It’s useful for storing things like database connections, external service clients, etc.

```python
app.state.db = some_database_connection
```

**Headers as Response**:

- FastAPI allows you to include custom headers in the response using `Response` or `JSONResponse`. This is useful for controlling caching, authentication tokens, or any custom headers.

```python
from fastapi import Response

@app.get("/items/")
async def get_items():
    headers = {"X-Custom-Header": "value"}
    return Response(content="Items list", headers=headers)
```

**Pydantic Validations**:

- FastAPI leverages **Pydantic** models for data validation. These models are used for request bodies, query parameters, and more. FastAPI automatically validates the data according to the defined Pydantic schema, raising a 422 error if validation fails.

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    description: str = None

@app.post("/items/")
async def create_item(item: Item):
    return {"item": item}
```

I also spent good amount of time playing quiz with ChatGPT on various subjects of FastAPI and it's prerequisites. I find that intriguing and rewarding at the same time.

So, that's it for today, see you tomorrow. Bye!

##### Dt. 16 May, 2025.

Few advance concepts of FastAPI are -

### Caching

- Use caching to store expensive computations or repeated query results.
- Use third-party libraries like `fastapi-cache2`, `aiocache`, or `redis`.

```bash
pip install fastapi-cache2 redis
```

```python
from fastapi import FastAPI
from fastapi_cache2 import FastAPICache
from fastapi_cache2.backends.redis import RedisBackend
from redis import asyncio as aioredis
from fastapi_cache2.decorator import cache

app = FastAPI()

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

@app.get("/items")
@cache(expire=60)
async def get_items():
    return {"data": "cached response"}
```

### Throttling

- Use `slowapi` for rate-limiting requests per client.
- Install: `pip install slowapi`

```python
from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/limited")
@limiter.limit("5/minute")
async def limited_view(request: Request):
    return {"message": "allowed"}
```

### Pagination

- Basic pagination using query parameters (`skip`, `limit`).
- Use Pydantic response models to return metadata.

```python
from fastapi import FastAPI, Query
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str

@app.get("/items/", response_model=List[Item])
async def read_items(skip: int = 0, limit: int = 10):
    items = [{"id": i, "name": f"Item {i}"} for i in range(1, 101)]
    return items[skip: skip + limit]
```

- For advanced pagination, use `fastapi-pagination`:

```bash
pip install fastapi-pagination
```

```python
from fastapi_pagination import Page, add_pagination, paginate

@app.get("/paginated-items/", response_model=Page[Item])
async def get_paginated_items():
    items = [{"id": i, "name": f"Item {i}"} for i in range(1, 101)]
    return paginate(items)

add_pagination(app)
```

### Mount Subapps

- Mount multiple FastAPI apps under one main app for modular architecture.

```python
from fastapi import FastAPI

main_app = FastAPI()
sub_app = FastAPI()

@sub_app.get("/info")
async def info():
    return {"subapp": "info"}

main_app.mount("/sub", sub_app)
```

- Access `GET /sub/info` for subapp routing.

### ORM

- Use SQLAlchemy or SQLModel for ORM.
- Include joins, group by, optimization techniques.

```python
from sqlmodel import SQLModel, Field, select, Session, create_engine, Relationship

class Author(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    books: list["Book"] = Relationship(back_populates="author")

class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    author_id: int = Field(foreign_key="author.id")
    author: Author = Relationship(back_populates="books")

engine = create_engine("sqlite:///db.sqlite3")
SQLModel.metadata.create_all(engine)
```

- Group By:

```python
from sqlalchemy import func

def get_book_counts(session: Session):
    statement = select(Author.name, func.count(Book.id)).join(Book).group_by(Author.name)
    return session.exec(statement).all()
```

- Query Optimization:

  - Use `.options(selectinload(...))` or `.options(joinedload(...))` to reduce queries.
  - Use indexes on frequently filtered fields.
  - Avoid N+1 problem by eager loading.

- Select Related (eager loading):

```python
from sqlalchemy.orm import selectinload

def get_authors_with_books(session: Session):
    stmt = select(Author).options(selectinload(Author.books))
    return session.exec(stmt).all()
```

- Prefetch Related (for reverse relationships):

```python
# Use selectinload on the reverse relationship to fetch children efficiently
stmt = select(Author).options(selectinload(Author.books))
```

- Filtering:

```python
stmt = select(Book).where(Book.title.contains("FastAPI"))
```

- Ordering:

```python
stmt = select(Book).order_by(Book.title.desc())
```

- Limit and Offset:

```python
stmt = select(Book).offset(0).limit(10)
```

#### Python Decouple (Instead of os and dotenv)

- **Purpose**: Used to separate configuration (like secrets, API keys, DB URLs) from source code.

- **Installation**:

  ```bash
  pip install python-decouple
  ```

- **.env File**: Create a `.env` file to store environment variables (not committed to version control).

  ```
  DEBUG=True
  SECRET_KEY=mysecret
  DATABASE_URL=postgresql://user:pass@localhost/dbname
  ```

- **Usage in Code**:

  ```python
  from decouple import config

  DEBUG = config('DEBUG', cast=bool)
  SECRET_KEY = config('SECRET_KEY')
  DATABASE_URL = config('DATABASE_URL')
  ```

- **Type Casting**: Automatically cast variables to `bool`, `int`, `float`, etc. using `cast=...`.

  ```python
  TIMEOUT = config('TIMEOUT', cast=int)
  ```

- **Default Values**: Provide fallback if variable not found.

  ```python
  MODE = config('MODE', default='production')
  ```

- **Security**: Keeps secrets out of source code and GitHub; use `.gitignore` to exclude `.env`.

- **Integration**: Commonly used in FastAPI, Django, and other Python web frameworks for managing configurations.

I had a sync-up meet with my mentor in which we discussed about the alembic issue that I had faced and how I resolved them, later he reviewed the relationships I have created in [InstaClone](/InstaClone/) directory.

Although, I have a few pending tasks to be implemented in InstaClone, which I will keep working on later.

I gave in a lot of my time in POCs. I have refactored the code in multiple files as per requirement. I have added metadata for Swagger docs, as well as docstrings to make the code readable. Then, I created its readme and now it is ready.

You can have a look at the POCs here -> [FastAPI-POC](https://github.com/Tanishqua-Simform/FastAPI-POC)

So that's it for this repo. See you on Monday, with a new course. Bye!

###### With this we come to an end for our FastAPI Course (Learning duration - 14 days)
