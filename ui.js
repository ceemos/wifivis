document.write('<div id="blub">Hello World!</div>')
$("#blub").attr('style', "color: red;")

update = function() {
    $.ajax({
        url: "/dynamic",
        dataType: "json",
    })
    .done(function( data ) {
        $("#blub").text(data["data"])
    
        window.setTimeout(update, 100)
    })
}

update()