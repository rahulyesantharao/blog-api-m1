// PASS TWO CMD PARAMETERS: THE POST FILE NAME (just name, no extension, no file path), THE POST TITLE
const mysql = require('mysql');
const fs = require('fs');
const slug = require('slug');
const path = require('path');

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'user',
  password: 'password',
  database: 'db'
});

connection.connect(function(err) {
  if(err) {
    console.error(err);
    return;
  }
  console.log('connected as id ' + connection.threadId);
});

var mdpath = path.resolve(__dirname, 'md_posts/' + process.argv[2] + '.md');
var htmlpath = path.resolve(__dirname, 'html_posts/' + process.argv[2] + '.html');
// var cur_date = { toSqlString: function() { return 'CURDATE()';}};
var date = mysql.raw('CURDATE()');
var title = process.argv[3];
var post_id = slug(title, {lower: true});
var author_id = 1;

try {
  var mdtext = fs.readFileSync(mdpath, 'utf8');
  var htmltext = fs.readFileSync(htmlpath, 'utf8');
  // mdtext = connection.escape(mdtext);
  // htmltext = mysql.escape(htmltext);
} catch(err) {
  console.error(err);
}

post = {
  post_id: post_id,
  date: date,
  title: title,
  md: mdtext,
  html: htmltext,
  author_id: author_id}

var query = connection.query('INSERT INTO posts SET ?', post, function(error, results, fields) {
  if(error) throw error;
  console.log('Solution: ', results[0].solution);
});
console.log(query.sql);

connection.end();
