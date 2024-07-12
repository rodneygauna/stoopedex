# STOOPEDEX

![STOOPEDEX](/app/static/img/stoop.png "STOOPEDEX")

Welcome to Stoopedex, your ultimate guide to finding the best stoop sales in your neighborhood. Whether you're looking for hidden treasures, unique finds, or just a fun weekend activity, we've got you covered.

## Codédex 2024 Summer Hackathon - Track 2 "Stoop Sale Website" (Solo Challenge)

[Codédex 2024 Summer Hackathon](https://www.codedex.io/hackathon) presented a wonderful opportunity to put my web dev skills to the test. With only 24 hours (and during work days), I had the chance to prove I am grasping what I'm learning with a rapid development project.

### Challenge

Create an interactive invitation to a Brooklyn Stoop Sale using HTML/CSS/JavaScript.

### Criteria

- ▶️ Make it interactive (Music? Animation? Be creative!!)
- 🗓️ Date & time (make this up!)
- 📍 Place with a map API (2nd Pl. and Court St)
- 🔗 Shareability
- ⭐️ VIBES: good quality, tasteful, and awesome things

🛍️ Here are some of the things we’ll be selling: clothes, home goods, shoes, tchotchkes -- things that can be set up on a table and one clothing rack on a corner in Brooklyn, NY lol

### Resources

- <https://www.codedex.io/html>
- <https://www.codedex.io/css>
- <https://www.codedex.io/javascript>
- <https://www.codedex.io/projects/deploy-a-website-with-vercel>
- [Google Maps](https://developers.google.com/maps)
- [Mapbox](https://www.mapbox.com/)

### Project Goals

I wanted to build a web app using Flask, Postgres, and my own CSS library [ZestyUX](https://zestyux.com). Functionality would include:

- Registration and Login
- Ability to create and view upcoming Stoop Sales
- Integrate Google Maps
- "Sign up"/show your interested in going to a posted Stoop Sale

### Outcomes

I was able to meet most of my goals, but I kept running into frontend issues with my own CSS framework. In the last few hours I had to pivot to Bootstrap.
I also didn't get to hit my "nice to have" list; such as creating an .ics file to add to your calendar, two-factor authenication, email notifications, in-app messaging, etc.
This is understandable with having to judge my normal day job and spending the evening with my family.

Next time, I'd like to join a team (when my schedule allows it). I think sharing the load/problems/bugs with others is a great opportunity to learn and share my own knowledge.

## How To Run The Project

### Docker

#### Environment Keys and Email Configuration

Before building the image and running the container, you'll have to create a `.env` file.
This can be done by creating a new file in the parent directory ('H3O_Inferno') with the filename of `.env`.
See the file named `.env.sample` for an example.

Open the `.env` file and add the following:

```text
SECRET_KEY="1234567890"
POSTGRES_USER="postgres_user"
POSTGRES_PASSWORD="password12345"
POSTGRES_DB="stoopedex-db"
GOOGLE_MAPS_API_KEY="key12345"
```

Remember to replace the example text in the quotes on your .env file.

Make the changes necessary and save the changes you've made.

#### Docker Build, Run, Stop, and Remove

Build the image and run the container:

```terminal
docker compose up --build -d
```

Stop and remove the image:

```terminal
docker compose down --rmi all
```

#### Make Commands

If you prefer to use [make](https://www.gnu.org/software/make/) instead of the Docker Compose commands, here are the corrisponding commands:

Build the image and run the container:

```terminal
make up
```

Stop and remove the image:

```terminal
make clean
```

You can also run the following command to populate the database with fake information:

```terminal
make test-env
```

And for quick restarts (combining multiple stop, clean, build, etc. commands), use:

```terminal
make restart
```

## Technology Used

### Backend

- Python
- Flask
- Faker

### Frontend

- WTForms
- Flask WTForms
- Bootstrap 5

### Database

- Postgres

### Deployment

- Docker

## Support

If you have any questions, you can do one of the following:

- Send an email to [rodneygauna@gmail.com](mailto:rodneygauna@gmail.com)
- Create an issue in the GitHub repo - guide here [GitHub - Create an issue or pull request](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/working-with-your-remote-repository-on-github-or-github-enterprise/creating-an-issue-or-pull-request-from-github-desktop)
