from module_1_part_2_using_github_workflows_mtr2130 import emdat_readin
import os

prefix = os.getcwd()
filepath1 = prefix + "\\.data\\public_emdat_2025-09-01.xlsx"

emdat_readin.read_in_certain_disaster_type_or_subtype(
    filepath1, "Disaster Type", "Flood"
)
