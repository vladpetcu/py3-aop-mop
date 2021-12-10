from aspectlib import Aspect, Proceed
from .cpu_analyzer import CpuAnalyzer
from .file_writer import FileWriter


class ResourceUsageMOP:

    @Aspect
    def with_cpu_usage(*args):
        cpu_analyzer = CpuAnalyzer()
        try:
            cpu_analyzer.start()
            yield Proceed
            cpu_analyzer.join()
        finally:
            avg, _sum, count = cpu_analyzer.stop()
            
            f_writer = FileWriter('./mop_logs/resource_usage.log')
            f_writer.open_file()
            f_writer.write(f'CPU: {avg}')
            f_writer.close()

