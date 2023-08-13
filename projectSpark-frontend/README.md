## ProjectSpark Frontend

Project Spark Frontend is the web interface for the idea sharing and collaboration platform powered by the Project Spark API. It is built using Next.js, a popular React framework, providing a modern and efficient development environment for frontend development.

### Frontend Structure

The frontend of ProjectSpark is built using Next.js, a popular React framework.

### Explanation of the Structure

- context: the context folder is applicable for state management in react, passing usestate values from one components to another.

- app: the app folder is an essential folder in nextjs which contains dynamic or static route for file base routing. It involves api route when working with MERN application (Mongodb, express, React and Nodejs)

- constants: this folder contains all static text that will be shown on the UI/ client aplication

- global: this folder contains CSS utility class that can be applied globally within the UI

- styles: this folder contains CSS utility that can be applied on individual components

- public: This folder contains the static files used in nextjs for client application only, such as the public assets folders for images

- constants: this folder contains all static text that will be shown on the UI/ client aplication

- components: This folder contains components e.g navbar that can be used in creating the layout of our application also contains reusable React components used across different pages e.g button.

- page: the page file in nextjs is an essential file in nextjs, which serve as Home page Or entry point in nextjs other componts can be rendered within the page components. The page file can be located inside the nextjs app folder.

- utils: This folder contains utility functions and services used in the frontend, such as API handling.

- .env: This file contains environment variables used in the frontend. It is used to store configuration details.

- .gitignore: This file specifies which files and folders should be ignored by Git version control.

- package.json: This file contains metadata and dependencies for the frontend project.

### Development Setup

To run the frontend locally, follow these steps:

1. Install *Node.js* and *npm (Node Package Manager)* if you haven't already.

2. Clone the repository and navigate to the *projectspark-frontend* directory.

3. Install the required dependencies using ``` npm install.```

4. Start the development server using ``` npm run dev. ```

The frontend will be accessible at https://localhost:3000.

Please note that this is a brief overview of the frontend structure, and additional details can be found within the individual files and folders of the project. If you have any specific questions or need more information, refer to the codebase or reach out to the development team.
