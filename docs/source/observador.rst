.. _observador:

Patrón Observador
=================

Para incluir el patron observador dentro del proyecto se decidió integrar una funcionalidad extra: informar a
una aplicacion server sobre los eventos de inicio de sesión asi como también sobre los eventos de creación de usuarios en el sistema.

Se implemento el módulo `pubsub.py` que contiene las clases: `Publisher` y `LogSubscriber`. Ambas clases trabajando juntas forman el
patrón observador.

Cuando se instancia el Publisher se definen los eventos para los cuales soportará publicar mensajes
de actualizaciones. Quienes reciben esas publicaciones son los subscriptores. Cada subscriptor, para recibir informacion
desde el publisher, debe registrarse en el mismo indicando a que evento desea subscribirse y mediante que método desea ser notificado.

Cuando llega la necesidad de notificar, quien haga uso de la instancia de Publisher
debe invocar el metodo `dispatch` informando `evento` y `mensaje`.
Este método repartira las notificaciones a los subscriptores correspondientes al evento que haya informado.


Codigo del Subscriptor
----------------------

.. literalinclude:: ../../logger/pubsub.py
    :pyobject: LogSubscriber


Codigo del Publisher
----------------------

.. literalinclude:: ../../logger/pubsub.py
    :pyobject: Publisher