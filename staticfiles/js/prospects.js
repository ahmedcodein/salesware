document.addEventListener('DOMContentLoaded', function() {

    const openProspectDetailModal = document.getElementById('open-prospect-detail-modal');
    const openCreateNewProspectModal = document.getElementById('open-create-new-prospect-modal');

    // Open the modal to display the prospect detail
    openProspectDetailModal.addEventListener('show.bs.modal', function(event) {

        const anchorOpenProspectDetailModal = event.relatedTarget;
        const urlAnchorOpenProspectDetailModal = anchorOpenProspectDetailModal.getAttribute('data-url');

        fetch(urlAnchorOpenProspectDetailModal)
        .then(response => response.text())
        .then(data => {
            document.getElementById('open-prospect-detail-modal-body').innerHTML = data;
        });
    });
    // Open the modal to display the new prospect form 
    openCreateNewProspectModal.addEventListener('show.bs.modal', function(event) {
        const NewProspectModalBtn = event.relatedTarget.getAttribute('action');
        fetch(NewProspectModalBtn)
        .then(response => response.text())
        .then(data => {
            document.getElementById('open-create-new-prospect-modal-body').innerHTML = data;
        });
    });

    // Submit the post request to the database to create new prospect
    document.getElementById('create-new-prospect-form').addEventListener('submit', function(event) {
        event.preventDefault();
        const createNewProspectBtn = document.getElementById('create-new-prospect-btn');
        const newProspectForm = event.target;
        const data = new FormData(newProspectForm);

        fetch(newProspectForm.action, {
            method: 'POST',
            body: data,
        })
        // Display the response message after Post request
        // and display it on the same modal window
        .then(response => response.json())
        .then(data => {
            const message = data.message;
            document.getElementById('open-create-new-prospect-modal-body').innerHTML = message;
            createNewProspectBtn.style.display = 'none';
            document.getElementById('create-new-prospect-cancel-btn').innerHTML = 'Close';
            // Reset the Modal and the form to their default state after the modal close
            const cancelCreateNewProspectModalBtn = document.getElementById('create-new-prospect-cancel-btn');
            const closeCreateNewProspectModalBtn = document.getElementById('create-new-prospect-close-btn');
            cancelCreateNewProspectModalBtn.addEventListener('click', function() {
                location.reload();
            });  
            closeCreateNewProspectModalBtn.addEventListener('click', function() {
                location.reload();
            });          
        });
    });

    // Submit the edit post request to the database to update prospect data
    document.getElementById('edit-prospect-btn').addEventListener('click', function(event) {
        event.preventDefault();
        const editProspectBtn = document.getElementById('edit-prospect-btn');
        const editedProspectForm = document.getElementById('edit-delete-prospect-form');
        const data = new FormData(editedProspectForm);

        fetch('/prospect_edit/', {
            method: 'POST',
            body: data,
        })
        // Display the response message after Post request
        // is sent for updating the prospect
        // and displays the response it on the same modal window
        .then(response => response.json())
        .then(data => {
            const message = data.message;
            const closeEditDeleteProspectBtn = document.getElementById('edit-delete-prospect-close-btn');
            const openProspectDetailModalCloseBtn = document.getElementById('open-prospect-detail-modal-close-btn')
            document.getElementById('open-prospect-detail-modal-body').innerHTML = message;
            editProspectBtn.style.display = 'none';
            document.getElementById('delete-prospect-btn').style.display = 'none';
            closeEditDeleteProspectBtn.addEventListener('click', function() {
                location.reload()
            })
            openProspectDetailModalCloseBtn.addEventListener('click', function() {
                location.reload()
            })        
        });
    });
    
    // Submit the delete post request to the database to update prospect data
    document.getElementById('prospect-delete-confirmed-btn').addEventListener('click', function(event) {
        event.preventDefault();
        const editedProspectForm = document.getElementById('edit-delete-prospect-form');
        const data = new FormData(editedProspectForm);

        const prospectDeleteConfirmedBtn = document.getElementById('prospect-delete-confirmed-btn')
        const prospectDeleteCloseConfirmModalXBtn = document.getElementById('prospect-delete-close-confirm-modal-x-btn')
        const prospectDeleteCloseConfirmModalBtn = document.getElementById('prospect-delete-close-confirm-modal-btn')

        fetch('/prospect_delete/', {
            method: 'POST',
            body: data,
        })
        // Display the response message after Post request
        // is sent for deleting the prospect
        // and displays the response on the same modal window
        .then(response => response.json())
        .then(data => {
            const message = data.message;
            prospectDeleteConfirmedBtn.style.display = 'none'
            document.getElementById('confirm-delete-prospect-modal-body').innerHTML = message;
            prospectDeleteCloseConfirmModalXBtn.addEventListener('click', function() {
                location.reload()
            })
            prospectDeleteCloseConfirmModalBtn.addEventListener('click', function() {
                location.reload()
            })      
        });
    });
});