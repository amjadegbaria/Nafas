from flows.flow3 import questions as q3
from flows.flow4 import questions as q4



questions_map = {
    'flow3': q3,
    'flow4': q4,
}
flows_map = {
    'flow1': 'flow3',
    'flow2': 'flow3',
    'flow3': 'flow4',
    'flow4': 'flow3'
}