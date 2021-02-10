$(document).ready(function () {
    $.getScript("../static/scripts/jquery.md5.js", function(){
        console.log("Script de encriptado cargado correctamente");
    });
    checkCookie();
    $(".btn-success").click(function () {
        var vemail = $('#emailInput').val();
        var vcontrasena = $('#contrasenaInput').val();
        var vmd5 = ($.md5(vcontrasena));
        $.get("URL-API-Gateway", { email: vemail, md5: vmd5 }, function (data) {
            function jsonEscape(string) {
                return string.replace(/\n/g, "\\\\n").replace(/\r/g, "\\\\r").replace(/\t/g, "\\\\t");
            }
            var json = data;
            alert("respuesta: " + JSON.stringify(json));
            if (json.datosCorrectos == 'True') {
                createCookie(vemail);
                alert('hola');
               	window.location.replace(json.redirect);
            }
        });
    });
});
function createCookie(email){
    var cookie = 'email=' + encodeURIComponent(email);
    cookie += '; expires=Thu, 31 Dec 2099 23:59:59 GMT; path=/';
    document.cookie = cookie;
    alert('Cookie establecida correctamente');
}
function checkCookie(){
    if(readCookie('email') != null){
        location.href = 'calculadora_lambda.html';
    }
}
function readCookie(cookieName){
    var name = cookieName + '=';
    var cookieSplit = document.cookie.split(';');

    for (let index = 0; index < cookieSplit.length; index++) {
        var char = cookieSplit[index];
        while(char.charAt(0) == ' '){
            char = char.substring(1, char.length);
        }
        if(char.indexOf(name) == 0){
            return decodeURIComponent(char.substring(name.length, char.length));
        }
    }
}
