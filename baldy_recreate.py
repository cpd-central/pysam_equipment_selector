import PySAM.Pvsamv1 as pv


#lists and dictionaries for variable parameters
MODULES = [ 
    {   
        'name': 'Jinko EaglePercG2 JKM395M-72HL-V-A1-US',
        'size': 395, 
        'specs': {
            'spe_a': -3.56,
            'spe_area': 2.012016,
            'spe_b': -0.075,
            'spe_bifacial_ground_clearance_height': 0,
            'spe_bifacial_transmission_factor': 0,
            'spe_bifaciality': 0,
            'spe_dT': 3,
            'spe_eff0': 19.63,
            'spe_eff1': 19.63,
            'spe_eff2': 19.63,
            'spe_eff3': 19.63,
            'spe_eff4': 19.63,
            'spe_fd': 1,
            'spe_is_bifacial': 0,
            'spe_module_structure': 0, 
            'spe_rad0': 200,
            'spe_rad1': 400,
            'spe_rad2': 600,
            'spe_rad3': 800,
            'spe_rad4': 1000,
            'spe_reference': 4,
            'spe_temp_coeff': -0.36,
            'spe_vmp': 41.7,
            'spe_voc': 49.8
        }
    },
    { 
        'name': 'Trina Duomax Twin SPLITMAX A-395W',
        'size': 395, 
        'specs': {
            'spe_a': -3.47 ,
            'spe_area': 2.03,
            'spe_b': -0.075,
            'spe_bifacial_ground_clearance_height': 0,
            'spe_bifacial_transmission_factor': 0,
            'spe_bifaciality': 0,
            'spe_dT': 3,
            'spe_eff0': 19.4,
            'spe_eff1': 19.4,
            'spe_eff2': 19.4,
            'spe_eff3': 19.4,
            'spe_eff4': 19.4,
            'spe_fd': 1,
            'spe_is_bifacial': 0,
            'spe_module_structure': 0,
            'spe_rad0': 200,
            'spe_rad1': 400,
            'spe_rad2': 600,
            'spe_rad3': 800,
            'spe_rad4': 1000,
            'spe_reference': 4,
            'spe_temp_coeff': -0.36,
            'spe_vmp': 40.6,
            'spe_voc': 49.8
        }
    }
]

INVERTERS = [
    {
        'name': 'Sunny Central 2500-EV',
        'specs': {
            'inv_snl_c0': -1.04494e-08,
            'inv_snl_c1': 7.85775e-06,
            'inv_snl_c2': 0.000749,
            'inv_snl_c3': -8.9e-05,
            'inv_snl_paco': 2.35387e06,
            'inv_snl_pdco': 2.43339e06,
            'inv_snl_pnt': 706.161,
            'inv_snl_pso': 8719.04,
            'inv_snl_vdcmax': 1425,
            'inv_snl_vdco': 994,
            'inv_tdc_cec_db': [[0, 0, 0]]
        }
    }
] 

RACKING_OPTIONS = [
    'SAT'
]

GCRS = [
    .25,
    .30,
    .35,
    .40,
    .45,
    .50
]

AZIMUTHS = [
    90,
    100,
    110,
    120,
    130,
    140,
    150,
    160,
    170,
    180,
    190,
    200,
    210,
    220,
    230,
    240,
    250,
    260,
    270
]

DCAC_RATIOS = [
    1,
    1.1,
    1.2,
    1.3,
    1.4,
    1.5
]

STRING_LENGTH = 27

AC_SIZE = 1e8
LAND_AVAILABLE = None 


############################################
#############CREATE MODEL###################
############################################
def determine_num_strings(dcac_ratio, string_length, module_size):
    string_size = string_length * module_size
    num_strings = (dcac_ratio / string_size)
    return num_strings 

def define_system_design(inv_count, az, gcr, string_length, num_mppt, num_strings, ac_size):
    system_design = {
        'enable_mismatch_vmax_calc': 0,
        'inverter_count': inv_count,
        'subarray1_azimuth': az,
        'subarray1_backtrack': 1,
        'subarray1_gcr': gcr,
        'subarray1_modules_per_string': string_length,
        'subarray1_mppt_input': num_mppt,
        'subarray1_nstrings': num_strings,
        'subarray1_rotlim': 60,
        'subarray1_tilt': 0,
        'subarray1_tilt_eq_lat': 0,
        'subarray1_track_mode': 1,
        'subarray2_enable': 0,
        'subarray3_enable': 0,
        'subarray4_enable': 0,
        'system_capacity': ac_size 
    }
    return system_design

def define_shading():
    shading = {
        'subarray1_shade_mode': 1,
        'subarray1_shading_string_option': 1
            }                               
    return shading

def define_layout(aspect_ratio):
    layout = {
        'module_aspect_ratio': aspect_ratio,
        'subarray1_mod_orient': 1,
        'subarray1_nmodx': 1,
        'subarray1_nmody': 81
        }
    return layout

def define_losses():
    losses = {
        'acwiring_loss': 0,
        'dcoptimizer_loss': 0,
        'en_snow_model': 0,
        'subarray1_dcwiring_loss': 0,
        'subarray1_diodeconn_loss': 0,
        'subarray1_mismatch_loss': 0,
        'subarray1_nameplate_loss': 0,
        'subarray1_rear_irradiance_loss': 0,
        'subarray1_soiling': [3 for c in range(0, 12)],
        'subarray1_tracking_loss': 0,
        'subarray2_dcwiring_loss': 0,
        'subarray2_diodeconn_loss': 0,
        'subarray2_mismatch_loss': 0,
        'subarray2_nameplate_loss': 0,
        'subarray2_rear_irradiance_loss': 0,
        'subarray2_soiling': [3 for c in range(0, 12)],
        'subarray2_tracking_loss': 0,
        'transformer_load_loss': 0,
        'transformer_no_load_loss': 0,
        'transmission_loss': 0
    } 
    return losses

def define_adjustment_factors():
    adjustment_factors = {
        'constant': 1,
        'dc_constant': 0
    }
    return adjustment_factors

def assign_model_parameters(model):
    """ 
    **kwargs method for later 
    for key, value in kwargs.items():
        exec("%s = %d" % (key, )) 
        model.key.assign(value)
    """ 
    return model 


def create_model(ac_size=None,
                modules=None, 
                inverters=None, 
                racking_options=None, 
                gcrs=None, 
                azimuths=None, 
                dcac_ratios=None,
                string_length=None):
    #create the new model
    model = pv.new()
    
    #define the module parameters to assign
    #weather file
    solar_resource = {
        'solar_resource_file': r'C:\Users\jmarsnik\SAM Downloaded Weather Files\centralia_il_38.526099_-89.133204_psmv3_60_tmy.csv',
        'albedo': [0.2 for c in range(0, 12)],
        'use_wf_albedo': 1
    } 
    #module model definition 
    module_model = {
        #0 for simple efficiency 
        'module_model': 0
    }
    #inverter model definition 
    inverter_model = {
        'inverter_model': 0,
        'inv_num_mppt': 1,
        'mppt_hi_inverter': 1425,
        'mppt_low_inverter': 850
    }  

    #now do our grid loop and update the module and inverter databases and build the system design/shading
    i = 0 
    model_dict = {} 
    for module in modules: 
        for inverter in inverters:
            for racking_option in racking_options:
                for gcr in gcrs:
                    for azimuth in azimuths:
                        for dcac_ratio in dcac_ratios: 
                            #to determine the number of strings, we need the dc to ac ratio, string length and module size
                            string_size = string_length * module['size']
                            #module definition:
                            module_specs = module['specs']
                            #inverter specifications: 
                            inverter_specs = inverter['specs']
                            inverter_ac_output = inverter_specs['inv_snl_paco'] 
                            #the amount of dc we can put on the inverter given the dcac_ratio 
                            inverter_dc_input = inverter_ac_output * dcac_ratio 
                            inv_num_strings = round(inverter_dc_input / string_size)
                            #system design (takes in gcr, dcac, azimuth, etc.)
                            inverter_count = round(ac_size / inverter_ac_output)
                            total_strings = inv_num_strings * inverter_count

                            system_design = define_system_design(inverter_count, 
                                                                 azimuth,
                                                                 gcr,
                                                                 string_length,
                                                                 inverter_model['inv_num_mppt'],
                                                                 total_strings,
                                                                 ac_size)     
                            shading = define_shading()
                            layout = define_layout(module_specs['spe_area']) 
                            losses = define_losses()
                            adjustment_factors = define_adjustment_factors() 
                            
                            #assign all of the model parameters, execute and get output

                            model.SolarResource.assign(solar_resource)
                            model.Module.assign(module_model)
                            model.Inverter.assign(inverter_model)
                            model.InverterCECDatabase.assign(inverter_specs)
                            model.SimpleEfficiencyModuleModel.assign(module_specs)
                            model.SystemDesign.assign(system_design)
                            model.Shading.assign(shading)
                            model.Losses.assign(losses)
                            model.Layout.assign(layout)
                            model.AdjustmentFactors.assign(adjustment_factors)
 
                            model.execute()

                            output = model.Outputs.export()
                            model_name = f"{module['name']}_{inverter['name']}_{racking_option}_{gcr}_{azimuth}_{dcac_ratio}"
                            model_energy = output['annual_energy']
                            model_dict[model_name] = model_energy 
                            print(f"{i} : {model_name} : {model_energy}")
                            i += 1
    max_energy_model = max(model_dict, key=model_dict.get)
    return max_energy_model 

max_energy_model = create_model(ac_size=AC_SIZE,
                          modules=MODULES, 
                          inverters=INVERTERS,
                          racking_options=RACKING_OPTIONS,
                          gcrs=GCRS,
                          azimuths=AZIMUTHS,
                          dcac_ratios=DCAC_RATIOS,
                          string_length=STRING_LENGTH)

print(f'Max energy model : {max_energy_model}')


