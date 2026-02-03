# Flask Website (Goal: With a Graph(s))

This basic Python Flask website will show a Dash graph on it.


Note to Self:
TODO: I need to decide how I want Flask and Dash to interact

Dash acts as a separate Dashboard - so 1 Dash app per any webpage displaying any graph. Yes, I could create 1 dashboard that has multiple tabs/lookdown options to show different graphs, but that would still be considered 1 webpage (unless I wnat to use Dash Pages for different routes for different graphs)

Flask cannot reach inside Dash. So if I want a website with multiple Flash webpages each with its own specific Dash graph(s), each Flask webpage must have its own Dash app.