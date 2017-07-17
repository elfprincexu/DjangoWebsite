Brief summary:

  1. a basic blog Django project, which enables
        Creation/View/Edit/Delete blogs.
        Comments thread
        Accounts: login, register, logout
  2. Use bootstrap, jqeury, javascript, pagedown to render the Layout
  3. Use permission control, comments deletion/post need login and correct permission


virtualenv ingerated: 

Installation: 
  1. git clone or download this project
  3. virtualenv .
  4. Scriptes\activate (windows)    or      bin/activate   (linux)
  5. pip install -r requirement
  6. cd src
  7. python manage.py runserver
  8. loginto "localhost:8000/blogs" to see blogs  
  
  Url mappings:
  1.    /                 ------------ home
  2.    /blogs            ------------ home
  3.    /blogs/[1-9]+   -------------- blog details
  4.    /blogs/[1-9]/edit ------------ blog edit
  5.    /blogs/[1-9]/delete ---------- blog delete
  6.    /blogs/create ---------------- blog creation
  

