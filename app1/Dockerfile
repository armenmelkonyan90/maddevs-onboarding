FROM nginx:latest

# Copy custom HTML and image
COPY index.html /usr/share/nginx/html/index.html
COPY image.jpg /usr/share/nginx/html/image.jpg

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
