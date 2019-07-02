# MS Graph Useful Links

Your app registration will need Calendars.Read permission

## Get all room names
https://graph.microsoft.com/beta/me/findRooms

## Get all events for a room (Liskov)
### Using service principal id
https://graph.microsoft.com/beta/users/56a6fc77-23e9-4860-88e8-0f9b2b22deb1/events
### Using room email address
https://graph.microsoft.com/beta/users/opie.liskov@headforwards.com/events 

## Get all room principals
[https://graph.microsoft.com/v1.0/me/people/?$filter=personType/class eq 'Other' and personType/subclass eq 'Room'](https://graph.microsoft.com/v1.0/me/people/?$filter=personType/class eq 'Other' and personType/subclass eq 'Room')

Try it out at Microsoft [Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer)
