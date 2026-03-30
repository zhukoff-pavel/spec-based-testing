from foo import bar, baz, string


class UsageExample:
    def __init__(self):
        self.baz = baz.Baz(1, 2)

    def use_bar(self):
        return bar.foo(1, 2)

    def use_baz(self):
        return self.baz.foo(3)

    def use_string(self):
        return string.get_name()