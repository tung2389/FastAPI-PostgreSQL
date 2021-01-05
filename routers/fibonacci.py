from fastapi import APIRouter, HTTPException, Depends
from utilities.jwtAuthenticate import authenticate
from service.tasks import calcFibonacci
from model.fibonacciModel import FibonacciModel

router = APIRouter()

@router.post("/", status_code = 200)
async def calc_fibonacci(req: FibonacciModel, authorized: bool = Depends(authenticate)):
    number = req.number
    task = calcFibonacci.delay(int(number))
    return {
        'taskId': task.id
    }

@router.get("/{taskId}", status_code = 200)
async def get_fibonacci(taskId: int, authorized: bool = Depends(authenticate)):
    with open("data.txt", "r") as dataFile:
        for line in dataFile:
            if line.split()[0] == taskId:
                return {
                    'result': line.split()[2]
                }
            else:
                raise HTTPException(
                    status_code = 400,
                    detail = "Not available"
                )


