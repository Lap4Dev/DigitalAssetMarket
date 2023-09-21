from django import forms


class ChoicesModelForm(forms.ModelForm):
    """
    A customized ModelForm class that automatically replaces the default
    widget of fields with choices with a Select widget, improving the
    user interface for selecting options.

    This form class is particularly useful when dealing with models that
    have fields using the 'choices' attribute, as it simplifies the user
    interaction by presenting the available choices in a drop-down select
    menu.

    Usage:
    To use this form class, simply inherit from it and provide your
    model as the 'model' attribute when defining your form class.

    Example:
    ```python
    class MyModelForm(ChoicesModelForm):
        class Meta:
            model = MyModel
    ```

    This will automatically replace the widgets of fields with 'choices'
    in the MyModel model with Select widgets.

    Note:
    Make sure that the fields in your model have the 'choices' attribute
    defined in the format expected by the Select widget, typically as a
    list of tuples.

    Example:
    ```python
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft',
    )
    ```

    Attributes:
        None
    """
    def __init__(self, *args, **kwargs):
        super(ChoicesModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if hasattr(field, 'choices'):
                field.widget = forms.Select(choices=field.choices)
