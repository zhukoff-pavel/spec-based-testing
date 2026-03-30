import dataclasses
import types


@dataclasses.dataclass
class Description:
    module_name: str
    module: types.ModuleType = dataclasses.field(default_factory=types.ModuleType, hash=False)
    classes: list[str] = dataclasses.field(default_factory=list, hash=False)
    functions: list[str] = dataclasses.field(default_factory=list, hash=False)


def parse_libsl(path) -> Description:
    match path:
        case "/foo/bar.libsl":
            module_name = "foo.bar"

            functions = ["foo"]
            classes = []

            gen_code = """
import random

def foo(a: int, b: int):
    assert a > 0, "Requirement POSITIVE_A not met"
    assert b > 0, "Requirement POSITIVE_B not met"

    return 100
            """

        case "/foo/baz.libsl":
            module_name = "foo.baz"
            functions = []
            classes = ["Baz"]
            gen_code = """
class Baz:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def foo(self, c: int):
        assert self.a > 0, "Requirement POSITIVE_A not met"
        assert self.b > 0, "Requirement POSITIVE_B not met"

        assert c > 0, "Requirement POSITIVE_C not met"

        return self.a + self.b + c + 5
            """

        case "/foo/string.libsl":
            module_name = "foo.string"
            functions = ["get_name"]
            classes = []
            gen_code = """
import sre_yield
import random

def get_name():
    generator = sre_yield.AllStrings(r"[a-zA-Z0-9]{1,5}")
    return generator.get_item(random.randint(0, generator.length))
            """

    module = types.ModuleType(f"test.{module_name}")
    exec(gen_code, module.__dict__)

    return Description(
        module_name=module_name,
        module=module,
        classes=classes,
        functions=functions,
    )
