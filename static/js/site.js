// $.ajaxPrefilter( function(options, originalOptions, jqXHR)
// {
// 	options.url = 'http://localhost:8000' + options.url;
// });

var Texts = Backbone.Collection.extend({
	url: '/sisko/3/medium/'
});

var TextOutput = Backbone.View.extend({
	el:'#update-form',
	template: _.template($('#text-list-template').html()),
	render: function()
	{
		var that = this;
		var texts = new Texts();
		texts.fetch(
		{
			// success: function(texts)
			// {
			// }
		});
		
	},
	events:
	{
		'change .form-group select' : 'updateText',
		'change .form-group input' : 'updateText',
		'submit .form-horizontal' : 'updateText'
	},

	updateText : function(ev)
	{
		var that = this;
		var texts = new Texts();
		paragraphs = $('#id_paragraphs').val();
		length = $('input:radio[name=length]:checked').val();
		texts.url = '/sisko/' + paragraphs + "/" + length + "/";

		texts.fetch(
		{
			success: function(data)
			{
				$('.page').empty();
				data.each(function(d)
				{
					$('.page').append(that.template(d.toJSON()));
				});
			}
		});
		return false;
	}
});

var textOutput = new TextOutput();

Backbone.history.start();