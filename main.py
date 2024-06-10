from fastapi import FastAPI

from api.api import api_router

app = FastAPI()

# Root path
@app.get("/")
async def read_version():
    return {"message": "v1.2.beta"}

# Include the API router with a prefix
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
