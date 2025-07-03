from django.shortcuts import render


def dashboard(request):
    context = {
        "title": "Dashboard",
        "stats": {
            "users": 120,
            "orders": 45,
            "visits": 2300,
        },
        "recent_orders": [
            {"id": 1, "item": "Laptop", "amount": "$1200"},
            {"id": 2, "item": "Phone", "amount": "$800"},
            {"id": 3, "item": "Tablet", "amount": "$600"},
        ]
    }
    return render(request, "dashboard.html", context)
