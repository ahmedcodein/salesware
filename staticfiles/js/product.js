document.addEventListener('DOMContentLoaded', function() {

    // Open Product Detail related variables
    const openProductDetailModal = document.getElementById('open-product-detail-modal');
    const openProductDetailModalBody = document.getElementById('open-product-detail-modal-body')

    /* Listen to the anchor element, and observe if the user clicks on any of the product's name
    and open the product detail of the user does the click!*/
    openProductDetailModal.addEventListener('show.bs.modal', function(event) {
        const urlProductDetail = event.relatedTarget.getAttribute('data-url');
        openProductDetail(urlProductDetail, openProductDetailModalBody)
    });
    // This function handles the user request to open product detail
    function openProductDetail(url, body) {
        fetch(url)
        .then(response => response.text())
        .then(data => {
            body.innerHTML = data
        })

    }
});