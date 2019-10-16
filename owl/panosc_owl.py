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
        newclass = types.new_class(
            "ExtendedXRayAbsorptionFineStructure", (Absorption,))
        exafs = types.new_class("InfraRedSpectroscopy", (Absorption,))
        exafs = types.new_class(
            "NearEdgeXrayAbsorptionFineStructure", (Absorption,))
        exafs = types.new_class("AbsorptionTimeResolvedStudies", (Absorption,))
        exafs = types.new_class("UltravioletCircularDichroism", (Absorption,))
        exafs = types.new_class("XrayMagneticCircularDichroism", (Absorption,))

    exafs = types.new_class("Crystallography", (Diffraction,))
    exafs = types.new_class(
        "CrystallographyBiologicalMacromolecules", (Diffraction,))
    exafs = types.new_class("PowerDiffraction", (Diffraction,))
    exafs = types.new_class("SurfaceDiffraction", (Diffraction,))
    exafs = types.new_class("DiffractionTimeResolvedStudies", (Diffraction,))
    exafs = types.new_class("Topography", (Diffraction,))

    exafs = types.new_class("Ellipsometry", (Emission,))
    exafs = types.new_class("MicroXrayFluorescence", (Emission,))
    exafs = types.new_class("Polarimetry", (Emission,))
    exafs = types.new_class("Reflectometry ", (Emission,))
    exafs = types.new_class("EmissionTimeResolvedStudies", (Emission,))
    exafs = types.new_class("XrayExcitedOpticalLuminescence", (Emission,))
    exafs = types.new_class("XrayFluorescence", (Emission,))

    exafs = types.new_class("CoherentDiffractiveImaging", (Imaging,))
    exafs = types.new_class("FluorescenceImaging", (Imaging,))
    exafs = types.new_class("InfraRedMicroscopy", (Imaging,))
    exafs = types.new_class("MedicalApplications", (Imaging,))
    exafs = types.new_class("PhotoemissionElectronMicroscopy", (Imaging,))
    exafs = types.new_class("Ptychography", (Imaging,))
    exafs = types.new_class("ScanningPhotoemissionElectronMicroscopy", (Imaging,))
    exafs = types.new_class("TeraHertzNearFieldMicroscopy", (Imaging,))
    exafs = types.new_class("XrayHolography", (Imaging,))
    exafs = types.new_class("XrayMicroscopy", (Imaging,))
    exafs = types.new_class("XrayTomography", (Imaging,))

    exafs = types.new_class("IonImaging", (IonSpectroscopy,))
    exafs = types.new_class("MassSpectrometry", (IonSpectroscopy,))

    exafs = types.new_class("ExtremeUltraVioletLithography", (Lithography,))
    exafs = types.new_class("XrayLithography", (Lithography,))

    exafs = types.new_class("AnomalousScattering", (Scattering,))
    exafs = types.new_class("CoherentScattering", (Scattering,))
    exafs = types.new_class("ElasticScattering", (Scattering,))
    exafs = types.new_class("InelasticScattering", (Scattering,))
    exafs = types.new_class("MagneticScattering", (Scattering,))
    exafs = types.new_class("NuclearResonantScattering", (Scattering,))
    exafs = types.new_class("QuasiElasticNeutronScattering", (Scattering,))
    exafs = types.new_class("Reflectivity", (Scattering,))
    exafs = types.new_class("ResonantScattering", (Scattering,))
    exafs = types.new_class("SmallAngleScattering", (Scattering,))
    exafs = types.new_class("SmallAngleNeutronScattering", (Scattering,))
    exafs = types.new_class("TimeResolvedScattering", (Scattering,))
    exafs = types.new_class("WideAngleScattering", (Scattering,))

    onto.save()


if __name__ == "__main__":
    main()
