#!/usr/bin/env python3
"""create owl"""
import owlready2


def main():
    """main"""
    onto = owlready2.get_ontology("file://test.owl")

    class Techniques(owlready2.Thing):
        """class emission"""
        namespace = onto

    class Absorption(Techniques):
        """class absorption"""

    class Diffraction(Techniques):
        """class emission"""

    class Emission(Techniques):
        """class emission"""

    class Imaging(Techniques):
        """class emission"""

    exafs = Absorption("Extended X-Ray Absorption Fine Structure (EXAFS)")
    exafs = Absorption("IR spectroscopy")
    exafs = Absorption("Near edge X-ray absorption fine structure (NEXAFS)")
    exafs = Absorption("Time-resolved studies")
    exafs = Absorption("Ultraviolet circular dichroism (UVCD)")
    exafs = Absorption("X-ray magnetic circular dichroism (XMCD)")

    exafs = Emission("Ellipsometry")


    onto.save()


if __name__ == "__main__":
    main()
