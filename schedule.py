from apscheduler.schedulers.blocking import BlockingScheduler
import autolike
import autoretweet
import removefollow


def timed_job():
    autolike.liketweet()
    autoretweet.autoretweet()

def remove_job():
    removefollow.remove()


if __name__=="__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(timed_job, 'cron',hour=7,minute=10)
    scheduler.add_job(remove_job,'cron',hour=7,minute=15)

    try:
        scheduler.start()
    except (KeyboardInterrupt,SystemExit):
        pass


