# Use the official Node.js image
FROM node:20

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install
RUN npm install --save-dev @types/react-router-dom

# Copy the rest of the application code
COPY ./app ./app
COPY ./components ./
COPY ./lib ./lib
COPY components*.* ./
COPY next*.* ./
COPY tsconfig*.* ./

# Build the application
RUN npm run build

# Expose the port the app runs on
EXPOSE 3000

# Command to run the application
CMD ["npm", "start"]