### Milestone 1

1. __Team members__:
    * Hien Phuong 
    * Budi Rahardja
    * Stephen Cockerill

2. __Software goal and concept__:
__Habit Farm__: An application to help users keep track of the habits they'd like to instill.
People often want to improve their lives by doing things that they know make them
happy, healthy, and successful. Such as taking the time to read before bed, flossing their
teeth in the morning, going to the gym, etc. But it can be difficult to incorporate the
small changes in a person's daily life needed to instill these habits, and it's often a
thankless job. __Habit Farm__ aims to give users a place to define the habits they'd like to
form, keep track of their progress, and feel rewarded for their efforts!

* __User stories__:
    * Karen has heard from her dentist, time and time again, that she should really start
      flossing! Friends casually talk about how often they floss, and Karen feels
      compelled to tell a white lie saying that she flosses too. She knows she should, but
      she just can't seem to stick with it. So she signs up for __Habit Farm__ and sets it
      up to track her daily habit of flossing her teeth. Each day, she gets a notification
      reminding her to floss. When she does floss, Karen logs that she does and she gets a
      sense of accomplishment. Here streak is up to 8 days now!
    * Harold was on the varsity cross country team in college, and considers himself an
      athlete. Years out of school, he has really excelled at his work, but isn't in
      the shape he'd like to be in. He wants to start running everyday, and does
      occassionally, but can't seem to find the time/motivation to do it regularly. So he
      sets up an account with __Habit Farm__ and it sends him a reminder everyday to go for
      a run. He logs each run he completes in the app, and he can now keep track of how
      often he's actually running. He always thought he was someone that would excercise
      in the morning, but it turns out more often than not, he finds the time after work.
      So now he's making it a part of his routine to stop at a park on the way home from
      work and take a run.

3. __Project specifications__:
We will implement a signup/login page to register/login users. We will provide a home
dashboard page that allows users to view all the habits they've configured in a list and
on a calendar. On this page, users can log when they've done a routine for their habit and
it will show up on the calendar as done for that day. Users can also add new habits from
this page. The add a habit button will bring up a modal form to input details about the
habit. Upon submitting, the user will be redirected back to the home page where their new
habit will appear in the list. When user's add a habit, the input the cadence that they
want to be doing their habit routine. We will use this information to send email reminders
to do the routine and log them in the application.

* __APIs__:
    * Django send_email needs a email server. We will look into MailGun or GMail.
    * We will use a MailChimp email template to format our email reminders.
    * We will use cookiecutter to setup our django project and to handle our signup/login
      pages.
* __WireFrames__:
    * signup:
        * ![](https://raw.githubusercontent.com/stephencockerill/habitfarm/master/milestones/img/signup.jpg)
    * login:
        * ![](https://raw.githubusercontent.com/stephencockerill/habitfarm/master/milestones/img/login.jpg)
    * home:
        * ![](https://raw.githubusercontent.com/stephencockerill/habitfarm/master/milestones/img/home.jpg)
    * add habit:
        * ![](https://raw.githubusercontent.com/stephencockerill/habitfarm/master/milestones/img/add_habit.jpg) 
    * email reminder:
        * ![](https://raw.githubusercontent.com/stephencockerill/habitfarm/master/milestones/img/email_reminder.jpg)
4. __Challenges and unkowns__:
    * Integrating with the MailGun/Gmail email apis is an integral part of our
      application. The reminders are the cue for the user to do the routine, as well as
      the hook to keep them engaged in the application. It's something we are not very
      familiar with so it's important that we spend the time up-front to get it working.
      If for some reason we can't, we will have to fall back to making an in app
      notification page or something like that.
    * Limiting the scope of our project into the time-frame that we have. We have a lot of
      idea about the awesome things we could do, but we need to be disciplined about what
      we're trying to accomplish. We are just starting to all arive at a shared vision of
      the purpose of the app. We need to stick with the minimum viable product and not
      lose course.

5. __Group roles__:
    * __Back-end__: Hien Phuong
        * Object Models
        * Views (business logic)
        * Infrastructure (Postgres, Heroku)
    * __API__: Budi Rahardja
        * API integrations (email notification system)
        * Views (business logic)
    * __Front-end__: Stephen Cockerill
        * HTML
        * CSS

