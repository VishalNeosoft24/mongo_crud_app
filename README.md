# 🚀 FastAPI MongoDB CRUD API

A simple CRUD (Create, Read, Update, Delete) REST API built with **FastAPI** and **MongoDB**, with a web-based admin UI via **mongo-express**.  
Ideal for testing MongoDB connectivity, API development, or containerized backend setups.

---

## 🛠 Tech Stack

- **FastAPI** – High-performance Python web framework
- **MongoDB** – NoSQL database
- **Pymongo** – MongoDB driver for Python
- **mongo-express** – Web-based admin interface for MongoDB
- **Docker** – (optional) for containerized development

---

## 📦 Features

✅ Create item  
✅ Read all items  
✅ Read item by ID  
✅ Update item  
✅ Delete item  
✅ Swagger UI for API testing  
✅ Mongo Express UI for DB browsing

---

## 📁 Project Structure

```
.
├── src/
│   ├── main.py          # FastAPI app and routes
│   ├── models.py        # Pydantic models
│   ├── crud.py          # CRUD logic
│   └── database.py      # MongoDB connection logic
├── .env                 # Environment variables (Mongo credentials)
├── requirements.txt     # Python dependencies
└── README.md            # Project overview
```

---

## ⚙️ Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/fastapi-mongo-crud.git
cd fastapi-mongo-crud
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create .env File

Create a `.env` file in the root directory:

```env
MONGO_USERNAME=your_user
MONGO_PASSWORD=your_pass
DB_NAME=testdb
MONGO_HOST=localhost
MONGO_PORT=27017
```

> 💡 If using Docker, `MONGO_HOST` can be:
>
> - `host.docker.internal` (macOS/Windows)
> - `172.17.0.1` (Linux)

### 4. Run the FastAPI App

```bash
uvicorn src.main:app --reload
```

API will be available at:  
📍 http://localhost:8000  
Swagger UI:  
📍 http://localhost:8000/docs

---

## 🐳 Docker Setup

### 1. Build Docker Image

```bash
docker build -t fast_mongo_app:1.0 .
```

### 2. Run FastAPI Container

```bash
docker run --name fast_mongo_container -p 8000:8000 --env-file .env fast_mongo_app:1.0
```

---

## 🧪 Mongo Express UI

Mongo Express is available at:  
📍 http://localhost:8081

---

## 🧾 Sample API Endpoints

| Method | Endpoint      | Description    |
| ------ | ------------- | -------------- |
| POST   | `/items/`     | Create item    |
| GET    | `/items/`     | Get all items  |
| GET    | `/items/{id}` | Get item by ID |
| PUT    | `/items/{id}` | Update item    |
| DELETE | `/items/{id}` | Delete item    |
