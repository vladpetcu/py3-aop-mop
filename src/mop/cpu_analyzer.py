import psutil
import threading

class CpuAnalyzer(threading.Thread):

    def run(self):
        self.running = False
        if not self.running:
            self.avg = 0
            self.sum = 0
            self.count = 1
            self.running = True

            currentProcess = psutil.Process()

            while self.running:
                cpu_usage = currentProcess.cpu_percent(interval=1)
                self.count += 1
                self.sum += cpu_usage

    def join(self):
        self.running = False
        threading.Thread.join(self)

    def stop(self):
        self.avg = self.sum / self.count
        self.running = False
        return self.avg, self.sum, self.count
