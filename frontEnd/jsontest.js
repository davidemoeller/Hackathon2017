const http = require('http');

const hostname = '192.241.193.9'
const port = 3000;

const server = http.createServer((req,res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('test\n');
});

server.listen(port, hostname, () => {
    console.log('Server running at http://${hostname}:${port}/');
});