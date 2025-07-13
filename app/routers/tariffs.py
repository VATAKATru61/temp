from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/views")

@router.get("/tariffs", response_class=HTMLResponse)
async def tariffs_view(request: Request):
    # Тестовые данные тарифов
    tariffs = [
        {
            'id': 1,
            'name': 'Базовый',
            'description': 'Подходит для начинающих пользователей',
            'price': 300.00,
            'currency': 'RUB',
            'duration_days': 30,
            'traffic_limit': 50.0,
            'servers_count': 3,
            'max_devices': 2,
            'is_active': True,
            'is_popular': False,
            'features': ['Базовая скорость', '3 сервера', 'Техподдержка']
        },
        {
            'id': 2,
            'name': 'Стандарт',
            'description': 'Оптимальный выбор для большинства пользователей',
            'price': 500.00,
            'currency': 'RUB',
            'duration_days': 30,
            'traffic_limit': 100.0,
            'servers_count': 6,
            'max_devices': 5,
            'is_active': True,
            'is_popular': True,
            'features': ['Высокая скорость', '6 серверов', 'Приоритетная поддержка']
        },
        {
            'id': 3,
            'name': 'Премиум',
            'description': 'Максимальные возможности и скорость',
            'price': 1000.00,
            'currency': 'RUB',
            'duration_days': 30,
            'traffic_limit': 500.0,
            'servers_count': 12,
            'max_devices': 10,
            'is_active': True,
            'is_popular': False,
            'features': ['Максимальная скорость', '12 серверов', 'VIP поддержка', 'Статический IP']
        },
        {
            'id': 4,
            'name': 'Эконом',
            'description': 'Бюджетный вариант с ограниченным функционалом',
            'price': 150.00,
            'currency': 'RUB',
            'duration_days': 30,
            'traffic_limit': 20.0,
            'servers_count': 2,
            'max_devices': 1,
            'is_active': False,
            'is_popular': False,
            'features': ['Базовая скорость', '2 сервера']
        }
    ]
    
    # Статистика
    total_tariffs = len(tariffs)
    active_tariffs = sum(1 for t in tariffs if t['is_active'])
    inactive_tariffs = total_tariffs - active_tariffs
    avg_price = sum(t['price'] for t in tariffs if t['is_active']) / active_tariffs if active_tariffs > 0 else 0
    
    return templates.TemplateResponse("tariffs.html", {
        "request": request,
        "tariffs": tariffs,
        "total_tariffs": total_tariffs,
        "active_tariffs": active_tariffs,
        "inactive_tariffs": inactive_tariffs,
        "avg_price": round(avg_price, 2)
    })
