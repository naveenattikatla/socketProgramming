const net = require("net")

const client   = net.createConnection({port  : 8083} , () =>{
    console.log("conection established...")
    client.write("data from node client server")
})


client.on("data", (data)=>{
    console.log(data.toString())
})
