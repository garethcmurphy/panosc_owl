#!/usr/bin/env python3
"""create owl"""
import owlready2


def main():
    """main"""
    onto = owlready2.get_ontology("file://test.owl")

    class Absorption(owlready2.Thing):
        """class emission"""
        namespace = onto

    class Emission(owlready2.Thing):
        """class emission"""
        namespace = onto

    onto.save()


if __name__ == "__main__":
    main()
