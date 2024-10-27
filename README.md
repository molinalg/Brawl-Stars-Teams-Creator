# Creador de Equipos Para Brawl Stars

## Descripción
"Brawl Stars Teams Creator" es un programa cuya finalidad fue crear equipos de máximo 3 personas para que jugaran juntos en la antigua Liga de Clubes de Brawl Stars. Estos se llevaban a cabo teniendo en cuenta ciertos aspectos que optimizaban la creación de equipos en los que todos los miembros pudieran compenetrarse bien y coincidir en sus horarios. 

**El programa fue utilizado activamente durante varios meses por un grupo de organizadores de clubes sirviendo de gran utilidad para automatizar procesos tediosos y temporalmente costosos generando además mejores resultados que los obtenidos de forma manual. Este grupo estaba a cargo de un total de 3 clubes dentro del juego con alrededor de 30 personas cada uno.**

**IMPORTANTE:** Por temas de privacidad se ha eliminado del código cualquier referencia a los clubes administrados al igual que el acceso a las hojas de cálculo utilizadas.

## Tabla de Contenidos
- [Qué es Brawl Stars](#qué-es-brawl-stars)
- [Motivo del Proyecto](#motivo-del-proyecto)
- [Funcionamiento del Sistema](#funcionamiento-del-sistema)
- [Criterios Utilizados Para la Creación de Equipos](#criterios-utilizados-para-la-creación-de-equipos)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Qué es Brawl Stars
Brawl Stars es un videojuego multijugador en línea desarrollado por Supercell y cuya versión beta fue lanzada en 2017. Desde entonces, se ha convertido en uno de los videojuegos más populares entre los jugadores de dispositivos móviles. 

En Brawl Stars, los jugadores pueden jugar diferentes modos de juego y formar los llamados "clubes" los cuales son agrupaciones de personas que cuentan con su propio chat privado para intercambiar mensajes y jugar juntos.

En el momento de creación de este programa, Brawl Stars contaba con un evento pensado para fomentar la colaboración de los diferentes miembros de un club llamado "Liga de Clubes". Este evento consistía en jugar partidas contra personas de diferentes clubes para ganar puntos de acuerdo al resultado obtenido. Los puntos ganados por todos los miembros del club se sumaban y el club con más puntos ganaba premios. **Además, los puntos ganados por cada partida jugada con gente del club se duplicaban lo que hacía que muchos líderes de clubes crearan equipos para que sus miembros jugaran juntos y ganar más puntos.**

Brawl Stars cuenta con una [API](https://developer.brawlstars.com/#/) pública que permitió la creación de este sistema.

## Motivo Del Proyecto
Este programa fue creado a partir de la necesidad de un grupo de administradores de clubes de agilizar ciertos procesos anteriormente realizados a mano. En concreto, **la creación de equipos para la Liga de Clubes era demasiado tediosa, repetitiva y consumía demasiado tiempo a los encargados** por lo que se creó este sistema para que los creara automáticamente. Las Ligas de Clubes ocurrían una vez cada 2 semanas por lo que un programa así **facilitó en gran manera el trabajo de estas personas**.

## Funcionamiento del Sistema
El sistema desarrollado cuenta con **3 principales procesos** necesarios para su correcto funcionamiento:

- **Datos de los miembros del club (Google Sheets):** Los equipos que genera este programa no son aleatorios sino que se optimizan según ciertos criterios que se numerarán en el siguiente apartado. Para poder operar con estos criterios, se requieren ciertos datos de las personas que serán agrupadas. Todas estas personas formaban parte de un servidor de Discord en común y se les solicitaba que rellenaran un **formulario de Google** para obtener cierta información sobre ellos necesaria para formar los equipos. **Las respuestas a este formulario se registraban automáticamente en una hoja de cálculo privada de Google, utilizada como base de datos.**

- **Procesado de los datos (API Google Sheets y Python):** Previo a la creación de los equipos, era necesario extraer y ordenar los datos de utilidad dentro de todos los guardados en la base de datos. Para ello, se decidió utilizar otro proyecto de hojas de cálculo de Google con una hoja para cada club (3 en total). El programa, desarrollado en Python, utiliza la **API de Google Sheets** y la **API de Brawl Stars** para extraer todas las entradas que correspondan a un miembro actual de uno de los 3 clubes y añadirlo a la nueva hoja, en concreto a la de su club. De esta forma, se obtenían listas ordenadas de los miembros de cada club y su información. De todo esto se encarga el script llamado "main.py" dentro del directorio "main".

- **Creación de los equipos (Python):** El último paso era la creación de los equipos. Una vez eran completados, teniendo en cuenta que iban a ser anunciados en un canal público del servidor de Discord, el programa generaba un mensaje genérico con la lista de todos los equipos y su horario y región para poder ser enviado directamente por los administradores. De todo esto se encarga el script "creador_equipos.py" en "team_managers".

Cabe destacar que el programa tuvo **una actualización que añadió funciones secundarias pero de utilidad como la posibilidad de asignar equipos prefabricados y la generación de estadísticas**. Estas estadísticas incluían el número de miembros de un club registrados en la base de datos y el número y nombre de aquellos que todavía no lo estaban con el fin de que los administradores se pusieran en contacto con ellos.

## Criterios Utilizados Para la Creación de Equipos
Los equipos que genera este programa cumplen las siguientes **normas**:

- En caso de que 2 o más miembros de un club quieran ir juntos, se les marcará con una etiqueta identificativa en la base de datos y **el programa les pondrá en el mismo equipo siempre**.

- El criterio principal a la hora de crear un equipo es su lugar de residencia que puede estar en una de las **3 regiones** identificadas por Supercell: Norteamérica y Latino América, Latino América del Sur y Europa, Oriente Medio y África. **Todos los integrantes de cada equipo deben de ser de la misma región** para compatibilizar horarios y optimizar el rendimiento del juego durante las partidas. La región de cada persona es uno de los datos pedidos en el formulario.

- El segundo criterio importante es **la disponibilidad horaria** que se divide en 3 posibilidades: por la mañana, por la tarde y por la noche. Los miembros pueden marcar en el formulario tantas opciones como correspondan en torno a su preferencia o disponibilidad para jugar con sus compañeros. Los equipos generados **se crean optimizando la coincidencia en esta elección asegurando que todos tengan al menos una opción coincidente**.

- Como es de esperar, los equipos que se generan para cada club **solo contienen miembros de un mismo club** ya que personas de diferentes clubes no pueden jugar juntos el evento.

## Licencia
Este proyecto está licenciado bajo la **Licencia MIT**. Esto significa que eres libre de usar, modificar y distribuir el software, pero debes incluir la licencia original y el aviso de derechos de autor en cualquier copia o porciones sustanciales del software.

## Contacto
En caso de que sea necesario, contactar con el dueño de este repositorio.
