# from django.db import connections, models

# def create_dynamic_table(data):
#     # Create a dynamic model class
#     class DynamicModel(models.Model):
#         pass

#     # Add fields to the dynamic model with inferred types
#     for column_name, column_value in data.items():
#         field_type = infer_data_type(column_value)
#         setattr(DynamicModel, column_name.lower().replace(" ", "_"), field_type)

#     # Create the table in the database
#     table_name = 'dynamic_model_table'
#     connection = connections['default']
#     with connection.schema_editor() as schema_editor:
#         schema_editor.create_model(DynamicModel)

#     # Create instances and save data
#     for entry in data:
#         instance = DynamicModel(**entry)
#         instance.save()

#     return DynamicModel

# # Example data
# data = [
#     {"Broker Name": "LOCKTON SOUTHEAST", "Duplicate Count": 1},
#     # Add other data as needed
# ]

# # Create dynamic table and insert data
# DynamicModel = create_dynamic_table(data)
