## const express = require("express")
from fastapi import FastAPI
import uvicorn

## Create the App object
## const app = express()
app = FastAPI()

## app.listen(4000, () => ...)
uvicorn.run(app, port=4000)