# GravityFallsAPI
A lightweight Python web application that provides character data from the Gravity Falls universe. Built with Flask and powered by SQLite, this API allows you to retrieve information about characters, including names, quotes, episodes, and images.

API Endpoints:

- /
```json
{
    Characters: "/characters"
}
```


- /characters

```json
{
    Count: {count}
}
```

- /characters/{id}

```json
{
    Id: 1
    Name: 8 Ball
    Quote: "So, you wanna eat him, or, something?"
    Like: "To party"
    Image: ""
}
```
