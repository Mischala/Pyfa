# subsystemBonusAmarrElectronicEnergyDestabilizerAmount
#
# Used by:
# Subsystem: Legion Electronics - Energy Parasitic Complex
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Neutralizer",
                                  "energyDestabilizationAmount", module.getModifiedItemAttr("subsystemBonusAmarrElectronic"), skill="Amarr Electronic Systems")
