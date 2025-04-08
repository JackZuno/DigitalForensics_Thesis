## GoPhish
### What is it?
GoPhish is a powerful, open-source phishing framework that makes it easy to test your organization's exposure to phishing. \
Gophish makes it easy to create or import pixel-perfect phishing templates in order to recreate realistic emails and websites. \
The way GoPhish works is quite straightforward. Once set up, it enables users to create and manage phishing campaigns from a centralized interface. The tool comes with a built-in editor, allowing administrators to craft emails that mimic real-world phishing tactics. These emails can be customized to appear as legitimate as possible, closely resembling the kinds of messages that employees might receive from known services, colleagues, or clients. \
After the emails are sent out, GoPhish tracks how recipients interact with them. It can monitor whether users open the emails, click on embedded links, or even enter sensitive information into fake login pages. This tracking capability provides valuable insights into how many employees were tricked by the phishing attempt, highlighting potential vulnerabilities in the organization's security culture. 

### How to Create and Launch a GoPhish Campaign

#### Sending Profile
The first essential task is to configure a **sending profile**, which is basically the SMTP server details that GoPhish will use to send out phishing emails. You'll need to enter information such as the server address, authentication credentials, and the email address that will appear as the sender. Setting this up correctly is crucial, as any issues here could prevent your emails from reaching the intended targets. \
To see how I create the sending profile look here: **[sending profile](gophish/sending_profile.md)**.

#### Landing Page
The **landing page** is where recipients will be directed if they click on a link in the phishing email. The landing page can be a cloned version of a legitimate website's login page or any other form that tricks users into entering sensitive information. GoPhish allows you to either import an HTML file or create a page using its editor, making it easier to customize the look and functionality of the page to suit your needs. \
If you want to capture the *submitted data* in the page, you must select the checkbox at the bottom of the landing page form creation (to capture the password there in another checkbox to select). \
It is also possible to redirect the victims to another website right after the insert the credentials, and this can be done by inserting the website link in the *Redirect To* field. \
To see how I create the landing page look here: **[landing page](gophish/landing_page.md)**.

#### Email Template
The **email template** will be used in the phishing campaign. GoPhish provides an editor where you can craft a message that resembles a legitimate email. For instance, you might design an email that looks like a security alert from a popular service, or a routine request from within the organization. The key is to make it as convincing as possible, using logos, layout styles, and even personalizing the message with variables like the recipient's name. \
A common phishing tactic is to include a hyperlink that directs the user to a malicious website. In GoPhish, you can embed links using anchor text, such as “Click here to update your account” or “Verify your identity.” \
To see how I create the email template look here: **[email template](gophish/email_templates.md)**.

#### Users & Groups
After setting up the email and landing page, you need to define your target audience. This involves creating a group of recipients by adding their names and email addresses. You can do this manually, or if you have a larger list, import it via a CSV file. Defining your target audience carefully ensures that the campaign reaches the right people and gives you accurate data on how different groups respond to the phishing attempt. \
To see an example of a group look here: **[users and groups](gophish/users_and_groups.md)**.

#### Campaigns
With all the components in place, you’re now ready to launch the **campaign**. You’ll give your campaign a name, choose the templates and landing pages you’ve created, and set the SMTP profile. You can also schedule the emails to be sent out immediately or at a specific time. Once launched, GoPhish begins sending the phishing emails to the recipients, tracking how they interact with them in real time. \
The moment your campaign is live, the dashboard will start displaying data on user interactions. You’ll be able to see who opened the email, who clicked on the link, and who submitted any information on the landing page (and if selected the option it will also show the data). This real-time monitoring is essential for understanding the effectiveness of your campaign and gauging how well-prepared your targets are against phishing threats. When the campaign concludes, GoPhish will generate a detailed report summarizing all these interactions. This report will help you analyze the results and determine which areas of your organization might need more training or better security measures. \
To see how I set up a gophish campaign look here: **[campaign](campaign/campaign.md)**.

### Get Scammed
### Victims
- Sarah Williams: Computer1
- John Doe: Computer2
- Emily Carter: Computer3
- James Foster: Computer4
- Sam Pointer: PC1

### Get Scammed Script
To make the scam more easier and automatic on my side, I made a script that looks for an email with a specific subject and in case it found it, it opens the email and looks for a link.\
After it found the email it clicks on the link and, if the victim gets scammed insert its credentials, if not it does nothing.
