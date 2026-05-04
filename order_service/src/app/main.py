# order_service/main.py (обновленная версия)
import os

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Order Service")

PRODUCT_SERVICE_URL = os.getenv(
    "PRODUCT_SERVICE_URL",
    "http://127.0.0.1:8001",
)

DISCOUNT_SERVICE_URL = os.getenv(
    "DISCOUNT_SERVICE_URL",
    "http://127.0.0.1:8003",
)


class OrderRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    promo_code: str | None = None


class OrderResponse(BaseModel):
    product_id: str
    quantity: int
    unit_price: float
    subtotal: float
    discount_percent: float
    discount_reason: str
    discount_amount: float
    total: float


class ProductFromService(BaseModel):
    id: str
    name: str
    price: float
    available: bool


class DiscountRequest(BaseModel):
    product_id: str
    quantity: int
    unit_price: float
    promo_code: str | None = None


class DiscountResponse(BaseModel):
    product_id: str
    quantity: int
    unit_price: float
    promo_code: str | None = None
    discount_percent: float
    reason: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "order-service"}


@app.post("/orders", response_model=OrderResponse)
async def create_order(order: OrderRequest) -> OrderResponse:
    product = await fetch_product(order.product_id)

    if not product.available:
        raise HTTPException(
            status_code=400,
            detail=f"Product '{order.product_id}' is not available",
        )

    subtotal = product.price * order.quantity
    discount_info = await fetch_discount(
        product_id=order.product_id,
        quantity=order.quantity,
        unit_price=product.price,
        promo_code=order.promo_code,
    )

    discount_percent = discount_info.discount_percent
    discount_amount = subtotal * (discount_percent / 100)
    total = subtotal - discount_amount

    return OrderResponse(
        product_id=product.id,
        quantity=order.quantity,
        unit_price=product.price,
        subtotal=subtotal,
        discount_percent=discount_percent,
        discount_reason=discount_info.reason,
        discount_amount=round(discount_amount, 2),
        total=round(total, 2),
    )


async def fetch_product(product_id: str) -> ProductFromService:
    url = f"{PRODUCT_SERVICE_URL}/products/{product_id}"

    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.get(url)
    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Product service is unavailable: {exc}",
        ) from exc

    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail=f"Product '{product_id}' was not found",
        )

    if response.status_code >= 400:
        raise HTTPException(
            status_code=502,
            detail="Product service returned an unexpected error",
        )

    return ProductFromService.model_validate(response.json())


async def fetch_discount(
        product_id: str,
        quantity: int,
        unit_price: float,
        promo_code: str | None
) -> DiscountResponse:
    url = f"{DISCOUNT_SERVICE_URL}/discounts/calculate"

    request_body = DiscountRequest(
        product_id=product_id,
        quantity=quantity,
        unit_price=unit_price,
        promo_code=promo_code,
    )

    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.post(url, json=request_body.model_dump())
    except httpx.RequestError as exc:
        return DiscountResponse(
            product_id=product_id,
            quantity=quantity,
            unit_price=unit_price,
            promo_code=promo_code,
            discount_percent=0.0,
            reason="Discount service unavailable, no discount applied",
        )

    if response.status_code >= 400:
        return DiscountResponse(
            product_id=product_id,
            quantity=quantity,
            unit_price=unit_price,
            promo_code=promo_code,
            discount_percent=0.0,
            reason="Discount service error, no discount applied",
        )

    return DiscountResponse.model_validate(response.json())
