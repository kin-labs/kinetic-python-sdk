from fastapi import FastAPI
from kinetic_sdk.kinetic_sdk import KineticSdk

app = FastAPI()

sdk = KineticSdk()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/balance/{account}")
async def get_balance(account):
    return sdk.get_balance(account)

@app.get("/history/{account}/mint/{mint}")
async def get_history(account, mint):
    return sdk.get_history(account, mint)

@app.get("/get_token_accounts/{account}/mint/{mint}")
async def get_token_accounts(account, mint):
    return sdk.get_token_accounts(account, mint)