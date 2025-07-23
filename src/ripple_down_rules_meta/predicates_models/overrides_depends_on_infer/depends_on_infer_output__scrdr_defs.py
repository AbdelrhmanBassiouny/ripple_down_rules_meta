from typing_extensions import Type, Tuple, Generator

from ripple_down_rules import has, dependsOn
from ripple_down_rules.datastructures.tracked_object import TrackedObjectMixin
from ripple_down_rules.rules import Rule
from ripple_down_rules_meta import DependsOn


def conditions_3929361033208322153670901849644072096(case) -> bool:
    def conditions_for_depends_on_evaluate(cls_: Type[DependsOn], dependent: Type[TrackedObjectMixin],
                                           dependency: Type[TrackedObjectMixin], recursive: bool,
                                           **kwargs) -> bool:
        """Get conditions on whether it's possible to conclude a value for depends_on_evaluate.output_  of type ."""
        return (isinstance(dependent, type) and isinstance(dependency, type) and
                issubclass(dependent, TrackedObjectMixin) and issubclass(dependency, TrackedObjectMixin))

    return conditions_for_depends_on_evaluate(**case)


def conclusion_3929361033208322153670901849644072096(case) \
        -> Generator[Tuple[Type[TrackedObjectMixin], Type[TrackedObjectMixin]], None, None]:
    def depends_on_evaluate(cls_: Type[DependsOn], dependent: Type[TrackedObjectMixin],
                            dependency: Type[TrackedObjectMixin], recursive: bool, **kwargs) \
            -> Generator[Tuple[Type[TrackedObjectMixin], Type[TrackedObjectMixin]], None, None]:
        """Get possible value(s) for depends_on_evaluate.output_  of type ."""
        yield from has(dependent, dependency, recursive=recursive)

    return depends_on_evaluate(**case)


def conditions_114740124515448400708123236287653930408(case) -> bool:
    def conditions_for_depends_on_evaluate(cls_: Type[DependsOn], dependent: Type[TrackedObjectMixin],
                                           dependency: Type[TrackedObjectMixin], recursive: bool, is_reversed: bool,
                                           **kwargs) -> bool:
        """Get conditions on whether it's possible to conclude a value for depends_on_evaluate.output_  of type ."""
        return isinstance(dependent, Rule) and isinstance(dependency, Rule)

    return conditions_for_depends_on_evaluate(**case)


def conclusion_114740124515448400708123236287653930408(case) \
        -> Generator[Tuple[Type[TrackedObjectMixin], Type[TrackedObjectMixin]], None, None]:
    def depends_on_evaluate(cls_: Type[DependsOn], dependent: Type[TrackedObjectMixin],
                            dependency: Type[TrackedObjectMixin], recursive: bool, is_reversed: bool, **kwargs) \
            -> Generator[Tuple[Type[TrackedObjectMixin], Type[TrackedObjectMixin]], None, None]:
        """Get possible value(s) for depends_on_evaluate.output_  of type ."""
        yield from (dependsOn(dependent_ct, dependency_ct, recursive=recursive, is_reversed=is_reversed)
                    for dependent_ct in dependent.conclusion.conclusion_type
                    for dependency_ct in dependency.conclusion.conclusion_type
                    if issubclass(dependent_ct, TrackedObjectMixin) and issubclass(dependency_ct, TrackedObjectMixin))

    return depends_on_evaluate(**case)
