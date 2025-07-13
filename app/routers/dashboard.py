from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime, date, timedelta
import httpx
import os

router = APIRouter()
templates = Jinja2Templates(directory="app/views")

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000/api")
ADMIN_TG_ID   = os.getenv("ADMIN_TG_ID", "0")
ADMIN_TOKEN   = os.getenv("ADMIN_TOKEN", "your_admin_token")

@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard_view(request: Request):
    # Тестовые данные для демонстрации
    stats = {
        'total_users': 1247,
        'users_today': 23,
        'total_subs': 856,
        'expired_subs': 12,
        'payments_sum': 125670.50,
        'payments_sum_today': 2340.00,
        'servers_available': 8,
        'servers_disabled': 1,
        'total_refs': 145,
        'refs_today': 5,
        'total_gifts': 34,
        'gifts_used': 28
    }
    
    # Пытаемся получить реальные данные из API (с таймаутом)
    try:
        async with httpx.AsyncClient(timeout=1.0) as client:
            # Пробуем получить пользователей
            try:
                users_resp = await client.get(
                    f"{API_BASE_URL}/users/",
                    params={"tg_id": ADMIN_TG_ID},
                    headers={"X-Token": ADMIN_TOKEN}
                )
                if users_resp.status_code == 200:
                    users = users_resp.json()
                    stats['total_users'] = len(users)
                    stats['users_today'] = sum(1 for u in users if u.get('created_at', '').startswith(str(date.today())))
            except:
                pass
                
            # Пробуем получить платежи
            try:
                payments_resp = await client.get(
                    f"{API_BASE_URL}/payments/",
                    params={"tg_id": ADMIN_TG_ID},
                    headers={"X-Token": ADMIN_TOKEN}
                )
                if payments_resp.status_code == 200:
                    payments = payments_resp.json()
                    stats['payments_sum'] = sum(float(p.get('amount', 0)) for p in payments)
                    stats['payments_sum_today'] = sum(float(p.get('amount', 0)) for p in payments if p.get('created_at', '').startswith(str(date.today())))
            except:
                pass
                
    except Exception as e:
        print(f"[INFO] Используем тестовые данные: {e}")
    
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "stats": stats
    })
