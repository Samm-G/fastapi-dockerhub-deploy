import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__=="__main__":
    # 0.0.0.0 means take the Localhost
    uvicorn.run(app, host="0.0.0.0",port=8000)