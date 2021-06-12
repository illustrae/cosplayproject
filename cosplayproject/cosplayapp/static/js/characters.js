var marCharac ={
    render: function() {
        var url='http://gateway.marvel.com/v1/public/characters?ts=1&apikey=e613f39e70935d2fd93475f1f44dfff4&hash=8b01b7154ae025c7bd2cd61d7104df79';
        var characterMsg = document.getElementById('characterMsg');
        var footer = document.getElementById('footer');
        var marvelImage = document.getElementById('marvelImage');

        $.ajax({
            url: url,
            type: 'GET',
            beforeSend: function() {
                characterMsg.innerHTML = 'Loading...';
            },
            complete: function() {
                characterMsg.innerHTML = 'Loaded';
            },
            success: function(data) {
                footer.innerHTML = data.attributionHTML;
                var string='';
                string += "<div class='row'>"

                for(var i= 0; i < data.data.results.length; i++) {
                    var element = data.data.results[i];
                
                    string += "<div class='cold-md-3'>";
                    string += "</div>";

                    if ((i+1) % 4 == 0)  {
                        string += "</div>";
                        string += "<div class='row'>";
                    }
                }

            },
            error: function() {
                message.innerHTML = 'Sorry...';

            }

        });

    }
}
marCharac.render();
