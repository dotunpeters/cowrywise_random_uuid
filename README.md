[![Codacy Badge](https://app.codacy.com/project/badge/Grade/fc0132181c454e56ac36a35825a16119)](https://www.codacy.com/gh/dotunpeters/cowrywise_random_uuid/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dotunpeters/cowrywise_random_uuid&amp;utm_campaign=Badge_Grade)

# Generate Random UUID

## Question

### Build a simple API that will return a key-value pair of randomly generated UUID. Key will be a timestamp and value will be UUID. While the server is running, whenever the API is called, it should return all the previous UUIDs ever generated by the API alongside a new UUID. Push the code to a git repository and share the link to the repo.*

Sample (note that the latest uuid is at the top).

    {
        "2021-05-21 12:10:19.484523": "e8c928fea580474cae5aa3934c59c26f"
        "2021-05-21 12:08:25.751933": "fcd25b46bec84ef79e14410b91fbf0b3",
        "2021-05-21 12:07:27.150522": "6270d1d412b546a28b7d2c98130e1a5a",
    }

* install dependencies: `pip install -r requirements.txt`
* run migration: `python manage.py migrate`
* Run server: `python manage.py runserver`
* Run test: `python manage.py test -v 0`
