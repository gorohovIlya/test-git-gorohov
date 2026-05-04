import os
from typing import Optional

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Discount Service")


class DiscountRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)
    promo_code: Optional[str] = None


class DiscountResponse(BaseModel):
    product_id: str
    quantity: int
    unit_price: float
    promo_code: Optional[str] = None
    discount_percent: float
    reason: str


# Правила для скидок
def calculate_discount(product_id: str, quantity: int, unit_price: float, promo_code: Optional[str]) -> tuple[
    float, str]:
    if promo_code and promo_code.upper() == "STUDENT10":
        return 10.0, "Promo code STUDENT10 applied"

    if promo_code and promo_code.upper() == "PROMO20":
        return 20.0, "Promo code PROMO20 applied"

    if quantity >= 10:
        return 15.0, "Wholesale discount for ordering 10+ items"

    if quantity >= 5:
        return 5.0, "Wholesale discount for ordering 5+ items"

    if unit_price > 100:
        return 3.0, "Premium product discount"

    return 0.0, "No discount applicable"


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "discount-service"}


@app.post("/discounts/calculate", response_model=DiscountResponse)
async def calculate_discount_endpoint(request: DiscountRequest) -> DiscountResponse:
    discount_percent, reason = calculate_discount(
        product_id=request.product_id,
        quantity=request.quantity,
        unit_price=request.unit_price,
        promo_code=request.promo_code,
    )

    return DiscountResponse(
        product_id=request.product_id,
        quantity=request.quantity,
        unit_price=request.unit_price,
        promo_code=request.promo_code,
        discount_percent=discount_percent,
        reason=reason,
    )