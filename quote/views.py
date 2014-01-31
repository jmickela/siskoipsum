from django.shortcuts import render, HttpResponse
import json
from .models import Quote
from .quote_forms import SelectionForm

lengths = {
	'short':300,
	'medium':450,
	'long':600,
}

def get_text(paragraphs=3, length='medium'):
	paragraphs = int(paragraphs)
	if paragraphs > 15:
		paragraphs = 15

	try:
		char_length = lengths[length]
	except:
		char_length = lengths['medium']

	texts = []
	for i in range(0, paragraphs):
		chars_remaining = char_length
		temp = ""
		while chars_remaining > 10:
			try:
				quote = Quote.objects.filter(char_count__lte=chars_remaining).order_by("?")[0]
				temp += quote.text + " "
				chars_remaining -= quote.char_count
			except:
				chars_remaining = 0
		texts.append({'text': temp})
	return texts

def home(request):
	#assume three paragraphs of medium length
	form = SelectionForm(request.POST or None)
	if form.is_valid():
		paragraphs = int(form.cleaned_data['paragraphs'])
		length = form.cleaned_data['length']
	else:
		paragraphs = 3
		length = 'medium'

	texts = get_text(paragraphs, length)
	
	return render(request, "base.html", {'texts':texts, 'form':form})

def ajax_response(request, paragraphs=3, length='medium'):
	texts = get_text(paragraphs, length)
	return HttpResponse(json.dumps(texts), content_type='application/json')
	
