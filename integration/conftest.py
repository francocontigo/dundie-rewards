MARKER = """\
unit: Mark unit tests
integration: Mark integration tests
high: High Priority
medium: Medium Priority
low: Low Priority
"""
def pytest_configure(config):
    map(lambda line: config.addnivalue_line("markers", line), MARKER.split("\n"))
