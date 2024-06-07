document.addEventListener("DOMContentLoaded", function() {
    setTimeout( function() {
        var messages = document.querySelectorAll('.messages .alert')
        messages.forEach(function(message) {
            message.style.display = "none";
        });
    }, 5000);
})