$(document).ready(function(){
    // Here specify your content or message, enclose between <p>
    $('.modal').modal(
        {
            dismissible: true, // Modal can be dismissed by clicking outside of the modal
            opacity: .7, // Opacity of modal background
            inDuration: 300, // Transition in duration
            outDuration: 200, // Transition out duration
            startingTop: '0%', // Starting top style attribute
            endingTop: '0%', // Ending top style attribute
            preventScrolling: true, // Prevent page from scrolling while modal is open.
            ready: function(modal, trigger) { // Callback for Modal open. Modal and trigger parameters available.
                alert("Ready");
                console.log(modal, trigger);
            },
            complete: function() { // Callback for Modal close
                alert('Closed');
            }
        }
    );

});

