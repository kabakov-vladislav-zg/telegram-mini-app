# FROM node:alpine AS build
# WORKDIR /app
# COPY package*.json ./
# RUN npm ci --only=production --silent --no-optional --no-audit --no-fund
# COPY . .
# RUN npm run build:web
FROM alpine/git as build
WORKDIR /app
RUN git clone -b gh-pages https://github.com/kabakov-vladislav-zg/telegram-mini-app.git

FROM nginx:stable-alpine
COPY --from=build /app/telegram-mini-app /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
