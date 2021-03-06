
class OperationStatistics:
    __instance = None

    @staticmethod
    def getInstance():
        if OperationStatistics.__instance == None:
            OperationStatistics()
        return OperationStatistics.__instance

    def __init__(self):
        if OperationStatistics.__instance != None:
            raise Exception("OperationStatistics Singleton already initialized.")
        self._op_counts = dict()
        OperationStatistics.__instance = self

    def register_operation(self, op_name, add_cnt=1):
        try:
            count = self._op_counts[op_name]
        except KeyError:
            count = 0

        count += add_cnt
        self._op_counts[op_name] = count

    def reset_statistics(self):
        self._op_counts = dict()

    def show_statistics(self):
        for op_name, op_count in self._op_counts.items():
            print(op_name, op_count)

    @property
    def statistics(self):
        return self._op_counts


def count_operation(operation_name, count=1):
    stats = OperationStatistics.getInstance()
    stats.register_operation(operation_name, add_cnt=count)
