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
