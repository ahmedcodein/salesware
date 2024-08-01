document.addEventListener('DOMContentLoaded', function() {
    const prospectModal = document.getElementById('staticBackdrop');
    console.log(prospectModal)

    prospectModal.addEventListener('show.bs.modal', function(event) {

        let anchor = event.relatedTarget;
        console.log('anchor attributes=', anchor)
        let url = anchor.getAttribute('data-url');

        fetch(url)
        .then(response => response.text())
        .then(data => {
            prospectModal.querySelector('.modal-body').innerHTML = data
        })
    });
});