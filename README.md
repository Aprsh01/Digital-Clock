This project uses Python and Tkinter (a built-in GUI library) to make a digital clock with a live time and date display. Here's what each part does:

*tk.Tk() creates the main window of the app.

*A label at the top shows the title "DIGITAL CLOCK" using a custom font and colors.

*The time() function gets the current time and date using strftime('%r\n%b %d,%Y').
  %r shows the current time in 12-hour format (with AM/PM).
  %b %d,%Y shows the date (e.g., Jul 21, 2025).
  
*This time is then shown on the screen using a label.

*The after(1000, time) line refreshes the time every 1000 milliseconds (1 second) so it keeps updating in real-time.

*root.mainloop() runs the app and keeps the window open.
