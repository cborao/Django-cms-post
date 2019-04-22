# Django-CMS-POST

Práctica "Django cms_post"

## Enunciado

Realizar un proyecto Django con la misma funcionalidad que
"Django cms_templates",pero atendiendo a una nueva familiar de recursos:
`/edit/`.
Cuando se acceda con un GET a un recurso que comience por `/edit`,
la aplicación web devolverá un formulario que permita editarlo
(si se detecta un usuario autenticado,
y si el nombre de recurso existe como página en la base de datos de
la aplicación).
Ese formulario tendrá un único campo que se precargará con el
contenido de esa página.
Si se accede con POST a un recurso que comience por `/edit/`,
se utilizará el valor que venga en él para actualizar la página correspondiente,
si el usuario está autenticado y la página existe.
Además, volverá a devolver el formulario igual que con el GET,
para que el usuario pueda continuar editando si así lo desea.