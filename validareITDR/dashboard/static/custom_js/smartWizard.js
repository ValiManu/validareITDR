
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
    $('#save_tranzaction').css('display', 'block');
}
var thirdStepOff = function () {
    $('#li_step-3').removeClass('active');
    $('#step-3').css('display', 'none')
    $('#step3').css('display', 'none');
}

firstStep();