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
});