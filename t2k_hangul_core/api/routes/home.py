from fastapi import APIRouter, Response

router = APIRouter(
    prefix="/home",
    tags=["home"],
    responses={404: {"description": "Not found"}}
)


@router.get("/")
async def home():
    return {"hello": "world"}
    # Response(
    #     content={"hello": "world"},
    #     media_type="application/json"
    # )
