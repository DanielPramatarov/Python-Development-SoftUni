from django import forms
from recipe.models import Item
 
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {'user_name': forms.HiddenInput()}






class DisabledFormMixin():
    def __init__(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True



class DeleteRecipeForm(ItemForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)
