from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from videos_updater import videoApi


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(videoApi.update_forecast, 'interval', minutes=0.1)
    scheduler.start()
