from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/views")

@router.get("/referrals", response_class=HTMLResponse)
async def referrals_view(request: Request):
    # Тестовые данные рефералов
    referrals = [
        {
            'id': 1,
            'referrer_id': '123456789',
            'referrer_username': 'ivan_petrov',
            'referred_id': '987654321',
            'referred_username': 'anna_sidorova',
            'bonus_amount': 100.00,
            'status': 'active',
            'created_at': '2024-01-10 15:30:00',
            'first_payment_at': '2024-01-11 10:15:00'
        },
        {
            'id': 2,
            'referrer_id': '555666777',
            'referrer_username': 'sergey_kozlov',
            'referred_id': '111222333',
            'referred_username': 'maria_volkova',
            'bonus_amount': 150.00,
            'status': 'pending',
            'created_at': '2024-01-12 12:00:00',
            'first_payment_at': None
        },
        {
            'id': 3,
            'referrer_id': '123456789',
            'referrer_username': 'ivan_petrov',
            'referred_id': '444555666',
            'referred_username': 'alex_petrov',
            'bonus_amount': 200.00,
            'status': 'active',
            'created_at': '2024-01-08 09:30:00',
            'first_payment_at': '2024-01-09 14:20:00'
        }
    ]
    
    return templates.TemplateResponse("referrals.html", {
        "request": request,
        "referrals": referrals,
        "total_referrals": len(referrals),
        "active_referrals": sum(1 for r in referrals if r['status'] == 'active'),
        "total_bonus": sum(r['bonus_amount'] for r in referrals if r['status'] == 'active')
    })


@router.delete("/referrals/one")
async def delete_referral_one(
    referrer_tg_id: int,
    referred_tg_id: int,
    tg_id: int,
    request: Request
):
    """
    Удаляет одну запись о реферале через внешний API.
    """
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.delete(
                f"{API_BASE_URL}/referrals/one",
                params={
                    "referrer_tg_id": referrer_tg_id,
                    "referred_tg_id": referred_tg_id,
                    "tg_id": tg_id
                },
                headers={"X-Token": ADMIN_TOKEN}
            )
            if resp.status_code == 200:
                return {"success": True}
            return {"success": False, "detail": resp.text}
        except Exception as e:
            return {"success": False, "detail": str(e)}


@app.get("/")
async def root():
    return {"message": "Hello World"}
