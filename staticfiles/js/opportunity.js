/* jshint esnext: true */
$(document).ready(function () {
    const opportunityCreateProspect = document.getElementById('opportunity-create-prospect');
    const opportunityCreateProduct = document.getElementById('opportunity-create-product');
    // Variables needed to progressBarController function
    const createSalesProcessStage = document.getElementById('opportunity-create-sales-process-stage');
    const editDeleteProcessStage = document.getElementById('opportunity-edit-delete-sales-process-stage');
    // Variables related to create/edit/delete form
    const opportunityCreateForm = document.getElementById('opportunity-create-form');
    const opportunityEditDeleteForm = document.getElementById('opportunity-edit-delete-form');
    /* Select prospect/product records with search functionality */
    $(opportunityCreateProspect).select2();
    $(opportunityCreateProduct).select2();
    /* Display Product price based on product selected */
    $(opportunityCreateProduct).on('change', function (event) {
        const productPrice = document.getElementById('opportunity-create-product-price');
        const status = document.getElementById('opportunity-create-status');
        changeProductBySelection(
            event,
            productPrice,
            status
        );
    });
    /* Function that Changes Product related inputs to the new values once 
    product is selected */
    function changeProductBySelection(
        event,
        firstFieldInput,
        secondFieldInput
    ) {

        const optionIndex = event.target.options.selectedIndex;
        const optionSelected = opportunityCreateProduct.options[optionIndex];
        const productPrice = optionSelected.getAttribute('data-price');
        if (productPrice === null) {
            firstFieldInput.placeholder = '';
            secondFieldInput.selectedIndex = 0;

        } else {
            firstFieldInput.placeholder = productPrice;
            secondFieldInput.selectedIndex = 1;
        }
    }
    /* Change progress bar for create */
    $(createSalesProcessStage).on('change', function () {
        const createProgressBar = document.getElementById('opportunity-create-progress-bar');
        progressBarController(createSalesProcessStage, createProgressBar);
    });
    /* Change progress bar for edit/delete */
    if (editDeleteProcessStage === null) {
        // if statement prevents reading processStage as null when opportunity list page is open
    } else {
        // if processStage is not null, load the saved value
        const editDeleteProgressBar = document.getElementById('opportunity-edit-delete-progress-bar');
        progressBarController(editDeleteProcessStage, editDeleteProgressBar);
    }
    /* Dynamically change the progress bar value in response to sales process stage value */
    $(editDeleteProcessStage).on('click', function () {
        const editDeleteProgressBar = document.getElementById('opportunity-edit-delete-progress-bar');
        progressBarController(editDeleteProcessStage, editDeleteProgressBar);
    });
    /** This function controls the progress bar value display if opportunity create is active*/
    function progressBarController(processStage, progressBar) {
        const stage = processStage.value;
        const stageInnerHtml = stage + ' ' + 'Stage';
        const barWidth = {
            Default: '0%',
            Lead: '25%',
            Proposal: '50%',
            Negotiation: '75%',
            Close: '100%'
        };
        const ariaValueNow = {
            Default: '0',
            Lead: '25',
            Proposal: '50',
            Negotiation: '75',
            Close: '100'
        };
        for (const [key, value] of Object.entries(barWidth)) {
            if (stage === key) {
                progressBar.style.width = value;
                if (key === 'Default') {
                    progressBar.innerHTML = '';
                } else {
                    progressBar.innerHTML = stageInnerHtml;
                }
            }
        }
        for (const [key, value] of Object.entries(ariaValueNow)) {
            if (stage === key) {
                progressBar.setAttribute('aria-valuenow', value);
            }
        }
    }
    /* Delete opportunity record */
    const opportunityCreateSubmitBtn = document.getElementById('opportunity-create-submit-btn');
    $(opportunityCreateSubmitBtn).on('click', function () {
        let data = new FormData(opportunityCreateForm);
        const url = opportunityCreateForm.action;
        const body = document.getElementById('opportunity-create-submit-modal-body');
        const CloseBtn = document.getElementById('opportunity-create-modal-close');
        const xCloseBtn = document.getElementById('opportunity-create-modal-x-close');
        const create = true;
        const edit = false;
        actionHandler(url, data, body, CloseBtn, xCloseBtn, create, edit, create);
    });
    /* Edit opportunity record */
    const opportunityEditSubmitBtn = document.getElementById('opportunity-edit-submit-btn');
    $(opportunityEditSubmitBtn).on('click', function () {
        const data = new FormData(opportunityEditDeleteForm);
        const url = '/opportunity/opportunity_edit/';
        const body = document.getElementById('opportunity-edit-submit-modal-body');
        const CloseBtn = document.getElementById('opportunity-edit-modal-close');
        const xCloseBtn = document.getElementById('opportunity-edit-modal-x-close');
        const create = false;
        const edit = true;
        actionHandler(url, data, body, CloseBtn, xCloseBtn, edit, create);
    });
    /* Delete opportunity record */
    const opportunityDeleteConfirmModalBtn = document.getElementById('opportunity-delete-confirm-modal-btn');
    $(opportunityDeleteConfirmModalBtn).on('click', function () {
        const data = new FormData(opportunityEditDeleteForm);
        const url = '/opportunity/opportunity_delete/';
        const body = document.getElementById('opportunity-delete-message-modal-body');
        const firstBtn = null;
        const secondBtn = null;
        const create = false;
        const edit = false;
        actionHandler(url, data, body, firstBtn, secondBtn, edit, create);
    });
    /** This function handles user request to: create/read/update/delete opportunity record. */
    function actionHandler(url, data, body, firstBtn, secondBtn, edit, create) {
        fetch(url, {
                method: 'POST',
                body: data,
            })
            .then(response => response.json())
            .then(data => {
                body.innerHTML = data.message;
                if (edit || create) {
                    $(firstBtn).on('click', function () {
                        if (data.success) {
                            window.location.href = ('/opportunity/');
                        }
                    });
                    $(secondBtn).on('click', function () {
                        if (data.success) {
                            window.location.href = ('/opportunity/');
                        }
                    });
                }
            });
    }
    returnToOpportunityList();
    /** Loop over back class btn and get back to opportunity
     * list if use click on back class btn
     */
    function returnToOpportunityList() {
        const backToBtn = document.getElementsByClassName('back');
        for (let i = 0; i < backToBtn.length; i++) {
            $(backToBtn[i]).on('click', function () {
                window.location.href = ('/opportunity/');
            });
        }
    }
});