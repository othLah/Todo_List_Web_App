from django import forms
from . import models

class Todo_Form_Model(forms.ModelForm):
	class Meta:
		model = models.Todo_Plan
		fields = ["plan"]
		widgets = {
			'plan': forms.TextInput(
					attrs={
						"type": "text", 
						"size": "40", 
						"maxlength": "40", 
						"placeholder": "Write one plan per time...",
						"required": "True",
						"autofocus": "True"
					}
				)
		}

'''
class Todo_Form(forms.Form):
	plan = forms.CharField(max_length=40,
			widget=forms.TextInput(
					attrs={
						"type": "text", "size": "40", "maxlength": "40", "placeholder": "Write one plan per time..."
					}
				),
			required=True
		)
'''