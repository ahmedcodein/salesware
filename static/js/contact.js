/* jshint esnext: true */
$(document).ready(function () {
    /* Create form variable */
    const contactForm = document.getElementById('contact-form');
    /* Create Modal Variables */
    const contactFormSendModal = new bootstrap.Modal(document.getElementById('contact-form-send-modal'));
    const contactFormSendModalBody = document.getElementById('contact-form-send-modal-body');
    const contactFormSendModalXCloseBtn = document.getElementById('contact-form-send-modal-x-close-btn');
    const contactFormSendModalCloseBtn = document.getElementById('contact-form-send-modal-close-btn');


    $(contactForm).on('submit', function (event) {
        event.preventDefault(); // prevent reload

        const formData = new FormData(contactForm);
        formData.append('service_id', 'service_bba1681');
        formData.append('template_id', 'template_efxib52');
        formData.append('user_id', 'zYSPWHBW8IEnrjQYz');
        formData.append('recipient', 'SalesWare Support');

        /* The validation step is added to prevent user from entering
        inputs with only spaces as apposed to valid characters */
        const formDataValues = formDataExtractor(formData);
        const validDataForm = formDataValidator(formDataValues);

        if (validDataForm) {
            $.ajax('https://api.emailjs.com/api/v1.0/email/send-form', {
                type: 'POST',
                data: formData,
                contentType: false, // auto-detection
                processData: false // no need to parse formData to string
            }).done(function () {
                contactFormSendModal.show(); /* Only show the modal when the form is valid */
                contactFormSendModalBody.innerHTML = 'We received your email! We sent you a confirmation email.';
                /* The next two function are introduced to reset the form
                after successful form submission */
                $(contactFormSendModalXCloseBtn).on('click', function () {
                    window.location.href = ('/');
                });
                $(contactFormSendModalCloseBtn).on('click', function () {
                    window.location.href = ('/');
                });
            }).fail(function () {
                contactFormSendModal.show(); /* Only show the modal when the form is valid */
                contactFormSendModalBody.innerHTML = 'Oops...Something went wrong';
            });
        } else {
            contactFormSendModal.show(); /* Only show the modal when the form is valid */
            contactFormSendModalBody.innerHTML = 'One or more inputs are missing. Submission failed!';
        }
    });

    /** formDataExtractor extracts every value in the formData Object
     * and return an array carries those values
     */
    function formDataExtractor(formData) {
        const formDataValues = [];
        formData.forEach((value) => {
            formDataValues.push(value);
        });
        return formDataValues;
    }
    /** formDataValidator takes in the formDataValues array and filters
     * empty inputs if available and return false if there is/are empty
     * inputs else it returns true
     * false = formData are not valid
     * true = formData are valid
     */
    function formDataValidator(formDataValues) {
        let emptyValesStorage = [];
        let emptyValesStorageLength = 0;
        emptyValesStorage = formDataValues.filter(input => input.trim().length === 0);
        emptyValesStorageLength = emptyValesStorage.length;
        if (emptyValesStorageLength === 0) {
            return true;
        } else {
            return false;
        }
    }
});