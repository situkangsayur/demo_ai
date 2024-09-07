from pydantic import BaseModel

class Predict(BaseModel):
    home_area: int
