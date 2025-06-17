from fastapi import APIRouter, HTTPException
from models.admin import login_admin, get_all_cars, add_car
from pydantic import BaseModel

router = APIRouter(prefix="/admin", tags=["Admin"])

class AdminLogin(BaseModel):
    username: str
    password: str

class NewCar(BaseModel):
    model: str
    image_url: str
    price_per_day: float
    status: str = "available"

@router.post("/login")
def admin_login(data: AdminLogin):
    admin = login_admin(data.username, data.password)
    if admin:
        return {"message": "Login successful", "admin": admin}
    raise HTTPException(status_code=401, detail="Invalid admin credentials")

@router.get("/cars")
def view_all_cars():
    return get_all_cars()

@router.post("/cars")
def add_new_car(data: NewCar):
    success = add_car(data.model, data.image_url, data.price_per_day, data.status)
    if success:
        return {"message": "Car added successfully"}
    raise HTTPException(status_code=400, detail="Failed to add car")
