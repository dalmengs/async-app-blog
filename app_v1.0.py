from fastapi import FastAPI
from Model.SignupRequestModel import SignupRequestModel
from Dto.BaseResponseDto import BaseResponseDto
from Logic.logic import *
import uvicorn

app = FastAPI()


@app.post("/api/v1/signup")
async def signup(signup_model: SignupRequestModel):
    await username_check()
    await password_validation()
    await password_encrypt()
    await create_user()
    await send_message()
    await send_email()
    return BaseResponseDto.ok()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8787)
