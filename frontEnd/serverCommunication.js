$(function() {
    $('button').click(function() {
      alert("FUCK");
//        var user = $('#txtUsername').val();
//        var pass = $('#txtPassword').val();
        // var coords = '75.77 85.32 -21.22 102.43';
        // var date-time = document.getElementById("date-time");
        // var time = '20:00'
        // var description = document.getElementById("document");
        // var invite = "[" + document.getElementById("inviteList") + "]";
        var coords = '72, 74, 75, 76';
        var openWindow = '10/21/2017 16:30';
        var closeWindow = '20:00' // TODO: delete
        var description = 'Lit smack party';
        var invite = "['Mason Hayes', 'Tommy Zarick', 'David Moeller', 'Yomali Kader', 'Bill Cosby']";

        $.ajax({
            url: 'http://192.241.193.9:3001/createEvent',
            data: {
              'loc': coords,
              'openTime': openWindow,
              'closeTime': closeWindow,
              'description': description,
              'invite': invite
              // 'name': "Tommy Zarick"
            },
            type: 'POST',
            success: function(err, response, body) {
                // alert("HELLO");
                // var  = JSON.parse(body);
                console.log(err);

                // alert(JSON.stringify(body.responseJSON.list));
                // alert(response);
                // alert(JSON.parse(response));
                // var list = body.list;
                // alert("HELLP");
                // alert(list);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
