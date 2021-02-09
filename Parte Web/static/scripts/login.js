$(document).ready(function () {
    $.getScript("../static/scripts/jquery.md5.js", function(){
        console.log("Script de encriptado cargado correctamente");
    });
    checkCookie();
    $(".btn-success").click(function () {
        var vemail = $('#emailInput').val();
        var vcontraseña = $('#contraseñaInput').val();
        var vmd5 = ($.md5(vcontraseña));
        alert(vmd5);
        $.get("URL", { email: vemail, md5: vmd5 }, function (data) {
            function jsonEscape(string) {
                return string.replace(/\n/g, "\\\\n").replace(/\r/g, "\\\\r").replace(/\t/g, "\\\\t");
            }
            var json = data;
            var response = JSON.stringify(json);
    
            if (response['datosCorrectos'] == 'True') {
                createCookie(response['mail']);
                window.location.href = '/calculadora_lambda.html';
            }
            else {
                alert('Datos incorrectos');
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
        window.location.replace('/calculadora_lambda.html');
    }
}
function readCookie(cookieName){
    var name = cookieName + '=';
    var cookieSplit = document.cookie.split(';');

    for (let index = 0; index < cookieSplit.length; index++) {
        var char = cookieSplit[index];
        while(char.charAt(0) == ' '){
            char = char.substring(1);
        }
        if(char.indexOf(name) == 0){
            return decodeURIComponent(cookieSplit.substring(name.length, char.length));
        }
    }
}