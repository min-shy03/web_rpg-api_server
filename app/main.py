from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="WEB_RPG API", version="1.0.0")

# CORS 설정 (프론트엔드 React 연동 대비)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # 어느 서버에서 요청을 보내던 허용
    allow_credentials=True,
    allow_methods=["*"],    # HTTP method 모든 방식 허용
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to RPG World!"}

@app.get("/api/v1/health")
async def health_check():
    return {"status": "alive", "version": "v1"}