from plyer import notification

notification_title = "Merhaba bu test başlığıdır."
notification_description = "Hmm bunu okuduğuna göre demekki kod çalışıyor.. niceee"

while True:
    notification.notify(
        title = notification_title,
        message = notification_description,
        app_icon = None,
        timeout = 0.4,
        toast = False
    )