/* jshint esnext: true */
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