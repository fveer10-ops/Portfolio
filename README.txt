Professional Portfolio - CSCI 1170

@author: Fatehveer Chahal
@Institution: Dalhousie University
@Banner ID: B01074417
@Live Site: https://fveer10-ops.github.io/Portfolio/


A) FOLDER STRUCTURE


Root/
|-- index.html          (Homepage)
|-- skills.html         (Skills and Certifications page)
|-- projects.html       (Projects page)
|-- feedback.html       (Feedback page)
|-- index_1.css         (Main stylesheet for all pages)
|-- index_1.js          (Main JavaScript file for all pages)
|-- Images/             (Folder containing all images and logos)
|   |-- favicon.png     (Browser tab icon)
|   |-- mypic.jpeg      (Professional headshot used in hero section)
|   |-- badge.png       (Cisco Networking Academy certification badge)
|   |-- calculatorcode_ss.jpeg  (Screenshot of Java calculator code)
|   |-- website.png     (Screenshot of portfolio website)
|   |-- packettracer.png        (Screenshot of Cisco Packet Tracer topology)
|   |-- aws-2.svg       (AWS logo for tools gallery)
|   |-- cisco.svg       (Cisco logo for tools gallery)
|   |-- java.svg        (Java logo for tools gallery)
|   |-- javascript.svg  (JavaScript logo for tools gallery)
|   |-- linux.svg       (Linux logo for tools gallery)
|   |-- python.svg      (Python logo for tools gallery)
|   |-- wireshark.svg   (Wireshark logo for tools gallery)
|-- Others/             (Folder containing media files)
|   |-- portfoliointro.mp3      (Audio introduction for homepage)
|   |-- java_calculator.mp4     (Video walkthrough of Java calculator)
|-- README.txt


B) HTML FILES

--- index.html ---
Purpose: Homepage of the portfolio. Entry point of the website that starts with a pop-up alert.
Contains: Hero section, About Me section, embedded YouTube video, audio introduction, navigation bar, footer with theme switcher.
Notable elements:
  - id="Alert" on <body> triggers the welcome alert in JavaScript
  - id="hero" is the hero/splash section with professional headshot
  - id="greets" is updated dynamically by greetingDisplay() in JS
  - id="audio" contains the audio player and its label



--- skills.html ---
Purpose: Displays technical skills, training, and certifications.
Contains: Skills table, certification badge, interactive hover demo, navigation bar, footer with theme switcher.
Notable elements:
  - class="tableDesign" on the skills table applies CSS border styling
  - id="interactive" triggers mouseOver() and mouseOut() JS functions
  - Cisco badge links externally to Credly for credential validation



--- projects.html ---
Purpose: Showcases current and planned projects in a grid layout.
Contains: Project cards grid, tools/technology logos gallery, navigation bar, footer with theme switcher.
Notable elements:
  - class="projects" is the CSS grid container (3 cols desktop,
    2 cols tablet, 1 col mobile)
  - class="roadmap" are the individual project cards
  - class="logos" is the photo gallery grid of technology logos
    (4 cols desktop, 2 cols mobile)
  - class="badge" marks the Network Security project as planned

--- feedback.html ---
Purpose: Collects feedback from visitors about the portfolio.
Contains: Feedback form with name, role, and suggestions fields, navigation bar, footer with theme switcher.
Notable elements:
  - id="feedback-form" is styled as a flexbox column
  - id="submitFeedback" is the styled submit button
  - form uses method="post" and action="#"



C) CSS FILE - index_1.css

Purpose: Stylesheet for all four pages of the portfolio.
Applied to all pages via: <link rel="stylesheet" href="index_1.css">

--- SELECTORS USED ---

Universal Selector (*)
  Location: Top of file
  Purpose: Applies font-family: inherit to every element on the page, ensuring consistent font rendering across all elements.

Child Selector (>)
  Location: nav > ul > li > a, #audio > p, section > p, #audio > :first-child
  Purpose: Targets direct children only. For example, nav > ul > li > a styles only the anchor tags that are direct children of li, which are direct children of ul, which are direct children of nav.

Sibling Selector (~)
  Location: #feedback-section h2 ~ p
  Purpose: Targets all <p> elements that are siblings of <h2> inside #feedback-section. Adds spacing below the heading paragraph.

Adjacent Sibling Selector (+)
  Location: h3 + ul
  Purpose: Targets a <ul> that immediately follows an <h3>. Applies decimal list style and line height to those specific lists.

Attribute Selector
  Location: table[class = "tableDesign"]
  Purpose: Targets the skills table specifically by its class attribute value. Applies border and width styling.

Multiple Selector (,)
  Location: #hero-text h1, #hero-text p
            .roadmap-body ul, .roadmap-body ol
  Purpose: Applies the same styles to multiple selectors at once. First instance makes hero heading and paragraph white. Second instance applies consistent list styling in project cards.

Pseudo-element Selector (::before)
  Location: h2::before
  Purpose: Inserts a decorative arrow character before every h2 heading on the page automatically without modifying HTML.

Pseudo-class Selectors (:hover, :active, :first-child)
  Location: nav ul li a:hover, footer a:hover, footer a:active, footer a:visited, #audio > :first-child
  Purpose: Styles elements based on user interaction state.

--- LAYOUT ---

.projects
  Purpose: CSS grid for project cards on projects.html.
  Desktop: repeat(3, 1fr) - 3 equal columns
  Tablet (601px-1024px): repeat(2, 1fr) - 2 columns
  Mobile (max 600px): 1fr - single column

.logos
  Purpose: CSS grid for technology logo gallery on projects.html.
  Desktop: repeat(4, 1fr) - 4 equal columns
  Mobile (max 600px): repeat(2, 1fr) - 2 columns

#feedback-form
  Purpose: Flexbox column layout for the feedback form on feedback.html.
  display: flex, flex-direction: column
  max-width: 30% desktop, 60% tablet, 90% mobile

#hero
  Purpose: Flexbox row layout for the hero section on index.html.
  display: flex, justify-content: space-between places text left,
  image right. On mobile switches to flex-direction: column.

--- RESPONSIVE DESIGN (MEDIA QUERIES) ---

Mobile (max-width: 600px):
  - Nav links: smaller font, nowrap, space-evenly to fit one row
  - .projects grid: 1 column
  - .logos grid: 2 columns
  - #feedback-form: max-width 90%
  - #hero: column direction, centered text
  - #pic: float removed, displays as block

Tablet (min-width: 601px and max-width: 1024px):
  - .projects grid: 2 columns
  - #feedback-form: max-width 60%

Desktop (above 1024px):
  - Default styles apply (3 column grid, 30% form, side-by-side hero)




D) JAVASCRIPT FILE - index_1.js


Purpose: Adds interactivity to all pages of the portfolio.
Applied to all pages via: <script src="index_1.js" defer></script>
Note: defer means the script runs after the HTML is fully loaded.

--- FUNCTIONS ---

Welcome Alert
  Purpose: Displays a welcome message when the homepage loads.
  How it works: Checks if element with id="Alert" exists (only present on index.html body tag). If found, shows alert dialog.
  Output: Browser alert box saying "Welcome to my portfolio website!"

greetingDisplay()
  Purpose: Updates the greeting heading based on the time of day.
  Input: Current hour from new Date().getHours()
  Output: Updates innerText of element with id="greets"
          - Before 12pm: "Good Morning! I'm Fatehveer Chahal."
          - 12pm to 6pm: "Good Afternoon! I'm Fatehveer Chahal."
          - After 6pm:   "Good Evening! I'm Fatehveer Chahal."
  Note: Wrapped in if(greeting) null check so it runs safely on pages without id="greets" (feedback.html) without crashing the script.
  Called: Once on page load.

timeDisplay()
  Purpose: Shows a live updating clock in the navigation bar.
  Input: Current time from new Date().toLocaleTimeString()
  Output: Updates innerHTML of element with id="clock" with current time.
  Called: Once immediately on load, then every 1000ms via setInterval.
  Dependent on: id="clock" span inside nav on all pages.

changeColor(theme)
  Purpose: Changes the website colour theme dynamically.
  Input: theme - string, one of "dark", "light", or "default"
  Output: Changes body background colour and nav/footer background colour.
  Example: changeColor('dark') sets background to black, nav/footer grey.
  Dependent on: Buttons in footer on all pages, querySelectorAll targets 'nav ul, footer, #hero'
  Themes:
    "dark"    - black background, white text, grey nav and footer
    "light"   - lavender background, black text, thistle nav and footer
    "default" - restores background image, #1B2A4A nav and footer

mouseOver()
  Purpose: Triggered when mouse enters the interactive demo box on skills.html.
  Input: None (triggered by onmouseover event on id="interactive")
  Output: Changes box content to cybersecurity focus text, sets background yellow, text grey, border solid black.
  Dependent on: id="interactive" div on skills.html

mouseOut()
  Purpose: Triggered when mouse leaves the interactive demo box on skills.html.
  Input: None (triggered by onmouseout event on id="interactive")
  Output: Resets box content to original prompt text, removes background color and border.
  Dependent on: id="interactive" div on skills.html




E) REFERENCES & ASSETS


Background Image:
  - backgroundImage.jpg: Personal/original photograph used as page background

Technology Logos (SVG format, sourced from public domain / open use):
  - AWS logo: Amazon Web Services brand assets
  - Cisco logo: Cisco Systems brand assets
  - Java logo: Oracle Java brand assets
  - JavaScript logo: Public domain JS logo
  - Linux logo: Linux Foundation brand assets
  - Python logo: Python Software Foundation brand assets
  - Wireshark logo: Wireshark brand assets

Certification Badge:
  - badge.png: Cisco Introduction to Cybersecurity badge
    Credential URL: https://www.credly.com/badges/b3c365a6-cc39-4983-9e0d-8289ac4e1bcc/public_url

YouTube Video (embedded, not downloaded):
  - "What is Cybersecurity" - https://www.youtube.com/embed/inWWhr5tnEA

Personal Media:
  - mypic.jpeg: Personal professional headshot photograph
  - portfoliointro.mp3: Personal audio introduction recording
  - java_calculator.mp4: Personal screen recording of Java calculator demo



Chahal, F. 2026. Personal Portfolio Website. CS Assignment 2. Dalhousie University.

GitHub. 2026. GitHub Pages Documentation. GitHub, Inc. Retrieved April 6, 2026 from https://docs.github.com/en/pages

Google Gemini. 2026. Assistance with box-shadow in CSS. Retrieved April 4, 2026 from https://gemini.google.com. 

W3Schools. 2026. HTML Tutorial. W3Schools Online Web Tutorials. Retrieved April 4, 2026 from https://www.w3schools.com/html/default.asp 

