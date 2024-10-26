from flows.flow1 import questions as q1
from flows.flow2 import questions as q2
from flows.flow3 import questions as q3


initial_flow = 'flow1'
questions_map = {
    'flow1': q1,
    'flow2': q2,
    'flow3': q3
}
# transition map between flows. When flow1 is done, it will transit to flow2
flows_map = {
    'flow1': 'flow2',
    'flow2': 'flow3',
    'flow3': 'flow1',
    'flow4': 'flow1'
}
