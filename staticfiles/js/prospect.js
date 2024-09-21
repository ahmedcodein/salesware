document.addEventListener('DOMContentLoaded', function () {
    // Open prospect detail modal
    document.getElementById('open-prospect-detail-modal').addEventListener('show.bs.modal', function (event) {
        const url = event.relatedTarget.getAttribute('data-url');
        const data = null;
        const openProspectDetailModalBody = document.getElementById('open-prospect-detail-modal-body');
        const edit = false;
        const del = false;
        actionHandler(
            url,
            data,
            openProspectDetailModalBody,
            edit,
            del
        );
    });
    // Open create new prospect modal
    document.getElementById('open-create-new-prospect-modal').addEventListener('show.bs.modal', function (event) {
        const url = event.relatedTarget.getAttribute('data-url');
        const data = null;
        const openCreateNewProspectModalBody = document.getElementById('open-create-new-prospect-modal-body');
        const edit = false;
        const del = false;
        actionHandler(
            url,
            data,
            openCreateNewProspectModalBody,
            edit,
            del
        );
    });
    // Create prospect record request
    document.getElementById('create-new-prospect-form').addEventListener('submit', function (event) {
        event.preventDefault();
        const url = event.target.action;
        const data = new FormData(event.target);
        const openCreateNewProspectModalBody = document.getElementById('open-create-new-prospect-modal-body');
        const createNewProspectBtn = document.getElementById('create-new-prospect-btn');
        const createNewProspectCancelBtn = document.getElementById('create-new-prospect-cancel-btn');
        const closeCreateNewProspectModalBtn = document.getElementById('create-new-prospect-close-btn');
        const fourthBtn = null;
        const edit = false;
        const del = false;

        actionHandler(
            url,
            data,
            openCreateNewProspectModalBody,
            createNewProspectBtn,
            createNewProspectCancelBtn,
            closeCreateNewProspectModalBtn,
            fourthBtn,
            edit,
            del
        );
    });
    // Update prospect record request
    document.getElementById('edit-prospect-btn').addEventListener('click', function (event) {
        event.preventDefault();
        const url = 'prospect_edit/';
        const editedProspectForm = document.getElementById('edit-delete-prospect-form');
        const data = new FormData(editedProspectForm);
        const openProspectDetailModalBody = document.getElementById('open-prospect-detail-modal-body');
        const editProspectBtn = document.getElementById('edit-prospect-btn');
        const deleteProspectBtn = document.getElementById('delete-prospect-btn');
        const closeEditDeleteProspectBtn = document.getElementById('edit-delete-prospect-close-btn');
        const openProspectDetailModalCloseBtn = document.getElementById('open-prospect-detail-modal-close-btn');
        const edit = true;
        const del = false;
        actionHandler(
            url,
            data,
            openProspectDetailModalBody,
            editProspectBtn,
            deleteProspectBtn,
            closeEditDeleteProspectBtn,
            openProspectDetailModalCloseBtn,
            edit,
            del
        );
    });
    // Delete prospect record request
    document.getElementById('prospect-delete-confirmed-btn').addEventListener('click', function (event) {
        event.preventDefault();
        const editedProspectForm = document.getElementById('edit-delete-prospect-form');
        const data = new FormData(editedProspectForm);
        const url = 'prospect_delete/';
        const confirmDeleteProspectModalBody = document.getElementById('confirm-delete-prospect-modal-body');
        const prospectDeleteConfirmedBtn = document.getElementById('prospect-delete-confirmed-btn');
        const prospectDeleteCloseConfirmModalXBtn = document.getElementById('prospect-delete-close-confirm-modal-x-btn');
        const prospectDeleteCloseConfirmModalBtn = document.getElementById('prospect-delete-close-confirm-modal-btn');
        const fourthBtn = null;
        const edit = false;
        const del = true;

        actionHandler(
            url,
            data,
            confirmDeleteProspectModalBody,
            prospectDeleteConfirmedBtn,
            prospectDeleteCloseConfirmModalXBtn,
            prospectDeleteCloseConfirmModalBtn,
            fourthBtn,
            edit,
            del
        );
    });
    /** This function handles user request to: create/read/update/delete prospect record. */
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