#!/usr/bin/env python3
"""create owl"""
import re
import types
import owlready2


def main():
    """main"""
    onto = owlready2.get_ontology("file://test.owl")

    class Technique(owlready2.Thing):
        """class emission"""
        namespace = onto

    Technique.comment = ["A scientific technique"]

    class Absorption(Technique):
        """class absorption"""

    Absorption.comment = ["Spectroscopic techniques that measure the absorption of radiation, as a function of frequency or wavelength, due to its interaction with a sample"]

    class Diffraction(Technique):
        """class diffraction"""
    Diffraction.comment = [" X-ray, neutron, or electron diffraction on samples for structural characterization of materials"]

    class Emission(Technique):
        """class emission"""

    Emission.comment = ["Scientific technique based on emission"]

    class Imaging(Technique):
        """class emission"""

    class IonSpectroscopy(Technique):
        """class emission"""

    class Lithography(Technique):
        """class emission"""

    class Scattering(Technique):
        """class emission"""

    with onto:
        exafs = types.new_class(
            "ExtendedXRayAbsorptionFineStructure", (Absorption,))
        exafs = types.new_class("InfraRedSpectroscopy", (Absorption,))
        exafs = types.new_class("InelasticNeutronScatteringSpectroscopy", (Absorption,))
        exafs = types.new_class("NeutronSpectroscopy", (Absorption,))
        exafs = types.new_class(
            "NearEdgeXrayAbsorptionFineStructure", (Absorption,))
        exafs = types.new_class("AbsorptionTimeResolvedStudies", (Absorption,))
        exafs = types.new_class("UltravioletCircularDichroism", (Absorption,))
        exafs = types.new_class("XrayMagneticCircularDichroism", (Absorption,))

    exafs = types.new_class("Crystallography", (Diffraction,))
    exafs = types.new_class(
        "CrystallographyBiologicalMacromolecules", (Diffraction,))
    exafs = types.new_class("NeutronDiffraction", (Diffraction,))
    exafs = types.new_class("PowderDiffraction", (Diffraction,))
    exafs = types.new_class("SurfaceDiffraction", (Diffraction,))
    exafs = types.new_class("DiffractionTimeResolvedStudies", (Diffraction,))
    exafs = types.new_class("Topography", (Diffraction,))

    exafs = types.new_class("Ellipsometry", (Emission,))
    exafs = types.new_class("MicroXrayFluorescence", (Emission,))
    exafs = types.new_class("Polarimetry", (Emission,))
    exafs = types.new_class("Reflectometry ", (Emission,))
    exafs = types.new_class("NeutronReflectometry ", (Emission,))
    exafs = types.new_class("EmissionTimeResolvedStudies", (Emission,))
    exafs = types.new_class("XrayExcitedOpticalLuminescence", (Emission,))
    exafs = types.new_class("XrayFluorescence", (Emission,))

    exafs = types.new_class("CoherentDiffractiveImaging", (Imaging,))
    exafs = types.new_class("FluorescenceImaging", (Imaging,))
    exafs = types.new_class("InfraRedMicroscopy", (Imaging,))
    exafs = types.new_class("MedicalApplications", (Imaging,))
    exafs = types.new_class("PhotoemissionElectronMicroscopy", (Imaging,))
    exafs = types.new_class("Ptychography", (Imaging,))
    exafs = types.new_class(
        "ScanningPhotoemissionElectronMicroscopy", (Imaging,))
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
    exafs = types.new_class("PolarisedNeutronReflectivity", (Scattering,))
    exafs = types.new_class("ResonantScattering", (Scattering,))
    exafs = types.new_class("SmallAngleScattering", (Scattering,))
    exafs = types.new_class("SmallAngleNeutronScattering", (Scattering,))
    exafs = types.new_class("SpinEchoSmallAngleNeutronScattering", (Scattering,))
    exafs = types.new_class("TimeResolvedScattering", (Scattering,))
    exafs = types.new_class("WideAngleScattering", (Scattering,))
    # print(list(onto.classes()))

    techniques = [Absorption,
                 Diffraction, Emission, Imaging,
                 IonSpectroscopy, Lithography, Scattering]
    for technique in techniques:
        scatter = list(onto.search(subclass_of=technique))
        print("\n")
        print(technique.name)
        print("\n")
        for i in scatter:
            if i.name != technique.name:
                label = re.sub("([a-z])([A-Z])", "\g<1> \g<2>", i.name)
                print("* ", label)

    onto.save()


if __name__ == "__main__":
    main()
