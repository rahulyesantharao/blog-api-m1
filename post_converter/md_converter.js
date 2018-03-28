// PASS 1 CMD ARGUMENT: THE POST NAME (just name, no extension, no file path)
const showdown = require('showdown');
const fs = require('fs');
const path = require('path');
// Extension
showdown.extension('targetlink', function() {
  return [{
    type: 'html',
    filter: function (text) {
        return (''+text).replace(/<a\s+href=/gi, '<a target="_blank" rel="noopener noreferrer" href=');
    }
  }];
});

var sourcePath = path.resolve(__dirname, 'md_posts/' + process.argv[2] + '.md');
var destPath = path.resolve(__dirname, 'html_posts/' + process.argv[2] + '.html');
var conv = new showdown.Converter({extensions: ['targetlink'], noHeaderId: true});
try {
  var text = fs.readFileSync(sourcePath, 'utf8');
  // console.log(text);
} catch(err) {
  console.error(err);
}
var html = conv.makeHtml(text);
fs.writeFileSync(destPath, html, 'utf8');
