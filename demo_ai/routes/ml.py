from fastapi import APIRouter

from demo_ai.cases.linear_regression import LinearRegression
from demo_ai.schemas.ml import Predict
ml = APIRouter()


@ml.post('/')
def predict(predict_data: Predict):
    algo = LinearRegression(1.24, 0.24)

    algo.load_model("demo_ai/model.json")
    result = algo.predict(predict_data.home_area / 100)
    return {"message": "success",
            "price prediction": result}

