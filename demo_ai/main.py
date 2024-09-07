from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from demo_ai.routes.ml import ml
from demo_ai.routes.sample import sample_route

app = FastAPI()

origins = [
    'http://localhost:8008'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(sample_route, tags=['sample'], prefix='/api/v1/healthcheck')
app.include_router(ml, tags=['Home Price'], prefix='/api/v1/home_price')


