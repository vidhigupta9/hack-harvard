$( document ).ready(function() {
    
    // If the mouse toggles on the title, an underline appears; when it leaves, the underline disappears
    $(document).on("mouseenter", ".law-title", function() {
        $(this).addClass("underline");
    })
    $(document).on("mouseleave", ".law-title", function() {
        $(this).removeClass("underline");
    })

    $(".input").keypress(function(event) { // submitting search result by pressing Enter
        if (event.keyCode === 13) {
          event.preventDefault();
          // copy the innerHTML of the search bar and move to the search results page
        }    
      });
})