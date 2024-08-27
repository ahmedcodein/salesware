document.addEventListener('DOMContentLoaded', function() {

    // Open prospect Detail related variables
    const openProspectDetailModal = document.getElementById('open-prospect-detail-modal');
    const openProspectDetailModalBody = document.getElementById('open-prospect-detail-modal-body');
    // Open New prospect Form related variables
    const openCreateNewProspectModal = document.getElementById('open-create-new-prospect-modal');
    const openCreateNewProspectModalBody = document.getElementById('open-create-new-prospect-modal-body');
    // Prospect create related variables
    const createNewProspectBtn = document.getElementById('create-new-prospect-btn');
    const closeCreateNewProspectModalBtn = document.getElementById('create-new-prospect-close-btn');
    const createNewProspectCancelBtn = document.getElementById('create-new-prospect-cancel-btn');
    // Prospect edit related variables
    const editProspectBtn = document.getElementById('edit-prospect-btn');
    const editedProspectForm = document.getElementById('edit-delete-prospect-form');
    const urlProspectEdit = 'prospect_edit/'
    const deleteProspectBtn = document.getElementById('delete-prospect-btn')
    const closeEditDeleteProspectBtn = document.getElementById('edit-delete-prospect-close-btn');
    const openProspectDetailModalCloseBtn = document.getElementById('open-prospect-detail-modal-close-btn')
    // Prospect Delete related variables
    const prospectDeleteConfirmedBtn = document.getElementById('prospect-delete-confirmed-btn');
    const urlProspectDelete = 'prospect_delete/';
    const confirmDeleteProspectModalBody = document.getElementById('confirm-delete-prospect-modal-body');    
    const prospectDeleteCloseConfirmModalXBtn = document.getElementById('prospect-delete-close-confirm-modal-x-btn');
    const prospectDeleteCloseConfirmModalBtn = document.getElementById('prospect-delete-close-confirm-modal-btn');

    /* Listen to the anchor element, and observe if the user clicks on any of the prospect's name
    to show the prospect detail*/
    openProspectDetailModal.addEventListener('show.bs.modal', function(event) {
        const urlProspectDetail = event.relatedTarget.getAttribute('data-url');
        openProspectDetail(urlProspectDetail, openProspectDetailModalBody)
    });
    /* Listen to the create new prospect btn element, and observe if the user clicks to create
    new prospect if the user does click!*/
    // Open the modal to display the new prospect form 
    openCreateNewProspectModal.addEventListener('show.bs.modal', function(event) {
        const urlNewProspectForm = event.relatedTarget.getAttribute('action');
        openProspectDetail(urlNewProspectForm, openCreateNewProspectModalBody)
    });
    // Submit the post request to the database to create new prospect
    document.getElementById('create-new-prospect-form').addEventListener('submit', function(event) {
        event.preventDefault();
        
        const url = event.target.action;
        const data = new FormData(event.target);

        createDeleteProspect(
            url,
            data,
            openCreateNewProspectModalBody,
            createNewProspectBtn,
            createNewProspectCancelBtn,
            closeCreateNewProspectModalBtn,
        );
    });
    // Submit the prospect edit post request to the database to update prospect data
    editProspectBtn.addEventListener('click', function(event) {
        event.preventDefault();
        const data = new FormData(editedProspectForm);
        editProspectRecord(
            urlProspectEdit,
            data,
            openProspectDetailModalBody,
            editProspectBtn,
            deleteProspectBtn,
            closeEditDeleteProspectBtn,
            openProspectDetailModalCloseBtn
        )
    });
    // Submit the delete post request to the database to delete prospect data
    document.getElementById('prospect-delete-confirmed-btn').addEventListener('click', function(event) {
        event.preventDefault();
        const data = new FormData(editedProspectForm);
        
        createDeleteProspect(
            urlProspectDelete,
            data,
            confirmDeleteProspectModalBody,
            prospectDeleteConfirmedBtn,
            prospectDeleteCloseConfirmModalXBtn,
            prospectDeleteCloseConfirmModalBtn,
        );
    });
    /* This function handles the user request to open prospect detail
    or the new prospect form */
    function openProspectDetail(url, body) {
        fetch(url)
        .then(response => response.text())
        .then(data => {
            body.innerHTML = data
        })
    }
    /* This function handles the user request to create new 
    or delete prospect and the subsequent response to the relevant modal */
    function createDeleteProspect(url, data, body, firstBtn, secondBtn, thirdBtn) {
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
    // This function handle the prospect edit request
    function editProspectRecord(url, data, body, firstBtn, secondBtn, thirdBtn, fourthBtn) {
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
            thirdBtn.addEventListener('click', function() {
                location.reload()
            })
            fourthBtn.addEventListener('click', function() {
                location.reload()
            })        
        });
    }
});