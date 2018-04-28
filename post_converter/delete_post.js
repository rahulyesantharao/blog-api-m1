// PASS ONE PARAMETER: POST NUMBER
const mysql = require('mysql');
const fs = require('fs');
const slug = require('slug');
const path = require('path');

// Create Connection to Database
var connection = mysql.createConnection({
  host: 'localhost',
  user: 'user',
  password: 'password',
  database: 'db'
});

// Connect to Database
connection.connect(function(err) {
  if(err) {
    console.error(err);
    return;
  }
  console.log('connected as id ' + connection.threadId);
});

// Read ID (primary key) from parameters
var id = process.argv[2];

// Save Post
var query = connection.query('DELETE FROM posts WHERE id = ?', id, function(error, results, fields) {
  if(error) throw error;
  console.log('# Rows Changed: ', results.changedRows);
});
console.log(query.sql);

// Close Connection
connection.end();
