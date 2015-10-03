// http://stackoverflow.com/questions/4270485/drawing-lines-on-html-page
function DrawLine(x1, y1, x2, y2, w, id){

    if(y1 < y2){
        var pom = y1;
        y1 = y2;
        y2 = pom;
        pom = x1;
        x1 = x2;
        x2 = pom;
    }

    var a = Math.abs(x1-x2);
    var b = Math.abs(y1-y2);
    var c;
    var sx = (x1+x2)/2 ;
    var sy = (y1+y2)/2 ;
    var width = Math.sqrt(a*a + b*b ) ;
    var x = sx - width/2 - w/2;
    var y = sy - w/2;

    a = width / 2;

    c = Math.abs(sx-x);

    b = Math.sqrt(Math.abs(x1-x)*Math.abs(x1-x)+Math.abs(y1-y)*Math.abs(y1-y) );

    var cosb = (b*b - a*a - c*c) / (2*a*c);
    var rad = Math.acos(cosb);
    var deg = (rad*180)/Math.PI

    var div = document.getElementById(id);
    if (!div) {
        htmlns = "http://www.w3.org/1999/xhtml";
        div = document.createElementNS(htmlns, "div");
        div.setAttribute("class", "line");
        div.setAttribute("id", id);
        document.getElementById("main").appendChild(div);
    }
    
    div.setAttribute('style','border-width:' + w + 'px;width:'+width+'px;height:0px;-moz-transform:rotate('+deg+'deg);-webkit-transform:rotate('+deg+'deg);position:absolute;top:'+y+'px;left:'+x+'px;');   

}

toId = function(name) {
    return "node" + name.replace(/:/g, "_")
}

lineId = function(name1, name2) {
    return "line" + (name1+name2).replace(/:/g, "_")
}

drawgraph = function(data) {
    var height = window.innerHeight
    var width = window.innerWidth
    var basesize = 50;
    var basewidth = 1;
    $.each(data, function(name, paras) {
        var id = toId(name)
        var div = $(document.getElementById(id)) 
        if (div.length == 0) {
            div = $('<div class="node" id="'+ id + '">' + name + '</div>')
            $("#main").append(div)
        }
        div.css("font-size", basesize * paras['weight'] + "px")
        div.css({
            position: "absolute",
            top: height * paras['y'] - div.height() / 2 + "px",
            left: width * paras['x'] - div.width()  / 2 + "px",
        })
    })
    
    $.each(data, function(name, paras) {
        var id_a = toId(name)
        var div_a = $(document.getElementById(id_a))
        $.each(paras['edges'], function(name2, weight) {
            var id_b = toId(name2)
            var div_b = $(document.getElementById(id_b)) 
            var pos_a = div_a.position();
            var pos_b = div_b.position();
            DrawLine(pos_a.left + div_a.width() / 2,
                     pos_a.top  + div_a.height() / 2,
                     pos_b.left + div_b.width() / 2,
                     pos_b.top  + div_b.height() / 2,
                     basewidth * weight,
                     lineId(name, name2)
                    )
        })
    })
    
}

update = function() {
    $.ajax({
        url: "/dynamic",
        dataType: "json",
    })
    .done(function( data ) {
        drawgraph(data)
        window.setTimeout(update, 100)
    })
}

$(function() {
    update()
})