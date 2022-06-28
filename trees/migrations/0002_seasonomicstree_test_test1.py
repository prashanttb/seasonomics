# Generated by Django 4.0.5 on 2022-06-25 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeasonomicsTree',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('start', models.CharField(blank=True, max_length=100, null=True)),
                ('end', models.CharField(blank=True, max_length=100, null=True)),
                ('today', models.CharField(blank=True, max_length=100, null=True)),
                ('logo', models.CharField(blank=True, max_length=100, null=True)),
                ('name_reporter', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('lat', models.CharField(blank=True, max_length=100, null=True)),
                ('lng', models.CharField(blank=True, max_length=100, null=True)),
                ('model_system', models.CharField(blank=True, db_column='model system', max_length=100, null=True)),
                ('additional_description', models.CharField(blank=True, db_column='additional description', max_length=100, null=True)),
            ],
            options={
                'db_table': 'seasonomics_tree',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('start', models.CharField(blank=True, max_length=100, null=True)),
                ('end', models.CharField(blank=True, max_length=100, null=True)),
                ('today', models.CharField(blank=True, max_length=100, null=True)),
                ('logo', models.CharField(blank=True, max_length=100, null=True)),
                ('name_reporter', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('lat', models.CharField(blank=True, max_length=100, null=True)),
                ('lng', models.CharField(blank=True, max_length=100, null=True)),
                ('field_location_altitude', models.CharField(blank=True, db_column='_location_altitude', max_length=100, null=True)),
                ('field_location_precision', models.CharField(blank=True, db_column='_location_precision', max_length=100, null=True)),
                ('time', models.CharField(blank=True, max_length=100, null=True)),
                ('temperature_max_min_c_and_humidity_field', models.CharField(blank=True, db_column='temperature (max-min °c) and humidity (%)', max_length=100, null=True)),
                ('model_system', models.CharField(blank=True, db_column='model system', max_length=100, null=True)),
                ('species_of_mosquitoes', models.CharField(blank=True, db_column='species of mosquitoes', max_length=100, null=True)),
                ('total_number_of_mosquitoes', models.CharField(blank=True, db_column='total number of mosquitoes', max_length=100, null=True)),
                ('additional_description', models.CharField(blank=True, db_column='additional description', max_length=100, null=True)),
                ('record_the_audio_10_15_sec_field', models.CharField(blank=True, db_column='record the audio (10-15 sec)', max_length=100, null=True)),
                ('picture', models.CharField(blank=True, max_length=100, null=True)),
                ('field_version_field', models.CharField(blank=True, db_column='__version__', max_length=100, null=True)),
                ('additional_picture', models.CharField(blank=True, db_column='additional picture', max_length=100, null=True)),
                ('field_version_field_0', models.CharField(blank=True, db_column='_version_', max_length=100, null=True)),
                ('field_version_001', models.CharField(blank=True, db_column='_version__001', max_length=100, null=True)),
                ('additional_video', models.CharField(blank=True, db_column='additional video', max_length=100, null=True)),
                ('name_of_the_observer', models.CharField(blank=True, db_column='name of the observer', max_length=100, null=True)),
                ('where_have_you_observed_this_field', models.CharField(blank=True, db_column='where have you observed this?', max_length=100, null=True)),
                ('field_where_have_you_observed_this_latitude', models.CharField(blank=True, db_column='_where have you observed this?_latitude', max_length=100, null=True)),
                ('field_where_have_you_observed_this_longitude', models.CharField(blank=True, db_column='_where have you observed this?_longitude', max_length=100, null=True)),
                ('field_where_have_you_observed_this_altitude', models.CharField(blank=True, db_column='_where have you observed this?_altitude', max_length=100, null=True)),
                ('field_where_have_you_observed_this_precision', models.CharField(blank=True, db_column='_where have you observed this?_precision', max_length=100, null=True)),
                ('what_is_the_time_of_observing_the_phyllanthus_sleeping_field', models.CharField(blank=True, db_column='what is the time of observing the phyllanthus sleeping?', max_length=100, null=True)),
                ('logo_001', models.CharField(blank=True, max_length=100, null=True)),
                ('details_of_the_tree_details_of_the_tree', models.CharField(blank=True, db_column='details_of_the_tree/details of the tree', max_length=100, null=True)),
                ('select_the_observation_type', models.CharField(blank=True, db_column='select the observation type', max_length=100, null=True)),
                ('mark_your_location_of_observation', models.CharField(blank=True, db_column='mark your location of observation', max_length=100, null=True)),
                ('field_mark_your_location_of_observation_latitude', models.CharField(blank=True, db_column='_mark your location of observation_latitude', max_length=100, null=True)),
                ('field_mark_your_location_of_observation_longitude', models.CharField(blank=True, db_column='_mark your location of observation_longitude', max_length=100, null=True)),
                ('field_mark_your_location_of_observation_altitude', models.CharField(blank=True, db_column='_mark your location of observation_altitude', max_length=100, null=True)),
                ('field_mark_your_location_of_observation_precision', models.CharField(blank=True, db_column='_mark your location of observation_precision', max_length=100, null=True)),
                ('add_any_description_esp_if_the_observation_if_others_field', models.CharField(blank=True, db_column='add any description (esp. if the observation if others)', max_length=100, null=True)),
                ('details_of_the_tree_header', models.CharField(blank=True, db_column='details of the tree/header', max_length=100, null=True)),
                ('details_of_the_tree_leaves', models.CharField(blank=True, db_column='details of the tree/leaves', max_length=100, null=True)),
                ('details_of_the_tree_flowers', models.CharField(blank=True, db_column='details of the tree/flowers', max_length=100, null=True)),
                ('location_of_observation', models.CharField(blank=True, max_length=100, null=True)),
                ('details_of_the_tree_fruits', models.CharField(blank=True, db_column='details of the tree/fruits', max_length=100, null=True)),
                ('local_name_of_the_model_organism', models.CharField(blank=True, db_column='local name of the model organism', max_length=100, null=True)),
                ('record_the_audio', models.CharField(blank=True, db_column='record the audio', max_length=100, null=True)),
                ('use_the_camera_to_record_a_video', models.CharField(blank=True, db_column='use the camera to record a video', max_length=100, null=True)),
                ('field_id', models.CharField(blank=True, db_column='_id', max_length=100, null=True)),
                ('field_uuid', models.CharField(blank=True, db_column='_uuid', max_length=100, null=True)),
                ('field_submission_time', models.CharField(blank=True, db_column='_submission_time', max_length=100, null=True)),
                ('field_validation_status', models.CharField(blank=True, db_column='_validation_status', max_length=100, null=True)),
                ('field_notes', models.CharField(blank=True, db_column='_notes', max_length=100, null=True)),
                ('field_status', models.CharField(blank=True, db_column='_status', max_length=100, null=True)),
                ('field_submitted_by', models.CharField(blank=True, db_column='_submitted_by', max_length=100, null=True)),
                ('field_tags', models.CharField(blank=True, db_column='_tags', max_length=100, null=True)),
                ('field_index', models.CharField(blank=True, db_column='_index', max_length=100, null=True)),
            ],
            options={
                'db_table': 'test',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Test1',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('name_reporter', models.CharField(blank=True, max_length=100, null=True)),
                ('lat', models.CharField(blank=True, max_length=100, null=True)),
                ('lng', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'test1',
                'managed': False,
            },
        ),
    ]
