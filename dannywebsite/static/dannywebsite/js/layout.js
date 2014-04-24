$(document).ready(function () {

    $("#site-search").select2({
      placeholder: 'Find a blog post'
    });

    $('#nav_blog').click( function() {
        $('#hidden_nav_container').attr('display', 'inline');
    });

    $("#contact-form-submit-btn").click(function(e) {
        e.preventDefault();
        $.ajax({
            url: '',
            type: 'POST',
            dataType: 'json',
            crossDomain: false, // needed by is_ajax() server side
            data: $("#contact-us-form").serialize(),
            success: function(data) {
              if (data['errors']) {
                $("#warning-message, #warning-list").remove();
                $("input, textarea").removeClass('validation-warning');

                for (m in data['errors']) {
                  if (m === 'email') {
                    $("#id_email").val("");
                  }
                  $("#id_" + m).addClass('validation-warning')
                               .attr('placeholder', m + " - " + data['errors'][m]);
                }
              } else {
                $( "#contact-us-form" ).slideUp( "slow");
                $( "#contact-us-success").removeClass("hide-it");
                $( "#contact-us-success").slideDown( "slow");
                $("#success-message").html(data['message'])
              }
            }
        });
    })

    if (matchMedia('only screen and (min-width: 767px)').matches) {

      $(".skill-category").click(function(e) {
        e.stopPropagation();
        if ($(this).hasClass("active")) {
          // we're looking at a category and want to hide the images
          $(".skill-text", this).css("display", "none");
          $("#portfolio .skills-img").css("width", "40%")
          $("#portfolio").css("opacity", "1");
          $('.skill-info').addClass("hide-it"); 
          $(this).removeClass("active");
          $(".skill-category").removeClass("focused");
          $("#portfolio").removeClass("focused");
        }
        else {
          // we want to look at a new category
          // first thing we do is make sure all skill rows are hidden
          $(".skill-text").css("display", "none");
          $("#portfolio").css("opacity", "0")
          $("#portfolio .skills-img").css("width", "20%")
          $('.skill-info').addClass("hide-it");
          // and that all the category images have opacity 1
          $(".skill-category").removeClass("focused")
          $(".skill-category").removeClass("active")

          // Reveal skill and blur out other categories
          $(".skill-text", this).css("display", "block");
          $(".skill-category").addClass("focused");
          $(this).addClass("active");
          $('.' + $(this).attr('id')).removeClass("hide-it"); 
        }
      });
  }

  if (matchMedia('only screen and (min-width: 767px)').matches) {
    $(document).click(function(e) {
      // look to see if any skill-category elements are visible / open
      // if they are close them!
      $(".skill-text", this).css("display", "none");
      $("#portfolio .skills-img").css("width", "40%")
      $("#portfolio").css("opacity", "1");
      $('.skill-info').addClass("hide-it"); 
      $(this).removeClass("active");
      $(".skill-category").removeClass("focused");
      $("#portfolio").removeClass("focused");
    });
  }

});