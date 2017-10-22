// TRASH
$(function sendEvent(geoFence){
        alert("HELLO");
        var vertices = geoFence.getPath();
        var coords = [];

        for (var i = 0; i < vertices.getLength(); i++) {
          var xy = vertices.getAt(i)
          if (i == 0) {
            coords.push(xy.lat()); // North side of rectangle
            coords.push(xy.lng()); // West side of rectangle
          }
          else if (i == 2) {
            coords.push(xy.lat()); // South side of rectangle
            coords.push(xy.lng());
          }
        }
        var coords = '72, 74, 75, 76';
        var openWindow = '10/21/2017 16:30';
        var closeWindow = '20:00' // TODO: delete
        var description = 'Lit smack party';
        var invite = "['Mason Hayes', 'Tommy Zarick', 'David Moeller', 'Yomali Kader', 'Bill Cosby']";
        alert(coords);
        $.ajax({
            url: 'http://192.241.193.9:3001/createEvent',
            data: {
              'loc': coords,
              'openWindow': date,
              'closeWindow': time,
              'description': description,
              'invite': invite
            },
            type: 'POST',
            success: function(err, response, body) {
                // alert("HELLO");
                // var  = JSON.parse(body);
                // console.log(err);
                //
                // alert(JSON.stringify(body.responseJSON.list));
                // alert(response);

            },
            error: function(error) {
                console.log(error);
            }
        });
});
