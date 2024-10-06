**Tests Captures**

# Lighthouse Tests Captures

## Lighthouse Desktop

### Communication Management

**Home Page**

![Home Page Desktop ](docs/tests/home_lighthouse_lg.png)

**Contact Page**

![Contact Page Desktop](docs/tests/contact_lighthouse_lg.png)

### Prospect Management 

**Prospect Page**

![Prospect Page Desktop](docs/tests/prospect_lighthouse_lg.png)

### Prospect Management

**Product Page**

![Product Page Desktop](docs/tests/product_lighthouse_lg.png)

### Opportunity Management 

**Opportunity List Page**

![Opportunity List Page Desktop](docs/tests/opportunity_lighthouse_lg.png)

**Opportunity Create Page**

![Opportunity Create Page Desktop](docs/tests/opportunity_lighthouse_create_lg.png)

**Opportunity Detail Page**

![Opportunity Detail Page Desktop](docs/tests/opportunity_lighthouse_detail_lg.png)

### Account Management

**Sign Up Page**

![Sign Up Page Desktop](docs/tests/signup_lighthouse_lg.png)

**Sign In Page**

![Sign In Page Desktop](docs/tests/signin_lighthouse_lg.png)

**Sign Out Page**

![Sign Out Page Desktop](docs/tests/signout_lighthouse_lg.png)


## Lighthouse Mobile

### Communication Management

**Home Page**

![Home Page Mobile ](docs/tests/home_lighthouse_sm.png)

**Contact Page**

![Contact Page Mobile](docs/tests/contact_lighthouse_sm.png)

### Prospect Management 

**Prospect Page**

![Prospect Page Mobile](docs/tests/prospect_lighthouse_sm.png)

### Prospect Management

**Product Page**

![Product Page Mobile](docs/tests/product_lighthouse_sm.png)

### Opportunity Management 

**Opportunity List Page**

![Opportunity List Page Mobile](docs/tests/opportunity_lighthouse_sm.png)

**Opportunity Create Page**

![Opportunity Create Page Mobile](docs/tests/opportunity_lighthouse_create_sm.png)

**Opportunity Detail Page**

![Opportunity Detail Page Mobile](docs/tests/opportunity_lighthouse_detail_sm.png)

### Account Management

**Sign Up Page**

![Sign Up Page Mobile](docs/tests/signup_lighthouse_sm.png)

**Sign In Page**

![Sign In Page Mobile](docs/tests/signin_lighthouse_sm.png)

**Sign Out Page**

![Sign Out Page Mobile](docs/tests/signout_lighthouse_sm.png)

# Wave Accessibility Tool

The first tests conducted by using the Wave tool show on every page an alert. The screenshot of the alert is shown below.

![Wave Tool Report With Alert](docs/tests/wave_every_page.png)

The alert reference is provided in the screenshot below.

![Wave Tool Alert Reference](docs/tests/wave_alert_explanation.png)

The author added **#** after the home page url. This seems to be an effective solution. The alert is cleared from all the pages. See the screenshot below.

> Note: The solution to the Redundant Link Alert  is found by looking at other CI student projects. Then the author tested those projects with Wave tool. Some projects do not produce such alert. In one of those projects, namely: [TaskFlow](https://github.com/leonp84/code-institute-project-4?tab=readme-ov-file), the author noticed that the developer of TaskFlow added **#** at the end of the home page url. The author put this # into the home page url and then tested the page again with Wave tool. The author found out that this action resolves the issue.

![Wave Tool Report Alert Free](docs/tests/wave_every_page_alert_error_free.png)

In addition to Redundant Link Alert, the opportunity create page had two additional alerts both with the same reference. The report is provided below.

![Wave Tool Opportunity Create Page Report](docs/tests/wave_opportunity_create.png)

The additional Alerts reference is shown below.

![Wave Tool Alert Reference of Opportunity Create Page](docs/tests/wave_opportunity_create_alert_explanation.png)

The author resolves the issue by removing the automatically invoked title attribute of **jQuery select2** using Javascript in opportunity.js file. The result of the test is shown below. Notice that the three alerts are removed now. The first one by using the earlier explained approach, that is of using **#** on the page url. The other two alerts by using JavaScript remove attribute.

![Wave Tool Alert Reference of Opportunity Create Page Alert and Error Free](docs/tests/wave_every_page_alert_error_free.png)


# HTML Validation Selected Test Screenshot

The first test of the Sign Up page using HTML returns the following errors.

![Sign Up Page HTML Validator Result](docs/tests/signup_page_html_validator.png)

As the reader can see the errors are related to a code that comes with django-alluath package. The author extracted the code using the "view source code ". The code is then analyzed by extracting the defected code to see if one can identify any issue. The code is provided below.

```
                                <p>
                                    <label for="id_password1">Password:</label>
                                    <input type="password" name="password1" placeholder="Password"
                                        autocomplete="new-password" required aria-describedby="id_password1_helptext"
                                        id="id_password1">
                                    <span class="helptext" id="id_password1_helptext">
                                        <ul>
                                            <li>Your password can’t be too similar to your other personal information.
                                            </li>
                                            <li>Your password must contain at least 8 characters.</li>
                                            <li>Your password can’t be a commonly used password.</li>
                                            <li>Your password can’t be entirely numeric.</li>
                                        </ul>
                                    </span>
                                </p> 

```

The author could not identify a clear source for the errors in the above code. However, when the the author removed the defected code from the entire source code and then pasted the cleaned code again into the HTML validator, all errors disappear.

Seeking the remove of this error, multiple approaches are evaluated. The use of crispy forms, however, proves to be helpful. The result of the validation shows no errors after implementing crispy form. A screenshot of the html validator after implementing the crispy form is provided below.

![Sign Up Page HTML Validator Result Error Free ](docs/tests/signup_page_html_validator_error_free.png)

---
[Go Back](README.md)