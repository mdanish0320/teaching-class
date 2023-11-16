const fs = require('fs')

const collection = require('./data/collection'); // any Postman collection JSON file
const { transpile } = require('postman2openapi');

// Returns a JavaScript object representation of the OpenAPI definition.
const openapi = transpile(collection);

fs.writeFileSync('./data/swagger.json', JSON.stringify(openapi, null, 2));