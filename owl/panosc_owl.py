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
        newclass = types.new_class("ExtendedXRayAbsorptionFineStructure", (Absorption,))
        exafs = types.new_class("InfraRedSpectroscopy", (Absorption,))
        exafs = types.new_class("NearEdgeXrayAbsorptionFineStructure", (Absorption,))
        exafs = types.new_class("TimeResolvedStudies", (Absorption,))
        exafs = types.new_class("UltravioletCircularDichroism", (Absorption,))
        exafs = types.new_class("XrayMagneticCircularDichroism", (Absorption,))

    exafs = types.new_class("Crystallography", (Diffraction,))
    exafs = types.new_class("CrystallographyBiologicalMacromolecules", (Diffraction,))
    exafs = types.new_class("PowerDiffraction", (Diffraction,))
    exafs = types.new_class("SurfaceDiffraction", (Diffraction,))
    exafs = types.new_class("TimeResolvedStudies", (Diffraction,))
    exafs = types.new_class("Topography", (Diffraction,))

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
