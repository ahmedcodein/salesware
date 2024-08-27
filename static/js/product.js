document.addEventListener('DOMContentLoaded', function() {

    // Open Product Detail related variables
    const openProductDetailModal = document.getElementById('open-product-detail-modal');
    const openProductDetailModalBody = document.getElementById('open-product-detail-modal-body')
    // Open New Product Form related variables
    const openCreateNewProductModal = document.getElementById('open-create-new-product-modal');
    const openCreateNewProductModalBody = document.getElementById('open-create-new-product-modal-body')

    /* Listen to the anchor element, and observe if the user clicks on any of the product's name
    and open the product detail of the user does the click!*/
    openProductDetailModal.addEventListener('show.bs.modal', function(event) {
        const urlProductDetail = event.relatedTarget.getAttribute('data-url');
        openProductDetail(urlProductDetail, openProductDetailModalBody)
    });
    // Open the modal to display the new product form 
    openCreateNewProductModal.addEventListener('show.bs.modal', function(event) {
        const urlNewProductForm = event.relatedTarget.getAttribute('action');
        openProductDetail(urlNewProductForm, openCreateNewProductModalBody)
    });
    /* This function handles the user request to open product detail
    or the new product form */
    function openProductDetail(url, body) {
        fetch(url)
        .then(response => response.text())
        .then(data => {
            body.innerHTML = data
        })
    }


    const createNewProductBtn = document.getElementById('create-new-product-btn');
    const closeCreateNewProductModalBtn = document.getElementById('create-new-product-close-btn');
    const createNewProductCancelBtn = document.getElementById('create-new-product-cancel-btn')
    // Submit the post request to the database to create new product
    document.getElementById('create-new-product-form').addEventListener('submit', function(event) {
        event.preventDefault();
        
        const url = event.target.action;
        const data = new FormData(event.target);

        createNewProduct(
            url,
            data,
            openCreateNewProductModalBody,
            createNewProductBtn,
            createNewProductCancelBtn,
            closeCreateNewProductModalBtn,
        );
    });
    
    /* This function handles the user request to create new product
    and the subsequent response to the relevant modal */
    function createNewProduct(url, data, body, firstBtn, secondBtn, thirdBtn) {
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
            secondBtn.addEventListener('click', function() {
                location.reload()
            })
            thirdBtn.addEventListener('click', function() {
                location.reload()
            });
        });
    }

    // Product edit
    const editProductBtn = document.getElementById('edit-product-btn');
    const editedProductForm = document.getElementById('edit-delete-product-form');
    const urlProductEdit = 'product_edit/'
    const deleteProductBtn = document.getElementById('delete-product-btn')
    const closeEditDeleteProductBtn = document.getElementById('edit-delete-product-close-btn');
    const openProductDetailModalCloseBtn = document.getElementById('open-product-detail-modal-close-btn')

    // Submit the edit post request to the database to update product data
    editProductBtn.addEventListener('click', function(event) {
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
        )
    });

    function editProductRecord(url, data, body, firstBtn, secondBtn, thirdBtn, fourthBtn) {
        fetch(url, {
            method: 'POST',
            body: data,
        })
        // Display the response message after Post request
        // is sent for updating the product
        // and displays the response it on the same modal window
        .then(response => response.json())
        .then(data => {
            const message = data.message;
            
            body.innerHTML = message;
            firstBtn.style.display = 'none';
            secondBtn.style.display = 'none';
            thirdBtn.addEventListener('click', function() {
                location.reload()
            })
            fourthBtn.addEventListener('click', function() {
                location.reload()
            })        
        });

    }
    // Product Delete
    const productDeleteConfirmedBtn = document.getElementById('product-delete-confirmed-btn');
    const urlProductDelete = 'product_delete/';
    const confirmDeleteProductModalBody = document.getElementById('confirm-delete-product-modal-body');    
    const productDeleteCloseConfirmModalXBtn = document.getElementById('product-delete-close-confirm-modal-x-btn');
    const productDeleteCloseConfirmModalBtn = document.getElementById('product-delete-close-confirm-modal-btn');

    // Submit the delete post request to the database to update product data
    document.getElementById('product-delete-confirmed-btn').addEventListener('click', function(event) {
        event.preventDefault();
        const data = new FormData(editedProductForm);
        
        deleteProductRecord(
            urlProductDelete,
            data,
            confirmDeleteProductModalBody,
            productDeleteConfirmedBtn,
            productDeleteCloseConfirmModalXBtn,
            productDeleteCloseConfirmModalBtn,
        );
    });

    function deleteProductRecord(url, data, body, firstBtn, secondBtn, thirdBtn) {
        fetch(url, {
            method: 'POST',
            body: data,
        })
        // Display the response message after Post request
        // is sent for deleting the product
        // and displays the response on the same modal window
        .then(response => response.json())
        .then(data => {
            const message = data.message;
            body.innerHTML = message;
            firstBtn.style.display = 'none'
            secondBtn.addEventListener('click', function() {
                location.reload()
            })
            thirdBtn.addEventListener('click', function() {
                location.reload()
            })      
        });
    }
});