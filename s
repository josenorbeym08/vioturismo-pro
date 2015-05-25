[33mcommit d294273e50ef85ef0f256dbdd83432bfe6d1f5e4[m
Author: jose <josenorbey-08@hotmail.es>
Date:   Mon May 25 09:27:10 2015 -0500

    mi primer comin

[1mdiff --git a/templates/base.html b/templates/base.html[m
[1mindex 698fabd..0247e24 100755[m
[1m--- a/templates/base.html[m
[1m+++ b/templates/base.html[m
[36m@@ -67,8 +67,8 @@[m
 							<li><a href="#about">Actores</a></li>[m
 							<li><a href="#project">Viota</a></li>[m
 							<li><a href="#news">Guia Turistica</a></li>[m
[31m-							<li><a href="servicios/page/1">Servicios</a></li>[m
[31m-							<li><a href="/productos/page/1/">Sitios</a></li>[m
[32m+[m							[32m<li><a href="/servicios/page/1/">Servicios</a></li>[m[41m[m
[32m+[m							[32m<li><a href="/sitiosts/page/1/">Sitios</a></li>[m[41m[m
 							<li><a href="{% url 'vista_contacto' %}">Contactans</a></li>[m
 							[m
 <!--							<li class="last"><a href="#contact">Contactanos</a></li>-->[m
[36m@@ -857,13 +857,14 @@[m
 			</div>[m
 		</div>[m
 		<div class="line6">[m
[32m+[m[41m[m
 					<iframe src="https://www.google.com/maps/embed?pb=!1m10!1m8!1m3!1d48386.401887313725!2d-73.9407136!3d40.7147117!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sru!2sua!4v1402409149092" width="100%" height="750" frameborder="0" style="border:0"></iframe>[m
 		</div>[m
 		<div class="container">[m
 			<div class="row ftext">[m
 				<div class="col-md-12">[m
 				<a id="features"></a>[m
[31m-				<h3>We Care About Our Clients and Can Make Their Life Easier!</h3>[m
[32m+[m				[32m<h3>We hhhhhhhhhhhhhhhhhhhhhhhhhttttttttttttuuuuuuuuuuuugggggggggger!</h3>[m[41m[m
 				<p>The main peculiarity of template is the striking presentation when visitors just need to use the scrolling option to find all necessary information about your web project. </p>[m
 				</div>[m
 				<div class="cBtn">[m
[1mdiff --git a/templates/sitios/SingleProducto.html b/templates/sitios/SingleProducto.html[m
[1mindex f88aa88..1cace6d 100644[m
[1m--- a/templates/sitios/SingleProducto.html[m
[1m+++ b/templates/sitios/SingleProducto.html[m
[36m@@ -6,5 +6,5 @@[m
 <h2><p> {{ producto.descripcion }}</p></h2>[m
 <h2><p> {{ producto.contacto }}</p></h2>[m
 <br><br>[m
[31m-<a href="javascript:window.history.go(-1);"> Regresar a la lista </a>[m
[32m+[m[32m<a href="javascript:window.history.go(-1);" class="btn btn-primary" > Regresar a la lista </a>[m
 {% endblock %}[m
\ No newline at end of file[m
[1mdiff --git a/templates/sitios/SingleServicio.html b/templates/sitios/SingleServicio.html[m
[1mnew file mode 100644[m
[1mindex 0000000..64b6c0d[m
[1m--- /dev/null[m
[1m+++ b/templates/sitios/SingleServicio.html[m
[36m@@ -0,0 +1,10 @@[m
[32m+[m[32m{% extends 'base.html' %}[m
[32m+[m[32m{% block title %} Servicio {{servicio.nombre}} {% endblock %}[m
[32m+[m[32m{% block content %}[m
[32m+[m[32m<h1> {{ servicio.nombre }}</h1><br>[m
[32m+[m[32m<img src="/media/{{ servicio.imagen }}" width="100%" heigth="100%"/>[m
[32m+[m[32m<h2><p> {{ servicio.descripcion }}</p></h2>[m
[32m+[m[32m<h2><p> {{ servicio.contacto }}</p></h2>[m
[32m+[m[32m<br><br>[m
[32m+[m[32m<a href="javascript:window.history.go(-1);" class="btn btn-primary" > Regresar a la lista </a>[m
[32m+[m[32m{% endblock %}[m
\ No newline at end of file[m
[1mdiff --git a/templates/sitios/contacto.html b/templates/sitios/contacto.html[m
[1mindex ed33d2d..c5a5809 100644[m
[1m--- a/templates/sitios/contacto.html[m
[1m+++ b/templates/sitios/contacto.html[m
[36m@@ -13,7 +13,7 @@[m
 		<form action="." method="POST">[m
 				{% csrf_token %}[m
 				{{form.as_p}}[m
[31m-		<input type="submit" value="submit"/>[m
[32m+[m		[32m<button class="btn btn-primary" type="submit"> Enviar Comentario  </button>[m
 		</form>[m
 {% endif %}[m
 {% endblock %}[m
\ No newline at end of file[m
[1mdiff --git a/templates/sitios/login.html b/templates/sitios/login.html[m
[1mindex 0546fc6..506267f 100755[m
[1m--- a/templates/sitios/login.html[m
[1m+++ b/templates/sitios/login.html[m
[3