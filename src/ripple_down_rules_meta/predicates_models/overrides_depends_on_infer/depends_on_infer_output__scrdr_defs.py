from typing_extensions import Type

from ripple_down_rules import has, dependsOn, PredicateOutputType
from ripple_down_rules.datastructures.tracked_object import TrackedObjectMixin
from ripple_down_rules.rules import Rule
from ripple_down_rules_meta import DependsOn


def conditions_3929361033208322153670901849644072096(case) -> bool:
    def conditions_for_depends_on_infer(cls_: Type[DependsOn], dependent: Type[TrackedObjectMixin],
                                           dependency: Type[TrackedObjectMixin], recursive: bool,
                                           **kwargs) -> bool:
        """Get conditions on whether it's possible to conclude a value for depends_on_infer.output_  of type ."""
        return (isinstance(dependent, type) and isinstance(dependency, type) and
                issubclass(dependent, TrackedObjectMixin) and issubclass(dependency, TrackedObjectMixin))

    return conditions_for_depends_on_infer(**case)


def conclusion_3929361033208322153670901849644072096(case) -> PredicateOutputType:
    def depends_on_infer(cls_: Type[DependsOn], dependent: Type[TrackedObjectMixin],
                            dependency: Type[TrackedObjectMixin], recursive: bool, **kwargs) -> PredicateOutputType:
        """Get possible value(s) for depends_on_infer.output_  of type ."""
        yield from has(dependent, dependency, recursive=recursive)

    yield from depends_on_infer(**case)


def conditions_114740124515448400708123236287653930408(case) -> bool:
    def conditions_for_depends_on_infer(cls_: Type[DependsOn], dependent: Type[TrackedObjectMixin],
                                           dependency: Type[TrackedObjectMixin], recursive: bool,
                                           **kwargs) -> bool:
        """Get conditions on whether it's possible to conclude a value for depends_on_infer.output_  of type ."""
        return isinstance(dependent, Rule) and isinstance(dependency, Rule)

    return conditions_for_depends_on_infer(**case)


def conclusion_114740124515448400708123236287653930408(case) -> PredicateOutputType:
    def depends_on_infer(cls_: Type[DependsOn], dependent: Type[TrackedObjectMixin],
                            dependency: Type[TrackedObjectMixin], recursive: bool, **kwargs) -> PredicateOutputType:
        """Get possible value(s) for depends_on_infer.output_  of type ."""
        yield from (dependsOn(dependent_ct, dependency_ct, recursive=recursive)
                for dependent_ct in dependent.conclusion.conclusion_type
                for dependency_ct in dependency.conclusion.conclusion_type
                if issubclass(dependent_ct, TrackedObjectMixin) and issubclass(dependency_ct, TrackedObjectMixin))

    yield from depends_on_infer(**case)
