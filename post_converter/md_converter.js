const showdown = require('showdown');
const fs = require('fs');

// Extension
showdown.extension('targetlink', function() {
  return [{
    type: 'lang',
    regex: /\[((?:\[[^\]]*]|[^\[\]])*)]\([ \t]*<?(.*?(?:\(.*?\).*?)?)>?[ \t]*((['"])(.*?)\4[ \t]*)?\)\{\:target=(["'])(.*)\6}/g,
    replace: function(wholematch, linkText, url, a, b, title, c, target) {

      var result = '<a href="' + url + '"';

      if (typeof title != 'undefined' && title !== '' && title !== null) {
        title = title.replace(/"/g, '&quot;');
        title = showdown.helper.escapeCharacters(title, '*_', false);
        result += ' title="' + title + '"';
      }

      if (typeof target != 'undefined' && target !== '' && target !== null) {
        result += ' target="' + target + '"';
      }

      result += ' rel="noopener noreferrer">' + linkText + '</a>';
      return result;
    }
  }];
});

var sourcePath = 'md_posts/' + process.argv[2] + '.md';
var destPath = 'html_posts/' + process.argv[2] + '.html';
var conv = new showdown.Converter({extensions: ['targetlink']});
try {
  var text = fs.readFileSync(sourcePath);
} catch(err) {
  console.error(err);
}
var html = conv.makeHtml(text);
fs.writeFileSync(destPath, html, 'utf8');
