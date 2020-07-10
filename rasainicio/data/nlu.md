## intent:adios
- adios
- hasta luego
- fin
- hasta pronto

## intent:afirmacion
- si
- vale
- bien
- correcto

## intent:ayuda
- ayuda

## lookup:organismo
- avila
- zaragoza
- valladolid
- toledo
- murcia

## lookup:apellido1
   data/txt/primer_apellido.txt

## lookup:elemento
- recibos
- valores
- expedientes
- personas
- tributos

## lookup:concepto
- ibi
- mercados
- coche
- vehiculo
- guarderia

## lookup:mes
- enero
- febrero
- marzo
- abril
- mayo
- junio
- julio
- agosto
- septiembre
- octubre
- noviembre
- diciembre

## lookup:fecharelativa
- hoy
- mañana
- ayer
- semana pasada
- primera semana del mes
- primer dia del mes
- a primeros de año
- a final de año

## regex:dia
- [0-9]{2}/[0-9]{2}/[0-9]{4}

## intent:organismos
- organismos

## lookup:numerovoluntaria
- primera
- segunda
- tercera
- 1
- 2
- 3
- 4

## intent:intentvoluntaria
- voluntaria  [1](numerovoluntaria) [zaragoza](organismo)
- voluntaria  [2](numerovoluntaria) [avila](organismo)
- voluntaria  [primera](numerovoluntaria) [zaragoza](organismo)
- voluntaria [primera](numerovoluntaria) [zaragoza](organismo)
- voluntaria [segunda](numerovoluntaria) [avila](organismo)
- [avila](organismo) primera[numerovoluntaria] voluntaria
- [1](numerovoluntaria) voluntaria [zaragoza](organismo)
- [2](numerovoluntaria) voluntaria [avila](organismo)
- [primera](numerovoluntaria) voluntaria [zaragoza](organismo)
- [primera](numerovoluntaria) voluntaria [zaragoza](organismo)
- [segunda](numerovoluntaria) voluntaria [avila](organismo)
- [avila](organismo) primera[numerovoluntaria] voluntaria



## intent:intentfecha
- [15/11/2010](dia)
- [14/01/2011](dia)
- [12/12/2015](dia)
- [15/11/2018](dia)
- [14/01/2014](dia)
- [12/12/2015](dia)
- [15/11/2016](dia)
- [14/01/2018](dia)
- [12/12/2015](dia)
- [enero](mes)
- [marzo](mes)
- [septiembre](mes)
- [octubre](mes)
- [noviembre](mes)
- [hoy](fecharelativa)
- [mañana](fecharelativa)
- [ayer](fecharelativa)
- [semana pasada](fecharelativa)
- [primera semana del mes](fecharelativa)
- [primer dia del mes](fecharelativa)
- [ultima dia del mes](fecharelativa)

## regex:siglas
- [A-Z]{2}

## regex:num1
- [0-9]{1-4}

## regex:num2
- [0-9]{1-9}

## regex:letra
- [A-Z]{2}


## intent:intentdir
- [PS](siglas) [SAN ESTEBAN](calle) [10](num1)  
- [DS](siglas) [PANTANO BURGUIL](calle)   
- [CL](siglas) [CID](calle) [7](num1)  
- [CL](siglas) [CARLOS III](calle) [1](num1)  
- [AV](siglas) [CARRILET](calle) [220](num1)  [1](planta) [1](puerta) 
- [CL](siglas) [NUESTRA SEÑORA DE SONSOLES](calle) [14](num1)  [1](planta)
- [CL](siglas) [CASTILLO](calle) [68](num1)  
- [CL](siglas) [IGLESIA](calle) [10](num1) [0](escalera) [2](planta) [B](puerta) 
- [CL](siglas) [IGLESIA](calle) [10](num1) [B](escalera) [2](planta) [B](puerta) 
- [CL](siglas) [IGLESIA](calle) [10](num1) [A](escalera) [2](planta) [B](puerta) 
- [CL](siglas) [SANTA ANA](calle) [44](num1)  
- [CL](siglas) [SAN ANTONIO](calle) [1](num1)  
- [CR](siglas) [AVILA DE](calle) [36](num1)  
- [CL](siglas) [FUENTE MOLINO D](calle) [15](num1)  
- [CL](siglas) [HUERTA MARQUES](calle) [1](num1)  
- [AV](siglas) [CASTELLDEFELS](calle) [122](num1)  [1](planta) [02](puerta) 
- [CL](siglas) [RUISEÑOR](calle) [2](num1)  [2](planta) [B](puerta) 
- [CL](siglas) [POZO](calle) [15](num1)  
- [CL](siglas) [FLOR](calle) [16](num1)  
- [CL](siglas) [RASUEROS](calle) [2](num1)  
- [CL](siglas) [GENERAL ARANDA](calle)   
- [CL](siglas) [GRAL MOSCARDO](calle) [11](num1)  
- [CL](siglas) [SAN BERNARDO](calle)   
- [AV](siglas) [FUENTE DE ABAJO](calle) [20](num1)  
- [AV](siglas) [FUENTE DE ABAJO](calle) [43](num1)  
- [PZ](siglas) [ESPAÑA](calle) [4](num1)  
- [CL](siglas) [PILONCILLO DEL](calle) [14](num1)  
- [CL](siglas) [COLON](calle) [4](num1)  
- [CL](siglas) [COLON](calle) [5](num1)  
- [CL](siglas) [COLON](calle) [52](num1)  
- [CL](siglas) [EJERCITO ESPAÑOL](calle) [16](num1)  
- [CL](siglas) [MORAL](calle) [13](num1)  
- [CL](siglas) [ADUANA](calle) [5](num1)  
- [CL](siglas) [AVILA](calle) [2](num1)  
- [PZ](siglas) [FERIA](calle) [5](num1)  [1](planta) [A](puerta) 
- [CL](siglas) [HUMERA](calle) [23](num1)  
- [CL](siglas) [MESONES](calle) [2](num1)  
- [CL](siglas) [ARCO DEL](calle) [60](num1)  
- [CL](siglas) [EJERCITO ESPAÑOL](calle)   
- [CL](siglas) [CHILLA](calle) [15](num1)  
- [CL](siglas) [ADUANA](calle) [19](num1)  
- [PZ](siglas) [GENERALISIMO](calle) [9](num1)  
- [CL](siglas) [JOSE ANTONIO](calle) [1](num1)  
- [CL](siglas) [CAMPILLO](calle) [16](num1)  
- [CL](siglas) [ABAJO](calle) [76](num1)  
- [AG](siglas) [GUIJUELOS](calle) [53](num1)  
- [CL](siglas) [CAMPILLO](calle) [7](num1)  
- [CL](siglas) [ABAJO](calle) [60](num1)  
- [CL](siglas) [CAMPILLO](calle) [80](num1)  
- [UR](siglas) [PUENTE REGAJO](calle) [11](num1)  
- [CL](siglas) [CUART DE POBET](calle) [88](num1)  
- [ER](siglas) [RINCONADA](calle) [97](num1)  
- [ER](siglas) [RINCONADA](calle) [52](num1)  
- [CL](siglas) [ALENZA](calle) [70](num1)  
- [CM](siglas) [MADROÑOS DEL](calle) [120](num1)  
- [TR](siglas) [ZURBARAN](calle) [220](num1)  
- [PZ](siglas) [EJERCITO](calle) [6](num1)  [3](planta) [A](puerta) 

## lookup:lid
- liquidar
- lid
- liquidacion
- hacer liquidacion
- hacer lid

## intent:liquidar
-  [liquidar](lid)
-  [liquidar](lid) [ibi](concepto) desde [2018](desde) a [2018](hasta) con referencia catastral [AER](rc) en [AREVALO](municipio) a [JUAN SALVADOR SALVADOR](nombre)
-  en [AREVALO](municipio) [liquidar](lid) [ibi](concepto) desde [2018](desde) a [2018](hasta) con referencia catastral [AER](rc)  a [JUAN SALVADOR SALVADOR](nombre)
-  en [AREVALO](municipio) desde [2018](desde) a [2018](hasta) [liquidar](lid) [ibi](concepto)  con referencia catastral [AER](rc)  a [JUAN SALVADOR SALVADOR](nombre)
-  a [JUAN SALVADOR SALVADOR](nombre) en [AREVALO](municipio) desde [2018](desde) a [2018](hasta) [liquidar](lid) [ibi](concepto)  con referencia catastral [AER](rc) 
-  [liquidar](lid) [ibi](concepto) desde [2018](desde) a [2018](hasta) con matricula [9680ABC](matricula) en [AREVALO](municipio) a [JUAN SALVADOR SALVADOR](nombre)
-  en [AREVALO](municipio) [liquidar](lid) [ibi](concepto) desde [2018](desde) a [2018](hasta) con matricula [0125ABC](matricula)  a [JUAN SALVADOR SALVADOR](nombre)
-  en [AREVALO](municipio) desde [2018](desde) a [2018](hasta) [liquidar](lid) [coche](concepto)  con matricula [0655ABC](matricula)  a [JUAN SALVADOR SALVADOR](nombre)
-  [liquidar](lid) a [JUAN SALVADOR SALVADOR](nombre) en [AREVALO](municipio) desde [2018](desde) a [2018](hasta) [liquidar](lid) [coche](concepto)  con matricula [0655ABC](matricula) 
-  [lid](lid)
-  [lid](lid) [ibi](concepto) desde [2018](desde) a [2018](hasta) con referencia catastral [AER](rc) en [AREVALO](municipio) a [JUAN SALVADOR SALVADOR](nombre)
-  en [AREVALO](municipio) [lid](lid) [ibi](concepto) desde [2018](desde) a [2018](hasta) con referencia catastral [AER](rc)  a [JUAN SALVADOR SALVADOR](nombre)
-  en [AREVALO](municipio) desde [2018](desde) a [2018](hasta) [lid](lid) [ibi](concepto)  con referencia catastral [AER](rc)  a [JUAN SALVADOR SALVADOR](nombre)
-  a [JUAN SALVADOR SALVADOR](nombre) en [AREVALO](municipio) desde [2018](desde) a [2018](hasta) [lid](lid) [ibi](concepto)  con referencia catastral [AER](rc) 
-  [lid](lid) [ibi](concepto) desde [2018](desde) a [2018](hasta) con matricula [9680ABC](matricula) en [AREVALO](municipio) a [JUAN SALVADOR SALVADOR](nombre)
-  en [AREVALO](municipio) [lid](lid) [ibi](concepto) desde [2018](desde) a [2018](hasta) con matricula [0125ABC](matricula)  a [JUAN SALVADOR SALVADOR](nombre)
-  en [AREVALO](municipio) desde [2018](desde) a [2018](hasta) [lid](lid) [coche](concepto)  con matricula [0655ABC](matricula)  a [JUAN SALVADOR SALVADOR](nombre)
-  [lid](lid) a [JUAN SALVADOR SALVADOR](nombre) en [AREVALO](municipio) desde [2018](desde) a [2018](hasta) [lid](lid) [coche](concepto)  con matricula [0655ABC](matricula) 

## intent:reset
- limpiar

## intent:buscar
- [recibos](elemento)
- [valores](elemento)
- [avila](organismo)
- [zaragoza](organismo)
- [12232A](nif)
- [13332B](nif)
- [15432C](nif)
- [ABC](rc)
- [DEF](rc)
- [AAA](rc)
- [12343](nf))
- [43341213](nf))
- [1243434454](nf))
- [9898](expediente)
- [763242357781](expediente)
- [343434821](expediente)
- [7845622323](expediente)
- [recibos](elemento)  [zaragoza](organismo)
- [tributos](elemento) [murcia](organismo)
- [zaragoza](organismo)[recibos](elemento) 
- [murcia](organismo)  [tributos](elemento)  
- [recibos](elemento)  [zaragoza](organismo)  [12232E](nif)  
- [recibos](elemento)  [avila](organismo)     [ABC](rc)
- [recibos](elemento)  [zaragoza](organismo)  [12345778](expediente)
- [valores](elemento)  [avila](organismo)     [12232G](nif)  
- [valores](elemento)  [avila](organismo)     [ABC](rc)
- [valores](elemento)  [zaragoza](organismo)  [12345778](expediente)
- [tributos](elemento) [avila](organismo)     [12232E](nif)  
- [tributos](elemento) [zaragoza](organismo)  [ABC](rc)
- [tributos](elemento) [avila](organismo)     [12345778](expediente)
- [VIEJO HUERTA JOSE](nombre)
- [VIEJO HUERTA JOSE](nombre)
- [MAR DE PAULA SL](nombre)
- [MAR REPRESENTACIONES Y ACT IVIDADES SL](nombre)
- [MAR-BLANTELL SL](nombre)
- [MARA N MEDINA MARIA](nombre)
- [MARA N NAVARRO PILAR](nombre)
- [MARA N SANCHEZ LUIS MIGUEL](nombre)
- [MARABAJAN LOPEZ ISABEL HEREDEROS DE](nombre)
- [MARABE CORDON JOSE](nombre)
- [MAR REPRESENTACIONES Y ACT IVIDADES SL](nombre) [18762B](nif)
- [MAR-BLANTELL SL](nombre) [11232B](nif)
- [MARA N MEDINA MARIA](nombre) [13873B](nif)
- [MARA N NAVARRO PILAR](nombre) [19812B](nif)
- [MARA N SANCHEZ LUIS MIGUEL](nombre) [18762B](nif)
- [MARABAJAN LOPEZ ISABEL HEREDEROS DE](nombre) [14552B](nif)
- [MARABE CORDON JOSE](nombre)
- [MARABE GUERRA VICTORIANO](nombre)
- [MARABEL MANGAS JACINTO](nombre)
- [MARAL CONFETEX SL](nombre)
- [MARANAN MACATANGAY REDINDO](nombre)
- [MARANDI Y ASOCIADOS SL](nombre)
- [MARANT SERVICIOS EXPRESS SL](nombre)
- [MARAOUI HASSAN](nombre)
- [MARASCA OLIVARI IDILIO](nombre)
- [MARATAN GONZALEZ JULIO](nombre)
- [MARAVALL GOMEZ ALLENDE ELISA](nombre)
- [MARAVALL GOMEZ ALLENDE HECTOR](nombre)
- [MARAVER BOYER JOSE](nombre)
- [MARAVER DE KOBBE BEATRIZ CARMEN](nombre)
- [MARAZO PINEDO JESUS](nombre)
- [MARAZUELA AGUIRRE ANTONIO](nombre)
- [MARAZUELA BURGUILLO BLANCA](nombre)
- [MARAZUELA BURGUILLO JOSE MARIA](nombre)
- [MARAZUELA CB](nombre)
- [MARAZUELA CEJUDO ENRIQUE](nombre)
- [MARAZUELA CEJUDO FRANCISCO](nombre)
- [MARAZUELA DE JUAN FRANCISCO](nombre)
- [MARAZUELA DE JUAN M ALMUDENA](nombre)
- [MARAZUELA DE JUAN MARIA LUISA](nombre)
- [MARAZUELA DE JUAN MARIA SONSOLES](nombre)
- [MARAZUELA HERNANDEZ OSCAR](nombre)
- [MARAZUELA LOPEZ ANTONIO](nombre)
- [MARAZUELA LOPEZ FIDEL](nombre)
- [MARAZUELA LOPEZ MARCOS](nombre)
- [MARAZUELA LOPEZ MARIA](nombre)
- [MARAZUELA LOPEZ TEOFILO HEREDEROS DE](nombre)
- [MARAZUELA MARCELINA](nombre)
- [MARAZUELA ROBLEDO JOSEFA](nombre)
- [MARAZUELA VELICIA FRANCISCO](nombre)
- [MARAZUELA VELICIA RAIMUNDA](nombre)
- [MARAÑA CAMENO GLORIA](nombre)
- [MARAÑON ARNAUD FRANCISCO DE BORJA](nombre)
- [MARAÑON GARCIA DIONISIO](nombre)
- [MARAÑON HIDALGO MANUEL](nombre)
- [MARAÑON MENDIZABAL JOSE](nombre)
- [MARAÑON MORAGO ANDRES](nombre)
- [MARAÑON MORAGO ANDRES](nombre)
- [MARAÑON NAVARRO PILAR](nombre)
- [MARAÑON SANCHEZ ANDRES](nombre)
- [MARAÑON SANCHEZ LUIS MIGUEL](nombre)
- [MARAÑON SANCHEZ RICARDO](nombre)
- [MARAÑON SANCHEZ RUBEN](nombre)
- [MARAÑON SEQUEIROS ROXANA SILVIA](nombre)
- [MARAÑON VIVANCO EMILIA HEREDEROS DE](nombre)
- [MARBA CB](nombre)
- [MARBAN BLAZQUEZ ANA](nombre)
- [MARBAN DORADO ESTHER](nombre)
- [MARBAN HARO VICTOR](nombre)
- [MARBAN VELA RAFAEL](nombre)
- [MARBE COMERCIAL G M SA](nombre)
- [MARBELLA ALEGRE FRANCISCA](nombre)
- [MARBELLA ALEGRE GREGORIA](nombre)
- [MARBELLA ALEGRE PANTALEONA HEREDEROS DE](nombre)
- [MARBELLA ANDALUZ DIONISIO HEREDEROS DE](nombre)
- [MARBELLA ANDALUZ LORENZO HEREDEROS DE](nombre)
- [MARBELLA FERNANDEZ DAVID](nombre)
- [MARBELLA FERNANDEZ HILARIA JULIA](nombre)
- [MARBELLA FERNANDEZ JUAN MANUEL](nombre)
- [MARBELLA FERNANDEZ MANUEL HEREDEROS DE](nombre)
- [MARBELLA FRANCISCO](nombre)
- [MARBELLA FRANCISCO](nombre)
- [MARBELLA GAMO MARIANO](nombre)
- [MARBELLA GARCIA BENIGNA](nombre)
- [MARBELLA GARCIA ESTEBAN](nombre)
- [MARBELLA GARCIA ESTEBAN](nombre)
- [MARBELLA GARCIA ESTEBAN HROS](nombre)
- [MARBELLA GARCIA FABIAN](nombre)
- [MARBELLA GARCIA FILOMENA](nombre)
- [MARBELLA GARCIA TIMOTEO](nombre)
- [MARBELLA GARCIA TIMOTEO](nombre)
- [MARBELLA GARCIA TIMOTEO HROS](nombre)
- [MARBELLA GONZALEZ EUGENIA HEREDEROS DE](nombre)
- [tributos](elemento) [avila](organismo)  [MARTIN GARCIA JOSE](nombre)  [ABC](rc) 
- [avila](organismo) [tributos](elemento)  [ANTONIO GARCIA JOSE](nombre)   [MKJ](rc) 
- [tributos](elemento) [avila](organismo)  [MARTIN GARCIA JOSE](nombre)  [IUE](rc)
- [avila](organismo) [tributos](elemento)  [ANTONIO GARCIA JOSE](nombre) [DAD](rc)
- [GARCIA](apellido)
- [RODRIGUEZ](apellido)
- [GONZALEZ](apellido)
- [FERNANDEZ](apellido)
- [LOPEZ](apellido)
- [MARTINEZ](apellido)
- [SANCHEZ](apellido)
- [PEREZ](apellido)
- [GOMEZ](apellido)
- [MARTIN](apellido)
- [JIMENEZ](apellido)
- [RUIZ](apellido)
- [HERNANDEZ](apellido)
- [DIAZ](apellido)
- [MORENO](apellido)
- [MUÑOZ](apellido)
- [ALVAREZ](apellido)
- [ROMERO](apellido)
- [ALONSO](apellido)
- [GUTIERREZ](apellido)
- [NAVARRO](apellido)
- [TORRES](apellido)
- [DOMINGUEZ](apellido)
- [VAZQUEZ](apellido)
- [RAMOS](apellido)
- [GIL](apellido)
- [RAMIREZ](apellido)
- [SERRANO](apellido)
- [BLANCO](apellido)
- [MOLINA](apellido)
- [MORALES](apellido)
- [SUAREZ](apellido)
- [ORTEGA](apellido)
- [DELGADO](apellido)
- [CASTRO](apellido)
- [ORTIZ](apellido)
- [RUBIO](apellido)
- [MARIN](apellido)
- [SANZ](apellido)
- [NUÑEZ](apellido)
- [IGLESIAS](apellido)
- [MEDINA](apellido)
- [CORTES](apellido)
- [GARRIDO](apellido)
- [CASTILLO](apellido)
- [SANTOS](apellido)
- [LOZANO](apellido)
- [GUERRERO](apellido)
- [CANO](apellido)
- [PRIETO](apellido)
- [MENDEZ](apellido)
- [CRUZ](apellido)
- [CALVO](apellido)
- [HERRERA](apellido)
- [GALLEGO](apellido)
- [FLORES](apellido)
- [MARQUEZ](apellido)
- [LEON](apellido)
- [PEÑA](apellido)
- [VIDAL](apellido)
- [CABRERA](apellido)
- [CAMPOS](apellido)
- [VEGA](apellido)
- [FUENTES](apellido)
- [CARRASCO](apellido)
- [DIEZ](apellido)
- [REYES](apellido)
- [CABALLERO](apellido)
- [NIETO](apellido)
- [AGUILAR](apellido)
- [SANTANA](apellido)
- [PASCUAL](apellido)
- [HERRERO](apellido)
- [MONTERO](apellido)
- [HIDALGO](apellido)
- [LORENZO](apellido)
- [GIMENEZ](apellido)
- [IBAÑEZ](apellido)
- [FERRER](apellido)
- [SANTIAGO](apellido)
- [DURAN](apellido)
- [VARGAS](apellido)
- [BENITEZ](apellido)
- [MORA](apellido)
- [ARIAS](apellido)
- [VICENTE](apellido)
- [CARMONA](apellido)
- [CRESPO](apellido)
- [ROMAN](apellido)
- [SOTO](apellido)
- [PASTOR](apellido)
- [SAEZ](apellido)
- [VELASCO](apellido)
- [MOYA](apellido)
- [SOLER](apellido)
- [PARRA](apellido)
- [ROJAS](apellido)
- [ESTEBAN](apellido)
- [BRAVO](apellido)
- [GALLARDO](apellido)


## regex:zipcode
- [0-9]{5}

## regex:nif
- [0-9]{5}[A-Z]{1}

## regex:rc
- [A-Z]{3}

## regex:expediente
- [0-9]{8}

## regex:nf
- [0-9]{3-12}

## regex:amtricula
- [0-9]{4}[A-Z]{3}


## intent:ejemplos
- ejemplos

## intent:rechazo
- no
- nunca
- no vale
- incorrecto
- no es correcto

## regex:cantidad
- [0-9]{1,6}

## regex:numeroplazos
- [0-9]{1,6}


## intent:fraccionar
- fraccionar los recibos que debo en plazos de [123](cantidad)
- fraccionar en plazos de [431](cantidad)
- fraccionar en [3](numeroplazos)
- fraccionar en [6](numeroplazos)
- aplazar el pago
- aplazar el pago del [ibi](concepto)
- aplazar el pago del [coche](concepto) 
- pagar a plazos el [coche](concepto) 
- pagar a plazos el [ibi](concepto) 


## lookup:entidad
- nombre
- nif
- num1
- num2
- escalera

## regex:valor
- \s*

## intent:cambiar
- cambia [num1](entidad) a [1232](valor)
- cambia [num2](entidad) a [IDIERE](valor)
- cambia [num1](entidad) a [1232](valor)
- cambia [escalera](entidad) a [6](valor)

## regex:aaaa
- [0-9]{1,4}


## intent:cuenta_gestion_recaudatoria
- cuenta de gestión [2019](aaaa) [diciembre](mes) [arevalo](municipio) [central](oficina)
- cargos [2019](aaaa) [enero](mes) [municipio](municipio) [concepto](concepto) [estado](estado_cargo) [tipodevalor](tipo_valor) [oficina](oficina)
- recaudacion [2019](aaaa) [municipio](municipio)
- multas [2019](aaaa) [municipio](municipio) [estado](estado_cargo)
- ingresos [2019](aaaa) [enero](mes) del [15/12/2019](fecha_desde) al [16/12/2019](fecha_hasta)
- ingresos por forma de pago del [15/12/2019](fecha_desde) al [16/12/2019](fecha_hasta)
- posicion cuentas

## intent:derechos_reconocidos
- derechos reconocidos [2019](aaaa) [municipio](municipio) [concepto](concepto)
- derechos reconocidos [2019](aaaa) [municipio](municipio) [concepto](concepto)

## intent:voluntaria
- voluntaria [numerovoluntaria] [municipio](municipio) [oficina](oficina)
- voluntaria liquidaciones [2019](aaaa) [municipio](municipio) [mes]

## intent:ejecutiva
- ejecutiva [2019](aaaa) [municipio](municipio) [oficina](oficina)
- pendiente por antiguedad [2019](aaaa) [municipio](municipio) [oficina](oficina)
- pendiente por conceptos y años [2019](aaaa) [municipio](municipio) [oficina](oficina) [concepto]
- pendiente por importe y años [2019](aaaa) [municipio](municipio) [oficina](oficina)
- pendiente por situacion   [municipio](municipio) [oficina](oficina)

## intent:embargos
- embargo de [cuentas](tipo_embargo) [2019](aaaa)
- embargo de [salarios](tipo_embargo) [2019](aaaa)
- embargo de [pensiones](tipo_embargo) [2019](aaaa)
- embargo de [devoluciones](tipo_embargo) [2019](aaaa)

## intent:levantamiento_embargos
- levantamiento de embargos [2019](aaaa) [envio]

## intent:prescripcion
- [prescripcion](tipo_precripcion) [municipio](municipio) [oficina](oficina)
- [supendidos](tipo_precripcion)  [municipio](municipio) [oficina](oficina)
- [fallidos](tipo_precripcion)

## intent:concursales
- procesos concursales [comun](tipo_concursal)
- procesos concursales [convenio](tipo_concursal)
- procesos concursales [liquidacion](tipo_concursal)
- procesos concursales [conclusion](tipo_concursal)

## intent:expediente_gestion
- expedientes por fecha de alta desde [15/01/2019](desde) a [16/01/2019](hasta) [tipo](tipo) [subtipo](subtipo) [oficina](oficina)
- expedientes finalizados y pendientes [municipio](municipio) [oficina](oficina) [tipo](tipo) [subtipo](subtipo)  desde [15/01/2019](desde) a [16/01/2019](hasta)
- expedientes antiguedad [municipio](municipio) [oficina](oficina) [tipo](tipo) [subtipo](subtipo) [solicitudes_reclamaciones]
- expedientes gestiones por usuario [2019](aaaa) desde [15/01/2019](desde) a [16/01/2019](hasta)  [oficina](oficina) 
- expedientes parados
- presentaciones electronicas [ovt](forma_entrada) [tramite]
- presentaciones electronicas [registro](forma_entrada) [tramite]

## intent:notificaciones
- notificaciones

## intent:ibi
- ficheros doc desde [15/01/2019](desde) a [16/01/2019](hasta)
- evolucion titular desconocido [municipio](municipio)

## intent:registro_transmisiones
- registro trasmisiones del [2019](aaaa) [municipio](municipio) [notario](notario) [causa_transmision](causa_transmision)

## intent:multas
- multas control [2019](aaaa) [municipio](municipio) [fecha_infraccion](modo_multa)
- multas control [2019](aaaa) [municipio](municipio) [fecha_grabacion](modo_multa)
- multas prescripcion [municipio](municipio)

## intent:fraccionamientos
- fraccionamientos [2019](aaaa)  desde  [15/01/2019](desde) a [16/01/2019](hasta) [oficina](oficina) [quincenal](periodo)
- fraccionamientos [2019](aaaa)  desde  [15/01/2019](desde) a [16/01/2019](hasta) [oficina](oficina) [mensual](periodo)
- fraccionamientos [2019](aaaa)  desde  [15/01/2019](desde) a [16/01/2019](hasta) [oficina](oficina) [bimenstral](periodo)
- fraccionamientos [2019](aaaa)  desde  [15/01/2019](desde) a [16/01/2019](hasta) [oficina](oficina) [trimestral](periodo)
- fraccionamientos [2019](aaaa)  desde  [15/01/2019](desde) a [16/01/2019](hasta) [oficina](oficina) [semestral](periodo)
- fraccionamientos [2019](aaaa)  desde  [15/01/2019](desde) a [16/01/2019](hasta) [oficina](oficina) [anual](periodo)

## intent:asistencia
- asistencias oficina [oficina](oficina) desde [15/01/2019](desde) a [16/01/2019](hasta)
- asistencias usuario [usuario] desde [15/01/2019](desde) a [16/01/2019](hasta)
- asistencias interanual [2019](aaaa) [presencial](tipo_asistencia) [oficina](oficina)
- asistencias interanual [2019](aaaa) [mail](tipo_asistencia) [oficina](oficina)
- asistencias interanual [2019](aaaa) [telefono entradante](tipo_asistencia) [oficina](oficina)
- asistencias interanual [2019](aaaa) [telefono saliente](tipo_asistencia) [oficina](oficina)
- asistencias interanual [2019](aaaa) [ovt](tipo_asistencia) [oficina](oficina)

## intent:personas
- personas mantenimiento desde [15/01/2019](desde) a [16/01/2019](hasta)
- personas evolucion [2019](aaaa)
- direcciones incorrectas [2019](aaaa)
- tratamiento de censo AEAT 
