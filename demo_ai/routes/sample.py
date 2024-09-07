from fastapi import APIRouter, Depends, HTTPException, Response, status

sample_route = APIRouter()


@sample_route.get('/')
def healthcheck():
    return {"message": "Welcome to demo sample API with sqlalchemy"}


