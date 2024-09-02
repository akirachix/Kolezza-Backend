#Kolezza Backend Project
##Project Overview
The Kolezza backend project provides a robust API for managing a speech therapy system. It includes functionalities for managing users, speech therapists, children, and related entities. This README covers the project setup, database schema, API documentation, and other essential information.

##Project Setup
Git Flow
We use Git Flow to manage the development process. The workflow includes:

Main Branch: The stable branch where releases are made.
Develop Branch: The branch where development occurs.
Staging Branch:  is a branch that serves as an intermediary between development and production. Its purpose and use can vary based on the specific Git workflow being followed.
Feature Branches: Created from the develop branch for new features.

##Repository Structure
/docs: Swagger documentation and Postman collections.
/src: Backend source code.
/sql: SQL scripts for database setup.
/tests: Unit tests and other test-related files.
README.md: This file.
Code Review Process
We follow a code review process to ensure code quality and consistency. Key steps include:

Pull Request Creation: Create a pull request (PR) from your feature branch.
Peer Review: Reviewers will examine the code for correctness and adherence to coding standards.
Approval: Obtain approval from at least one reviewer.
Merge: Merge the PR into the develop branch after approval.

##SQL Scripts
https://codehive2024.slack.com/files/U06G25F8HB5/F07KDB4F6DR/kolezza__sawatok_script.sql
The SQL scripts for setting up the database are located in the /sql directory. The scripts define the tables and relationships required for the project. Key tables include:


User Table: Manages user accounts.
Speech Therapist Table: Stores information about speech therapists.
Child Table: Tracks children undergoing therapy.
Level of Stuttering Table: Defines different levels of stuttering.
Module Table: Manages therapy modules.
Guardian Table: Contains information about guardians.
Child Progress Table: Records progress for each child.
Session Table: Logs therapy session details.
Backend APIs
The backend APIs allow interaction with the database. The primary endpoints include:

User Endpoints
GET /users: List all users.
POST /users: Create a new user.
GET /users/{userId}: Retrieve user details by ID.
PUT /users/{userId}: Update user details.
DELETE /users/{userId}: Delete a user.
Speech Therapist Endpoints
GET /speech-therapists: List all speech therapists.
POST /speech-therapists: Create a new speech therapist.
GET /speech-therapists/{therapistId}: Retrieve speech therapist details by ID.
PUT /speech-therapists/{therapistId}: Update speech therapist details.
DELETE /speech-therapists/{therapistId}: Delete a speech therapist.

Child Endpoints
GET /child: List all children.
POST /child: Create a new child.
GET /child/{childId}: Retrieve child details by ID.
PUT /child/{childId}: Update child details.
DELETE /child/{childId}: Delete a child.

Level of Stuttering Endpoints
GET /levels-of-stuttering: List all levels of stuttering.
POST /levels-of-stuttering: Create a new level of stuttering.
GET /levels-of-stuttering/{levelId}: Retrieve level of stuttering details by ID.
PUT /levels-of-stuttering/{levelId}: Update level of stuttering details.
DELETE /levels-of-stuttering/{levelId}: Delete a level of stuttering.

Module Endpoints
GET /modules: List all modules.
POST /modules: Create a new module.
GET /modules/{moduleId}: Retrieve module details by ID.
PUT /modules/{moduleId}: Update module details.
DELETE /modules/{moduleId}: Delete a module.

Guardian Endpoints
GET /guardians: List all guardians.
POST /guardians: Create a new guardian.
GET /guardians/{guardianId}: Retrieve guardian details by ID.
PUT /guardians/{guardianId}: Update guardian details.
DELETE /guardians/{guardianId}: Delete a guardian.

Child Progress Endpoints
GET /child-progress: List all child progress records.
POST /child-progress: Create a new child progress record.
GET /child-progress/{progressId}: Retrieve child progress details by ID.
PUT /child-progress/{progressId}: Update child progress details.
DELETE /child-progress/{progressId}: Delete a child progress record.

Session Endpoints
GET /sessions: List all sessions.
POST /sessions: Create a new session.
GET /sessions/{sessionId}: Retrieve session details by ID.
PUT /sessions/{sessionId}: Update session details.
DELETE /sessions/{sessionId}: Delete a session.
Swagger Documentation
The Swagger documentation is available in the /docs directory. It provides a detailed description of the API endpoints, request and response formats, and other relevant details.

Postman Collection
A Postman collection for testing the API endpoints is also available in the /docs directory. It includes pre-configured requests for all API endpoints, making it easy to test and interact with the backend.

Running the Project
Clone the Repository: https://github.com/akirachix/Kolezza-Backend.git

bash
Copy code
git clone 
cd kolezza-backend
Install Dependencies:

bash
Copy code
npm install
Run the Application:

bash
Copy code
npm start
Run Migrations:

bash
Copy code
npm run migrate
Access Swagger UI: Navigate to http://localhost:8000/api-docs to view the Swagger documentation.

Import Postman Collection: Open Postman, and import the collection from /docs/Postman_Collection.json.

Contributing
Fork the Repository.

Create a Feature Branch:

bash
Copy code
git checkout -b feature/your-feature
Make Changes and Commit:

bash
Copy code
git add .
git commit -m "Add new feature"
Push Changes and Create a Pull Request:

bash
Copy code
git push origin feature/your-feature
Submit a Pull Request to the develop branch for review.

License
This project is licensed under the MIT License - see the LICENSE file for details.
