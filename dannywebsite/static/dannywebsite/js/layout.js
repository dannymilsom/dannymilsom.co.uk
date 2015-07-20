(function($) {
  'use strict';

  var layout = {
    init: function() {

      this.prepareDOM();
      this.bindListeners();

    },
    prepareDOM: function() {

      $("#site-search").select2({
        placeholder: 'Find a blog post'
      });

    },
    bindListeners: function() {

      if (matchMedia('only screen and (min-width: 767px)').matches) {

        var $skillCategory = $(".skill-category"),
            $skillText = $(".skill-text"),
            $portfolio =  $("#portfolio");

        $skillCategory.on('click', function(e) {
          e.stopPropagation();

          if ($(this).hasClass("active")) {
            // hide text
            $skillText.removeClass("show-skills-text");

            // remove inline margin
            $portfolio.css("margin-top", "");

            // remove focused and active classes
            $skillCategory.removeClass("focused");
            $(this).removeClass("active");
          }
          else {
            // make sure all skill rows are hidden
            $skillText.removeClass("show-skills-text");

            // calculate how much margin we need for the text
            $portfolio.css("margin-top", $(".skill-text", this).innerHeight());

            // ensure all the category images have opacity 1
            $skillCategory.removeClass("focused active");

            // Reveal skill and blur out other categories
            $(".skill-text", this).addClass("show-skills-text");
            $skillCategory.addClass("focused");
            $(this).addClass("active");
          }
        });
      }

      $("#contact-us-form").submit(function(e) {
          e.preventDefault();

          var response = $.ajax({
            type: 'POST',
            dataType: 'json',
            crossDomain: false, // needed by is_ajax() server side
            data: $(this).serialize()
          });

          response.done(function(data) {
            if (data['errors']) {
              $("#warning-message, #warning-list").remove();
              $("input, textarea").removeClass('validation-warning');

              for (var m in data['errors']) {
                if (m === 'email') {
                  $("#id_email").val("");
                }
                $("#id_" + m).addClass('validation-warning')
                             .attr('placeholder', m + " - " + data['errors'][m]);
              }
            } else {
              $("#contact-us-form").slideUp( "slow");
              $("#contact-us-success").removeClass("hide-it")
                                       .slideDown("slow");
              $("#success-message").html(data['message']);
            }
          });
      });

    }
  };

   /**
  * initialise the website JavaScript once the DOM is ready
  */
  $(function() {
    layout.init();
  });

})(jQuery);
