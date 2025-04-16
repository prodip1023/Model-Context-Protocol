from fastmcp import FastMCP
from fastapi import FastAPI,Body
import uvicorn

app = FastAPI()
mcp = FastMCP("demo server for test")

@mcp.tool()
def multiply(a,b):
    return a*b
@app.post("/prodip/mcp/multiply")
def call_multiply(data:dict=Body(...)):
    return {"result":multiply(data.get("a",0),data.get("b",0))}
@app.get("/")
def home():
    return {"message": "Welcome to the FastMCP demo server!"}


if __name__ =="__main__":
    uvicorn.run(app=app,host="127.0.0.1",port=8089)
