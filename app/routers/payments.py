from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/views")

@router.get("/payments", response_class=HTMLResponse)
async def payments_view(request: Request):
    # Тестовые данные платежей
    payments = [
        {
            'id': 1,
            'tg_id': '123456789',
            'username': 'ivan_petrov',
            'amount': 500.00,
            'currency': 'RUB',
            'status': 'completed',
            'payment_method': 'bank_card',
            'created_at': '2024-01-15 10:30:00',
            'description': 'Подписка на 1 месяц',
            'transaction_id': 'TXN_001_2024'
        },
        {
            'id': 2,
            'tg_id': '987654321',
            'username': 'anna_sidorova',
            'amount': 300.00,
            'currency': 'RUB',
            'status': 'pending',
            'payment_method': 'qiwi',
            'created_at': '2024-01-15 08:15:00',
            'description': 'Продление подписки',
            'transaction_id': 'TXN_002_2024'
        },
        {
            'id': 3,
            'tg_id': '555666777',
            'username': 'sergey_kozlov',
            'amount': 1000.00,
            'currency': 'RUB',
            'status': 'completed',
            'payment_method': 'bank_card',
            'created_at': '2024-01-14 16:45:00',
            'description': 'VIP подписка на 2 месяца',
            'transaction_id': 'TXN_003_2024'
        },
        {
            'id': 4,
            'tg_id': '111222333',
            'username': 'maria_volkova',
            'amount': 200.00,
            'currency': 'RUB',
            'status': 'failed',
            'payment_method': 'yoomoney',
            'created_at': '2024-01-14 12:20:00',
            'description': 'Пробная подписка',
            'transaction_id': 'TXN_004_2024'
        },
        {
            'id': 5,
            'tg_id': '444555666',
            'username': 'alex_petrov',
            'amount': 750.00,
            'currency': 'RUB',
            'status': 'completed',
            'payment_method': 'crypto',
            'created_at': '2024-01-13 14:30:00',
            'description': 'Подписка на 1.5 месяца',
            'transaction_id': 'TXN_005_2024'
        }
    ]
    
    # Статистика
    total_payments = len(payments)
    completed_payments = sum(1 for p in payments if p['status'] == 'completed')
    pending_payments = sum(1 for p in payments if p['status'] == 'pending')
    failed_payments = sum(1 for p in payments if p['status'] == 'failed')
    total_amount = sum(p['amount'] for p in payments if p['status'] == 'completed')
    
    return templates.TemplateResponse("payments.html", {
        "request": request,
        "payments": payments,
        "total_payments": total_payments,
        "completed_payments": completed_payments,
        "pending_payments": pending_payments,
        "failed_payments": failed_payments,
        "total_amount": total_amount
    })