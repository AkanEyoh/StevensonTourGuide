const express = require('express');
const app = express();
const port = 7777;

app.use(express.static('images'));
app.listen(port, () => {console.log('Server started on 7777')});
