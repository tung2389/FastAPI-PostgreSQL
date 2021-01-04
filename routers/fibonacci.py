from fastapi import APIRouter

router = APIRouter()

@router.post("/fibonacci", tags = ["fibonacci"])
async def calc_fibonacci():
    return {"test"}

@router.get("/fibonacci/{taskId}", tags = ["fibonacci"])
async def get_fibonacci(taskId: int):
    return {taskId}

