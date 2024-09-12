$('#contact-form').on('submit', function(event) {
    event.preventDefault(); // prevent reload
    console.log(this)
    
    const formData = new FormData(this);
    formData.append('service_id', 'service_cmj5z1c');
    formData.append('template_id', 'template_h8t73vr');
    formData.append('user_id', 'dxEqK4OEkA7Rdb0Tz');
 
    $.ajax('https://api.emailjs.com/api/v1.0/email/send-form', {
        type: 'POST',
        data: formData,
        contentType: false, // auto-detection
        processData: false // no need to parse formData to string
    }).done(function() {
        alert('Your mail is sent!');
    }).fail(function(error) {
        alert('Oops... ' + JSON.stringify(error));
    });
});