FROM node:24-alpine
 
WORKDIR /client
 
COPY package*.json ./
 
RUN npm install
 
COPY . .
 
EXPOSE 5173
 
CMD ["npm", "run", "dev"]