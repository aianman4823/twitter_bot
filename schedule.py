from apscheduler.schedulers.blocking import BlockingScheduler
import autolike
import autoretweet
import removefollow


scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval',hour=18)
def timed_job():
    autolike.liketweet()
    autoretweet.autoretweet()


if __name__=="__main__":
    scheduler.start()

scheduler_remove = BlockingScheduler()

@scheduler_remove.scheduled_job('interval',weeks=1)
def remove_job():
    removefollow.remove()

if __name__ == "__main__":
    scheduler_remove.start()

