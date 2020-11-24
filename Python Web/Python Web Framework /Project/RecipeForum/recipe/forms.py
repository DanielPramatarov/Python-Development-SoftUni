from django import forms
from recipe.models import Item
 
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {'user_name': forms.HiddenInput(),
                   'item_name' : forms.TextInput(attrs = {'placeholder': 'Recipe Name'}),
                   'item_desc' : forms.Textarea (attrs = {'placeholder': 'Enter Recipe Description'}),
                   'item_time_to_cook' : forms.NumberInput(attrs = {'placeholder': 'Time to be cooked'}),
                   'item_image' : forms.TextInput (attrs = {'placeholder': 'Link to image'}),
                  
                  }






class DisabledFormMixin():
    def __init__(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True



class DeleteRecipeForm(ItemForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)
