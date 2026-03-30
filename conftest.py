import pytest
import parser


class LibSLMocker:
    def __init__(self, mocker):
        self.cache = {}
        self.mocker = mocker

    def __call__(self, path: str):
        if path in self.cache:
            return

        desc = self._parse(path)
        for class_name in desc.classes:
            self.mocker.patch(f"{desc.module_name}.{class_name}", getattr(desc.module, class_name))

        for function_name in desc.functions:
            self.mocker.patch(f"{desc.module_name}.{function_name}", getattr(desc.module, function_name))

    def _parse(self, path: str) -> parser.Description:
        desc = parser.parse_libsl(path)

        self.cache[path] = desc
        return desc


@pytest.fixture(scope="session")
def libsl_mocker(session_mocker):
    return LibSLMocker(session_mocker)