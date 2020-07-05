from functools import wraps

# def logit(func):
#     @wraps(func)
#     def my_decorator(*args,**kwargs):
#         log_string = func.__name__ + " was cal."
#         print(log_string)

#         return func(*args,**kwargs)
#     return my_decorator

def logit1(logFile='out.log'):
    """
    返回一个包裹函数
    """
    def log_decorator(func):
        @wraps(func)
        def wraps_function(*args,**kwargs):
            log_string = func.__name__ + " was cal ."
            print(log_string)
            with open(logFile,'a') as logfile:
                logfile.write(log_string)
            return func(*args,**kwargs)
        return wraps_function
    return log_decorator

class logit(object):
    """
    
    """
    def __init__(self,logfile='out.log'):
        self.logfile = logfile

    def __call__(self,func):

        @wraps(func)
        def my_decorator(*args,**kwargs):
            log_string = func.__name__ + " was cal. "
            self.notify()
            with open(self.logfile,'a') as logfile:
                logfile.write(log_string+"\n")
            return func(*args,**kwargs)  
        return my_decorator

    def notify(self):
        print("打印日志信息到屏幕")

class emain_log(logit):
    """

    """
    def __init__(self,emali='admin@163.com',*args,**kwargs):
        self.emali = emali
        super(emain_log,self).__init__(*args,**kwargs)

    def notify(self):
        print("打屏的基础上将日志信息发送到邮箱")


# @emain_log()
@logit1()
def add(a,b):
    return a+b

if __name__ == '__main__':
    add(1,2)
   