# Create a README.md

## EM-DAT

This is for use with the EM-DAT database, which captures data on disasters around the world.
It can be found here:
https://public.emdat.be/data

## Calling in and filtering

The program emdat_readin.py includes a function which helps to automatically call in and filter the disaster data based on the disaster type that you want to look at.  For example, if you want to see flood data, you would put in the file path for the excel that is downloaded, "Disaster Type" (because flooding is a general disaster type and not a subtype), and "Flood".  This will then return the database, but only with floods selected.
