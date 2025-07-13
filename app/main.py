from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from starlette.status import HTTP_302_FOUND

from app.routers import dashboard, keys, users, servers, tariffs, coupons, payments, referrals, gifts
from app.config import SECRET_KEY, ADMIN_PASSWORD, ADMIN_USERNAME

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/views")


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/dashboard")


@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
async def login_process(request: Request, username: str = Form(...), password: str = Form(...)):
    print("[FORM] username:", repr(username))
    print("[FORM] password:", repr(password))
    print("[ENV ] ADMIN_USERNAME:", repr(ADMIN_USERNAME))
    print("[ENV ] ADMIN_PASSWORD:", repr(ADMIN_PASSWORD))

    if username.strip() == ADMIN_USERNAME.strip() and password.strip() == ADMIN_PASSWORD.strip():
        request.session["admin"] = True
        return RedirectResponse("/dashboard", status_code=302)
    else:
        print("❌ Не совпадает логин/пароль")
        return templates.TemplateResponse("login.html", {
            "request": request,
            "error": "Неверные учётные данные"
        })


@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/login", status_code=302)


def is_logged_in(request: Request):
    if not request.session.get("admin"):
        raise HTTPException(
            status_code=HTTP_302_FOUND,
            headers={"Location": "/login"}
        )
    return True


app.include_router(dashboard.router, dependencies=[Depends(is_logged_in)])
app.include_router(keys.router, dependencies=[Depends(is_logged_in)])
app.include_router(users.router, dependencies=[Depends(is_logged_in)])
app.include_router(servers.router, dependencies=[Depends(is_logged_in)])
app.include_router(tariffs.router, dependencies=[Depends(is_logged_in)])
app.include_router(coupons.router, dependencies=[Depends(is_logged_in)])
app.include_router(payments.router, dependencies=[Depends(is_logged_in)])
app.include_router(referrals.router, dependencies=[Depends(is_logged_in)])
app.include_router(gifts.router, dependencies=[Depends(is_logged_in)])
