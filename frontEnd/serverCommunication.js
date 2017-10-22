$(function() {
    $('button').click(function() {
//        var user = $('#txtUsername').val();
//        var pass = $('#txtPassword').val();
        var coords = '75.77 85.32 -21.22 102.43';
        var date = '10/21/2017';
        var time = '20:00';
        var description = 'Lit smack party';
        var invite = "['Mason Hayes', 'Tommy Zarick', 'David Moeller', 'Yomali Kader', 'Bill Cosby']";
        $.ajax({
            url: 'http://192.241.193.9:3001/createEvent',
            data: {
              'loc': coords,
              'date': date,
              'time': time,
              'description': description,
              'invite': invite
            },
            type: 'POST',
            success: function(response) {
                alert(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
