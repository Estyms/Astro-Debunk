var urlParams = new URLSearchParams(window.location.search);
if (urlParams.get('prenom') != null && urlParams.get('prenom').length  >  0){
    $.getJSON( "/Astro-Debunk/Files/Classement.json", function( data ) {
        name = urlParams.get('prenom').normalize("NFD").replace(/[\u0300-\u036f]/g, "");

        $.getJSON( "/Astro-Debunk/Files/Classement.json", function( data ) {
            
            var items = [];
            $.each( data, function( key, val ) {
                if (key.toLowerCase() == name.toLowerCase()) {
                  str = ""
                  if (val.score < 60) str = "Pas très Sexy comme <b>0.02%</b> des Gens";
                  if (val.score < 300) str = "Assez Sexy comme <b>1.73%</b> des Gens";
                  if (val.score < 600) str = "Très Sexy comme <b>15.02%</b> des Gens";
                  if (val.score > 599) str = "Le plus sexy comme <b>83.23%</b> des Gens";
                  console.log("HEY");
                  items.push("<h4>" + val.classement +"# "+ key + "<h4/><h5>" + val.score + " Points</h5><h6>" + str + "</h6>" );
                }
            });
           if (items.length == 0) items.push("<h4> Ce prénom n'est pas dans la base de données.");
            $( "<div>", {
              "class": "end collection",
              "style": "margin-bottom:50px",
              html: items.join( "" )
            }).appendTo( "body" );
            i=0;
            $.getJSON( "/Astro-Debunk/Files/Classement.json", function( data ) {
                var items = [];
                $.each( data, function( key, val ) {
                  items.push( "<li class='collection-item'><h6>" + val.classement +"# "+ key + "<h6/>" + val.score + " Points </li>" );
                  i++;
                  if (i == 100) return false;
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
          if (i == 100) return false;
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