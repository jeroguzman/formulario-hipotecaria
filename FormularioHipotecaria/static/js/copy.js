function copyUrl(e) {
    /* Get the text field */
    // var copyText = document.getElementById('url-field');
    
    /* Select the text field */
    var url = e.getAttribute('data-url');
    
    navigator.clipboard.writeText(url);
    /* Copy the text inside the text field */
    document.execCommand('copy');
    
    /* Alert the copied text */
    // alert('Se ha copiado en el portapapeles: ' + url);
    $("#success-alert").fadeTo(2000, 500).slideUp(500, function(){
        $("#success-alert").slideUp(500);
    });
}
