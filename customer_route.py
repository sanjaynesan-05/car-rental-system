from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models.customer import (
    login_customer, book_car, get_rentals_by_customer,
    cancel_rental, get_all_available_cars
)

router = APIRouter(prefix="/customer", tags=["Customer"])

# Request models
class CustomerLogin(BaseModel):
    customer_id: int
    phone: str

class BookingRequest(BaseModel):
    customer_id: int
    car_id: int
    rental_date: str  # e.g., '2024-04-10'
    days_rented: int

# Routes
@router.post("/login")
def customer_login(data: CustomerLogin):
    customer = login_customer(data.customer_id, data.phone)
    if customer:
        return {"message": "Login successful", "data": customer}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@router.post("/book")
def book_car_route(data: BookingRequest):
    success = book_car(data.customer_id, data.car_id, data.rental_date, data.days_rented)
    if success:
        return {"message": "Car booked successfully"}
    raise HTTPException(status_code=400, detail="Booking failed")

@router.get("/{customer_id}/rentals")
def view_rentals(customer_id: int):
    rentals = get_rentals_by_customer(customer_id)
    if rentals:
        return rentals
    raise HTTPException(status_code=404, detail="No rentals found")

@router.delete("/{customer_id}/rental/{rental_id}")
def cancel_booking(customer_id: int, rental_id: int):
    success = cancel_rental(rental_id, customer_id)
    if success:
        return {"message": "Rental cancelled successfully"}
    raise HTTPException(status_code=400, detail="Cancellation failed")

@router.get("/cars/available")
def list_available_cars():
    cars = get_all_available_cars()
    return cars
