# Milestone 4: Full Stack Frameworks with Django - Crawler Emporium

<figure>
    <img src="documentation/ceamiresponsive.webp" alt="Crawler Emporium shown loading on a monitor, laptop, tablet and phone">
</figure>

## Crawler Emporium

### Project Overview & Context

This full-stack web application is an immersive, e-commerce site built for Milestone 4 of the Code Institute Level 5 Diploma in Web Application Development. Inspired by the "Dungeon Crawler Carl" universe, the platform operates as a loot shop that users, known as crawlers, can browse unique loot boxs, view their cart (backpack), and securely process transactions using Stripe to checkout. The site also features a Support area where users can submit tickets and read through FAQs and finally a Showrunners blog where key showrunners can post blogs and logged in users can leave comments. 

**View the deployed project here:** [The Crawler Emporium](https://web-production-06923.up.railway.app/)

![Github Last Commit](https://img.shields.io/github/last-commit/MrsG33k/CI-MS4-CrawlerEmporium)
![Github language count](https://img.shields.io/github/languages/count/MrsG33k/CI-MS4-CrawlerEmporium)

---

## CONTENTS
* [User Experience (UX)](#user-experience-ux)
  * [User Stories](#user-stories)
* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)
* [Features](#features)
  * [Core Application Features](#core-application-features)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)
* [Database Schema & Architecture](#database-schema--architecture)
* [Technologies Used](#technologies-used)
* [Deployment & Local Development](#deployment--local-development)
* [Testing](#testing)
* [Credits & Acknowledgments](#credits--acknowledgments)

---

## User Experience (UX)

### Target Audience & Theme
Unlike a standard e-commerce site, **Crawler Emporium** is a fan tribute application designed for enthusiasts of the 'Dungeon Crawler Carl' book franchise. 
To immerse the user in the universe and engage them fully, the platform is designed to operate 'in-universe'. The primary intended audience are known as "crawlers" who are navigating a dangerous, gamified survival environment. Crawler Emporium is a place for them to buy lootboxes to level up their stats. 

Because the platform acts to simulate what a crawler would see in the books, some of the  traditional e-commerce components have been translated into a language matching the books:
* **The Shopping Cart** is represented as an interactive system **Backpack**.
* **Order Success Alerts & Notifications** are styled as **Achievement Logs**.
* **The Customer Service Desk** is presented as a sarcastic, aliem monitored terminal based on a character known as the Dungeon AI.

### User Stories

#### First Time Visitor Goals
* **As a First Time Visitor**, I want to instantly understand the sites purpose and see what items are available for purchase.
* **As a First Time Visitor**, I want to navigate smoothly through inventory categories and filter or sort items by price or category.
* **As a First Time Visitor**, I want to click into individual products to view more details and add to my cart.
* **As a First Time Visitor**, I want to easily checkout and receive confirmation of my purchase without being forced to create an account. 


#### Registered/Returning Customer Goals
* **As a Returning Visitor**, I want to create an account to manage my default shipping details and view a log of my purchases.
* **As a Returning Visitor**, I want to add items to my cart directly from product lists or carousels, update quantities, and have them persist whilst logged in.
* **As a Returning Visitor**, I want to receive automated emails upon account registration, ticket logging and performing other account functions.

#### Site Administrator Goals
* **As an Admin**, I want to securely Create, Read, Update, and Delete products and categories in the `lootboxes` app; tickets in the `support` app, and blog posts in the `showrunners` app. 
* **As an Admin**,  I want to be able to block non-administrative profiles from viewing, accessing, or tampering with products, tickets or blog posts. 

---

## Design

### Colour Scheme

<table border="0">
  <tr>
    <td><img src="documentation/palette.webp" alt="Colour Palette" width="400"></td>
    <td><img src="documentation/dccbookcover.webp" alt="Dungeon Crawler Carl Book Cover" height="300"></td>
  </tr>
</table>

The colour scheme for this project is based on the first Dungeon Crawler Carl book. A bright neon palette of Pink and Yellow against dark grey and black. 

* **Black and Onyx (`--dungeon-dark`, `--vault-black`):** Onyx `#0F1012` and black `#050607` to allow inventory items and text to stand out.
* **Gold (`--hazard-yellow`):** A bright gold `#FFD200` is used across navigation hovers, primary checkout buttons, and badge profiles. It is also used on sub-headings and headers throughout the site.
* **Neon Pink (`--neon-pink`):** Neon pink `#FF007F` is used on some icons and accents. It is also used on the toasts/achievements. It is also used as sub-headings throughout the site. 

Once again, these colours are declared as global CSS variables inside the `:root` selector. This guarantees colour changes are managed in one location rather than hardcoded throughout the file.

