<h1 align="center"> The-Hot-Hatch-Club </h1>
![Hero Image](Readme_files/Hero_image/default.jpg)

<h2>Table Of Contents</h2>

1.  [Introduction](#Introduction)
2.  [UX Design](#UX-Design)
     - [User Stories](#User-Stories)
     - [Colour Pallet](#Colour-Pallet)
     - [Fonts](#Fonts)
3.  [WireFrames](#WireFrames)
4.  [ERD](#ERD)
5.  [Deployment](#Deployment)
6.  [Features](#Features)
7.  [Tech Stack](#Tech-Stack)
8.  [Agile Design](#Agiles-Design)
9.  [Testing](#Testing)
10. [AI Usage](#AI-Usage)
11. [Credits](#Credits)


<h2 align="center">Introduction</h2>

**Hot Hatch Club** is a community-focused web application built with Django, designed for performance car enthusiasts to share and celebrate their favorite hot hatches. Users can register, log in, and create detailed posts about their vehicles, including make, engine size, horsepower, and year. Each post is displayed in a clean, responsive layout that ensures a smooth experience across devices.<br>
The application features robust user authentication and role-based permissions. Authors can manage their own content, while administrators oversee post approvals to maintain quality and consistency. Approved posts are clearly separated from pending submissions, creating a trustworthy and well-organized platform.<br>
Built as a Django capstone project, Hot Hatch Club showcases key web development skills including CRUD functionality, user management, responsive design, and deployment to Heroku. It reflects a passion for both technical precision and community-building—bringing car lovers together through shared stories and specs.



<h2>UX Design</h2>
<h3>User Stories<h3>

<h4>Must Haves</h4>
As a **visitor** I can **register** so that **I can post about my vehicle**.

*Acceptance Criteria*

- A registration form collects username and password securely

- Registered users can access protected content

- Registration page opens


As a **post author** I can **edit my posts** so that **can keep my content accurate and up to date.**

*Acceptance Criteria*

- The Edit button is visible only to the post author.

- Unauthorized users cannot access edit views.

- Updates reflect on both the post detail and homepage. 


As a **admin** I can **approve user posts** so that **the site content stays appropriate and moderated.**

*Acceptance Criteria*

- Admin role is assigned using Django’s is_staff attribute

- Admins have access to post approval toggle

- Only approved posts are displayed on the homepage


As a **visitor** I can **log in & out** so that **I can edit my posts & comments.**

*Acceptance Criteria*

- Log in screen opens

- Login and logout functionality works across all pages

- Registered users can access protected content


As a **post author** I can **delete my posts** so that **can keep my content accurate and up to date.**

*Acceptance Criteria*

- Delete button is visible only to the post author

- Unauthorized users cannot access delete posts

- Updates reflect on the post detail and homepage


As a **logged user** I can **create a post about my hot hatch** so that **others can view my car details.**

*Acceptance Criteria*

- Post form includes: Make, Engine Size, BHP, Year, Comments,
- Posts are linked to the logged-in user
- Posts require admin approval before public display


As a **visitor** I can **click on a post for full details** so that **I can learn more about the vehicle.**

*Acceptance Criteria*

- Each post has a dedicated detail page

- Image (if uploaded) is displayed at the top

- Vehicle details and user comments are shown clearly


<h4>Should Haves</h4>
As a **post author** I can **upload photos** so that **I can show off my vehicle**

*Acceptance Criteria*

- Photo upload is optional during post creation

- Uploaded images are stored securely using Cloudinary

- If a photo is uploaded, it displays at the top of the post detail page


As a **logged in user** I can **add comments to a post** so that **I can share feedback or start a conversation with other club members.**

*Acceptance Criteria*

- Comment form appears below the post detail view for authenticated users

- Submitted comments are saved and displayed with author and timestamp

- Comment section updates dynamically or on page reload to include new messages


<h4>Could Haves</h4>
As a **club member** I can **view upcoming organised events** so that **I can plan to attend and engage with the Hot Hatch community.**

*Acceptance Criteria*

- Events are listed with key details: title, date, location, and description

- Only approved events are shown to all users

- Events display on a dedicated page or section accessible from the main navigation

<h3>Colour Pallet</h3>
[View Colour Pallet](./Readme_files/Colour_pallet/The_Hot_Hatch1_Club.png)

<h3>Wireframes</h3>
[View Wireframes](./Readme_files/Wireframes/The_Hot_Hatch_Club.bmpr)

<h2>ERD</h2>

<h2>Deployment</h2>
Deployment was done in several stages.
Github and VS code
Stage 1 – Created a repo on Github and cloned the repository into VS code.
Stage 2 – Set up eny.py files & created gitignore.
Stage 3 – Installed gunicorn & added it to requirements.txt 
Stage 4 – Created and updated Procfile
Stage 5 – Ensured all secret data is in the gitignore file
##Heroku
Stage 6 – Created an app on Heroku and connected it to Github
Stage 7 – Disabled Collectstatic and added secret_key on Heroku convig vars
Stage 8 – Ensured it is set to EcoDyno
Stage 9 – Connect to Github
Stage 10 – Deploy on Heroku and view app to confirm deployment

<h2>Features</h2>

- Home page,
- Post page
- Login page
- Nav bar
- Footer
- Signup page & sign in page
- Admin page from Heroku
- Post detail page

<h2>Tech Stack</h2>

- Django (Python)
- HTML, CSS, Bootstrap 
- Heroku (deployment)
- Git & GitHub (version control)


<h2>Agile Design</h2>

To stay on track with the Agile framework and make sure I delivered a solid Minimum Viable Product (MVP), I used a Kanban board along with the MoSCoW prioritization method. This helped me organize tasks by importance—focusing on what must be done first, while keeping less critical features for later. Using these tools made it easier to manage progress, avoid delays, and stay focused on the key features needed for the MVP. It also gave me flexibility to adjust as the project developed

<h2>Testing</h2>

<h2>AI Usage</h2>

AI tools were used throughout the development process to enhance efficiency, accuracy, and decision-making. GitHub Copilot and inline chat supported code creation by completing repetitive structures and suggesting relevant snippets, allowing me to focus on core logic. Inline chat also played a key role in debugging, helping identify and resolve issues quickly while deepening my understanding of the codebase.
For testing and optimisation, I used tools like Lighthouse to assess performance and accessibility, and W3Schools AI assistant to clarify HTML, CSS, and JavaScript behavior during frontend refinement. These tools provided actionable insights that improved both user experience and code quality. Copilot also generated Django unit tests for key features, which I reviewed and adjusted to ensure meaningful coverage and logical accuracy.
Overall, AI tools significantly improved my workflow by reducing manual effort, accelerating problem-solving, and supporting better design decisions. I plan to continue using them during final testing and will expand this reflection as further refinements are made.

<h2>Credits</h2>