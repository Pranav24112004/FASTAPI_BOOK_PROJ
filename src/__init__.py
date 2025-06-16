from fastapi import FastAPI
from src.books.routes import book_router

version ="v1"

app=FastAPI(
    title="Bookly",
    description="A RESTAPI for book review web service",
    version=version
)

app.include_router(book_router, prefix="/api/{version}/books", tags=['books'])