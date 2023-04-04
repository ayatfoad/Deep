from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile

import uvicorn
# 1. Define an API object
app = FastAPI()
print(1)

# 2. Define data type
class Msg(BaseModel):
    msg: str


@app.post("/files")
async def UploadImage(file: bytes = File(...)):
    with open('image.jpg','wb') as image:
        image.write(file)
        image.close()
    return 'got it'
#
# # 3. Map HTTP method and path to python function
# @app.get("/")
# async def root():
#     return {"message": "Hello World. Welcome to the API home page!"}
#
#
# @app.get("/path")
# async def function_demo_get():
#     return {"message": "This is /path endpoint, use post request to transform text to uppercase"}
#
#
# @app.post("/path")
# async def function_demo_post(inp: Msg):
#     return {"message": inp.msg.upper()}
#
#
# @app.get("/path/{path_id}")
# async def function_demo_get_path_id(path_id: int):
#     return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}

if __name__== "__main__":
    uvicorn.run(app, host="0.0.0.0" , port=8000)

print(2)