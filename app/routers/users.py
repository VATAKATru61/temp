from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime, date

router = APIRouter()
templates = Jinja2Templates(directory="app/views")

@router.get("/users", response_class=HTMLResponse)
async def users_view(request: Request):
    # Тестовые данные пользователей
    users = [
        {
            'id': 1,
            'tg_id': '123456789',
            'username': 'ivan_petrov',
            'first_name': 'Иван',
            'last_name': 'Петров',
            'created_at': '2024-01-15 10:30:00',
            'is_active': True,
            'subscription_end': '2024-02-15 10:30:00'
        },
        {
            'id': 2,
            'tg_id': '987654321',
            'username': 'anna_sidorova',
            'first_name': 'Анна',
            'last_name': 'Сидорова',
            'created_at': '2024-01-14 15:20:00',
            'is_active': False,
            'subscription_end': None
        },
        {
            'id': 3,
            'tg_id': '555666777',
            'username': 'sergey_kozlov',
            'first_name': 'Сергей',
            'last_name': 'Козлов',
            'created_at': '2024-01-13 09:45:00',
            'is_active': True,
            'subscription_end': '2024-03-13 09:45:00'
        },
        {
            'id': 4,
            'tg_id': '111222333',
            'username': 'maria_volkova',
            'first_name': 'Мария',
            'last_name': 'Волкова',
            'created_at': '2024-01-12 14:15:00',
            'is_active': True,
            'subscription_end': '2024-01-20 14:15:00'
        },
        {
            'id': 5,
            'tg_id': '444555666',
            'username': 'alex_petrov',
            'first_name': 'Александр',
            'last_name': 'Петров',
            'created_at': '2024-01-10 11:00:00',
            'is_active': False,
            'subscription_end': None
        }
    ]
    
    return templates.TemplateResponse("users.html", {
        "request": request,
        "users": users
    })

@router.get("/users/{user_id}", response_class=HTMLResponse)
async def user_detail_view(request: Request, user_id: int):
    # Тестовые данные для конкретного пользователя
    user = {
        'id': user_id,
        'tg_id': '123456789',
        'username': 'ivan_petrov',
        'first_name': 'Иван',
        'last_name': 'Петров',
        'created_at': '2024-01-15 10:30:00',
        'is_active': True,
        'subscription_end': '2024-02-15 10:30:00',
        'balance': 250.00,
        'referral_count': 5,
        'total_payments': 1500.00
    }
    
    # Тестовые ключи пользователя
    keys = [
        {
            'id': 1,
            'name': 'Основной ключ',
            'key': 'vless://test-key-1...',
            'created_at': '2024-01-15 10:30:00',
            'expiry_time': '2024-02-15 10:30:00',
            'is_active': True
        },
        {
            'id': 2,
            'name': 'Дополнительный ключ',
            'key': 'vless://test-key-2...',
            'created_at': '2024-01-10 12:00:00',
            'expiry_time': '2024-02-10 12:00:00',
            'is_active': False
        }
    ]
    
    # Тестовые платежи пользователя
    payments = [
        {
            'id': 1,
            'amount': 500.00,
            'currency': 'RUB',
            'status': 'completed',
            'created_at': '2024-01-15 10:30:00',
            'description': 'Подписка на 1 месяц'
        },
        {
            'id': 2,
            'amount': 1000.00,
            'currency': 'RUB',
            'status': 'completed',
            'created_at': '2024-01-05 14:20:00',
            'description': 'Подписка на 2 месяца'
        }
    ]
    
    return templates.TemplateResponse("user_detail.html", {
        "request": request,
        "user": user,
        "keys": keys,
        "payments": payments
    })
