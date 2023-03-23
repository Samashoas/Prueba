var http = require("http");

var manage = function(sol, res){
    console.log("Nueva respuesta");
    res.end("Juan Pablo Samayoa Ruiz_202109705");
};

var servidor = http.createServer(manage);

servidor.listen(3000);