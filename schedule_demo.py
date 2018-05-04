import schedule
import time

def job():
    print('yubx')
    time
schedule.every(3).seconds.do(job)
schedule.every(1).monday.do(job)


if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)

