# FastFoodMenuCreator

FastFoodMenuCreator is a web application designed to help restaurant owners, especially those managing fast food, create and manage their menu catalog. The application provides an intuitive interface for building a personalized menu, which can then be visualized and exported for use in digital kiosks, like those found in fast food restaurants such as McDonald's. This allows owners to quickly configure and deploy their menu for customer use.

## Features

1. **Visualize Menu**: Allows users to create and preview their menu in a kiosk-like interface to see how it would appear on a digital ordering screen.
2. **Catalog Creation**: Users can add, edit, and organize food items, categories, and prices to build their custom catalog.
3. **Export Functionality**: Once the menu is created, it can be exported to different formats for deployment on various systems (e.g., JSON, CSV).
4. **User-Friendly Interface**: Designed to replicate the fast-food ordering experience for a seamless transition to deployment.

## Tech Stack

- **Frontend**: 
  - **React JS**: Used for building dynamic and interactive user interfaces.
- **Backend**: 
  - **Flask**: Python framework used to handle server-side operations and API requests.
- **Database**: 
  - **MongoDB**: NoSQL database to store menu items and user data in a flexible schema.
- **Containerization**: 
  - **Docker**: Used for setting up a stable and consistent development environment.
  - Docker compose(V2)
  
## Prerequisites

- **Python 3.12**
- **Flask**: Backend framework used to handle server-side functionality.
- **React JS**: Frontend framework used for creating interactive user interfaces.
- **Node JS and NPM**: Required for running the frontend environment and managing dependencies.
- **MongoDB**: NoSQL database for storing the menu catalog.

## Docker setup

1) Before install [Docker](https://docs.docker.com/get-started/get-docker/) in your computer.
2) Clone the repository :
```bash
git clone https://github.com/Eliott133/FastFoodMenuCreator.git
```
```bash
cd FastFoodMenuCreator
```
3) Start deployment
```bash
docker-compose up --build
```

## Usage

- Access the application through the frontend by navigating to http://localhost:3000 in your browser.
- The Flask backend API will be available at http://localhost:5000 to handle requests.


