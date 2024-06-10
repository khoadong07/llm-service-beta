from http.client import HTTPException

from fastapi import APIRouter
from loguru import logger

from core.inference import process_inference
from helpers.response_template import success, bad_request
from model.inference_model import InferenceResponse, InferenceRequest

api_router = APIRouter()

# @api_router.get("/")
# async def read_api_root():
#     return {"message": "Welcome to the API"}
#
# @api_router.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id, "message": "Item retrieved successfully"}


@api_router.post("/inference")
def inference_endpoint(request: InferenceRequest):
    try:
        result = process_inference(request.content_input, request.main_brand)
        return success(message="Successfully", data=result)
    except Exception as e:
        logger.error(f"Error during core: {str(e)}")
        return bad_request(message="Failure", data=str(e))
