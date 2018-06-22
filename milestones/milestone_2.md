# Milestone 2

## HTML & CSS Click-through

### Sign in
Initial landing page for unauthenticated users to sign in.
![](https://raw.githubusercontent.com/habitfarm/habitfarm/master/milestones/img/clickthrough/1_signin.jpg)

### Sign up
Users can click the "Sign up" button from the sign in page,to navigate 
to the sign up page and register.
![](https://raw.githubusercontent.com/habitfarm/habitfarm/master/milestones/img/clickthrough/2_signup.jpg)

### Verify email 
After submitting the sign up form, users get an automated email to verify
the email provided.
![](https://raw.githubusercontent.com/habitfarm/habitfarm/master/milestones/img/clickthrough/3_verify_email.jpg)

### Confirm email 
Opening the link in the verification email will bring them to a confirmation
page.
![](https://raw.githubusercontent.com/habitfarm/habitfarm/master/milestones/img/clickthrough/4_confirm_email.jpg)

### Sign in
Clicking the "Confirm" button takes the user to the sign in page.
![](https://raw.githubusercontent.com/habitfarm/habitfarm/master/milestones/img/clickthrough/5_signin.jpg)

### Habits list
The user is taken to the overview page that lists all their habits.
This is the main page in our application. It lists the user's configured
habits in a table with basic information about how often they are doing the 
routine associated with their habit. At the top of the page is a calendar that
will display when habit routines were logged. Not shown in this click through
will be a button to log when a routine has been completed.
![](https://raw.githubusercontent.com/habitfarm/habitfarm/master/milestones/img/clickthrough/6_habits_list.jpg)

### Habits create
Clicking the "Add a habit" button will take users to the habit create page. 
Here users can add new habits that they'd like to track. This will eventually 
be a modal instead of a separate page.
![](https://raw.githubusercontent.com/habitfarm/habitfarm/master/milestones/img/clickthrough/7_habits_create.jpg)
![](https://raw.githubusercontent.com/habitfarm/habitfarm/master/milestones/img/clickthrough/8_habits_create.jpg)

### Habits list
After adding a habit, users are taken back to the habits list page where the
new habit will appear in the list.
![](https://raw.githubusercontent.com/habitfarm/habitfarm/master/milestones/img/clickthrough/9_habits_list.jpg)

### Sign out
Clicking the "Sign Out" option in the nav bar allows users to logout.
![](https://raw.githubusercontent.com/habitfarm/habitfarm/master/milestones/img/clickthrough/10_signout.jpg)

## Wireframes
Wireframes of the front-end design we are striving for.

### Sign up
The sign up page will have a nice banner image across the top with a
promotional section about what's awesome about the platform on the left, and 
the actual sign up form on the right.
![](https://raw.githubusercontent.com/habitfarm/habitfarm/master/milestones/wireframe/sign_up.jpg)

### Sign in
The sign in page will have banner across the top, similar to the sign in page,
with a centered sign in form.
![](https://raw.githubusercontent.com/habitfarm/habitfarm/master/milestones/img/sign_in.jpg)

### Habits list
This page will have a calendar at the top, and a list of habits at the bottom.
The calendar will fill in colors on each day that the corresponding habit,
with the same color in the list, has had a routine logged. The navigation will
be on a column on the left hand side, with the plaform logo in the top-left
corner.
![](https://raw.githubusercontent.com/habitfarm/habitfarm/master/milestones/wireframe/habits_list.jpg)

### Habits create
This will be a modal that pops up when the user clicks "Add a habit" on the
habits list page. The modal will allow the user to add the 
habit name, frequency that they'd like to do the routine, an icon
or color for the habit list page,
and a description of the habit.
![](https://raw.githubusercontent.com/habitfarm/habitfarm/master/milestones/wireframe/habits_create.jpg)

### Email notification
Based on the configured frequency of the habit, we will send email reminders
to ask the user if they've done their routines yet today, and log it in the
platform.
![](https://raw.githubusercontent.com/habitfarm/habitfarm/master/milestones/wireframe/email_notification.jpg)

## Backend Concepts
Our backend data model consists of user, habits, and log entries. Each user
can have many habits. Each habit has many log entries for when a routine was
completed.
* __User__:
    * Built in django concept of a user.
    * Has multiple habits.
* __Habit__:
    * The behaviour that the user wants to instill.
    * Essential fields:
        * `name`: name of the habit
        * `desiredFrequency`: how often the user want to do the routine associated with the habit
* __LogEntry__:
    * Timestamped table of each time the user does a routine for a habit,
    * Each habit has multiple log entries.
    * Essential fields:
        * `habit_id`: foreign key to habits table
        * `completed`: timestamp of when the routine was completed

