FROM node

# Prepare app directory
RUN mkdir -p /usr/src/app
ADD . /usr/src/app

# Install dependencies
WORKDIR /usr/src/app
COPY package.json .
RUN npm install

# Expose the app port
EXPOSE 8000

# Start the app
CMD npm start