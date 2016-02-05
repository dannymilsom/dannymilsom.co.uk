(function($) {
  'use strict';

  var FormView = Backbone.View.extend({
    el: $('form'),
    events: {
      "submit": "formSubmit",
    },

    formSubmit: function(e) {
      self = this;
      e.preventDefault();

      var response = $.ajax({
        type: 'POST',
        dataType: 'json',
        crossDomain: false, // needed by is_ajax() server side
        data: this.$el.serialize()
      });

      response.always(function(){
        self.$el.find('input, textarea').removeClass('validation-warning');
      });

      response.fail(function(response) {
        $.each(response.responseJSON, function(key, val) {
          $("#id_" + key).addClass('validation-warning')
                         .attr('placeholder', val);
        });
      });

      response.done(function() {
        $("#contact-form-submit-btn").attr('disabled', true)
                                     .attr('value', 'Email sent!')
      });

    }

  });

  var formView = new FormView();

})(jQuery);
