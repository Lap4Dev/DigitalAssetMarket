from django.contrib import admin


class AutoConfigAdmin(admin.ModelAdmin):
    """
    A custom Django admin.ModelAdmin class that simplifies the configuration
    of list display and search fields for the admin interface.

    This class automatically generates the 'list_display' and 'search_fields'
    attributes based on the fields defined in the model associated with the
    admin class. It helps reduce redundancy and code repetition when setting
    up the admin interface for models.

    Usage:
    To use this class, simply inherit from it when defining your admin class
    and specify the model you want to configure. The 'list_display' and
    'search_fields' attributes will be automatically populated based on the
    fields defined in the model.

    Example:
    ```python
    class MyModelAdmin(AutoConfigAdmin):
        model = MyModel
    ```

    This will generate the 'list_display' and 'search_fields' attributes for
    the MyModelAdmin class based on the fields defined in the MyModel model.

    Attributes:
        model (django.db.models.Model): The model class associated with the
            admin class. This is the model for which the admin interface
            configuration is being simplified.

    Methods:
        get_list_display(request): Generates the 'list_display' attribute for
            the admin class based on the fields defined in the associated model.

        get_search_fields(request): Generates the 'search_fields' attribute for
            the admin class based on the fields defined in the associated model.
    """
    def get_list_display(self, request):
        fields = self.model._meta.fields
        list_display = [field.name for field in fields]

        return list_display

    def get_search_fields(self, request):
        fields = self.model._meta.fields
        search_fields = [field.name for field in fields]

        return search_fields
