$(document).ready(function() {
  $('.list-group-item').each(function(index, element) {
    $(element).find('.addButton').click(function(e) {
      e.preventDefault();
      console.log(this.id);
      var betId = this.id.substring(5);
      console.log(betId);
      var data = { betId: betId } ;
      $.ajax({
        type: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json',
        url: '/addbet/' + betId + '/',
        success: function (response) {
          console.log(response);
          $(element).find('.addButton').remove();
        },
        error: function (response) {
        }
      });
    });
  });
});