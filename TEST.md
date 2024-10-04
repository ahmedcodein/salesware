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

The Wave tool shows on every page an alert. The screenshot of the alert is shown below.

![Wave Tool Report](docs/tests/wave_every_page.png)

The alert reference is provided in the screenshot below.

![Wave Tool Alert Reference](docs/tests/wave_alert_explanation.png)

In addition to Redundant Link Alert, the opportunity create page has two additional alert with the same reference. The report is provided below.

![Wave Tool Opportunity Create Page Report](docs/tests/wave_opportunity_create.png)

The additional Alerts has the following explanation.

![Wave Tool Alert Reference of Opportunity Create Page](docs/tests/wave_opportunity_create_alert_explanation.png)

# HTML Validation Selected Test Screenshot

The test of the Sign Up page using HTML returns the following errors.

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

The author could not identify a clear indication of an error in the above code. However, when the the author removed removed the defected code from the entire source code then pasted the cleaned code again into the HTML validator, all errors disappear.

---
[Go Back](README.md)