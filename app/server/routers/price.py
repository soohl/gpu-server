from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..database import database
from ..database import models
from .. import utilities

router = APIRouter()

############# CRUD OPERATION (CREATE PRICE) #############
@router.post("/gpu/price", tags=["price"])
async def add_gpu_price(id: str, price: models.Price = Body(...)):
    price_encoded = jsonable_encoder(price)
    price_encoded["date"] = utilities.get_today_date()
    result = await database.add_gpu_price(id, price_encoded)
    return result


############# CRUD OPERATION (READ PRICE) #############
@router.get("/gpu/price/", tags=["price"])
async def get_gpu_price(id: str):
    result = await database.get_gpu_price(id)
    return result


# ############# CRUD OPERATION (UPDATE PRICE) #############
# @router.put("/gpu/price/{id}", tags=["price"])
# async def update_gpu_price(id: str, price_data: models.PriceUpdate = Body(...)):
#     req = {k: v for k, v in price_data.dict().items() if v is not None}
#     result = await database.update_gpu_price(id, req)
#     return result


# ############# CRUD OPERATION (DELETE PRICE) #############
# @router.delete("/gpu/price/{id}", tags=["price"])
# async def delete_gpu_price(id: str, date: str):
#     result = await database.delete_gpu_price(id, date)
#     return result
