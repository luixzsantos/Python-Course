ALERTS_ENABLED = False
def respond(action):
    if not ALERTS_ENABLED:
        return

    if action == "ALERT":
        ...


from win10toast import ToastNotifier
from datetime import datetime

toaster = ToastNotifier()

def respond(action):
    now = datetime.now().strftime("%H:%M:%S")

    if action == "ALERT":
        toaster.show_toast(
            "⚠️ Alerta de Segurança",
            f"Atividade suspeita detectada às {now}",
            duration=10
        )

    elif action == "BLOCK":
        toaster.show_toast(
            "🚨 ATAQUE BLOQUEADO",
            f"Ataque bloqueado às {now}",
            duration=10
        )
