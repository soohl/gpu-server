from apscheduler.schedulers.asyncio import AsyncIOScheduler
import app.crawler as crawler


sched = AsyncIOScheduler()


@sched.scheduled_job("cron", day_of_week="mon-sun", hour=23)
def scheduled_job():
    crawler.start()


sched.start()
