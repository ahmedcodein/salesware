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
        formData.append('service_id', 'service_cmj5z1c');
        formData.append('template_id', 'template_h8t73vr');
        formData.append('user_id', 'dxEqK4OEkA7Rdb0Tz');

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
                    location.reload();
                });
                $(contactFormSendModalCloseBtn).on('click', function () {
                    location.reload();
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
document.addEventListener('DOMContentLoaded', function () {

    // Open product Detail related variables
    const openProductDetailModal = document.getElementById('open-product-detail-modal');
    const openProductDetailModalBody = document.getElementById('open-product-detail-modal-body');
    // Open New product Form related variables
    const openCreateNewProductModal = document.getElementById('open-create-new-product-modal');
    const openCreateNewProductModalBody = document.getElementById('open-create-new-product-modal-body');
    // product create related variables
    const createNewProductBtn = document.getElementById('create-new-product-btn');
    const closeCreateNewProductModalBtn = document.getElementById('create-new-product-close-btn');
    const createNewProductCancelBtn = document.getElementById('create-new-product-cancel-btn');
    // product edit related variables
    const editProductBtn = document.getElementById('edit-product-btn');
    const editedProductForm = document.getElementById('edit-delete-product-form');
    const urlProductEdit = 'product_edit/';
    const deleteProductBtn = document.getElementById('delete-product-btn');
    const closeEditDeleteProductBtn = document.getElementById('edit-delete-product-close-btn');
    const openProductDetailModalCloseBtn = document.getElementById('open-product-detail-modal-close-btn');
    // product Delete related variables
    const productDeleteConfirmedBtn = document.getElementById('product-delete-confirmed-btn');
    const urlProductDelete = 'product_delete/';
    const confirmDeleteProductModalBody = document.getElementById('confirm-delete-product-modal-body');
    const productDeleteCloseConfirmModalXBtn = document.getElementById('product-delete-close-confirm-modal-x-btn');
    const productDeleteCloseConfirmModalBtn = document.getElementById('product-delete-close-confirm-modal-btn');

    /* Listen to the anchor element, and observe if the user clicks on any of the product's name
    to show the product detail*/
    openProductDetailModal.addEventListener('show.bs.modal', function (event) {
        const urlProductDetail = event.relatedTarget.getAttribute('data-url');
        openProductDetail(urlProductDetail, openProductDetailModalBody);
    });
    /* Listen to the create new product btn element, and observe if the user clicks to create
    new product if the user does click!*/
    // Open the modal to display the new product form 
    openCreateNewProductModal.addEventListener('show.bs.modal', function (event) {
        const urlNewProductForm = event.relatedTarget.getAttribute('data-url');
        openProductDetail(urlNewProductForm, openCreateNewProductModalBody);
    });
    // Submit the post request to the database to create new product
    document.getElementById('create-new-product-form').addEventListener('submit', function (event) {
        event.preventDefault();

        const url = event.target.action;
        const data = new FormData(event.target);

        createProductRecord(
            url,
            data,
            openCreateNewProductModalBody,
            createNewProductBtn,
            createNewProductCancelBtn,
            closeCreateNewProductModalBtn
        );
    });
    // Submit the product edit post request to the database to update product data
    editProductBtn.addEventListener('click', function (event) {
        event.preventDefault();
        const data = new FormData(editedProductForm);
        editProductRecord(
            urlProductEdit,
            data,
            openProductDetailModalBody,
            editProductBtn,
            deleteProductBtn,
            closeEditDeleteProductBtn,
            openProductDetailModalCloseBtn
        );
    });
    // Submit the delete post request to the database to delete product data
    document.getElementById('product-delete-confirmed-btn').addEventListener('click', function (event) {
        event.preventDefault();
        const data = new FormData(editedProductForm);

        deleteProductRecord(
            urlProductDelete,
            data,
            confirmDeleteProductModalBody,
            productDeleteConfirmedBtn,
            productDeleteCloseConfirmModalXBtn,
            productDeleteCloseConfirmModalBtn
        );
    });
    /* This function handles the user request to open product detail
    or the new product form */
    function openProductDetail(url, body) {
        fetch(url)
            .then(response => response.text())
            .then(data => {
                body.innerHTML = data;
            });
    }
    /* This function handles the user request to create new 
    and the subsequent response to the relevant modal */
    function createProductRecord(url, data, body, firstBtn, secondBtn, thirdBtn) {
        fetch(url, {
                method: 'POST',
                body: data,
            })
            .then(response => response.json())
            .then(data => {
                const message = data.message;
                body.innerHTML = message;
                firstBtn.style.display = 'none';
                secondBtn.innerHTML = 'Close';
                // Reset the Modal and the form to default state once closes
                secondBtn.addEventListener('click', function () {
                    location.reload();
                });
                thirdBtn.addEventListener('click', function () {
                    location.reload();
                });
            });
    }
    // This function handle the product edit request
    function editProductRecord(url, data, body, firstBtn, secondBtn, thirdBtn, fourthBtn) {
        fetch(url, {
                method: 'POST',
                body: data,
            })
            .then(response => response.json())
            .then(data => {
                const message = data.message;

                body.innerHTML = message;
                firstBtn.style.display = 'none';
                secondBtn.style.display = 'none';
                thirdBtn.addEventListener('click', function () {
                    location.reload();
                });
                fourthBtn.addEventListener('click', function () {
                    location.reload();
                });
            });
    }

    // This function handle the product edit request
    function deleteProductRecord(url, data, body, firstBtn, secondBtn, thirdBtn) {
        fetch(url, {
                method: 'POST',
                body: data,
            })
            .then(response => response.json())
            .then(data => {
                const message = data.message;
                body.innerHTML = message;
                firstBtn.style.display = 'none';
                secondBtn.addEventListener('click', function () {
                    location.reload();
                });
                thirdBtn.addEventListener('click', function () {
                    location.reload();
                });
            });
    }
});