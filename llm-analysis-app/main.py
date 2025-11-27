from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

SECRET = "SkyQuiz2025!"  # SAME as in Google Form

@app.post("/")
async def solve_quiz(req: Request):
    try:
        data = await req.json()
    except:
        return JSONResponse(status_code=400, content={"error": "Invalid JSON"})
    
    if data.get("secret") != SECRET:
        return JSONResponse(status_code=403, content={"error": "Invalid secret"})

    return JSONResponse(status_code=200, content={
        "message": "Quiz request received",
        "email": data.get("email"),
        "note": "Automation placeholder active"
    })
