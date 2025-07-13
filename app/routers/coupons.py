from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/views")

@router.get("/coupons", response_class=HTMLResponse)
async def coupons_view(request: Request):
    # Тестовые данные купонов
    coupons = [
        {
            'id': 1,
            'code': 'WELCOME50',
            'discount': 50,
            'type': 'percent',
            'description': 'Скидка 50% для новых пользователей',
            'usage_count': 25,
            'max_usage': 100,
            'is_active': True,
            'created_at': '2024-01-10 12:00:00',
            'expires_at': '2024-02-10 23:59:59'
        },
        {
            'id': 2,
            'code': 'SAVE200',
            'discount': 200,
            'type': 'fixed',
            'description': 'Фиксированная скидка 200 рублей',
            'usage_count': 8,
            'max_usage': 50,
            'is_active': True,
            'created_at': '2024-01-12 10:30:00',
            'expires_at': '2024-03-12 23:59:59'
        },
        {
            'id': 3,
            'code': 'EXPIRED10',
            'discount': 10,
            'type': 'percent',
            'description': 'Истёкший купон на 10%',
            'usage_count': 100,
            'max_usage': 100,
            'is_active': False,
            'created_at': '2024-01-01 00:00:00',
            'expires_at': '2024-01-15 23:59:59'
        },
        {
            'id': 4,
            'code': 'VIP25',
            'discount': 25,
            'type': 'percent',
            'description': 'VIP скидка 25% для премиум пользователей',
            'usage_count': 5,
            'max_usage': 20,
            'is_active': True,
            'created_at': '2024-01-14 15:00:00',
            'expires_at': '2024-04-14 23:59:59'
        }
    ]
    
    # Статистика
    total_coupons = len(coupons)
    active_coupons = sum(1 for c in coupons if c['is_active'])
    inactive_coupons = total_coupons - active_coupons
    total_usage = sum(c['usage_count'] for c in coupons)
    
    return templates.TemplateResponse("coupons.html", {
        "request": request,
        "coupons": coupons,
        "total_coupons": total_coupons,
        "active_coupons": active_coupons,
        "inactive_coupons": inactive_coupons,
        "total_usage": total_usage
    })
