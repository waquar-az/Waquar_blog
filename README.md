#Waquar_blog

This is django based blog. 
Where admin can create and delete post. User can read the blog post and cant change anything. user can go detail by clicking on Read more.Or click on Title also.

Let Folder-Name=Waquar_blog

#git init,git --version

#setup explian

python -m venv venv

Waquar_blog>cd venv

Waquar_blog\env\Scripts\avtivate OR scripts> Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

.\activate

#virtual environment activited. {venv}

{venv} Waquar _blog\venv\Scripts>

#install django

pip install django

cd..

{venv} Waquar _blog>

django-admin startproject blog

cd blog

{venv} Waquar_blog\blog>

{venv} Waquar_blog\blog>django-admin startapp App

#create model for databse

{venv} Waquar_blog\blog> py manage.py makemigrations

 {venv} Waquar_blog\blog> py manage.py migrate

#createsuperuser

{venv} Waquar_blog\blog> py manage.py createsuperuser

{venv} Waquar_blog\blog>py manage.py runserver

#push code

git add .

git commit -m 'changes commited'

git branch

git remote add origin http

git push

![Screenshot (877)](https://github.com/waquar-az/Waquar_blog/assets/106869966/e4cb073a-3838-4abc-a2da-a9fa01ba5157)


![Screenshot (876)](https://github.com/waquar-az/Waquar_blog/assets/106869966/9e37853e-df87-4536-9c3d-4dae27c3f31c)

