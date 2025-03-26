from PyQt6.QtCore import QThread


class Worker(QThread):
    def __init__(self, func, args: None | tuple = None) -> None:
        super().__init__()
        self.func = func
        self.args = args

    def run(self) -> None:
        if self.args:
            self.func(*self.args)
        else:
            self.func()
