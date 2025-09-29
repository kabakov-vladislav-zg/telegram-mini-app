# build environment
FROM node:alpine as build
WORKDIR /app
COPY . .
RUN npm ic
RUN npm run bild:web

# production environment
FROM nginx:stable-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY --from=build /app/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]