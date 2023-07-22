import time

class Snowflake:
    def __init__(self, worker_id, datacenter_id):
        self.worker_id = worker_id
        self.datacenter_id = datacenter_id
        self.sequence = 0
        self.last_timestamp = -1

    def generate_id(self):
        timestamp = int(time.time() * 1000)

        if timestamp < self.last_timestamp:
            raise Exception("时间戳错误，无法生成ID")

        if timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & 4095
            if self.sequence == 0:
                timestamp = self.wait_next_millis(self.last_timestamp)
        else:
            self.sequence = 0

        self.last_timestamp = timestamp

        return ((timestamp - 1635724800000) << 22) | (self.datacenter_id << 17) | (self.worker_id << 12) | self.sequence

    def wait_next_millis(self, last_timestamp):
        timestamp = int(time.time() * 1000)
        while timestamp <= last_timestamp:
            timestamp = int(time.time() * 1000)
        return timestamp
