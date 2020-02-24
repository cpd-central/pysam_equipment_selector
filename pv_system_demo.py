import PySAM.Pvwattsv5 as pv

d = pv.default('PVWattsSingleOwner')

d.LocationAndResource.solar_resource_file = 'resource.csv'
d.execute()








