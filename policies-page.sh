#!/bin/sh

cd `dirname $0`

echo '<html><head><title>Policies</title><meta name="url" content="policies" /><meta name="save_as" content="policies/index.html" /></head><body><ul class="policies">' >content/pages/policies.html

sed -r 's/([^.]*)\.pdf/<li><a href=\"\/files\/\0\">\1<\/a><\/li>/g' >>content/pages/policies.html <<EOF
Accident and Incident Policy.pdf
Alcohol, Smoking and Other Substances Policy.pdf
A Safeguarding Policy.pdf
Behaviour Management Policy.pdf
Complaints Policy.pdf
Fees Policy.pdf
Fire Policy and Evacuation Plan.pdf
Health and Safety Policy.pdf
Healthy Eating Policy.pdf
Illness and Sickness Policy.pdf
Lost Child Policy.pdf
Medication Policy.pdf
Partnership With Parents Policy.pdf
Risk Assessment Policy.pdf
Uncollected Child Policy.pdf
Visitors Policy.pdf
EOF

echo '</ul></body></html>' >>content/pages/policies.html
