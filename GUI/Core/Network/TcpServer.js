class TcpServer
{
    #commandsEnum = {

    }

    #ipAddress = '127.0.0.1'
    #port = 1337;
    #net = require('net');
    #server;
    #client;

    setClient(client) {this.#client = client;}
    getClient() {return this.#client;}
    getNetwork() {return this.#net;}
    getServer() {return this.#server};

    start() {
        const self = this;
        this.#server = this.#net.createServer(function (socket){
            self.setClient(socket);

            self.#client.on('data', function (data){
                console.log("Received "+data);
            })
        })

        this.#server.listen(this.#port, this.#ipAddress);
    }

    send(message)
    {
        if (this.#client !== undefined && message !== undefined){
            this.#client.write(message);
        }
    }
    sendTo(sock,message)
    {
        if (sock !== undefined && message !== undefined){
            sock.write(message)
        }
    }
    receive()
    {

    }
}

module.exports = TcpServer