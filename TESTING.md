# Crawler Emporium - System Diagnostic & Testing Log

<figure>
    <img src="documentation/ceamiresponsive.webp" alt="Crawler Emporium shown loading on a monitor, laptop, tablet and phone">
</figure>

Testing was ongoing throughout the entire build. I utilised Chrome developer tools whilst building to pinpoint and troubleshoot any issues as I went along. The documentation below records the  manual and automated testing, accessibility compliance, and validation logs conducted across the Crawler Emporium application.

---

## 1. Validation Testing

### Code Validation (HTML, CSS, JavaScript, Python)
All source code files were run through syntax checkers to confirm structural integrity and PEP8  compliance.

* **HTML Validation:** Checked using the [W3C Markup Validation Service](https://validator.w3.org/). 
* **CSS Layout Validation:** Checked using the [W3C CSS Validation Jigsaw Service](https://jigsaw.w3.org/css-validator/).
* **JavaScript Validation:** Checked using [JSHint](https://jshint.com/).
* **Python Compliance:** Checked using the [Flake8](https://flake8.pycqa.org/en/latest/).


### HTML & Layout Templates
HTML validation was carried out by copying the URL from the live production environment for the relevant pages and running it through the [W3C Nu HTML Validator](https://validator.w3.org/#validate_by_input). One fix that was carried out across the pages was removing the `<h>` tag and replacing it with `<p>` tags. This was because the styling was being completely handled by the CSS and so the heading tags were irrelevant. 

| Pages | Link Stem | Validation Status | Screenshot Evidence |
| :--- | :--- | :---: | :--- |
| **Home Page** (Homepage) | [The Crawler Emporium](https://web-production-06923.up.railway.app/) | **PASS** | [View W3C Confirmation](documentation/html-home.webp) |
| **Loot Boxes** (Inventory Feed) | [/lootboxes/](https://web-production-06923.up.railway.app/lootboxes/) | **PASS** | [View W3C Confirmation](documentation/html-lootbox.webp) |
| **Lootbox Product detail** (Product View) | [/lootboxes/detail/](https://web-production-06923.up.railway.app/lootboxes/2) | **PASS** | [View W3C Confirmation](documentation/html-lootboxdetail.webp) |
| **Backpack** (Backpack View) | [/backpack/](https://web-production-06923.up.railway.app/backpack/) | **PASS** | [View W3C Confirmation](documentation/html-backpack.webp) |
| **Crawler Support** (Support Center) | [/support/](https://web-production-06923.up.railway.app/support/) | **PASS** | [View W3C Confirmation](documentation/html-support.webp) |
| **The Showrunners** (Showrunners Blog) | [/showrunners/](https://web-production-06923.up.railway.app/showrunners/) | **PASS** | [View W3C Confirmation](documentation/html-blog.webp) |

---

### Python (PEP8 Compliance)
[Flake8](https://flake8.pycqa.org/en/latest/) was used for checking the compliance of the .py files across the multiple app against the PEP8 guidelines. As part of this testing I utilised the `# noqa: E501` on some lines as it was not possible to split the string across multiple lines. `# noqa: F401` was also used on crawleremporium/settings.py to denote that .env was imported but not used. This has been kept in as a toggle so that I could work between the development and the production servers when developing and deploying the project. All other tests passed. Details of the files tested are below: 

| System App  | Core Files Tested | Compliance Status |
| :--- | :--- | :---: |
| **`crawleremporium`** | `settings.py`, `urls.py` | **PASS** |
| **`home`** | `apps.py`, `urls.py`,`views.py` | **PASS** |
| **`lootboxes`** | `models.py`, `urls.py` `views.py` | **PASS** |
| **`backpack`** | `contexts.py` `urls.py`, `views.py` | **PASS** |
| **`checkout`** |`admin.py`, `forms.py`, `models.py`, `signals.py`, `urls.py`, `views.py`, `webhook_handler.py`, `webhooks.py` | **PASS** |
| **`support`** | `models.py`, `views.py`, `forms.py` | **PASS** |
| **`showrunners`** | `forms.py`, `models.py`, `views.py`, `forms.py` | **PASS** |

---

### CSS Styles & Javascript Validation
* **CSS Validation:** The styling `base.css` was validated using the [W3C CSS Validation Jigsaw Service](https://jigsaw.w3.org/css-validator/). | 
        <p>
            <a href="https://jigsaw.w3.org/css-validator/check/referer">
                <img style="border:0;width:88px;height:31px"
                    src="https://jigsaw.w3.org/css-validator/images/vcss-blue"
                    alt="Valid CSS!" />
            </a>
        </p>

* **JavaScript Validation:** The system log ticker was validated using [JSHint](https://jshint.com/).

| Javascript Section | Validator | Status | Evidence|
| :--- | :--- | :---: | :--- |
| System Log Ticker | JSHint | **PASS** | [View Evidence](documentation/systemlog-jshint.webp |
| Stripe Elements| JSHint | **PASS** | [View Evidence](documentation/stripe-jshint.webp |
| Remove from Backpack| JSHint | **PASS** | [View Evidence](documentation/backpack-jshint.webp |

---

## 2. Automated Telemetry Testing



---

## 3. Manual Feature & User Story Matrix

Every core interactive element was manually validated across multiple viewports (Desktop, Tablet, Mobile) and cross-checked against our foundational UX criteria.

### User Story Verification


| I want to be able to... | So that I can... | How is this achieved? | Status |
| :--- | :--- | :--- | :---: |
| **FIRST TIME VISITORS ("CRAWLERS")** | | | |
| I want to instantly understand the sites purpose and see what items are available for purchase. | Determine if the platform fits my interests.|The home page loads with an immersive, themed layout, featuring a live system log ticker and clear Flickity product carousels displaying premium loot box assets. | **PASS** |
| I want to navigate smoothly through inventory categories and filter or sort items by price or category. | Find specific inventory items efficiently without scrolling endlessly. | A dedicated navigation bar isolates specific product categories. The master products grid features custom sorting dropdown options to sort items  by price or category name. | **PASS** |
|  I want to click into individual products to view more details and add to my cart. | Make an informed purchasing choice. | Selecting a product card loads a detailed view displaying item descriptions, and a quantity selector to add items directly to the Backpack. | **PASS** |
| I want to easily checkout and receive confirmation of my purchase without being forced to create an account. | Complete an easy, and anonymous purchase. | Guest users can bypass user authentication entirely, using the checkout route to process payments securely via fully integrated Stripe checkout cards. | **PASS** |
| **REGISTERED & RETURNING CUSTOMERS** | | | |
| I want to create an account to manage my default shipping details and view a log of my purchases.| Keep on top of my previous orders | A secure profile hub powered by Django Allauth allows authenticated users to save and modify their default address, update their password and review a  history of all past orders. | **PASS** |
|I want to add items to my cart directly from product lists or carousels, update quantities, and have them persist whilst logged in. | I don't have to keep readding items to cart unnecessarily | Authenticated accounts can add items and update quantities seamlessly across all areas of the site and across page refreshes and logouts. | **PASS** |
| I want to receive automated emails upon account registration, ticket logging and performing other account functions. | Verify that my actions have completed successfully. | The project us integrated with an Anymail HTTP API layer connecting to Brevo cloud mail servers, automatically sending confirmation emails upon registration, order creation and support ticket creation. | **PASS** |
| **SITE ADMINISTRATORS ("SHOWRUNNERS")** | | | |
|I want to securely Create, Read, Update, and Delete products and categories in the `lootboxes` app; tickets in the `support` app, and blog posts in the `showrunners` app. | Maintain full control over the system configuration | Full database CRUD capabilities are securely accessible inside the built-in Django administration platform (`/admin`), providing full control over products, tickets, and blog data. | **PASS** |
|  I want to be able to block non-administrative profiles from viewing, accessing, or tampering with products, tickets or blog posts | Guarantee system security and data isolation. | Backend route protection is managed via Django's native authentication. Any unauthenticated or standard profile attempting to access admin URLs is blocked and sentback to a secure login wall. | **PASS** |


### Device Compatibility
Manual interface passes were conducted across Chrome, Firefox, and Safari on the following display setups, where available.
* **Mobile Viewports:** Samsung Galaxy S23, Pixel 9a, iPhone 14
* **Tablet Viewports:** Kindle Fire, Samsung Galaxy Tab A9
* **Desktop Monitors:** 14-inch Laptop Screen Lenovo Yoga 7i, 21-inch monitor.

---

## 4. Bugs Tracker

This section details the bugs encountered and where possible fixed during the development cycle.

### Solved Bugs
