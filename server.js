const net =  require("net")

const client = net.createServer((socket) =>{
    // whenever user is sending data , call back function triggers
    socket.on("data" , (data)=>{
        console.log(data.toString())
    })
    socket.write("message recieved from  node server ")

})


client.listen(8083 , ()=>{
    console.log("server is running at port 8083")
})