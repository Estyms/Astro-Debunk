var urlParams = new URLSearchParams(window.location.search);
if (urlParams.get('prenom') != null && urlParams.get('prenom').length  >  0){
    $.getJSON( "/Astro-Debunk/Files/Classement.json", function( data ) {
        name = urlParams.get('prenom').normalize("NFD").replace(/[\u0300-\u036f]/g, "");

        $.getJSON( "/Astro-Debunk/Files/Classement.json", function( data ) {
            
            var items = [];
            $.each( data, function( key, val ) {
                if (key.toLowerCase() == name.toLowerCase()) {
                    console.log("HEY");
                    items.push("<h4>" + val.classement +"# "+ key + "<h4/><h5>" + val.score + " Points</h5>" );
                }
            });
           if (items.length == 0) items.push("<h4> Ce prénom n'est pas dans la base de données.");
            $( "<div>", {
              "class": "end collection",
              "style": "margin-bottom:50px",
              html: items.join( "" )
            }).appendTo( "body" );
            $.getJSON( "/Astro-Debunk/Files/Classement.json", function( data ) {
                var items = [];
                $.each( data, function( key, val ) {
                  items.push( "<li class='collection-item'><h6>" + val.classement +"# "+ key + "<h6/>" + val.score + " Points </li>" );
                  i++;
                  if (i == 100) return;
                });
               
                $( "<ul>", {
                  "class": "collection",
                  html: items.join( "" )
                }).appendTo( "body" );
              });
          });
    });
    
} else{
    $.getJSON( "/Astro-Debunk/Files/Classement.json", function( data ) {
        var items = [];
        i = 0;
        $.each( data, function( key, val ) {
          items.push( "<li class='collection-item'><h6>" + val.classement +"# "+ key + "<h6/>" + val.score + " Points </li>" );
          i++;
          if (i == 100) return;
        });
       
        $( "<ul>", {
          "class": "collection",
          html: items.join( "" )
        }).appendTo( "body" );
      });
}



history.pushState({
    id: 'homepage'
}, 'Calc-Name', "/Astro-Debunk");   