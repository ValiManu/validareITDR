$(document).ready(function() {
    setTimeout(function() {
        $('#inputStep1').change(function(){
            var input_value = document.getElementById('inputStep1').value;
	        $.ajax({
		    url: 'http://127.0.0.1:7000/transactions/ajax_response',
		    data: {
		    'ticket': input_value
	        },
	        dataType: 'json',
	        success: function(data) {
		        if (data.is_taken) {
			    $('.sw-btn-next').hide();
			    $('#inputStep1').after('<ul class="parsley-errors-list filled" id="errorMsg"><li class="parsley-type">Numarul de bon exista deja.</li></ul>');

		        } else {
			        console.log(input_value);
			        $('#errorMsg').remove();
			        $('.sw-btn-next').show();
		        }
	        }
	        });
        });
    }, 1000);
})