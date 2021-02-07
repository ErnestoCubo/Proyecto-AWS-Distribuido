$(document).ready(function () {
    $("button").click(function () {
        var vop1 = document.getElementById("op1").value;
        var vop2 = document.getElementById("op2").value;
        var vop = document.getElementById("op").value;
        var vres = "";

        var asd = $.get("https://6ceb939oi9.execute-api.eu-west-2.amazonaws.com/prueba_calculadora", { method: "operacion", op1: vop1, op2: vop2, op: vop }, function (data) {
                function jsonEscape(str) {
                    return str.replace(/\n/g, "\\\\n").replace(/\r/g, "\\\\r").replace(/\t/g, "\\\\t");
                }
                var json = data;
                alert('page content: ' + JSON.stringify(json));
                document.getElementById("res").innerHTML = "Resultado recibido:" + json.res;
                window.location.replace(json.redirect);
            })
            .done(function () {
                alert("second success");
            })
            .fail(function () {
                alert("error");
            });
        asd.always(function () {
            alert("second finished");
        });
    });
});