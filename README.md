# SalesWare

**SalesWar** is a sales process software tool. It aims to digitalize the sales activity in order to boost the productivity of your sales team.
The market entry of **SalesWare** is small businesses and startups. More specifically, those businesses that:
 - are neither content with using excel sheets to track their sales activity due to complexity and generality.
 - nor can offered the subscription fees of the established Software tools like Microsoft Dynamic or SalesForce.

**SalesWare** is built as a foundational module of a Customer Relationship Management (CRM) software. The envisioned CRM then represents the ultimate vision of this project. This vision includes other modules like MarketingWare, ServiceWare, SupportWare and DataWare. Moreover, each of those modules will integrate Data Analytics to bring additional value to our users.

**SalesWare** in its current state should not be viewed as a solution that promises all the expected features an established sales process tool or a CRM tool is assumed to have. But rather as a minimum viable product (MVP) with the main purpose of getting the Author at the door step of potential buyers. Through their feedbacks and unique sales process, **SalesWare** can be further developed to evolve into much more sophisticated sales tool.

![Main View](docs/introduction/amIresponsive.PNG)

## 1 Introduction

SalesWare is developed to help sales team to digitalize their sales process and track opportunities progress. In this introduction, the user will find all the required information to start working with the SalesWare.

In this section, we provide you with all the information required to use our solution, SalesWare. First we define the important terms and then provide a complete user manual which will help you start working with SalesWare.

### 1.1 Getting Started

Before embarking on how to use the tool, SalesWare user must be acquainted with few terms. These terms are organization, admin, user, prospect, product and opportunity.

#### Organization:
An organization is an owner of SalesWare license. This organization consists of multiple departments. The ultimate user of the SalesWare within this organization is the Sales Department team members.

#### Admin:
The admin is a member of the organization Sales department. The admin has unlimited user permissions over the SalesWare application. To add some colors, the admin is the Head of Sales Department, or any other title that is responsible for the sales team of that organization.

#### User:
A user is a member of the organization sales department with limited user permission. Most likely, the user is a sales manager, business developer etc.

#### Prospect:
A prospect is an external firm that is interested in one or more of the organization offerings.

#### Product:
A product is one of the organization offerings. It can be either a product or a service.

#### Opportunity:
An opportunity is a chance of selling the defined product to the defined prospect.

Since the main terms now are established, we can provide some detail about the software main components. In the current version, SalesWare comes with four main components. These are:

- **Prospect Management:**\
  The prospect management concerns with the listing/reading/creating/updating/deleting a prospect record.
- **Product Management;**\
  The prospect management concerns with the listing/reading/creating/updating/deleting a product record. 
- **Opportunity Management:**\
  The Opportunity Management concerns with the listing/reading/creating/updating/deleting an opportunity record.  
- **Communication Management:**\
  This Communication Management provides a communication means between SalesWare and its customer/users. 

  More information on each of the four component is provided in the next section. We will also explain how these terms and components are implemented and used to track your sales deals in addition to how to sign up, sing in and sign out of SalesWare.

### 1.2 SalesWare User Manual

The SalesWare User Manual is available on the following link: [User Manual](MANUAL.md)

## 2 Planing

### 2.1 Project Objective

This section is devoted to explain the rational behind developing SalesWare. It aims to answer the following questions:

Why SalesWare?
What drives the author to develop SalesWare?
Why the user should care about using SalesWare?

Sales activity is one of the main activities of any businesses. It produces important metrics of any organization. Senior-level executives use those metrics to analyze and evaluate the firm's health, competitions, product demands etc.. In addition, sales forecast drives most of the firm's future plans that touch upon every aspect of a business.

Having a sales software that collects, stores and present such data like, customers' data, firm's offerings, opportunities tracking, historical sales data, customer acquisition metrics and sales pipeline is , therefore, of a great help to the firm decision makers.

The Software As A Service (SAAS) has taped into this need. We witnessed in the last couple of decades an explode in the number of Sales tools and CRM systems. Yet, there is still a nontrivial number of organizations, small businesses and startups, use excel sheets or similar products to track and record their sales activity. This is due to the fact that the license cost of the sophisticated SAAS solutions are quite high making it a burden on those small businesses to acquire.

On the other hand, tools like excel sheets are not designed to serve sales people. They are built for general purposes, hence they are not easy to use. Furthermore, the customization of such tools comes with high cost. In addition, any change to the firm sales activity in terms of process, business rules or metrics will lead to massive adaptation cost.

All that led the author to consider developing a sales tool that can support those businesses by providing an affordable sales activity-tailored solution.

### 2.2 Design Concept

The design concept of SalesWare is based on the general Reference Model used to develop an information system. This reference model is widely used in the enterprise architecture design. The adopted Reference Model core layers are Process, Data and application layers. The other two layers are the strategy and the infrastructure. The former is briefly explained in the previous section. It involves the strategic rational behind developing and/or integrating an enterprise solution to the business operation. The latter layer is the infrastructure layer. It is concerned with the infrastructure required to build and integrate the information system (solution). This layer is out of this project scope.

The following subsections aim to provide a detailed account of the main three layers mentioned above to shed some light on how the solution is designed.

#### 2.2.1 Process

The process layer covers the procedure of a specific activity within a firm's value chain. It is the corner stone of developing any enterprise information system solution. Hence, the author first has devised a generic sales process. This process is devised to help the development of the MVP. **SalesWare** *can be adapted to assume any other sales process upon a request from the user*.

The devised sales process is shown in the figure below.

![process](docs/design_concept/process.png)

By establishing the process, the main entities and business rules can easily be extracted. Those entities and business rules are essential to design the data model, the logic to be implemented into the code and also to extract the general requirements of the application. For instance, one can observe that there are four entities that are essential to this business scenario. These are Prospect, Product and Opportunity. In addition, one can notice, that the process goes into different stages these are Lead, Proposal, Negotiation and finally Close. The process is said to be Closed if it is a Won or Lost. Such information are crucial to the development of the logical data model which is the subject of the next subsection.

#### 2.2.2 Data

This section is devoted to present the data model of SalesWare. The Data Model is built to reflect the business process described in the Process subsection. The data model implemented is depicted in the figure below.

![Data Model](docs/design_concept/data.png)

#### 2.2.3 Application

The application layer is the last layer of the reference model. In the context of this project, the author first extracts only a list of high-level requirements of the application based on the outcomes of the process and data layers. Then the author uses this list as the basis for creating the Epics and breaks down those Epics into a comprehensive list of user stories. The list of the high-level requirements are listed below .

- Account Management Capability\
  Sign in, sing out and sign up, admin user with unlimited permissions, users with limited permissions, 
- Prospect Management Capability\
  read/create/update/delete of prospects
- Product Management Capability\
  read/create/update/delete of product
- Opportunity Management Capability\
  read/create/update/delete of opportunity
- Communication Management Capability\
  Means of communication between user/visitor and the software developer

##### 2.2.3.1 Epics and User Stories

Agile methodology is used to develop the Software. The high-level requirements presented in the previous section are followed to define the five Epics of the project. Those Epics are then broke down into 32 User Stories.

**Epic SW-1 Account Management**\
*Description:* A set of features that allows the site visitor to create user accounts and for the user to access and use the application features. Additionally, this part also concerns with dedicated features for the admin account.

  - **Register a User account**
    - As a Site Visitor, I can register as User so that I can log in securely into the website.
  - **Store login information**
    - As a Site User, I can store my login information securely so that I can logout and login again into the website.
  - **Admin User Account**
    - As a Site Admin, I can see all the Users so that I can control who has access to the software.
  
**Epic SW-2 Prospect Management**\
*Description:* A set of features that allows the users to manage prospects entry.

  - **Create Prospect Entry**
    - As a Site User, I can create a new Prospect so that I can save it in the database.
  - **Open and Read Prospect Entry**
    - As a Site User, I can click on a Prospect name so that I can open and read its information.
  - **Edit Prospect Entry**
    - As a Site User, I can edit the Prospect information so that I can save any updated information about the prospect.
  - **Delete Prospect Entry**
    - As a Site User, I can delete the Prospect so that I can remove it from the database.
  - **Prospect Name Case Sensitive**
    - As a User, I can always save the prospect name in upper case in DB, so that I can not accidentally duplicate the name if I entered it as a whole or partially in lower case.
  - **Prospect Page**
    - As a Site User, I can view all the prospect in a dedicated page so that I can view all the prospects in an excel sheet-like display.

**Epic SW-3 Product Management**\
*Description:* A set of features that allows the users to manage product entry.

  - **Products Page**
    - As a Site User, I can view all the products in a dedicated page so that I can view all the products in an excel sheet-like display.
  - **Create Product Entry**
    - As a Site User, I can create a new Product so that I can save it in the database.
  - **Open and Read Product**
    - As a Site User, I can click on the Product name so that I can open and read its information.  
  - **Edit Product Entry**
    - As a Site User, I can edit the product information so that I can save any updated information about the product.
  - **Delete Product Entry**
    - As a Site User, I can delete the product so that I can remove it from the database.
  - **Product Name Case Sensitive**
    - As a User, I can always save the product name in upper case in DB, so that I can not accidentally duplicate the name if I entered it as a whole or partially in lower case.
    
**Epic SW-4 Opportunity Management**\
*Description:* A set of features that allows the user to manage the sales cycle of a specific product according to the defined sales process and displays this cycle in a specialized dashboard

  - **Opportunities Page**
    - As A Site User, I can open the opportunity page, so that I can see the list of all the opportunities I have created.
  - **Create Opportunity Entry**
    - As a Site User, I can create new opportunity so that I can save it in the database.
  - **Open and Read Opportunity**
    - As a Site User, I can click on the opportunity to open it so that I can read its information.  
  - **Edit Opportunity Entry**
    - As a Site User, I can update the opportunity so that I can save any updates of that opportunity.
  - **Delete Opportunity Entry**
    - As a Site User, I can delete the opportunity so that I can remove it from the database.
  - **Opportunity Name Case Sensitive**
    - As a User, I can always save the opportunity name in upper case in DB, so that I cannot accidentally duplicate the name if I entered it as a whole or partially in lower case.
  - **Return to Opportunity list**
    - As a User, I can automatically return to the opportunity list page after creating/editing/deleting an opportunity record, so I can see the updated list after my action.  
  - **Opportunity Back Button links to Opportunity List Page**
    - As a User, I can click on a back button on the opportunity detail/create pages, so I can go back to the opportunity list page.
  - **Opportunity Record Control**
    - As a User, I cannot edit or delete Opportunity Record that i do not own unless I am the admin, so that I can ensure that I have a full control about the data that I create.

**Epic SW-6 Communication Management**\
*Description:* A set of feature to enable the user to communicate with SalesWare team

  - **Home Page**
    - As a Site Visitor, I can find an engaging and purposefully designed landing page so that I can feel appealed to create an account and use the application
  - **Contact Page**
    - As a Site Visitor or User, I can Contact the Website Developer so that I can get more information or purchase a customized version of the application
  - **Email Received**
    - As a Site Visitor or User, I can receive email message so that I can be sure that message to the site owner is received.
  - **Confirmation Modal Message**
    - As a Site Visitor or User, I can see a confirmation message that my message is sent once I sent the contact form so that I can know that i filled out the contact form correctly.
  - **Contact Form Received**
    - As a Site Owner, I can receive an email if a user sent a contact form, so that I can read what the user inquiry is.
  - **Sign-Up or Sign-In Errors Related Messages**
    - As a Site Visitor or User, I can see Sign-Up or Sign-In related errors with red color style, so I can distinguish them quickly from the rest of the text in the Sign-Up or Sign-In pages.
  - **Link to Contact Page**
    - As A User or Site Visitor, I can reach the contact page from the home page, so that I got directly to the contact page
  - **Active Page** 
    - As a Site Visitor or User, I can see the page I am in using a signifier, so that I can always know what page I am at.
  
Further detail on the Agile Methodology followed in this project is provided in the execution section.

> **Note:** There is a discrepancy in the Epics numberings. Where Epic 5 is missing. This is due to the fact that Jira keeps the numbering continue even if an epic is deleted. The author deleted Epic 5 as this Epic is shifted to be part of the future work. The author touches upon this point in the section of Future Work.
>  

### 2.3 Wireframes

The Wireframes design concept is structured in a way that reflects the sequence of the Epics presented in the Application requirements section. For example, Account Management consists of the pages that is responsible for Sign Up, Sign In and Sign Out and so on for the rest of the epics and their respective pages. The Wireframes designs presented in this section cover both PC and Mobile screen view scenarios.

#### 2.3.1 Account Management

![Sign in/up/out Management](docs/wireframes/sign_in_out_up.png)

#### 2.3.2 Prospect Management

![Prospect Management](docs/wireframes/prospect.png)

#### 2.3.3 Product Management

![Product Management](docs/wireframes/product.png)

#### 2.3.4 Opportunity Management

![Opportunity Management](docs/wireframes/opportunity.png)

#### 2.3.5 Communication Management

![Communication Management](docs/wireframes/communication.png)

### 2.4 Color

The following color pallette is used for building up the website text, line breaks, buttons background the general background colors.

![Color Pallet](docs/colors/color_palette.PNG)

The following table explains the usage of those colors.

| Color Code | Usage | Usage |
| ----------- | ----------- | ----------- |
| #ffffff: White | Buttons text, text over #0e253f |  |
| #6c757d: Slate-gray | Close or Cancel background buttons, background color of select options elements | Bootstrap Secondary Background Color|
| #198754: Sea-green | Update background button | Bootstrap Success Background Color  |
| #dc3545: Rusty-red | Delete and Confirm buttons, Account Management error messages | Bootstrap Danger Background Color |
| #213e60: Indigo-dye | Text over #ffffff Background | SalesWare Brand Text Color |
| #0e253f: Oxford-blue | General background color, "Send" and "+" buttons  | SalesWare Brand Background Color |

The contrast evaluation of the selected colors is provided in the figure below.

![Contrast Grid](docs/colors/contrast_grid.PNG)


### 2.5 Typography

No specific font is used for this project. The author decides to implement the default font.

## 3 Execution

The sections explains the execution activity. The section begins with the Technologies used to develop SalesWare. It also provides a summary about the agile methodology implemented with brief summary about the project management performance evaluation. Another subsection is devoted to list all SalesWare features followed by a comprehensive testing documentation. A separate subsection is dedicated to discuss the bugs and a brief discussion on the public API of EmailJS service. The section then concludes with subsection dedicated for the deployment procedure.

### 3.1 Technologies Used

a List of the technologies and tools used to develop this project is provided below:

| Technology | Description | 
| ----------- | ----------- |
| HTML | Hypertext Markup Language |
| CSS | Style Sheet Language |
| JavaScript | Programming Language |
| Python | Programming Language |
| Bootstrap | Frontend toolkit |
| jQuery | JavaScript library |
| Django | Python web framework |
| CI Database | Code Institute Postgres Database |
| EmailJS | Sending Email from Code Service |
| GitHub | Development Platform |
| Gitpod | Cloud Development Environment |
| Heroku | Development Platform |
| Chrome DevTools | Web developer toolkit |
| Jira | Project Management Tool |
| Wave Evaluation Tool | Accessibility evaluation tool |
| CI Python Linter | Code Institute Python code style convention checker |
| JShint | Static code JavaScript code analysis tool |
| W3C Markup Validation Service | HTML Validator |
| W3C CSS Validation Service | CSS Validator | 

### 3.2 Agile Development

The philosophy adopted to develop SalesWare follows the Agile methodology. The project is broke down into five Epics. Each epic is further broke down into user stories. The backlog is then created. It consists of five Epics which contains 32 User Stories, please refer to [Epics and User Stories subsection](README.md#2231-epics-and-user-stories) to review the complete list of the stories. 

The work is then executed in iterations. Each iteration (Sprint) is set to span two weeks except the third sprint. The third sprint is extended by 6 days to add additional features where not first included into the backlog. The entire development consumed seven weeks excluding documentation. The project development commencement on 21.07.2024 which is the date of starting the first sprint. Due to summer break, the second sprint started on 19.08.2024. The third sprint is then followed and ends on 22.09.2024. The figure below shows Jira project timeline.

![TimeLine](docs/agile_development/development_timeline.png)

Epics' user stories are distributed over the sprints according to the User Story priority. The user stories distribution over each sprint is summarized in Jira-export excel sheet.

![Sprint Distribution](docs/agile_development/sprints_distribution.png)
 
The development velocity is increased during the second sprint and significantly in the third sprint. There are technical and management reasons for that. With respect to the technicality, two main issues are considered to be the cause. On one hand, the learning curve possessed a low slop due to the structural complexity of Django project. In particular, the phase of creating the project with its first two Apps were a bit of challenge with respect to connecting the main components of the project together, namely: urls, views, templates and how to correctly pass the information from one to the other. On the other hand, the difficulty that comes with implementing Bootstrap and making the templates content responsive.

The management difficulty is related to the author undertaking of two roles at the same time. On other words, being the developer and the product owner simultaneously. Being more focused on getting the code working has left some user stories defined in the first two sprints to be quite general with less adequate granularity than what it needs to be. The reader could observe this by comparing the quality of the user stories descriptions of the third sprint and those of the first two sprints.

In the third sprint, the author becomes technically more comfortable. Consequently, this is translated into a better management style and quality. This two dimensional improvement (Technical and management) resulted into the inclusion of additional user stories to the third sprint. The reader might expect this should be obvious, considering that the third sprint is **40%** longer than a two-week sprint. Which is quite true, the additional time certainly contributed. But in the same time, the reader can see from the figure below that in the third sprint alone, the author got **60%** of the user stories done with significantly better user story scop granularity definition. Please review the [user stories](/README.md#2231-epics-and-user-stories) again for description quality comparison. 

![Velocity Report](docs/agile_development/velocity_report.PNG)

### 5.2. Features

#### 5.2.1 Communication App

Describe home and contact pages of the website.

#### 5.2.2 Prospect App

Detail the prospect page of the website.

#### 5.2.3 Product App

Describe product page of the website.

#### 5.2.3 Opportunity App

Describe opportunity page of the website.

#### 5.2.4 Login, logout and sign up pages

Describe Login, logout and sign up pages of the website.

### 5.3 Test

#### 5.3.1 Javascript Code Quality Test

Describe the verification tests conducted.

#### 5.3.2 Python Code Quality Test

List the validation tests and their outcomes.

#### 5.3.3 HTML Validation

Explain the process and results of HTML validation.

#### 5.3.4 CSS Validation

Detail CSS validation process and results.

#### 5.3.5 Accessibility

Describe how accessibility was ensured.

#### 5.3.6 Lighthouse Validation

Provide details and results of Lighthouse validation.

#### 5.3.7 Device Testing

Explain how device testing was conducted and the results.

#### 5.3.8 Browser Compatibility

Detail the browser compatibility checks that were performed.

#### 5.3.9 Manual Tests

#### 5.3.10 Unit Tests

### 5.3.11 Bugs

#### 5.3.12 Fixed Bugs

List the bugs that were identified and fixed.

#### 5.3.13 Unfixed Bugs

Mention any bugs that have not yet been fixed.

## 6 Deployment

Explain how the website is deployed and any steps needed to deploy it to a new environment.

### 6.1 Github Setup

### Heroku Setup

## 7 Future Work

Explain the future work

## 8 Credits

### 8.1 References

List any references used in the development of the project.

### 8.2 Content

Credit the sources of website content.

### 8.3 Tools

List the tools used in the project.

## 9 Acknowledgements

I would like to express my sincere gratitude to Mr. David Bowers for his outstanding mentorship. His follow up, the provision of additional time to answer questions are extraordinary. He always is available to offer the help in finding solutions and sharing his recommendations on further readings on a variety of related topic. Those spectacular traits of Mr. Bowers comes only second to his genuine passion of helping others to succeed. The PP4 is my last project under his mentorship, I truly hope that we cross paths again in the near future. 
Finally, I would also like to thank my family for helping me by providing the continuous encouragement and with the valuable help with the manual testing.
