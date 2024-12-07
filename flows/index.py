from flows.flow1 import flow as flow1
from flows.flow2 import flow as flow2
from flows.flow3 import flow as flow3
from flows.flow4 import flow as flow4

initial_flow = 'flow1'

flows = {
    'flow1': flow1,
    'flow2': flow2,
    'flow3': flow3,
    'flow4': flow4
}

# transition map between flows. When flow1 is done, it will transit to flow2
flows_map = {
    'flow1': 'flow2',
    'flow2': 'flow3',
    'flow3': 'flow4',
    'flow4': 'flow1',
}