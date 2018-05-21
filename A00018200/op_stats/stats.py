import psutil

class Stats():

    @classmethod
    def get_cpu(cls):
        cpu_percent=psutil.cpu_percent()
        return cpu_percent

    @classmethod
    def get_memory(cls):
        memory=psutil.virtual_memory().available
        return memory

    @classmethod
    def get_disk(cls):
        disk=psutil.disk_usage('/').free
        return disk

