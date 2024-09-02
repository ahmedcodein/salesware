$(document).ready(function () {
    /* Select records with search functionality */
    $('#opportunity-create-prospect').select2();
    $('#opportunity-create-product').select2();
    /* Variable relevant to Prospect Selection */
    const opportunityCreateProduct = document.getElementById('opportunity-create-product')
    const opportunityCreateProductPrice = document.getElementById('opportunity-create-product-price');
    const opportunityCreateWinningProbability = document.getElementById('opportunity-create-winning-probability')

    /* Variable relevant to Product Selection */
    const opportunityCreateProspect = document.getElementById('opportunity-create-prospect')
    const opportunityCreateStatus = document.getElementById('opportunity-create-status')
    const opportunityCreateProcessStage = document.getElementById('opportunity-create-process-stage')
    const opportunityCreateProgressBar = document.getElementById('opportunity-create-progress-bar')
  
    /* Change Product related inputs to new values once prospect
    /* is selected */

    $(opportunityCreateProspect).on('change', function(event) {
        changeProspectBySelection(
            event,
            opportunityCreateStatus,
            opportunityCreateProcessStage,
            opportunityCreateProgressBar,            
        )
    });

    /* Change Product related inputs to new values once product
    is selected */
    $(opportunityCreateProduct).on('change', function(event) {
        changeProductBySelection(
            event,
            opportunityCreateProductPrice,
            opportunityCreateWinningProbability,          
        )
    });

    /* Function that Changes Prospect related inputs to the new values once 
    product is selected */
    function changeProspectBySelection(
        event,
        firstFieldInput,
        secondFieldInput,
        thirdFieldInput

    ){
        const optionIndex = event.target.options.selectedIndex
        const optionSelected = opportunityCreateProduct.options[optionIndex]
        const productPrice = optionSelected.getAttribute('data-price')
        if (productPrice === null) {
            firstFieldInput.placeholder = ''
            secondFieldInput.placeholder = ''
            thirdFieldInput.setAttribute('aria-valuenow', '0')
            thirdFieldInput.style.width = '0%'

        } else {
            firstFieldInput.placeholder = 'Open'
            secondFieldInput.placeholder = 'Lead'
            thirdFieldInput.setAttribute('aria-valuenow', '25')
            thirdFieldInput.style.width = '25%'
        }
    };

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
            secondFieldInput.placeholder = ''

        } else {
            firstFieldInput.placeholder = productPrice
            secondFieldInput.placeholder = '25%'
        }        
    }
})