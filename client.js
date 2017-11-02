var net = require('net');
var utf8 = require('utf8');

var client = new net.Socket();
client.connect(12345, '127.0.0.1', function() {
    console.log('Connected');
    client.write('香蕉230');
});

client.on('data', function(data) {
	arr = []
	data = data.toString()
	console.log(JSON.parse(data))
  client.destroy(); // kill client after server's response
});
