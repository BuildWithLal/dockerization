from fastapi import FastAPI

app = FastAPI(
    title="Build With Lal",
    description="Ease your build!"
)

@app.get("/")
async def home():
    return {"success": True, "message": "Welcome to Build With Lal from ECS!"}