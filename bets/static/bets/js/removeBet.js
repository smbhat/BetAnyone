$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (settings.type == 'POST' || settings.type == 'PUT' || settings.type == 'DELETE') {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    }
});

$(document).ready(function() {
  $('.list-group-item').each(function(index, element) {
    $(element).find('.deleteButton').click(function(e) {
      e.preventDefault();
      console.log(this.id);
      var betId = this.id.substring(5);
      console.log(betId);
      $.ajax({
        type: 'POST',
        data: {betId: betId, csrfmiddlewaretoken: '{{ csrf_token }}'},
        contentType: 'application/json',
        url: '/deletebet/' + betId + '/',
        success: function (response) {
          console.log(response);
          $(element).remove();
        },
        error: function (response) {
        }
      });
    });
  });
});

$(document).ready(function() {
  $('.list-group-item').each(function(index, element) {
    $(element).find('.deleteButton2').click(function(e) {
      e.preventDefault();
      var user = this.id.substring(4);
      console.log(user);
      $.ajax({
        type: 'POST',
        data: {User: user, csrfmiddlewaretoken: '{{ csrf_token }}'},
        contentType: 'application/json',
        url: '/deleteuser/' + user + '/',
        success: function (response) {
          console.log(response);
          $(element).remove();
        },
        error: function (response) {
        }
      });
    });
  });
});