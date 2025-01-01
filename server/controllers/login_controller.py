from fastapi.responses import JSONResponse
from services.login_service import login_check

def login_kam(data):
    if login_check(data):
        return JSONResponse(status_code=200, content={"message": "Login Successful"})
    else:
        return JSONResponse(status_code=401, content={"message": "Login Failed"})
