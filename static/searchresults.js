$( document ).ready(function() {
    var searchClick = document.getElementsByClassName("enter"); 
    var inputs = document.getElementsByClassName("input");
    
    // If the mouse toggles on the title, an underline appears; when it leaves, the underline disappears
    $(document).on("mouseenter", ".law-title", function() {
        $(this).addClass("underline");
    })
    $(document).on("mouseleave", ".law-title", function() {
        $(this).removeClass("underline");
    })

    // inputs.addEventListener("keyup", function(event) { // submitting search result by pressing Enter
    //     if (event.keyCode === 13) {
    //       event.preventDefault();
    //       searchClick.click();
    //     }    
    //   });
})