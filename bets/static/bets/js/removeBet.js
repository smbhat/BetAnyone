$(document).ready(function() {
  $('.list-group-item').each(function(index, element) {
    $(element).find('.deleteButton').click(function(e) {
      console.log('----here2');

      e.preventDefault();
      console.log(this.id);
      var betId = this.id.substring(5);
      console.log(betId);
      var data = { betId: betId } ;
      $.ajax({
        type: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json',
        url: '../deletebet/' + betId,
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