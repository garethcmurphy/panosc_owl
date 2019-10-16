#!/usr/bin/env python3
"""create owl"""
import owlready2 

onto = owlready2.get_ontology("file://test.owl")

class Emission(owlready2.Thing):
    """class emission"""
    namespace = onto


print(Emission.iri)
onto.save()