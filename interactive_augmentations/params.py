import cv2

blur_params = {
    "blur_limit": ["int_range", 3, 100, "all"],
}

center_crop_params = {
    "height": ["int", 1, "height", "all"],
    "width": ["int", 1, "width", "all"],
}

channel_dropout_params = {"channel_drop_range": ["int_range", 1, "channels-1", "all"]}

channel_shuffle_params = {}

clahe_params = {
    "clip_limit": ["float_range", 1, 100, "all"],
    "tile_grid_size": ["int_range", 1, 50, "all"],
}

fancypca_params = {"alpha": ["float", -10.0, 10.0, "all"]}

flip_params = {}

gaussianblur_params = {
    "blur_limit": ["int_range", 1, 101, "odd"],
    # "sigma_limit": ["float_range",0,100,"all"] RAISES AN ERROR
}

gaussnoise_params = {
    "var_limit": ["float_range", 0, 100, "all"],
    "mean": ["float", -100, 100, "all"],
}

glassblur_params = {
    "sigma": ["float", 0.01, 100, "all"],
    "max_delta": ["int", 1, 10, "all"],
    "iterations": ["int", 1, 100, "all"],
    "mode": ["str", ("fast", "exact"), "all"],
}

griddistortion_params = {
    "num_steps": ["int", 1, 100, "all"],
    "distort_limit": ["float_range", -1, 1, "all"],
}

horizontal_flip_params = {}
huesaturationvalue_params = {
    "hue_shift_limit": ["int_range", -100, 100, "all"],
    "sat_shift_limit": ["int_range", -100, 100, "all"],
    "val_shift_limit": ["int_range", -100, 100, "all"],
}
imagecompression_params = {
    "quality_upper": ["int", 0, 100, "all"],
    "quality_lower": ["int", 0, 100, "all"],
}
invertimg_params = {}

isonoise_params = {
    "color_shift": ["float_range", 0, 360, "all"],
    "intensity": ["float_range", 0, 100, "all"],
}

jpegcompression_params = {
    "quality_upper": ["int", 0, 100, "all"],
    "quality_lower": ["int", 0, 100, "all"],
}

longestmaxsize_params = {"max_size": ["int", 1, 10000, "all"]}

medianblur_params = {
    "blur_limit": ["int_range", 1, 20, "odd"],
}

motionblur_params = {
    "blur_limit": ["int_range", 3, 101, "odd"],
}

normalize_parms = {}

opticaldistortion_params = {
    "distort_limit": ["float_range", -1, 1, "all"],
    "shift_limit": ["float_range", -1, 1, "all"],
}

posterize_params = {"num_bits": ["int_range", 0, 8, "all"]}

randombrightness_params = {"limit": ["float_range", -1, 1, "all"]}

randombrightnesscontrast_params = {
    "brightness_limit": ["float_range", -1, 1, "all"],
    "contrast_limit": ["float_range", -1, 1, "all"],
    "brightness_by_max": ["bool", (True, False), "all"],
}

randomcontrast_params = {"limit": ["float_range", -1, 1, "all"]}

randomcrop_params = {
    "height": ["int", 1, "height", "all"],
    "width": ["int", 1, "width", "all"],
}

randomfog_params = {
    "fog_coef_upper": ["float", 0, 1, "all"],
    "fog_coef_lower": ["float", 0, 1, "all"],
    "alpha_coef": ["float", 0, 1, "all"],
}

randomgamma_params = {"gamma_limit": ["int_range", -200, 200, "all"]}

randomgridshuffle_params = {"grid": ["int_range", 1, 30, "all"]}

randomrain_params = {
    "slant_upper": ["float", -20, 20, "all"],
    "slant_lower": ["float", -20, 20, "all"],
    "drop_length": ["int", 0, 100, "all"],
    "drop_width": ["int", 1, 5, "all"],
    "blur_value": ["int", 1, 100, "all"],
    "brightness_coefficient": ["float", 0.0, 1, "all"],
    "rain_type": ["str", (None, "drizzle", "heavy", "torrential"), "all"],
}

randomrotate90_params = {}

randomscale_params = {"scale_limit": ["float_range", 0, 10, "all"]}

randomsnow_params = {
    "snow_point_upper": ["float", 0, 1, "all"],
    "snow_point_lower": ["float", 0, 1, "all"],
    "brightness_coeff": ["float", 0, 100, "all"],
}

rotate_params = {
    "limit": ["float_range", -360, 360, "all"],
    "border_mode": [
        "str",
        (
            cv2.BORDER_CONSTANT,
            cv2.BORDER_REPLICATE,
            cv2.BORDER_REFLECT,
            cv2.BORDER_WRAP,
            cv2.BORDER_REFLECT_101,
        ),
        "all",
    ],
}

rgbshift_params = {
    "r_shift_limit": ["int_range", -100, 100, "all"],
    "g_shift_limit": ["int_range", -100, 100, "all"],
    "b_shift_limit": ["int_range", -100, 100, "all"],
}

resize_params = {"height": ["int", 1, 2000, "all"], "width": ["int", 1, 2000, "all"]}


shiftscalerotate_params = {
    "rotate_limit": ["int_range", -360, 360, "all"],
    "shift_limit": ["float_range", -1, 1, "all"],
    "scale_limit": ["float_range", -10, 10, "all"],
    "border_mode": [
        "str",
        (
            cv2.BORDER_CONSTANT,
            cv2.BORDER_REPLICATE,
            cv2.BORDER_REFLECT,
            cv2.BORDER_WRAP,
            cv2.BORDER_REFLECT_101,
        ),
        "all",
    ],
}

smallestmaxsize_params = {"max_size": ["int", 1, 2000, "all"]}

solarize_params = {"threshold": ["float", 0, 400, "all"]}

togray_params = {}

tosepia_params = {}

transpose_params = {}


vertical_flip_params = {}

parameters_dictionary = {
    "Blur": blur_params,
    "ShiftScaleRotate": shiftscalerotate_params,
    "CenterCrop": center_crop_params,
    "ChannelDropout": channel_dropout_params,
    "CLAHE": clahe_params,
    "FancyPCA": fancypca_params,
    "Flip": flip_params,
    "GaussianBlur": gaussianblur_params,
    "GaussNoise": gaussnoise_params,
    "GlassBlur": glassblur_params,
    "GridDistortion": griddistortion_params,
    "HorizontalFlip": horizontal_flip_params,
    "HueSaturationValue": huesaturationvalue_params,
    "InvertImg": invertimg_params,
    "ImageCompression": imagecompression_params,
    "ISONoise": isonoise_params,
    "JpegCompression": jpegcompression_params,
    "LongestMaxSize": longestmaxsize_params,
    "MedianBlur": medianblur_params,
    "MotionBlur": motionblur_params,
    "Normalize": normalize_parms,  # NOT DONE,
    "OpticalDistortion": opticaldistortion_params,
    "Posterize": posterize_params,
    "RandomBrightness": randombrightness_params,
    "RandomBrightnessContrast": randombrightnesscontrast_params,
    "RandomContrast": randomcontrast_params,
    "RandomCrop": randomcrop_params,
    "RandomFog": randomfog_params,
    "RandomGamma": randomgamma_params,
    "RandomGridShuffle": randomgridshuffle_params,
    "RandomRain": randomrain_params,
    "RandomScale": randomscale_params,
    "Rotate": rotate_params,
    "RGBShift": rgbshift_params,
    "Resize": resize_params,
    "ChannelShuffle": channel_shuffle_params,
    "RandomRotate90": randomrotate90_params,
    "RandomSnow": randomsnow_params,
    "SmallestMaxSize": smallestmaxsize_params,
    "Solarize": solarize_params,
    "ToGray": togray_params,
    "ToSepia": tosepia_params,
    "Transpose": transpose_params,
    "VerticalFlip": vertical_flip_params,
}
