from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/views")

@router.get("/servers", response_class=HTMLResponse)
async def servers_view(request: Request):
    # Тестовые данные серверов
    servers = [
        {
            'id': 1,
            'name': 'Сервер RU-1',
            'host': 'server1.example.com',
            'port': 443,
            'location': 'Москва, Россия',
            'is_enabled': True,
            'max_users': 1000,
            'current_users': 234,
            'cpu_usage': 45.2,
            'memory_usage': 67.8,
            'disk_usage': 23.1,
            'network_upload': 156.7,
            'network_download': 892.3,
            'uptime': 99.9,
            'last_check': '2024-01-15 12:45:00'
        },
        {
            'id': 2,
            'name': 'Сервер EU-1',
            'host': 'server2.example.com',
            'port': 443,
            'location': 'Амстердам, Нидерланды',
            'is_enabled': True,
            'max_users': 800,
            'current_users': 567,
            'cpu_usage': 72.5,
            'memory_usage': 81.2,
            'disk_usage': 34.8,
            'network_upload': 234.1,
            'network_download': 1205.6,
            'uptime': 99.7,
            'last_check': '2024-01-15 12:44:00'
        },
        {
            'id': 3,
            'name': 'Сервер US-1',
            'host': 'server3.example.com',
            'port': 443,
            'location': 'Нью-Йорк, США',
            'is_enabled': True,
            'max_users': 1200,
            'current_users': 89,
            'cpu_usage': 18.3,
            'memory_usage': 34.5,
            'disk_usage': 12.7,
            'network_upload': 67.4,
            'network_download': 423.8,
            'uptime': 99.8,
            'last_check': '2024-01-15 12:43:00'
        },
        {
            'id': 4,
            'name': 'Сервер ASIA-1',
            'host': 'server4.example.com',
            'port': 443,
            'location': 'Сингапур',
            'is_enabled': False,
            'max_users': 600,
            'current_users': 0,
            'cpu_usage': 0.0,
            'memory_usage': 0.0,
            'disk_usage': 45.2,
            'network_upload': 0.0,
            'network_download': 0.0,
            'uptime': 0.0,
            'last_check': '2024-01-14 18:20:00'
        }
    ]
    
    # Статистика
    total_servers = len(servers)
    enabled_servers = sum(1 for server in servers if server['is_enabled'])
    disabled_servers = total_servers - enabled_servers
    total_users = sum(server['current_users'] for server in servers)
    avg_cpu = sum(server['cpu_usage'] for server in servers if server['is_enabled']) / enabled_servers if enabled_servers > 0 else 0
    avg_memory = sum(server['memory_usage'] for server in servers if server['is_enabled']) / enabled_servers if enabled_servers > 0 else 0
    
    return templates.TemplateResponse("servers.html", {
        "request": request,
        "servers": servers,
        "total_servers": total_servers,
        "enabled_servers": enabled_servers,
        "disabled_servers": disabled_servers,
        "total_users": total_users,
        "avg_cpu": round(avg_cpu, 1),
        "avg_memory": round(avg_memory, 1)
    })