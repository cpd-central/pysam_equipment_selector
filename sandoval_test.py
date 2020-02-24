#single owner model
import PySAM.Pvsamv1 as pv

model = pv.new()

#weather file
solar_resource = {
    'solar_resource_file': r'C:\Users\jmarsnik\SAM Downloaded Weather Files\centralia_il_38.526099_-89.133204_psmv3_60_tmy.csv',
    'albedo': [0.2 for c in range(0, 12)],
    'use_wf_albedo': 1
}

#module model
module = {
    'module_model': 0
}

#simple efficiency module model
simple_eff_module_model = {
    'spe_a': -3.56,
    'spe_area': 1.94236,
    'spe_b': -0.075,
    'spe_bifacial_ground_clearance_height': 0,
    'spe_bifacial_transmission_factor': 0,
    'spe_bifaciality': 0,
    'spe_dT': 3,
    'spe_eff0': 16.99,
    'spe_eff1': 16.99,
    'spe_eff2': 16.99,
    'spe_eff3': 16.99,
    'spe_eff4': 16.99,
    'spe_fd': 0,
    'spe_is_bifacial': 0,
    'spe_module_structure': 0,
    'spe_rad0': 200,
    'spe_rad1': 400,
    'spe_rad2': 600,
    'spe_rad3': 800,
    'spe_rad4': 1000,
    'spe_reference': 4,
    'spe_temp_coeff': -0.41,
    'spe_vmp': 37.65,
    'spe_voc': 46.4
}

#cec database module parameters
"""
cec_perf_model_module = {
    'cec_a_ref': 1,
    'cec_adjust': 1,
    'cec_alpha_sc': 0.004,
    'cec_area': 1.88,
    'cec_array_cols': 324,
    'cec_array_rows': 28,
    'cec_backside_temp': 20,
    'cec_beta_oc': -0.137,
    'cec_bifacial_ground_clearance_height': 1,
    'cec_bifacial_transmission_factor': 1,
    'cec_bifaciality': 1,
    'cec_gamma_r': -0.385,
    'cec_gap_spacing': 2,
    'cec_heat_transfer': 1,
    'cec_height': 0,
    'cec_i_l_ref': 9.28541,
    'cec_i_mp_ref': 8.8,
    'cec_i_o_ref': 4.53172e-11,
    'cec_i_sc_ref': 9.3,
    'cec_is_bifacial': 0,
    'cec_module_length': 1.960,
    'cec_module_width': .991,
    'cec_mounting_config': 0,
    'cec_mounting_orientation': 1,
    'cec_n_s': 72,
    'cec_r_s': 0.385724,
    'cec_r_sh_ref': 661.401,
    'cec_standoff': 6,
    'cec_t_noct': 45.1,
    'cec_temp_corr_mode': 0,
    'cec_v_mp_ref': 37.7,
    'cec_v_oc_ref': 46.4
}
"""

#modeul parameters user input
"""
cec_perf_model_module_user_input = {
    '6par_aisc': 0.058,
    '6par_area': 1.94,
    '6par_bifacial_ground_clearance_height': 2,
    '6par_bifacial_transmission_factor': 2,
    '6par_bifaciality': 2,
    '6par_bvoc': -0.330,
    '6par_celltech': 1,
    '6par_gpmp': -0.410,
    '6par_imp': 8.77,
    '6par_is_bifacial': 0,
    '6par_isc': 9.28,
    '6par_mounting': 0,
    '6par_nser': 72,
    '6par_standoff': 6,
    '6par_tnoct': 45,
    '6par_vmp': 37.65,
    '6par_voc': 46.40
}
"""
#inverter model
inverter = {
    'inverter_model': 0,
    'inv_num_mppt': 1,
    'mppt_hi_inverter': 1300,
    'mppt_low_inverter': 870
}

#inverter parameters
"""
inv_datasheet = {
    'inv_ds_eff': 98.8,
    'inv_ds_paco': 125000,
    'inv_ds_pnt': 2,
    'inv_ds_pso': 250,
    'inv_ds_vdcmax': 1500,
    'inv_ds_vdco': 1085,
    'inv_tdc_ds': [[0, 0 , 0]]
}
"""

#inverter cec database parameters
inv_cec_database = {
    'inv_snl_c0': -8.7415e-08,
    'inv_snl_c1': 1.9e-05,
    'inv_snl_c2': 0.001616,
    'inv_snl_c3': 0.000381,
    'inv_snl_paco': 125000,
    'inv_snl_pdco': 127275,
    'inv_snl_pnt': 37.5,
    'inv_snl_pso': 143.167,
    'inv_snl_vdcmax': 1300,
    'inv_snl_vdco': 1000,
    'inv_tdc_cec_db': [[0, 0, 0]]
}


#system design parameters
system_design = {
    'enable_mismatch_vmax_calc': 0,
    'inverter_count': 16,
    'subarray1_azimuth': 180,
    'subarray1_backtrack': 1,
    'subarray1_gcr': .1,
    'subarray1_modules_per_string': 27,
    'subarray1_mppt_input': 1,
    'subarray1_nstrings': 228,
    'subarray1_rotlim': 60,
    'subarray1_tilt': 0,
    'subarray1_tilt_eq_lat': 0,
    'subarray1_track_mode': 1,
    'subarray2_azimuth': 180,
    'subarray2_backtrack': 1,
    'subarray2_enable': 1,
    'subarray2_gcr': .1,
    'subarray2_modules_per_string': 27,
    'subarray2_mppt_input': 1,
    'subarray2_nstrings': 72,
    'subarray2_rotlim': 60,
    'subarray2_tilt': 0,
    'subarray2_tilt_eq_lat': 0,
    'subarray2_track_mode': 1,
    'subarray3_enable': 0,
    'subarray4_enable': 0,
    'system_capacity': 2674543
}

#shading parameters
shading = {
    'subarray1_shade_mode': 1,
    'subarray1_shading_string_option': 1,
    'subarray2_shade_mode': 1,
    'subarray2_shading_string_option': 1
}

#layout parameters
layout = {
    'module_aspect_ratio': 1.978,
    #NOTE: trackers are in landscape if looking from the south yes?
    'subarray1_mod_orient': 1,
    'subarray1_nmodx': 1,
    'subarray1_nmody': 81,
    'subarray2_mod_orient': 1,
    'subarray2_nmodx': 1,
    'subarray2_nmody': 81
}

#losses parameters
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

#adjustment factors
adjustment_factors = {
    'constant': 1,
    'dc_constant': 0
}

#outputs
outputs = [
    'annual_export_to_grid_energy'
]

model.SolarResource.assign(solar_resource)
model.Module.assign(module)
model.Inverter.assign(inverter)
#model.InverterDatasheet.assign(inv_datasheet)
model.InverterCECDatabase.assign(inv_cec_database)
model.SimpleEfficiencyModuleModel.assign(simple_eff_module_model)
#model.CECPerformanceModelWithModuleDatabase.assign(cec_perf_model_module)
#model.CECPerformanceModelWithUserEnteredSpecifications.assign(cec_perf_model_module_user_input)
model.SystemDesign.assign(system_design)
model.Shading.assign(shading)
model.Losses.assign(losses)
model.Layout.assign(layout)
model.AdjustmentFactors.assign(adjustment_factors)

model.execute(1)

output = model.Outputs.export()

print(output['annual_energy'])



