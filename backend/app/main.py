from fastapi import FastAPI
from app.routers import query_router

app = FastAPI()

# Include the router for query-related endpoints
app.include_router(query_router.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the RAG backend API"}
