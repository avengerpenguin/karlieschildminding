#!/bin/sh

cd `dirname $0`

mkdir -p output/files
cd output/files

echo "<html>\n<body>\n<h1>Policies</h1>\n<hr/>\n<pre>" >index.html

ls -1pa | grep -v "^\./$" | grep -v "^\.\./$" | grep -v "^index\.html$" | sed 's/.*/<a href=\"\0\">\0<\/a>\n/g' >>index.html

echo "</pre></body></html>" >>index.html
