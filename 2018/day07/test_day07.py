from .day07_pt1 import get_order

tdata = 'Step C must be finished before step A can begin.\n'\
        'Step C must be finished before step F can begin.\n'\
        'Step A must be finished before step B can begin.\n'\
        'Step A must be finished before step D can begin.\n'\
        'Step B must be finished before step E can begin.\n'\
        'Step D must be finished before step E can begin.\n'\
        'Step F must be finished before step E can begin.\n'


def test_get_order():
    assert get_order(tdata) == 'CABDFE'
