#!/usr/bin/env python3
from owlready2 import *

onto = get_ontology("http://test.org/onto.owl")

class Emission(Thing):
    namespace = onto

print(Emssion.iri)