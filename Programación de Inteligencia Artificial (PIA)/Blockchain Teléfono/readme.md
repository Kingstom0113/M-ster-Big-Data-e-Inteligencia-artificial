# Respuestas a las Actividades del Proyecto Teléfono Escacharrado con Blockchain

1.  **¿Por qué se usa un hash en cada bloque del blockchain?**

    * El hash se utiliza para garantizar la integridad de los datos en cada bloque. Actúa como una "huella digital" única del contenido del bloque. Cualquier modificación en el mensaje o en el hash anterior resultará en un hash completamente diferente. Esto permite detectar cualquier intento de alteración de los datos.

2.  **¿Qué papel cumple el `hash_anterior` en la integridad de la cadena?**

    * El `hash_anterior` crea un vínculo entre los bloques, formando una cadena. Cada bloque contiene el hash del bloque precedente, lo que significa que si se modifica un bloque, el hash de ese bloque cambiará, y los hashes de los bloques siguientes ya no coincidirán con el hash del bloque alterado. Esto permite detectar alteraciones en cualquier punto de la cadena.

3.  **¿Qué similitudes hay entre el juego del teléfono escacharrado y esta simulación?**

    * Ambos ilustran cómo la información puede distorsionarse o alterarse a medida que se transmite a través de múltiples "intermediarios" (personas en el juego, bloques en la simulación). En ambos casos, el mensaje final puede ser muy diferente del mensaje original.

4.  **¿Se puede “arreglar” la cadena alterando todos los hashes? ¿Por qué eso no es viable en blockchains reales?**

    * Técnicamente, sería posible recalcular todos los hashes para que coincidan con los datos alterados. Sin embargo, en blockchains reales, esto es extremadamente difícil debido a:
        * El consenso: Las blockchains descentralizadas requieren el consenso de múltiples participantes para validar los bloques. Alterar una cadena requeriría el consenso de la mayoría, lo cual es muy difícil de lograr.
        * La prueba de trabajo/prueba de participación: Los blockchains utilizan mecanismos como la prueba de trabajo o la prueba de participación, que requieren una gran cantidad de poder computacional para generar nuevos bloques. Alterar bloques antiguos requeriría rehacer este trabajo, lo cual es computacionalmente costoso.

5.  **Personaliza el mensaje inicial.**

    * Esto ya se ha implementado en el código, donde puedes cambiar la variable `mensaje_inicial` a cualquier texto deseado.

6.  **Controla el porcentaje de error aleatorio (ej. 10%, 30%, etc.).**

    * Esto también se ha implementado en el código, donde la variable `probabilidad_error` controla el porcentaje de error. Puedes cambiar este valor para ajustar la frecuencia de las alteraciones en los mensajes.

7.  **Activa el modo trampa para modificar un bloque a propósito.**

    * La función `modo_trampa` permite modificar un bloque específico en la cadena, lo que demuestra cómo se detectan las alteraciones.

8.  **Guarda la cadena completa en un .txt, con información por bloque.**

    * La función `guardar_cadena` guarda la información de cada bloque (mensaje, hash, hash anterior) en un archivo de texto.

9.  **Implementa una función de reparación de cadena (recalcular hashes).**

    * La función `reparar_cadena` recalcula los hashes de los bloques posteriores al bloque alterado para restaurar la integridad de la cadena.

10. **Agrega una función de verificación de integridad de principio a fin.**

    * La función `verificar_integridad` verifica que todos los hash anteriores coincidan con los hash de los bloques anteriores. Esto verifica la integridad de toda la cadena.