$(function() {
    $('#submit_button').click(function() {

	$.ajax({
	    url: '/create_entry',
	    data: $('form').serialize(),
	    type: 'POST',
	    success: function(response) {
            console.log(response);
		  $.ajax({
              type:"POST",
              url: '/redirect',
              success: function(response) {
                  console.log(response); #not sure if I have to do something with response; compare to tutorial, they just wanted to print a debug msg @ beginning..
              } //END success_ajax2
          });
	    },
	    error: function(error) {
		console.log(error);
	    }
	});
    });
});
