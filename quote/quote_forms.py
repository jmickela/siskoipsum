from django import forms
from django.utils.translation import ugettext as _

choices_p=(
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),
	(6, 6),
	(7, 7),
	(8, 8),
	(9, 9),
	(10, 10),
)

choices_l=(
	('short', 'Short'),
	('medium', 'Medium'),
	('long', 'Long'),
)

class SelectionForm(forms.Form):
	paragraphs = forms.ChoiceField(label=_('Paragraphs'), required=False, choices=choices_p, initial=3, widget=forms.Select(attrs={'class':'form-control'}))
	length = forms.ChoiceField(widget = forms.RadioSelect(), label=_('Length'), required=False, choices=choices_l, initial='medium')