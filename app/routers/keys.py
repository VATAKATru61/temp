from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime, date

router = APIRouter()
templates = Jinja2Templates(directory="app/views")

@router.get("/keys", response_class=HTMLResponse)
async def keys_view(request: Request):
    # Тестовые данные ключей
    keys = [
        {
            'id': 1,
            'name': 'Основной ключ - Иван',
            'key': 'vless://12345678-1234-5678-9012-123456789012@server1.example.com:443?type=tcp&security=tls&sni=server1.example.com#IvanKey',
            'tg_id': '123456789',
            'username': 'ivan_petrov',
            'created_at': '2024-01-15 10:30:00',
            'expiry_time': '2024-02-15 10:30:00',
            'is_active': True,
            'traffic_used': 2.5,
            'traffic_limit': 100.0,
            'server_name': 'Сервер RU-1'
        },
        {
            'id': 2,
            'name': 'Дополнительный ключ - Анна',
            'key': 'vless://87654321-4321-8765-2109-876543210987@server2.example.com:443?type=tcp&security=tls&sni=server2.example.com#AnnaKey',
            'tg_id': '987654321',
            'username': 'anna_sidorova',
            'created_at': '2024-01-14 15:20:00',
            'expiry_time': '2024-02-14 15:20:00',
            'is_active': False,
            'traffic_used': 45.2,
            'traffic_limit': 50.0,
            'server_name': 'Сервер EU-1'
        },
        {
            'id': 3,
            'name': 'VIP ключ - Сергей',
            'key': 'vless://55566677-5566-7788-9900-555666777888@server3.example.com:443?type=tcp&security=tls&sni=server3.example.com#SergeyVIP',
            'tg_id': '555666777',
            'username': 'sergey_kozlov',
            'created_at': '2024-01-13 09:45:00',
            'expiry_time': '2024-03-13 09:45:00',
            'is_active': True,
            'traffic_used': 12.8,
            'traffic_limit': 200.0,
            'server_name': 'Сервер US-1'
        },
        {
            'id': 4,
            'name': 'Пробный ключ - Мария',
            'key': 'vless://11122233-1122-3344-5566-111222333444@server1.example.com:443?type=tcp&security=tls&sni=server1.example.com#MariaTest',
            'tg_id': '111222333',
            'username': 'maria_volkova',
            'created_at': '2024-01-12 14:15:00',
            'expiry_time': '2024-01-20 14:15:00',
            'is_active': True,
            'traffic_used': 8.3,
            'traffic_limit': 25.0,
            'server_name': 'Сервер RU-1'
        },
        {
            'id': 5,
            'name': 'Истёкший ключ - Александр',
            'key': 'vless://44455566-4455-6677-8899-444555666777@server2.example.com:443?type=tcp&security=tls&sni=server2.example.com#AlexExpired',
            'tg_id': '444555666',
            'username': 'alex_petrov',
            'created_at': '2024-01-05 11:00:00',
            'expiry_time': '2024-01-10 11:00:00',
            'is_active': False,
            'traffic_used': 23.7,
            'traffic_limit': 30.0,
            'server_name': 'Сервер EU-1'
        }
    ]
    
    # Статистика
    total_keys = len(keys)
    active_keys = sum(1 for key in keys if key['is_active'])
    expired_keys = total_keys - active_keys
    total_traffic = sum(key['traffic_used'] for key in keys)
    
    return templates.TemplateResponse("keys.html", {
        "request": request,
        "keys": keys,
        "total_keys": total_keys,
        "active_keys": active_keys,
        "expired_keys": expired_keys,
        "total_traffic": round(total_traffic, 1)
    })
