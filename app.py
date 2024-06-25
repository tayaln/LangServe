from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
from langchain_community.chat_models import ChatOpenAI
import uvicorn
import os

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

#This initializes a FastAPI application with a title, version, and description. The app will serve as the main entry point for your API.
app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)

#This adds a route to the FastAPI app.
add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

model=ChatOpenAI()
prompt=ChatPromptTemplate.from_template("provide me an essay about {topic}")
prompt1=ChatPromptTemplate.from_template("provide me a poem about {topic}")

#These lines add two more routes to the FastAPI app
add_routes(
    app,
    prompt|model,
    path="/essay"

)

add_routes(
    app,
    prompt1|model,
    path="/poem"

)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)