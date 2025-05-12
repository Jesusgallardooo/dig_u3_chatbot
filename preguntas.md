# Fase 2: Análisis de utilidad y aplicación

Analiza cómo el software desarrollado se adapta a las necesidades de una empresa ficticia o real, evaluando su utilidad, impacto y viabilidad a través de una serie de preguntas relacionadas con los indicadores de los criterios de evaluación.

### Criterio 6a) Objetivos estratégicos:

#### - ¿Qué objetivos estratégicos específicos de la empresa aborda tu software?

Los objetivos para mi empresa ficticia serían:

1. **Automatización de procesos internos**: Reduce la dependencia de tareas manuales en la gestión del inventario.

2. **Reducción de errores humanos**: Al registrar productos y cantidades automáticamente mediante comandos simples, se minimizan errores comunes como el ingreso incorrecto de datos en hojas de cálculo.

3. **Mejora de la eficiencia operativa**: Permite a cualquier empleado autorizado interactuar con el sistema a través de Telegram desde cualquier lugar, sin necesidad de acceder a un sistema ERP complejo.

4. **Centralización y trazabilidad de información**: Toda la información se guarda en Firebase, permitiendo seguimiento, consulta y auditoría de los movimientos de inventario.

#### - ¿Cómo se alinea el software con la estrategia general de digitalización?

El bot se alinea con una estrategia digital moderna basada en estos principios:

1. **Accesibilidad y movilidad**: El uso de Telegram permite acceder al sistema desde dispositivos móviles sin requerir infraestructura adicional.

2. **Uso de la nube**: Al utilizar Firebase, se reduce la necesidad de servidores locales y se garantiza escalabilidad, seguridad y acceso en tiempo real.

3. **Integración sencilla**: Es un primer paso hacia la digitalización, que puede integrarse más adelante con otros sistemas de ventas o ERPs más robustos.

4. **Adopción rápida**: Por su interfaz conversacional y comandos simples, puede ser adoptado por el equipo sin requerir formación técnica extensa.


### Criterio 6b) Áreas de negocio y comunicaciones:

#### - ¿Qué áreas de la empresa (producción, negocio, comunicaciones) se ven más beneficiadas con tu software?

El chatbot de gestión de inventario beneficia principalmente las siguientes áreas de TechMarket S.A.:

1. **Área de operaciones/logística**:
Facilita la gestión diaria del inventario, como el control de existencias, entradas y salidas de productos, y reposición de stock.

2. **Área de negocio/ventas**:
Garantiza que los productos estén disponibles en el momento oportuno, evitando quiebres de stock que afectan la satisfacción del cliente y las ventas.

3. **Área de soporte técnico o administración**:
Proporciona una herramienta sencilla para registrar, consultar o actualizar el inventario sin necesidad de software especializado.


#### - ¿Qué impacto operativo esperas en las operaciones diarias?

- **Mayor velocidad en la gestión de inventario**:
Los comandos simples permiten registrar productos y consultar el stock al instante desde cualquier dispositivo con Telegram.

- **Mejor visibilidad del inventario en tiempo real**:
El uso de Firebase permite que todos los usuarios autorizados tengan acceso sincronizado al mismo inventario actualizado.

- **Reducción de tareas repetitivas**:
Elimina la necesidad de llevar inventarios en papel o planillas, reduciendo el tiempo dedicado a tareas manuales.

- **Mejora en la toma de decisiones**:
El acceso rápido a la información del inventario ayuda a prever necesidades de reposición y a planificar compras de manera más eficiente.

### Criterio 6c) Áreas susceptibles de digitalización:

#### - ¿Qué áreas de la empresa son más susceptibles de ser digitalizadas con tu software?

El software de chatbot para inventario facilita la digitalización especialmente en las  áreas de Gestión de inventario, Logística y almacén y en Comunicación interna de operaciones, por razones obvias.


#### - ¿Cómo mejorará la digitalización las operaciones en esas áreas?

La digitalización mediante el chatbot permite agilizar procesos al simplificar tareas complejas en simples comandos por chat, reduciendo así el tiempo y esfuerzo requerido. Además, minimiza errores humanos al eliminar registros manuales, mejorando la precisión de los datos.

También ofrece mayor accesibilidad desde cualquier dispositivo con Telegram, automatiza tareas repetitivas como el conteo de inventario y proporciona trazabilidad completa de los movimientos, lo que facilita auditorías y mejora la transparencia operativa.

### Criterio 6d) Encaje de áreas digitalizadas (AD):

#### - ¿Cómo interactúan las áreas digitalizadas con las no digitalizadas?

Interactúan a través del servidor y de telegram. El cliente utiliza la aplicación para llevar una gestión exhaustiva del stock de su tienda, proveedora del artículo que sea. Es decir, lo no digitalizado actúa con lo digitalizado a través de un cliente humano que haga las consultas en mi app.



#### - ¿Qué soluciones o mejoras propondrías para integrar estas áreas?


Una mejora sería crear una interfaz más sencilla para que los empleados no familiarizados con la tecnología puedan integrar fácilmente sus tareas manuales con el sistema digital. También se podrían implementar notificaciones automáticas o recordatorios para informar a los empleados sobre las tareas de inventario, y considerar integrar el sistema con otros programas de gestión (como un ERP) para sincronizar y actualizar los datos automáticamente entre las áreas digitalizadas y no digitalizadas.



### Criterio 6e) Necesidades presentes y futuras:

#### - ¿Qué necesidades actuales de la empresa resuelve tu software?

Mi software resuelve la necesidad de gestionar el inventario de manera eficiente y automatizada. Permite a las empresas realizar un seguimiento preciso de sus productos, evitando los errores humanos y la falta de visibilidad en el stock. A través de comandos en un bot de Telegram, los empleados pueden agregar, listar y eliminar productos de forma rápida, reduciendo el tiempo dedicado a tareas manuales y mejorando la precisión de los registros. Esto facilita el control de inventario en tiempo real, sin necesidad de herramientas externas o procesos complicados.


### Criterio 6f) Relación con tecnologías:

#### - ¿Qué tecnologías habilitadoras has empleado y cómo impactan en las áreas de la empresa?

He utilizado Firebase para la base de datos, Telegram para interactuar con los usuarios, y Python para automatizar procesos. Estas tecnologías impactan principalmente en la gestión de inventario, facilitando un sistema más rápido y accesible para los empleados.

#### - ¿Qué beneficios específicos aporta la implantación de estas tecnologías?

Estas tecnologías mejoran la precisión en la gestión del inventario, reducen errores humanos, y facilitan el acceso a la información. Además, automatizan tareas repetitivas, lo que libera tiempo para tareas más estratégicas.

### Criterio 6g) Brechas de seguridad:

#### - ¿Qué posibles brechas de seguridad podrían surgir al implementar tu software?

Por mi parte, solo se ha desarrollado "en local", por lo que en telegram y a la hora de ejecutarlo, se necesita un token y unas credenciles únicas concretas para poder usarlo correctamente. Estas credenciales no te las deja subir ni el propio github, por lo que asumo que si cualquier persona que las consiga hace un mal uso de ellas.

#### - ¿Qué medidas concretas propondrías para mitigarlas?

Para mitigar estas brechas, es recomendable utilizar autenticación de dos factores (2FA) para las cuentas de Telegram y Firebase, así como cifrar las comunicaciones entre el bot y el servidor. Además, las credenciales sensibles deben almacenarse de forma segura, utilizando herramientas como variables de entorno o servicios de gestión de secretos, en lugar de incluirlas directamente en el código.

### Criterio 6h) Tratamiento de datos y análisis:

#### - ¿Cómo se gestionan los datos en tu software y qué metodologías utilizas?



#### - ¿Qué haces para garantizar la calidad y consistencia de los datos?



