class Logger:
    logs = []

    @classmethod
    def add_log(cls, string: any):
        cls.logs.append(string)

    @classmethod
    def print_logs(cls):
        print('Debbug logs')
        counter = 0
        for log in cls.logs:
            counter += 1
            print(counter, log)
