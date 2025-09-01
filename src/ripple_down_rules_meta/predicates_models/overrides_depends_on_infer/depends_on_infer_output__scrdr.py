from types import NoneType

from ripple_down_rules import PredicateOutputType
from ripple_down_rules.datastructures.case import Case, create_case
from typing_extensions import Optional, Dict
from .depends_on_infer_output__scrdr_defs import *


attribute_name = 'output_'
conclusion_type = (PredicateOutputType,)
mutually_exclusive = True
name = 'output_'
case_type = Dict
case_name = 'depends_on_evaluate'


def classify(case: Dict, **kwargs) -> Optional[PredicateOutputType]:
    if not isinstance(case, Case):
        case = create_case(case, max_recursion_idx=3)

    if conditions_3929361033208322153670901849644072096(case):
        yield from conclusion_3929361033208322153670901849644072096(case)

    elif conditions_114740124515448400708123236287653930408(case):
        yield from conclusion_114740124515448400708123236287653930408(case)
    else:
        return None
