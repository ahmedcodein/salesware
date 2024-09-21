document.addEventListener('DOMContentLoaded', function () {
    // Open product detail modal
    document.getElementById('open-product-detail-modal').addEventListener('show.bs.modal', function (event) {
        const url = event.relatedTarget.getAttribute('data-url');
        const data = null;
        const openProductDetailModalBody = document.getElementById('open-product-detail-modal-body');
        const edit = false;
        const del = false;
        actionHandler(
            url,
            data,
            openProductDetailModalBody,
            edit,
            del
        );
    });
    // Open create new product modal
    document.getElementById('open-create-new-product-modal').addEventListener('show.bs.modal', function (event) {
        const url = event.relatedTarget.getAttribute('data-url');
        const data = null;
        const openCreateNewProductModalBody = document.getElementById('open-create-new-product-modal-body');
        const edit = false;
        const del = false;
        actionHandler(
            url,
            data,
            openCreateNewProductModalBody,
            edit,
            del
        );
    });
    // Create product record request
    document.getElementById('create-new-product-form').addEventListener('submit', function (event) {
        event.preventDefault();
        const url = event.target.action;
        const data = new FormData(event.target);
        const openCreateNewProductModalBody = document.getElementById('open-create-new-product-modal-body');
        const createNewProductBtn = document.getElementById('create-new-product-btn');
        const createNewProductCancelBtn = document.getElementById('create-new-product-cancel-btn');
        const closeCreateNewProductModalBtn = document.getElementById('create-new-product-close-btn');
        const fourthBtn = null;
        const edit = false;
        const del = false;

        actionHandler(
            url,
            data,
            openCreateNewProductModalBody,
            createNewProductBtn,
            createNewProductCancelBtn,
            closeCreateNewProductModalBtn,
            fourthBtn,
            edit,
            del
        );
    });
    // Update product record request
    document.getElementById('edit-product-btn').addEventListener('click', function (event) {
        event.preventDefault();
        const url = 'product_edit/';
        const editedProductForm = document.getElementById('edit-delete-product-form');
        const data = new FormData(editedProductForm);
        const openProductDetailModalBody = document.getElementById('open-product-detail-modal-body');
        const editProductBtn = document.getElementById('edit-product-btn');
        const deleteProductBtn = document.getElementById('delete-product-btn');
        const closeEditDeleteProductBtn = document.getElementById('edit-delete-product-close-btn');
        const openProductDetailModalCloseBtn = document.getElementById('open-product-detail-modal-close-btn');
        const edit = true;
        const del = false;
        actionHandler(
            url,
            data,
            openProductDetailModalBody,
            editProductBtn,
            deleteProductBtn,
            closeEditDeleteProductBtn,
            openProductDetailModalCloseBtn,
            edit,
            del
        );
    });
    // Delete product record request
    document.getElementById('product-delete-confirmed-btn').addEventListener('click', function (event) {
        event.preventDefault();
        const editedProductForm = document.getElementById('edit-delete-product-form');
        const data = new FormData(editedProductForm);
        const url = 'product_delete/';
        const confirmDeleteProductModalBody = document.getElementById('confirm-delete-product-modal-body');
        const productDeleteConfirmedBtn = document.getElementById('product-delete-confirmed-btn');
        const productDeleteCloseConfirmModalXBtn = document.getElementById('product-delete-close-confirm-modal-x-btn');
        const productDeleteCloseConfirmModalBtn = document.getElementById('product-delete-close-confirm-modal-btn');
        const fourthBtn = null;
        const edit = false;
        const del = true;

        actionHandler(
            url,
            data,
            confirmDeleteProductModalBody,
            productDeleteConfirmedBtn,
            productDeleteCloseConfirmModalXBtn,
            productDeleteCloseConfirmModalBtn,
            fourthBtn,
            edit,
            del
        );
    });
    /** This function handles user request to: create/read/update/delete product record. */
    function actionHandler(url, data, body, firstBtn, secondBtn, thirdBtn, fourthBtn, edit, del) {
        if (data === null) {
            fetch(url)
                .then(response => response.text())
                .then(data => {
                    body.innerHTML = data;
                });
        } else {
            fetch(url, {
                    method: 'POST',
                    body: data,
                })
                .then(response => response.json())
                .then(data => {
                    const message = data.message;
                    body.innerHTML = message;
                    firstBtn.style.display = 'none';
                    if (!edit) {
                        if (!del) {
                            secondBtn.innerHTML = 'Close';
                        }
                        // Reset the Modal and the form to default state once closes
                        secondBtn.addEventListener('click', function () {
                            location.reload();
                        });
                        thirdBtn.addEventListener('click', function () {
                            location.reload();
                        });
                    } else {
                        secondBtn.style.display = 'none';
                        // Reset the Modal and the form to default state once closes
                        thirdBtn.addEventListener('click', function () {
                            location.reload();
                        });
                        fourthBtn.addEventListener('click', function () {
                            location.reload();
                        });
                    }
                });
        }
    }
});