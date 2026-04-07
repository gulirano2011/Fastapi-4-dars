# 1️⃣ FastAPI kutubxonasini chaqiramiz
from fastapi import FastAPI
from pydantic import BaseModel

# 2️⃣ FastAPI ilovasini yaratamiz
app = FastAPI(
    title="FastAPI Interaktiv API Hujjatlari",
    description="Bu dastur Swagger UI (/docs) sahifasi orqali)"
)

# 3️⃣ Ma’lumot modelini yaratamiz (POST uchun)
class Foydalanuvchi(BaseModel):
    ism: str
    yosh: int

# 4️⃣ GET so‘rov — oddiy salomlashuv
@app.get("/")
def read_root():
    """
    Asosiy sahifa.
    Bu endpoint JSON formatda 'salom' so‘zini qaytaradi.
    """
    return {"salom": "FastAPI dunyosiga xush kelibsiz!"}

# 5️⃣ GET so‘rov — parametr bilan ishlash
@app.get("/salom/{ism}")
def salom_ber(ism: str):
    """
    Foydalanuvchining ismini qabul qiladi va unga salom beradi.
    """
    return {"xabar": f"Salom, {ism}!"}

# 6️⃣ POST so‘rov — ma’lumot yuborish
@app.post("/foydalanuvchi/")
def foydalanuvchi_qoshish(foydalanuvchi: Foydalanuvchi):
    """
    Yangi foydalanuvchi ma’lumotini qabul qilib, uni qaytaradi.
    """
    return {
        "xabar": f"Foydalanuvchi qabul qilindi!",
        "ma'lumot": foydalanuvchi
    }
