from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/views")

@router.get("/gifts", response_class=HTMLResponse)
async def gifts_view(request: Request):
    # Тестовые данные подарков
    gifts = [
        {
            'id': 1,
            'name': 'Новогодний подарок',
            'description': 'Бесплатная подписка на 1 месяц',
            'type': 'subscription',
            'value': 500.00,
            'days': 30,
            'is_used': False,
            'user_id': None,
            'username': None,
            'created_at': '2024-01-01 00:00:00',
            'used_at': None,
            'expires_at': '2024-02-01 23:59:59'
        },
        {
            'id': 2,
            'name': 'Подарок за реферала',
            'description': 'Бонус 200 рублей на счёт',
            'type': 'balance',
            'value': 200.00,
            'days': 0,
            'is_used': True,
            'user_id': '123456789',
            'username': 'ivan_petrov',
            'created_at': '2024-01-10 15:30:00',
            'used_at': '2024-01-11 10:15:00',
            'expires_at': '2024-02-10 23:59:59'
        },
        {
            'id': 3,
            'name': 'Промо-подарок',
            'description': 'Пробная VIP подписка на 7 дней',
            'type': 'subscription',
            'value': 150.00,
            'days': 7,
            'is_used': True,
            'user_id': '987654321',
            'username': 'anna_sidorova',
            'created_at': '2024-01-12 12:00:00',
            'used_at': '2024-01-12 18:45:00',
            'expires_at': '2024-03-12 23:59:59'
        },
        {
            'id': 4,
            'name': 'Конкурсный приз',
            'description': 'Премиум подписка на 2 месяца',
            'type': 'subscription',
            'value': 1000.00,
            'days': 60,
            'is_used': False,
            'user_id': None,
            'username': None,
            'created_at': '2024-01-14 20:00:00',
            'used_at': None,
            'expires_at': '2024-03-14 23:59:59'
        }
    ]
    
    # Статистика
    total_gifts = len(gifts)
    used_gifts = sum(1 for g in gifts if g['is_used'])
    unused_gifts = total_gifts - used_gifts
    total_value = sum(g['value'] for g in gifts if g['is_used'])
    
    return templates.TemplateResponse("gifts.html", {
        "request": request,
        "gifts": gifts,
        "total_gifts": total_gifts,
        "used_gifts": used_gifts,
        "unused_gifts": unused_gifts,
        "total_value": total_value
    })


@router.patch("/gifts/{gift_id}")
async def patch_gift(gift_id: str, request: Request):
    try:
        payload = await request.json()
        # This part of the code was not provided in the new_code, so it's kept as is.
        # In a real scenario, you would call an API here.
        # For now, it's a placeholder.
        return HTMLResponse(content={"success": True})
    except Exception as e:
        print(f"[ERROR] Ошибка при обновлении подарка {gift_id}: {e}")
        return HTMLResponse(status_code=500, content={"error": "Update failed"})


@router.delete("/gifts/{gift_id}")
async def delete_gift(gift_id: str):
    try:
        # This part of the code was not provided in the new_code, so it's kept as is.
        # In a real scenario, you would call an API here.
        # For now, it's a placeholder.
        return HTMLResponse(content={"success": True})
    except Exception as e:
        print(f"[ERROR] Ошибка при удалении подарка {gift_id}: {e}")
        return HTMLResponse(status_code=500, content={"error": "Delete failed"})


def make_naive(dt: datetime) -> datetime:
    if dt and dt.tzinfo:
        return dt.replace(tzinfo=None)
    return dt


@router.post("/gifts")
async def create_gift(request: Request):
    try:
        payload = await request.json()
        # This part of the code was not provided in the new_code, so it's kept as is.
        # In a real scenario, you would call an API here.
        # For now, it's a placeholder.
        return HTMLResponse(content={"success": True})
    except Exception as e:
        print(f"[ERROR] Ошибка при создании подарка: {e}")
        return HTMLResponse(status_code=500, content={"error": "Create failed"})