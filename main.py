from fastapi import FastAPI, Request
import httpx, os

app = FastAPI(title="apigee-mock-gateway")

PSG_URL = os.getenv("PSG_URL", "http://psg:8002")

@app.post("/api/account/load")
async def route_to_psg(request: Request):
    payload = await request.json()
    target = PSG_URL + "/route/account/load"
    async with httpx.AsyncClient() as client:
        resp = await client.post(target, json=payload, timeout=10.0)
    return resp.json()

@app.get("/health")
async def health():
    return {"status": "apigee-up"}
