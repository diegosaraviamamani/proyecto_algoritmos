# Proyecto para la materia de algoritmos

## Menu principal {#principal}

| Opciones                               | Descripción                       |
| -------------------------------------- | --------------------------------- |
| [Universidades](#modulo-universidades) | Nos envia al Módulo Universidades |
| [Estudiantes](#modulo-estudiantes)     | Nos envia al Módulo Estudiantes   |
| [Trabajadores](#modulo-trabajadores)   | Nos envia al Módulo Trabajadores  |
| Salir                                  | Salir del sistema                 |

## Menu Módulo Universidades {#modulo-universidades}

| Opciones                                   | Descripción                                                              |
| ------------------------------------------ | ------------------------------------------------------------------------ |
| Listar Universidades                       | Nos muestra la lista de universidades con su respectiva posición (index) |
| [Ingresar a una universidad](#universidad) | Pide el index de la universidad e ingresa al menu                        |
| Crear Nueva universidad                    | Pedir nombre, ciudad y crear nueva unviersidad                           |
| [Volver](#principal)                       | Nos envia al menu principal                                              |

### Menu Universidad {#universidad}

| Opciones             | Descripción                                        |
| -------------------- | -------------------------------------------------- |
| Mostrar Datos        | Nos mmuestra los datos de la univesidad            |
| Listar estudiantes   | Muestra la lista de estudiantes registrados        |
| Agregar estudiante   | Nos pide información para crear nuevo estudiante   |
| Listar Trabajadores  | Muestra la lista de trabajadores registrados       |
| Agregar Trabajador   | Nos pide información para crear nuevo trabajador   |
| Listar Departamentos | Muestra la lista de departamentos registrados      |
| Agregar Departamento | Nos pide información para crear nuevo departamento |
| [Volver](#principal) | Nos envia al menu principal                        |

## Menu Módulo Estudiantes {#modulo-estudiantes}

Podemos:

| Opciones                                 | Descripción                                         |
| ---------------------------------------- | --------------------------------------------------- |
| Listar Estudiantes                       | Nos muestra la lista de estudiantes                 |
| [Seleccionar un estudiante](#estudiante) | podemos hacer la seleccion de reigistro por la (CI) |
| Crear nuevo estudiante                   | Nos pide información para crear nuevo estudiante    |
| [volver](#principal)                     | Nos muestra lista de trabajadores resgistrados      |

### Menu Estudiante {#estudiante}

| Opciones                      | Descripción                                                      |
| ----------------------------- | ---------------------------------------------------------------- |
| Mostrar Datos Estudiantes     | Mostrar todos los datos del estudinte                            |
| Asignar a una universidad     | Listar universidades, y pedir index de la universidad a asignar. |
| [Volver](#modulo-estudiantes) | Nos envia al modulo estudiante                                   |

## Menu Modulo Trabajadores {#modulo-trabajadores}

| Opciones                            | Descripción                   |
| ----------------------------------- | ----------------------------- |
| [Ingresa a Modulo PDI](#modulo-pdi) | Nos envia al modulo PDI       |
| [Ingresa a Modulo PAS](#modulo-pas) | Nos envia al modulo PAS       |
| [Volver](#principal)                | Nos envia al modulo principal |

### Menu Modulo PDI {#modulo-pdi}

| Opciones                       | Descripción                               |
| ------------------------------ | ----------------------------------------- |
| Listar PDI                     | Nos muestra la lista de PDI               |
| [Seleccionar PDI](#pdi)        | Seleccion de las opciones de un PDI       |
| Nuevo PDI                      | Nos pide valores para crear un nuevo PDI. |
| [Volver](#modulo-trabajadores) | Nos envia al modulo estudiante            |

#### Menu PDI {#pdi}

| Opciones              | Descripción                                    |
| --------------------- | ---------------------------------------------- |
| Mostrar Datos         | Nos muestra la lista pdi                       |
| Asignar un trabajador | Se asigna un trabajador al puesto              |
| Método Investigar     | Nos muestra el resultado del método investigar |
| Método enseñar        | Nos muestra el resultado del método enseñar    |
| [Volver](#modulo-pdi) | Nos envia al modulo pdi                        |

### Menu Módulo PAS {#modulo-pas}

| Opciones                       | Descripción                               |
| ------------------------------ | ----------------------------------------- |
| Listar PAS                     | Nos muestra la lista de PAS               |
| [Seleccionar PAS](#pas)        | Seleccion de las opciones de un PAS       |
| Nuevo PAS                      | Nos pide valores para crear un nuevo PAS. |
| [Volver](#modulo-trabajadores) | Nos envia al modulo trabajadores          |

#### Menu PAS {#pas}

| Opciones              | Descripción                                    |
| --------------------- | ---------------------------------------------- |
| Mostrar Datos         | Nos muestra la lista pas                       |
| Método Investigar     | Nos muestra el resultado del método investigar |
| Método enseñar        | Nos muestra el resultado del método enseñar    |
| [Volver](#modulo-pas) | Nos envia al modulo pas                        |
