document.addEventListener('DOMContentLoaded', function() {
    const openProspectDetailModal = document.getElementById('open-prospect-detail-modal');
    console.log(openProspectDetailModal)

    openProspectDetailModal.addEventListener('show.bs.modal', function(event) {

        let anchor = event.relatedTarget;
        console.log('anchor attributes=', anchor)
        let url = anchor.getAttribute('data-url');

        fetch(url)
        .then(response => response.text())
        .then(data => {
            openProspectDetailModal.querySelector('.modal-body').innerHTML = data
        })
    });
});