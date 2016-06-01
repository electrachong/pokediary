$(function() {
    $('#submit_button').click(function() {

	$.ajax({
	    url: '/create_entry',
	    data: $('form').serialize(),
	    type: 'POST',
	    success: function(response) {
		console.log(response);
	    },
	    error: function(error) {
		console.log(error);
	    }
	});
    });
});
