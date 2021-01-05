def saveResultToFile(taskId, result):
    with open("data.txt", "a+") as dataFile:
        dataFile.write(f"{taskId} - {result}\n")  