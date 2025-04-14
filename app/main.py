from fastapi import FastAPI
# import rasterio 
from rasterio.features import geometry_mask

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
