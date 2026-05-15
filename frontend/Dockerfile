FROM nginx:alpine

# copy static website files, perhaps include dockerignore file later
COPY . /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]