from django.forms import ModelForm
from .models import Recipe



class RecipeForm(ModelForm):
	class Meta:
		model = Recipe
		fields = '__all__'



class DisabledFormMixin():
    def __init__(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True



class DeleteRecipeForm(RecipeForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)
