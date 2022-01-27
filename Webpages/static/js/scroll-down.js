$(function() {
    $('section a, .nav-link-heading').on('click', function(e) {
      e.preventDefault();
      
      //get where you want to go
      let href = $(this).attr("href");
      
      //get current file
      let pathname = $(location).attr('pathname');

      //check if its contact as it exists on both pages
      if (href == "#section-Contact")
      {
        $("html, body").animate({ scrollTop: $(href).offset().top }, 500);
      }
      
      //check if on different page
      //from portfolio to home page
      else if (pathname=="/portfolio" && (!href.startsWith("/portfolio")))
      {
        location.replace("/" + href);
      }

      //is on same page
      else
      {
        $("html, body").animate({ scrollTop: $(href).offset().top }, 500);
      }
    });
});

