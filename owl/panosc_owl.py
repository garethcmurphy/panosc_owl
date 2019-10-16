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

    class IonSpectroscopy(Techniques):
        """class emission"""

    class Lithography(Techniques):
        """class emission"""

    class Scattering(Techniques):
        """class emission"""

    exafs = Absorption("Extended X-Ray Absorption Fine Structure (EXAFS)")
    exafs = Absorption("IR spectroscopy")
    exafs = Absorption("Near edge X-ray absorption fine structure (NEXAFS)")
    exafs = Absorption("Time-resolved studies")
    exafs = Absorption("Ultraviolet circular dichroism (UVCD)")
    exafs = Absorption("X-ray magnetic circular dichroism (XMCD)")

    exafs = Diffraction("Ellipsometry")
    exafs = Diffraction("Micro XRF")
    exafs = Diffraction("Polarimetry")
    exafs = Diffraction("Reflectometry ")
    exafs = Diffraction("Time-resolved studies")
    exafs = Diffraction("X-ray excited optical luminescence (XEOL)")
    exafs = Diffraction("X-ray fluorescence (XRF)")

    exafs = Emission("Ellipsometry")

    exafs = Imaging("Ellipsometry")

    exafs = IonSpectroscopy("Ellipsometry")

    exafs = Lithography("Ellipsometry")

    exafs = Scattering("Ellipsometry")


    onto.save()


if __name__ == "__main__":
    main()
