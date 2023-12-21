# Waquar_blog
This is django based blog.
Where admin can create and delete post.
User can read the blog  post and cant change anything.
user can go detail by clicking on Read more.Or click on Title also.

Let Folder-Nmae=Waquar_blog

#git init,git status

#setup explian 

python -m venv venv 

Waquar_blog>cd venv

Waquar_blog\env\Scripts\avtivate  OR scripts> Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

.\activate

#virtual environment  activited. {venv}

{venv} Waquar _blog\venv\Scripts>

#install django

pip install django

cd..

{venv} Waquar _blog>

django-admin startproject blog

cd blog

{venv} Waquar_blog\blog>

django-admin startapp App

#create model for databse

py manage.py makemigrations

py manage.py migrate

#createsuperuser

py manage.py createsuperuser

py manage.py runserver 

#push code

git add .

git commit -m 'changes commited'

git branch

git remote add origin http

git push

