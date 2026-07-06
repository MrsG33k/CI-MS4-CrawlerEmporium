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

### Typography
Fonts were imported via [Google Fonts](https://fonts.google.com) for this project alongside system fonts.

* **Headings, Badges, & Navigation Headers:** `Encode Sans Condensed` (Weights: 700, 900) provides a blocky, compact look similar to the book title font.
  <br>
  <img src="documentation/encodesansfont.webp" alt="Encode Sans font" width="400">
* **Toasts & System Readouts:** `Courier New` / Monospace was used in areas of the project to simulate a machine-terminal narrative. 
  <br>
  <img src="documentation/couriernewfont.webp" alt="Courier New font" width="400">
* **General Informational Reading:** `Helvetica Neue` / Arial variants used in areas with heavy text content,such as the Support FAQ text, to improve readability and avoid eye strain. 
  <br>
  <img src="documentation/helveticafont.webp" alt="Helvetica Neue font" width="400">
  <br>

### Imagery
* **System Logo (`celogo.svg`):** A custom asset was created in Photopea based on the colours, typography and assets found on the Dungeon Crawler Carl books. 
    <br>
    <img src="static/images/celogo.svg" alt="Crawler Emporium Font" width="300">
    <br>
* **Favicon (`favicon.ico`):** A custom favicon was created based on the lettering and loot box found in the logo for the project.
    <br>
    <img src="static/images/favicon.ico" alt="Crawler Emporium Font" width="50">
    <br>
* **Loot Box / Blog Graphics:** A collection of 20 themed loot box items, three supporting blog post images and the background on the carousel were generated through [Magnific.com](https://magnific.com) 
    <br>
* **Fallback Asset (`no-image.webp`):** A custom image created using [Canva.com](https://www.canva.com) used across the site if an inventory item is created without an image - to ensure it blends in seamlessly with the project theming.
    <br>
    <img src="static/images/noimage.webp" alt="Fallback Image" width="300">
  <br>
* **404 (`404.png`):** A custom image was created using [Magnific.com](https://magnific.com) for the 404 landing page. It was designed to look like an exploded lootbox. 
    <br>
    <img src="static/images/404.png" alt="Fallback Image" width="300">
  <br>

### Wireframes
Wireframes were mocked up during the early software analysis phase using Canva to plan grid configurations across responsive breakpoints (Desktop vs Mobile layouts). These documents allowed for clean tracking of text-wrapping parameters before building out custom HTML columns.

---
