import threading
from time import sleep, ctime


def demo_one(time):
    print('one的开始时间：',ctime())
    sleep(time)
    print('one的结束时间：',ctime())

def demo_two(time):
    print('two的开始时间：',ctime())
    sleep(time)
    print('two的结束时间：', ctime())

def demo_three(time):
    print('three的开始时间：',ctime())
    sleep(time)
    print('three的结束时间：', ctime())

def main():
    print('main的开始时间：', ctime())
    t1=threading.Thread(target=demo_one,args=(1,))
    t2 = threading.Thread(target=demo_two, args=(3,))
    t3 = threading.Thread(target=demo_three, args=(5,))
    t1.start()
    t2.start()
    t3.start()
    print('main的结束时间：', ctime())

if __name__ == '__main__':
    main()

