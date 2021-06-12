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
                characterMsg.innerHTML = 'Get familiar';
            },
            success: function(data) {
                footer.innerHTML = data.attributionHTML;
                var string="";
                string += "<div class='row'>"

                for(var i= 0; i < data.data.results.length; i++) {
                    var element = data.data.results[i];
                
                    string += "<div class='col-sm-2 '>";
                    string += " <a href='"+element.urls[0].url+"'target='_blank'>";
                    string += " <img src='"+element.thumbnail.path+"/portrait_medium."+element.thumbnail.extension+"'/>";
                    string += "</a>"
                    string += " <h6>" +element.name + "</h6>"
                    string += "</div>";

                    if ((i+1) % 6 == 0)  {
                        string += "</div>";
                        string += "<div class='row'>";
                    }
                }

                marvelImage.innerHTML = string;

            },
            error: function() {
                message.innerHTML = 'Sorry...';

            }

        });

    }
}
marCharac.render();

