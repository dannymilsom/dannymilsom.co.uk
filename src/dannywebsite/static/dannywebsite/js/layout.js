(function($) {
  'use strict';

  var layout = {
    init: function() {

      this.bindListeners();

    },
    bindListeners: function() {

      $(".contact form").submit(function(e) {
          e.preventDefault();

          var response = $.ajax({
            type: 'POST',
            dataType: 'json',
            crossDomain: false, // needed by is_ajax() server side
            data: $(this).serialize()
          });

          response.always(function(){
            $('input, textarea').removeClass('validation-warning');
          });
          response.done(function(response) {
            $(".confirmation").removeClass('hidden')
                              .find('.message').html(response['message']);
          });
          response.fail(function(response) {
            $.each(response.responseJSON, function(key, val) {
              $("#id_" + key).addClass('validation-warning')
                             .attr('placeholder', val);
            });
          })
      });

    }
  };

   /**
  * initialise once the DOM is ready
  */
  $(function() {
    layout.init();
  });

})(jQuery);
