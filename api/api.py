from fastapi import APIRouter
from loguru import logger

from core.context_inference import context_inference
from core.inference import process_inference, general_inference
from helpers.response_template import success, bad_request
from model.inference_model import InferenceRequest, ContextSentimentRequest

api_router = APIRouter()




@api_router.post("/context-inference")
async def read_api_root(request: ContextSentimentRequest):
    try:
        result = context_inference(content_input=request.post, comment_input=request.comment)
        return success(message="Successfully", data=result)
    except Exception as e:
        logger.error(f"Error during core: {str(e)}")
        return bad_request(message="Failure", data=str(e))


@api_router.post("/inference")
def inference_endpoint(request: InferenceRequest):
    try:
        result = None
        if request.main_brand == "bank":
            result = process_inference(request.content_input, request.main_brand)
        result = general_inference(request.main_brand, request.content_input)
        print(result)

        return success(message="Successfully", data=result)
    except Exception as e:
        logger.error(f"Error during core: {str(e)}")
        return bad_request(message="Failure", data=str(e))
