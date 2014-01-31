from django.db import models
from django.utils.translation import ugettext as _
from django.contrib import admin

character = (
	('ben', "Ben"),
	('jake', 'Jake'),
)


# Create your models here.
class Quote(models.Model):
	text = models.TextField(_('Quote'))
	char_count = models.IntegerField(_('Character Count'), blank=True)
	character=models.CharField(_('Character'), default='ben', choices=character, blank=True, max_length=32)

	def save(self, *args, **kwargs):
		self.char_count = self.text.__len__()
		super(Quote, self).save(*args, **kwargs)

	def __unicode__(self):
		return (self.text[:75] + '...') if len(self.text) > 75 else self.text

admin.site.register(Quote)