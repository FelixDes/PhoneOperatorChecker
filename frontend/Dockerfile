FROM node
WORKDIR /frontend
COPY package.json /frontend
RUN npm i
COPY . /frontend
EXPOSE 3000
CMD ["npm", "run", "dev"]