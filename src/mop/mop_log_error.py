
class MopLogError(Exception):

    def __init__(self, caller_name, message):
        self.caller_name = caller_name
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f'{self.caller_name}.error: {self.message}'
