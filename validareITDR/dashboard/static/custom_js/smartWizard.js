
$('#wizard').addClass('sw-main sw-theme-default');
$('ul').addClass('nav nav-tabs step-anchor');
$('li').addClass('nav-item');

var firstStep = function () {
    secondStepOff();
    thirdStepOff();
    $('#step1').css('display', '');
    $('#li_step-1').addClass('active');
    $('#step-1').css('display', 'block')
    $('.sw-container').css('min-height', '94px');
    $('#li_step-2').removeClass('done');
};
var firstStepOff = function () {
    $('#step3').css('display', 'none');
    $('.step-1').removeClass('active');
    $('#step-1').css('display', 'none');
    $('#li_step-1').addClass('done');
    $('#li_step-1').removeClass('active');
}
var secondStep = function () {
    firstStepOff();
    thirdStepOff();
    $('#li_step-2').addClass('active');
    $('#step-2').css('display', 'block')
    $('#step1').css('display', 'none');
    $('#step2').css('display', '');
};
var secondStepOff = function () {
    $('#step2').css('display', 'none');
    $('#step3').css('display', 'none');
    $('#li_step-2').removeClass('active');
    $('#step-2').css('display', 'none')
    $('.alert').css('display', 'none')
}
var thirdStep = function () {
    secondStepOff();
    $('#li_step-3').addClass('active');
    $('#step-3').css('display', 'block')
    $('#step3').css('display', '');
    $('#li_step-2').addClass('done');
}
var thirdStepOff = function () {
    $('#li_step-3').removeClass('active');
    $('#step-3').css('display', 'none')
    $('#step3').css('display', 'none');
}
var ticketValidation = function () {
    var input_value = document.getElementById('ticketValue').value;
    $.ajax({
        url: 'http://127.0.0.1:7000/transactions/ticket-validation',
        data: {
            'ticket': input_value
        },
        success: function (data) {
            if ($('#errorMsg').length > 0) {
                $('#errorMsg').remove();
            }
            if (data.is_taken == 1) {
                $('#ticketValue').after('<ul class="parsley-errors-list filled" id="errorMsg"><li class="parsley-type">Numarul de bon nu este valid.</li></ul>');
            } else if (data.is_taken == 2) {
                $('#ticketValue').after('<ul class="parsley-errors-list filled" id="errorMsg"><li class="parsley-type">Numarul de bon exista deja.</li></ul>');
            } else {
                secondStep();
            }
        }
    });
};

var productValidation = function () {
    var products = [];
    for (var i = 0; i < $('.prodValue').length; i++) {
        if ($('.prodValue')[i].value == '') {
            $('.prodValue')[i].value = 0;
        }
        products.push($('.prodValue')[i].value);
    };

    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:7000/transactions/product-validation',
        data: {
            'products': products
        },
        success: function (response) {
            if (response.response) {
                thirdStep();
                document.getElementById('img_prize').src = response.url_img;
                $('#name_prize').html(response.name);
                document.getElementById('id_prize').value = response.id;
            }
            else {
                console.log('Nu a fost selectat nicun produs');
                $('.alert').css('display', 'block')
            }
        },
        error: function (response) {
            console.log(response);
        }
    });
};

var saveData = function () {
    var ticketNo = document.getElementById('ticketValue').value;
    var productsSell = [];
    for (var i = 0; i < $('.prodValue').length; i++) {
        if ($('.prodValue')[i].value != '' && $('.prodValue')[i].value != '0') {
            productsSell.push({
                id: $('.prodValue')[i].id,
                value: $('.prodValue')[i].value
            });
        }
    };
    console.log(productsSell);
    var idPrize = document.getElementById('id_prize').value;

    var data = {
        'ticketNo': ticketNo,
        'productsSell': JSON.stringify(productsSell),
        'idPrize': idPrize
    }
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:7000/transactions/save-data',
        data: data,
        success: function (response) {
            if (response.response) {
                console.log('Datele au fost salvate');
                window.location.reload()
            }
            else {
                console.log('Nu a fost selectat nicun produs');
                $('.alert').css('display', 'block')
            }
        },
        error: function (response) {
            console.log(response);
        }
    });
};


    //Start
firstStep();

$(function () {
    $("#popupContainer").dxPopup({
        title: "Popup Title"
    });

    $("#buttonContainer").dxButton({
        text: "Show the Popup",
        onClick: function () {
            $("#popupContainer").dxPopup("show");
        }
    });
});