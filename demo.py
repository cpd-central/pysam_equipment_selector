import PySAM.Pvwattsv5 as pv
model = pv.new()

model.SystemDesign.__setattr__('azimuth', 10)

#print(model.SystemDesign.__getattribute__('azimuth'))

sysD = {'azimuth': 100,
        'gcr': 0.5}

model.SystemDesign.assign(sysD)
#print(model.SystemDesign.__getattribute__('gcr'))

resource = {'solar_resource_file': 'file.csv'}

model_dict = {'SystemDesign': sysD, 'LocationAndResource': resource}
model.assign(model_dict)
#print(model.export())

error_dict = {'azimuth': 0, 'DNE': 0}

model.execute()
#model.SystemDesign.assign(error_dict)



