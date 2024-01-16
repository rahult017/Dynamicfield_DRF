from django.db import models, connections

connection = connections["default"]

def get_field_type(column_value):
    if isinstance(column_value, int):
        return models.IntegerField()
    elif isinstance(column_value, float):
        return models.FloatField()
    elif isinstance(column_value, bool):
        return models.BooleanField()
    elif isinstance(column_value, str):
        return models.CharField(max_length=255)  # Specify max_length for CharField
    else:
        return models.CharField(max_length=255)  # Specify max_length for CharField

def create_dynamic_table(model_name, data):

    class BaseModel(models.Model):
        pass

    for column_name in data.columns:
        field_name = column_name.replace(" ", "_")
        field_type = get_field_type(data[column_name].iloc[0])  # Use the first row to determine the field type
        setattr(BaseModel, field_name, field_type)

    model_name = model_name.replace(" ", "_")
    dynamic_model = type(model_name, (BaseModel,), {"__module__": __name__})
    dynamic_model._meta.app_label = 'excel_api'
    dynamic_model._meta.db_table = f'dynamic_table_{model_name}'
    dynamic_model._meta.managed = False
    dynamic_model.save()

    for _, row in data.iterrows():
        instance = dynamic_model()
        for column_name in data.columns:
            field_name = column_name.replace(" ", "_")
            setattr(instance, field_name, row[column_name])
        instance.save()
