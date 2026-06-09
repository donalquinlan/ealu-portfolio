FROM nginx:1.27-alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html ai-governance.html case-ppp.html case-fiserv.html case-vineti.html case-ealu.html styles.css script.js /usr/share/nginx/html/
COPY thumbnails/ /usr/share/nginx/html/thumbnails/
COPY resume.pdf /usr/share/nginx/html/
