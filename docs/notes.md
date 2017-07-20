## Nice-to-haves

- user login/auth
- web-based self-service scheduling by volunteers
- reminder e-mails to volunteers

## Current system

### scheduling request

click on cell with time and link to search form
search for id
click on update to retreive volunteer info
click on update again to fill in the cell with the person's info

### separate form for logging hours

volunteer tells them ID and num hours and they enter it (autopopulate with datetime.now()?)

### Data

postgres database
web forms to modify records
sections of schedule grid for each factory location

x: close the shift (unavailable, station closed)
o: open it back up to available
e: edit to change time or date or geek id

## Development Plan

- try out django-diary
- introspect pg dump -> models.py
- print/PDF of data map

- enable continuous deployment using hackoregon devops stack (ansible)
- try a react app from hackoregon?
- try appointment edit/insert using django-admin
