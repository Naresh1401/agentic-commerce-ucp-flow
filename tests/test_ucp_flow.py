import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location('sample_ucp_flow', Path('ucp-flow/sample_ucp_flow.py'))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def test_ucp_flow_has_required_steps():
    steps = module.build_flow()
    assert len(steps) == 11
    assert steps[4]['name'] == 'cart_mandate_creation'

