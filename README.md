#### Workshop_3 

Technical requirements: Python 3.6, Django 2.1.3,Faker 1.0.2, please see requirements.txt

Example screenshot from application: workshop3_screenshot.png

Simple application for booking conference rooms in an office building.
The user can only book rooms for whole day.

Application features:
1.	 On the home page user sees all the conference rooms and their status of the day: free or busy. Next to the name of each room there is a link to modify the room's data
and also an option to remove it.
2.	 A user can click on the name of the room and see all the room's data: its name,
capacity and information, whether it has a projector. In addition, user sees a list of days when the room is booked, but does not see days that have passed.
The user will see a link that will allow to book this room.
3.	 The user can add a new room.
4.	 User after entering the edit option for a room, can provide data (name, capacity,
projector, if necessary, other data).
5.	 After entering the reservation,user can see again a list of booked dates for chosen room(conditions as in point 2). The user can specify the booking date. System takes care not to duplicate any booking date.
6.	 User can search for rooms with the following criteria: room name, day, room capacity, projector availability.
