$(document).ready(function () {
    $('#contact-form').on('submit', function (event) {
        event.preventDefault(); // prevent reload
        const contactFormSendModalBody = document.getElementById('contact-form-send-modal-body')
        const contactFormSendModalXCloseBtn = document.getElementById('contact-form-send-modal-x-close-btn')
        const contactFormSendModalCloseBtn = document.getElementById('contact-form-send-modal-close-btn')

        const formData = new FormData(this);
        formData.append('service_id', 'service_cmj5z1c');
        formData.append('template_id', 'template_h8t73vr');
        formData.append('user_id', 'dxEqK4OEkA7Rdb0Tz');

        $.ajax('https://api.emailjs.com/api/v1.0/email/send-form', {
            type: 'POST',
            data: formData,
            contentType: false, // auto-detection
            processData: false // no need to parse formData to string
        }).done(function () {
            contactFormSendModalBody.innerHTML = 'Your mail is sent!';
            $(contactFormSendModalXCloseBtn).on('click', function () {
                location.reload()
            })
            $(contactFormSendModalCloseBtn).on('click', function () {
                location.reload()
            })
        }).fail(function () {
            contactFormSendModalBody.innerHTML = 'Oops...Something went wrong';
        });
    });
});