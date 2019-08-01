from apscheduler.schedulers.blocking import BlockingScheduler
import autolike




def timed_job():
    autolike.liketweet()



if __name__=="__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(timed_job, 'interval',days=1)

    try:
        scheduler.start()
    except (KeyboardInterrupt,SystemExit):
        pass


