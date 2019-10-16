#!/usr/bin/env python3
"""create owl"""
import types
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

    with onto:
        newclass = types.new_class("EXAFS", (Absorption,))
    # exafs = Absorption("Extended X-Ray Absorption Fine Structure (EXAFS)")
    exafs = Absorption("IR spectroscopy")
    exafs = Absorption("Near edge X-ray absorption fine structure (NEXAFS)")
    exafs = Absorption("Time-resolved studies")
    exafs = Absorption("Ultraviolet circular dichroism (UVCD)")
    exafs = Absorption("X-ray magnetic circular dichroism (XMCD)")

    exafs = Diffraction("Crystallography")
    exafs = Diffraction("Crystallography (biological macromolecules)")
    exafs = Diffraction("Power diffraction")
    exafs = Diffraction("Surface Diffraction")
    exafs = Diffraction("Time resolved studies")
    exafs = Diffraction("Topography")

    exafs = Emission("Ellipsometry")
    exafs = Emission("Micro XRF")
    exafs = Emission("Polarimetry")
    exafs = Emission("Reflectometry ")
    exafs = Emission("Time-resolved studies")
    exafs = Emission("X-ray excited optical luminescence (XEOL)")
    exafs = Emission("X-ray fluorescence (XRF)")

    exafs = Imaging("Ellipsometry")
    exafs = Imaging("Coherent diffractive imaging")
    exafs = Imaging("Fluorescence imaging")
    exafs = Imaging("IR Microscopy")
    exafs = Imaging("Medical application")
    exafs = Imaging("Photoemission EM")
    exafs = Imaging("Ptychography")
    exafs = Imaging("Scanning photoemission EM")
    exafs = Imaging("THz near-field microscopy")
    exafs = Imaging("X-ray holography")
    exafs = Imaging("X-ray microscopy")
    exafs = Imaging("X-ray tomography")

    exafs = IonSpectroscopy("Ellipsometry")

    exafs = Lithography("Ellipsometry")

    exafs = Scattering("Ellipsometry")

    onto.save()


if __name__ == "__main__":
    main()
