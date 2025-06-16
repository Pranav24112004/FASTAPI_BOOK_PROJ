# 📚 Bookly – A Simple FastAPI Project

Bookly is a minimal REST API built with **FastAPI** for managing a collection of books. It demonstrates clean structuring using `APIRouter`, `Pydantic` models, and in-memory data for CRUD operations.

---

## 🚀 Features

- ✅ List all books  
- 🔍 Get book by ID  
- ➕ Add a new book  
- 🛠 Update existing book  
- ❌ Delete book  

All operations are performed on a static in-memory list located in `book_data.py`.

---

## 📁 Project Structure

```
FASTAPI_POS/
├── env/                   # Virtual environment (ignored in .gitignore)
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── src/
    ├── __init__.py        # Main FastAPI app with routing setup
    └── books/
        ├── __init__.py
        ├── book_data.py   # Sample book list (5 books)
        ├── routes.py      # API routes for books
        └── schemas.py     # Request/response models using Pydantic
```


---

## 📝 Example Book Entry

```python
{
  "id": 1,
  "title": "Think Python",
  "author": "Allen B. Downey",
  "publisher": "O'Reilly Media",
  "published_date": "2021-01-01",
  "page_count": 1234,
  "language": "English"
}
```

---

## ⚙️ Installation & Setup

Clone the repository:

```bash
git clone [https://github.com/your-username/fastapi-bookly.git](https://github.com/your-username/fastapi-bookly.git)
cd fastapi-bookly
```

Create virtual environment:

```bash
python -m venv env
env\Scripts\activate   # On Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Server

```bash
uvicorn src:app --reload
```

Open in your browser:

* **Swagger Docs**: `http://127.0.0.1:8000/docs`
* **ReDoc**: `http://127.0.0.1:8000/redoc`

---

## 📦 Dependencies (`requirements.txt`)

Includes essential FastAPI, Pydantic, Uvicorn, and Starlette packages, among others.






