from fastapi import FastAPI

import src.controllers.person_controller as routes

app = FastAPI()

app.include_router(routes.person)
