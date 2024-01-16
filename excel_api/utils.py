from django.db import models, connection

def get_field_type():
    return models.CharField(max_length=255,null=True,blank=TR)

def create_dynamic_table(model_name, data):
    model_name = model_name.replace(" ", "_")
    app_label = 'excel_api'

    # Create dynamic model
    fields = {}
    for column_name in data.columns:
        field_name = column_name.replace(" ", "_")
        field_type = get_field_type()  # Use the get_field_type function without arguments
        fields[field_name] = field_type

    # Create Meta class for the dynamic model
    meta_class = type('Meta', (), {'app_label': app_label})

    # Create dynamic model class
    dynamic_model = type(model_name, (models.Model,), {'__module__': __name__, 'Meta': meta_class, **fields})

    # Create the table in the database
    with connection.schema_editor() as schema_editor:
        schema_editor.create_model(dynamic_model)
        
    for index, row in data.iterrows():
        instance = dynamic_model()
        for column_name in data.columns:
            field_name = column_name.replace(" ", "_")
            setattr(instance, field_name, row[column_name])
        instance.save()

    return dynamic_model

