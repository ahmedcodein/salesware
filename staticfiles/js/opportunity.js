$(document).ready(function () {
    const opportunityCreateProspect = document.getElementById('opportunity-create-prospect')
    const opportunityCreateProduct = document.getElementById('opportunity-create-product')
    const opportunityCreateProductPrice = document.getElementById('opportunity-create-product-price');
    const opportunityCreateStatus = document.getElementById('opportunity-create-status')
    const opportunityCreateSalesProcessStage = document.getElementById('opportunity-create-sales-process-stage')
    const opportunityCreateProgressBar = document.getElementById('opportunity-create-progress-bar')
    /* Select records with search functionality */
    $(opportunityCreateProspect).select2();
    $(opportunityCreateProduct).select2();
    /* Variable relevant to Prospect Selection */

    /* Change Product related inputs to new values once product
    is selected */
    $(opportunityCreateProduct).on('change', function(event) {
        changeProductBySelection(
            event,
            opportunityCreateProductPrice,
            opportunityCreateStatus,       
        )
    });

    /* Function that Changes Product related inputs to the new values once 
    product is selected */
    function changeProductBySelection(
        event,
        firstFieldInput,
        secondFieldInput,
    ) {

        const optionIndex = event.target.options.selectedIndex
        const optionSelected = opportunityCreateProduct.options[optionIndex]
        const productPrice = optionSelected.getAttribute('data-price')
        if (productPrice === null) {
            firstFieldInput.placeholder = ''
            secondFieldInput.selectedIndex = 0

        } else {
            firstFieldInput.placeholder = productPrice
            secondFieldInput.selectedIndex = 1
        }        
    }
    /* Change progress bar based on process stage */
    $(opportunityCreateSalesProcessStage).on('change', function() {
        progressBarControl(opportunityCreateSalesProcessStage)
    });
    /* This function handles changing the progress bar
    attribute values based on the process stage */
    function progressBarControl(progressBar){
        const stage = progressBar.value
        const stageInnerHtml = stage + ' ' + 'Stage'
        const barWidth = {
            Default: '0',
            Lead: '25%',
            Proposal: '50%',
            Negotiation: '75%',
        }
        const ariaValueNow = {
            Default: '0',
            Lead: '25',
            Proposal: '50',
            Negotiation: '75',
        }

        for (const [key, value] of Object.entries(barWidth)){
            if (stage === key){
                opportunityCreateProgressBar.style.width = value
                if (key === 'Default'){
                    opportunityCreateProgressBar.innerHTML = ''
                } else {
                    opportunityCreateProgressBar.innerHTML = stageInnerHtml
                }
            }
        }
        for (const [key, value] of Object.entries(ariaValueNow)){
            if (stage === key){
                opportunityCreateProgressBar.setAttribute('aria-valuenow', value)
            }
        }
    }
});