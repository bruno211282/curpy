Decorador
=========

Descripcion general
-------------------

Para la aprobacion del curso se solicito que se desarrollara una funcionalidad mediante el concepto de decorador.

En este desarrollo se eligio hacer un decorador que cuando se aplique a una funcion o método, éste registre a un archivo dos mensajes:

* Informe sobre la accion que se esta por realizar
* Resultado exitoso de la accion ó
* Resultado erroneo de la accion.

Ademas de registrar dichos mensajes, tambien se encapsula a la funcion o método dentro de un bloque `try ... except` para capturar los posibles errores.


Codigo del decorador
--------------------

.. literalinclude:: ../../logger/logger.py
    :pyobject: log_try_exc_deco


