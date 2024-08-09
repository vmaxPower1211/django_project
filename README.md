This is the project using django as backend

In this project we implemented database to MySQL
And change MySQL database dataset into tree structure

migrating modelling data following command

python manage.py makemigrations
python manage.py migrate

Data inputting to Tree structure is taking under following command

python manage.py shell

Inside shell input following code

TreeNode.objects.create(name='Root', parent='')

TreeNode.objects.create(name='child1', parent=root)
TreeNode.objects.create(name='child2', parent=root)

TreeNode.objects.create(name='grand_child1', parent=child1)
TreeNoide.objects.create(name='grand_child2', parent=child2)


Run this project following command
python manage.py runserver 127.0.0.1:8000
