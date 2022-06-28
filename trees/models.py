from django.db import models

# Create your models here.

class SeasonomicsTree(models.Model):
    id = models.IntegerField(blank=True, null=False,primary_key=True)
    start = models.CharField(max_length=100, blank=True, null=True)
    end = models.CharField(max_length=100, blank=True, null=True)
    today = models.CharField(max_length=100, blank=True, null=True)
    logo = models.CharField(max_length=100, blank=True, null=True)
    name_reporter = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    # field_location_altitude = models.CharField(db_column='_location_altitude', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    # field_location_precision = models.CharField(db_column='_location_precision', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    # time = models.CharField(max_length=100, blank=True, null=True)
    # temperature_max_min_c_and_humidity_field = models.CharField(db_column='temperature (max-min °c) and humidity (%)', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    model_system = models.CharField(db_column='model system', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    # species_of_mosquitoes = models.CharField(db_column='species of mosquitoes', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    # total_number_of_mosquitoes = models.CharField(db_column='total number of mosquitoes', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    additional_description = models.CharField(db_column='additional description', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    # record_the_audio_10_15_sec_field = models.CharField(db_column='record the audio (10-15 sec)', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    # picture = models.CharField(max_length=100, blank=True, null=True)
    # field_version_field = models.CharField(db_column='__version__', max_length=100, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    # additional_picture = models.CharField(db_column='additional picture', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    # field_version_field_0 = models.CharField(db_column='_version_', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    # field_version_001 = models.CharField(db_column='_version__001', max_length=100, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    # additional_video = models.CharField(db_column='additional video', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    # name_of_the_observer = models.CharField(db_column='name of the observer', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    # where_have_you_observed_this_field = models.CharField(db_column='where have you observed this?', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    # field_where_have_you_observed_this_latitude = models.CharField(db_column='_where have you observed this?_latitude', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    # field_where_have_you_observed_this_longitude = models.CharField(db_column='_where have you observed this?_longitude', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    # field_where_have_you_observed_this_altitude = models.CharField(db_column='_where have you observed this?_altitude', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    # field_where_have_you_observed_this_precision = models.CharField(db_column='_where have you observed this?_precision', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    # what_is_the_time_of_observing_the_phyllanthus_sleeping_field = models.CharField(db_column='what is the time of observing the phyllanthus sleeping?', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    # logo_001 = models.CharField(max_length=100, blank=True, null=True)
    # details_of_the_tree_details_of_the_tree = models.CharField(db_column='details_of_the_tree/details of the tree', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    # select_the_observation_type = models.CharField(db_column='select the observation type', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    # mark_your_location_of_observation = models.CharField(db_column='mark your location of observation', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    # field_mark_your_location_of_observation_latitude = models.CharField(db_column='_mark your location of observation_latitude', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    # field_mark_your_location_of_observation_longitude = models.CharField(db_column='_mark your location of observation_longitude', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    # field_mark_your_location_of_observation_altitude = models.CharField(db_column='_mark your location of observation_altitude', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    # field_mark_your_location_of_observation_precision = models.CharField(db_column='_mark your location of observation_precision', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    # add_any_description_esp_if_the_observation_if_others_field = models.CharField(db_column='add any description (esp. if the observation if others)', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    # details_of_the_tree_header = models.CharField(db_column='details of the tree/header', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    # details_of_the_tree_leaves = models.CharField(db_column='details of the tree/leaves', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    # details_of_the_tree_flowers = models.CharField(db_column='details of the tree/flowers', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    # location_of_observation = models.CharField(max_length=100, blank=True, null=True)
    # details_of_the_tree_fruits = models.CharField(db_column='details of the tree/fruits', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    # local_name_of_the_model_organism = models.CharField(db_column='local name of the model organism', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    # record_the_audio = models.CharField(db_column='record the audio', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    # use_the_camera_to_record_a_video = models.CharField(db_column='use the camera to record a video', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    # field_id = models.CharField(db_column='_id', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    # field_uuid = models.CharField(db_column='_uuid', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    # field_submission_time = models.CharField(db_column='_submission_time', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    # field_validation_status = models.CharField(db_column='_validation_status', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    # field_notes = models.CharField(db_column='_notes', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    # field_status = models.CharField(db_column='_status', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    # field_submitted_by = models.CharField(db_column='_submitted_by', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    # field_tags = models.CharField(db_column='_tags', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    # field_index = models.CharField(db_column='_index', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'seasonomics_tree'


class Sampledata23June22(models.Model):
    id = models.IntegerField(blank=True, null=False,primary_key=True,)
    start = models.CharField(max_length=100, blank=True, null=True)
    end = models.CharField(max_length=100, blank=True, null=True)
    today = models.CharField(max_length=100, blank=True, null=True)
    logo = models.CharField(max_length=100, blank=True, null=True)
    name_reporter = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    field_location_altitude = models.CharField(db_column='_location_altitude', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    field_location_precision = models.CharField(db_column='_location_precision', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    time = models.CharField(max_length=100, blank=True, null=True)
    temperature_max_min_c_and_humidity_field = models.CharField(db_column='temperature (max-min °c) and humidity (%)', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    model_system = models.CharField(db_column='model system', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    species_of_mosquitoes = models.CharField(db_column='species of mosquitoes', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    total_number_of_mosquitoes = models.CharField(db_column='total number of mosquitoes', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    additional_description = models.CharField(db_column='additional description', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    record_the_audio_10_15_sec_field = models.CharField(db_column='record the audio (10-15 sec)', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    picture = models.CharField(max_length=100, blank=True, null=True)
    field_version_field = models.CharField(db_column='__version__', max_length=100, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    additional_picture = models.CharField(db_column='additional picture', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field_version_field_0 = models.CharField(db_column='_version_', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_version_001 = models.CharField(db_column='_version__001', max_length=100, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    additional_video = models.CharField(db_column='additional video', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    name_of_the_observer = models.CharField(db_column='name of the observer', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    where_have_you_observed_this_field = models.CharField(db_column='where have you observed this?', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    field_where_have_you_observed_this_latitude = models.CharField(db_column='_where have you observed this?_latitude', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_where_have_you_observed_this_longitude = models.CharField(db_column='_where have you observed this?_longitude', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_where_have_you_observed_this_altitude = models.CharField(db_column='_where have you observed this?_altitude', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_where_have_you_observed_this_precision = models.CharField(db_column='_where have you observed this?_precision', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    what_is_the_time_of_observing_the_phyllanthus_sleeping_field = models.CharField(db_column='what is the time of observing the phyllanthus sleeping?', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logo_001 = models.CharField(max_length=100, blank=True, null=True)
    details_of_the_tree_details_of_the_tree = models.CharField(db_column='details_of_the_tree/details of the tree', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    select_the_observation_type = models.CharField(db_column='select the observation type', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    mark_your_location_of_observation = models.CharField(db_column='mark your location of observation', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field_mark_your_location_of_observation_latitude = models.CharField(db_column='_mark your location of observation_latitude', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_mark_your_location_of_observation_longitude = models.CharField(db_column='_mark your location of observation_longitude', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_mark_your_location_of_observation_altitude = models.CharField(db_column='_mark your location of observation_altitude', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_mark_your_location_of_observation_precision = models.CharField(db_column='_mark your location of observation_precision', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    add_any_description_esp_if_the_observation_if_others_field = models.CharField(db_column='add any description (esp. if the observation if others)', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    details_of_the_tree_header = models.CharField(db_column='details of the tree/header', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    details_of_the_tree_leaves = models.CharField(db_column='details of the tree/leaves', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    details_of_the_tree_flowers = models.CharField(db_column='details of the tree/flowers', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    location_of_observation = models.CharField(max_length=100, blank=True, null=True)
    details_of_the_tree_fruits = models.CharField(db_column='details of the tree/fruits', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    local_name_of_the_model_organism = models.CharField(db_column='local name of the model organism', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    record_the_audio = models.CharField(db_column='record the audio', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    use_the_camera_to_record_a_video = models.CharField(db_column='use the camera to record a video', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field_id = models.CharField(db_column='_id', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    field_uuid = models.CharField(db_column='_uuid', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    field_submission_time = models.CharField(db_column='_submission_time', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    field_validation_status = models.CharField(db_column='_validation_status', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    field_notes = models.CharField(db_column='_notes', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    field_status = models.CharField(db_column='_status', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    field_submitted_by = models.CharField(db_column='_submitted_by', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    field_tags = models.CharField(db_column='_tags', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    field_index = models.CharField(db_column='_index', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'sampledata_23june22'

    def __str__(self):
        return self


class Test(models.Model):
    id = models.IntegerField(blank=True, null=False,primary_key =True)
    start = models.CharField(max_length=100, blank=True, null=True)
    end = models.CharField(max_length=100, blank=True, null=True)
    today = models.CharField(max_length=100, blank=True, null=True)
    logo = models.CharField(max_length=100, blank=True, null=True)
    name_reporter = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    field_location_altitude = models.CharField(db_column='_location_altitude', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    field_location_precision = models.CharField(db_column='_location_precision', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    time = models.CharField(max_length=100, blank=True, null=True)
    temperature_max_min_c_and_humidity_field = models.CharField(db_column='temperature (max-min °c) and humidity (%)', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    model_system = models.CharField(db_column='model system', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    species_of_mosquitoes = models.CharField(db_column='species of mosquitoes', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    total_number_of_mosquitoes = models.CharField(db_column='total number of mosquitoes', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    additional_description = models.CharField(db_column='additional description', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    record_the_audio_10_15_sec_field = models.CharField(db_column='record the audio (10-15 sec)', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    picture = models.CharField(max_length=100, blank=True, null=True)
    field_version_field = models.CharField(db_column='__version__', max_length=100, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    additional_picture = models.CharField(db_column='additional picture', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field_version_field_0 = models.CharField(db_column='_version_', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_version_001 = models.CharField(db_column='_version__001', max_length=100, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    additional_video = models.CharField(db_column='additional video', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    name_of_the_observer = models.CharField(db_column='name of the observer', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    where_have_you_observed_this_field = models.CharField(db_column='where have you observed this?', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    field_where_have_you_observed_this_latitude = models.CharField(db_column='_where have you observed this?_latitude', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_where_have_you_observed_this_longitude = models.CharField(db_column='_where have you observed this?_longitude', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_where_have_you_observed_this_altitude = models.CharField(db_column='_where have you observed this?_altitude', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_where_have_you_observed_this_precision = models.CharField(db_column='_where have you observed this?_precision', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    what_is_the_time_of_observing_the_phyllanthus_sleeping_field = models.CharField(db_column='what is the time of observing the phyllanthus sleeping?', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logo_001 = models.CharField(max_length=100, blank=True, null=True)
    details_of_the_tree_details_of_the_tree = models.CharField(db_column='details_of_the_tree/details of the tree', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    select_the_observation_type = models.CharField(db_column='select the observation type', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    mark_your_location_of_observation = models.CharField(db_column='mark your location of observation', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field_mark_your_location_of_observation_latitude = models.CharField(db_column='_mark your location of observation_latitude', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_mark_your_location_of_observation_longitude = models.CharField(db_column='_mark your location of observation_longitude', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_mark_your_location_of_observation_altitude = models.CharField(db_column='_mark your location of observation_altitude', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_mark_your_location_of_observation_precision = models.CharField(db_column='_mark your location of observation_precision', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    add_any_description_esp_if_the_observation_if_others_field = models.CharField(db_column='add any description (esp. if the observation if others)', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    details_of_the_tree_header = models.CharField(db_column='details of the tree/header', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    details_of_the_tree_leaves = models.CharField(db_column='details of the tree/leaves', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    details_of_the_tree_flowers = models.CharField(db_column='details of the tree/flowers', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    location_of_observation = models.CharField(max_length=100, blank=True, null=True)
    details_of_the_tree_fruits = models.CharField(db_column='details of the tree/fruits', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    local_name_of_the_model_organism = models.CharField(db_column='local name of the model organism', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    record_the_audio = models.CharField(db_column='record the audio', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    use_the_camera_to_record_a_video = models.CharField(db_column='use the camera to record a video', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field_id = models.CharField(db_column='_id', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    field_uuid = models.CharField(db_column='_uuid', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    field_submission_time = models.CharField(db_column='_submission_time', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    field_validation_status = models.CharField(db_column='_validation_status', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    field_notes = models.CharField(db_column='_notes', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    field_status = models.CharField(db_column='_status', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    field_submitted_by = models.CharField(db_column='_submitted_by', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    field_tags = models.CharField(db_column='_tags', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    field_index = models.CharField(db_column='_index', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'test'

class Test1(models.Model):
    id = models.IntegerField(blank=True, null=False,primary_key=True,)
    name_reporter = models.CharField(max_length=100, blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test1'