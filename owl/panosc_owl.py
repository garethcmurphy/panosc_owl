#!/usr/bin/env python3
"""create owl"""
import owlready2 

onto = owlready2.get_ontology("http://test.org/onto.owl")

class Emission(owlready2.Thing):
    """class emission"""
    namespace = onto

print(Emission.iri)