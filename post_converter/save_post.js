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

// Read Post Metadata
var metadata = JSON.parse(fs.readFileSync('', 'utf8'));
var postmeta = metadata[id]
var title = postmeta.title;
var post_id = slug(title, {lower: true});

// Read Post Text
var mdpath = path.resolve(__dirname, 'md_posts/post' + id + '.md');
var htmlpath = path.resolve(__dirname, 'html_posts/post' + id + '.html');
try {
  var mdtext = fs.readFileSync(mdpath, 'utf8'); // connection.escape?
  var htmltext = fs.readFileSync(htmlpath, 'utf8'); // mysql.escape?
} catch(err) {
  console.error(err);
}

// Create Other Post Attributes
var date = mysql.raw('CURDATE()');
var author_id = 1;

// Create Post
post = {
  id: id,
  post_id: post_id,
  date: date,
  title: title,
  md: mdtext,
  html: htmltext,
  author_id: author_id
}

// Save Post
var query = connection.query('INSERT INTO posts SET ?', post, function(error, results, fields) {
  if(error) throw error;
  console.log('Solution: ', results[0].solution);
});
console.log(query.sql);

// Close Connection
connection.end();
