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
- 
- [0002415611](rc)
- [0007616398](rc)
- [0002840971](rc)
- [0013752379](rc)
- [0015451613](rc)
- [0008134842](rc)
- [0017952591](rc)
- [0014768005](rc)
- [0012460715](rc)
- [0018293470](rc)
- [0018497996](rc)
- [0013165722](rc)
- [0012403796](rc)
- [0007898072](rc)
- [0014727904](rc)
- [0011716210](rc)
- [0018307978](rc)
- [0008903811](rc)
- [0013380084](rc)
- [0007513621](rc)
- [0006826335](rc)
- [0004597800](rc)
- [0000911771](rc)
- [0012841438](rc)
- [0013456118](rc)
- [0000568810](rc)
- [0018925440](rc)
- [0013576574](rc)
- [0000815669](rc)
- [0008809169](rc)
- [0011629614](rc)
- [0012919559](rc)
- [0006520012](rc)
- [0003649163](rc)
- [0010954301](rc)
- [0009880889](rc)
- [0016306623](rc)
- [0009855786](rc)
- [0006645885](rc)
- [0008596838](rc)
- [0015621703](rc)
- [0009123882](rc)
- [0016105905](rc)
- [0011153896](rc)
- [0005681435](rc)
- [0008900630](rc)
- [0017733209](rc)
- [0011963814](rc)
- [0014161861](rc)
- [0002454133](rc)
- [0003980004](rc)
- [0007749352](rc)
- [0010103767](rc)
- [0007986089](rc)
- [0019786941](rc)
- [0018337180](rc)
- [0017229409](rc)
- [0001223494](rc)
- [0007361596](rc)
- [0009452431](rc)
- [0018845688](rc)
- [0009850770](rc)
- [0012097717](rc)
- [0011657001](rc)
- [0003339371](rc)
- [0015268636](rc)
- [0019943737](rc)
- [0007508091](rc)
- [0001941304](rc)
- [0002443778](rc)
- [0013437228](rc)
- [0009195894](rc)
- [0005636707](rc)
- [0016954151](rc)
- [0007428767](rc)
- [0008692090](rc)
- [0019255024](rc)
- [0005151702](rc)
- [0014565158](rc)
- [0018481990](rc)
- [0009350349](rc)
- [0016403915](rc)
- [0004699794](rc)
- [0014479952](rc)
- [0001737327](rc)
- [0002051916](rc)
- [0002164533](rc)
- [0017161495](rc)
- [0008212168](rc)
- [0005056239](rc)
- [0019297602](rc)
- [0000055387](rc)
- [0006955713](rc)
- [0002087822](rc)
- [0014385410](rc)
- [0004924880](rc)
- [0004738123](rc)
- [0002118463](rc)
- [0007435825](rc)
- [0013492506](rc)
- [215850H](nif)
- [234038J](nif)
- [273064P](nif)
- [359720T](nif)
- [441427B](nif)
- [516177B](nif)
- [539136Q](nif)
- [948856Z](nif)
- [965143V](nif)
- [1001529V](nif)
- [1112066Q](nif)
- [1123360V](nif)
- [1143054T](nif)
- [1378895E](nif)
- [1533803W](nif)
- [1777667C](nif)
- [1783344Q](nif)
- [1800136H](nif)
- [1894879R](nif)
- [2073103K](nif)
- [2470173L](nif)
- [4527796Q](nif)
- [5243014A](nif)
- [5355963E](nif)
- [6043961K](nif)
- [6369985C](nif)
- [6369986K](nif)
- [6379996A](nif)
- [6402509E](nif)
- [6402642V](nif)
- [6402643H](nif)
- [6402756Q](nif)
- [6402777Z](nif)
- [6402827H](nif)
- [6402905G](nif)
- [6402997G](nif)
- [6403086R](nif)
- [6403088A](nif)
- [6403144J](nif)
- [6403188B](nif)
- [6403233X](nif)
- [6446975Y](nif)
- [6452676](nif)
- [6463956J](nif)
- [6468367P](nif)
- [6468398Q](nif)
- [6490928Y](nif)
- [6491378L](nif)
- [6492293Z](nif)
- [6501142P](nif)
- [6502335M](nif)
- [6502529S](nif)
- [6502732B](nif)
- [6503051P](nif)
- [6503052D](nif)
- [6504213C](nif)
- [6510547Y](nif)
- [6514572Y](nif)
- [6514795E](nif)
- [6517129X](nif)
- [6518440X](nif)
- [6520401Q](nif)
- [6522969P](nif)
- [6524131C](nif)
- [6527823D](nif)
- [6529109F](nif)
- [6529421C](nif)
- [6529647Q](nif)
- [6532648G](nif)
- [6542925T](nif)
- [6544593N](nif)
- [6545348P](nif)
- [6545410R](nif)
- [6549195Z](nif)
- [6553461W](nif)
- [6554523Y](nif)
- [6554929K](nif)
- [6556554J](nif)
- [6557745P](nif)
- [6562871M](nif)
- [6567154X](nif)
- [6567386N](nif)
- [6567693C](nif)
- [6567763K](nif)
- [6569334M](nif)
- [6572877Y](nif)
- [6575019D](nif)
- [6580294V](nif)
- [6581378C](nif)
- [9369499N](nif)
- [11798283L](nif)
- [12608578R](nif)
- [15357604K](nif)
- [16732230Y](nif)
- [21683067R](nif)
- [23229240E](nif)
- [48341448W](nif)
- [50152744W](nif)
- [50179590F](nif)
- [50548156K](nif)
- [50713100D](nif)
- [51084261L](nif)
- [51092843E](nif)
- [51095651R](nif)
- [51352268F](nif)
- [51821517X](nif)
- [51839240T](nif)
- [51841848D](nif)
- [51972589H](nif)
- [51976997X](nif)
- [52503424J](nif)
- [64030880](nif)
- [70479453R](nif)
- [70742772Q](nif)
- [70779701F](nif)
- [70788021R](nif)
- [70797417J](nif)
- [70810401W](nif)
- [70814565A](nif)
- [70826981E](nif)
- [70835045J](nif)
- [72113334P](nif)
- [99099999Z](nif)
- [A 28078020](nif)
- [A 33591611](nif)
- [A 33789793](nif)
- [A 78564168](nif)
- [A 78793288](nif)
- [A 82716010](nif)
- [A 86521309](nif)
- [B 05009642](nif)
- [B 05113105](nif)
- [B 05126602](nif)
- [B 05134606](nif)
- [B 05159843](nif)
- [B 05198528](nif)
- [B 05222138](nif)
- [B 05235122](nif)
- [B 05239090](nif)
- [B 05244017](nif)
- [B 05259627](nif)
- [B 05261466](nif)
- [B 05262043](nif)
- [B 05264429](nif)
- [B 10182137](nif)
- [B 10474138](nif)
- [B 36283562](nif)
- [B 50350875](nif)
- [B 63922512](nif)
- [B 64430937](nif)
- [B 64629389](nif)
- [B 73464646](nif)
- [B 78893781](nif)
- [B 80802408](nif)
- [B 80806839](nif)
- [B 81330235](nif)
- [B 81330243](nif)
- [B 81417289](nif)
- [B 81764482](nif)
- [B 82827452](nif)
- [B 83157271](nif)
- [B 83192468](nif)
- [B 83669044](nif)
- [B 84028760](nif)
- [B 84303304](nif)
- [B 84596360](nif)
- [B 86085651](nif)
- [B 86185352](nif)
- [B 86503836](nif)
- [B 86553500](nif)
- [B 86622719](nif)
- [B 86760147](nif)
- [B 87988887](nif)
- [B 88098199](nif)
- [B 93285427](nif)
- [E 05229711](nif)
- [E 05232772](nif)
- [E 05248869](nif)
- [J 05207170](nif)
- [J 26206987](nif)
- [PAMPLONA/](nif)
- [S 05160041](nif)
- [U 47537923](nif)
- [V 63275259](nif)
- [V 63511554](nif)
- [V 63803969](nif)
- [V 65102576](nif)
- [V 83975060](nif)
- [V 84530526](nif)
- [V 84887579](nif)
- [X 1691406D](nif)
- [X 3734425F](nif)
- [X 4098604G](nif)
- [X 4586807D](nif)
- [X 5881902C](nif)
- [X 6624989T](nif)
- [X 6683892T](nif)
- [EX0011904248](expediente)
- [EX0007081215](expediente)
- [EX0001728821](expediente)
- [EX0011841184](expediente)
- [EX0001294602](expediente)
- [EX0018922197](expediente)
- [EX0004513901](expediente)
- [EX0004640898](expediente)
- [EX0005162807](expediente)
- [EX0006331824](expediente)
- [EX0009481261](expediente)
- [EX0004036020](expediente)
- [EX0011260920](expediente)
- [EX0012143062](expediente)
- [EX0010626538](expediente)
- [EX0012287485](expediente)
- [EX0015509403](expediente)
- [EX0002217035](expediente)
- [EX0005561219](expediente)
- [EX0003763139](expediente)
- [EX0006272541](expediente)
- [EX0011156558](expediente)
- [EX0008805170](expediente)
- [EX0011068512](expediente)
- [EX0005995026](expediente)
- [EX0016787655](expediente)
- [EX0005683548](expediente)
- [EX0008039207](expediente)
- [EX0013907580](expediente)
- [EX0018268742](expediente)
- [EX0015903819](expediente)
- [EX0007213338](expediente)
- [EX0012481190](expediente)
- [EX0015719198](expediente)
- [EX0012069702](expediente)
- [EX0004335905](expediente)
- [EX0017857982](expediente)
- [EX0016928662](expediente)
- [EX0007623707](expediente)
- [EX0016149863](expediente)
- [EX0005300435](expediente)
- [EX0002812557](expediente)
- [EX0003989638](expediente)
- [EX0001419882](expediente)
- [EX0014035249](expediente)
- [EX0019758960](expediente)
- [EX0014213636](expediente)
- [EX0011206622](expediente)
- [EX0011177055](expediente)
- [EX0016648266](expediente)
- [EX0018166666](expediente)
- [EX0012248934](expediente)
- [EX0011241375](expediente)
- [EX0008685587](expediente)
- [EX0012259578](expediente)
- [EX0005418555](expediente)
- [EX0014408405](expediente)
- [EX0004048052](expediente)
- [EX0018321370](expediente)
- [EX0009211971](expediente)
- [EX0004695932](expediente)
- [EX0009835489](expediente)
- [EX0012984250](expediente)
- [EX0008729993](expediente)
- [EX0001767636](expediente)
- [EX0013781443](expediente)
- [EX0000499380](expediente)
- [EX0007690719](expediente)
- [EX0012256078](expediente)
- [EX0014266592](expediente)
- [EX0008693150](expediente)
- [EX0009326216](expediente)
- [EX0008580148](expediente)
- [EX0012367422](expediente)
- [EX0018016414](expediente)
- [EX0013348035](expediente)
- [EX0009589650](expediente)
- [EX0001591985](expediente)
- [EX0009668199](expediente)
- [EX0010680569](expediente)
- [EX0004915087](expediente)
- [EX0012399463](expediente)
- [EX0000950033](expediente)
- [EX0012377533](expediente)
- [EX0011353137](expediente)
- [EX0000293520](expediente)
- [EX0013504650](expediente)
- [EX0010478881](expediente)
- [EX0016466291](expediente)
- [EX0017494723](expediente)
- [EX0008100916](expediente)
- [EX0017260204](expediente)
- [EX0003724927](expediente)
- [EX0000260039](expediente)
- [EX0009312311](expediente)
- [EX0012404392](expediente)
- [EX0004510555](expediente)
- [EX0008939312](expediente)
- [EX0014076169](expediente)
- [EX0013097176](expediente)

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
