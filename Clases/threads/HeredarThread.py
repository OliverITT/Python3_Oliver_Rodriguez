from threading import Thread

class MyThread(Thread):


    name = ''

    def __int__(self,name):
        super(MyThread, self).__init__(self)
        self.name =name


    def run(self):
        while True:
            print(self.name)

if __name__ == '__main__':
    names = ['Oliver', 'Mildred']
    for i in range(len(names)):
        my = MyThread(i)
        my.start()
