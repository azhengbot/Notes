class Foo:
    def display(self, message):
        print(f"Foo's display: {message}")


class LoggerMixin:
    def log(self, message, message2):
        print(f"minxin log: {message} ----> {message2}")

    def display(self, message):
        print("mixin's display")

        super().display(message)
        self.log(message)


class MySubClass(LoggerMixin, Foo):
    def log(self, message):
        print(f"MySubClass's log: {message}")
        super().log(message, message2="subclasslog.txt")


print(MySubClass.__mro__)

obj = MySubClass()
obj.display("This string will be shown and logged in subclasslog.txt")
