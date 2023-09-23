-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: campeones_del_mundo
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `detalles_pedido`
--

DROP TABLE IF EXISTS `detalles_pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalles_pedido` (
  `ID_detalle` int NOT NULL AUTO_INCREMENT,
  `ID_pedido` int NOT NULL,
  `ID_producto` int NOT NULL,
  `Cantidad` int NOT NULL,
  `Subtotal` float NOT NULL,
  PRIMARY KEY (`ID_detalle`),
  KEY `ID_producto_idx` (`ID_producto`),
  KEY `ID_pedido_idx` (`ID_pedido`),
  CONSTRAINT `ID_pedido` FOREIGN KEY (`ID_pedido`) REFERENCES `pedidos` (`ID_pedido`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `ID_producto` FOREIGN KEY (`ID_producto`) REFERENCES `productos` (`ID_Producto`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalles_pedido`
--

LOCK TABLES `detalles_pedido` WRITE;
/*!40000 ALTER TABLE `detalles_pedido` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalles_pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `formas_de_pago`
--

DROP TABLE IF EXISTS `formas_de_pago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `formas_de_pago` (
  `ID_Forma_de_pago` int NOT NULL AUTO_INCREMENT,
  `Descripcion` varchar(150) NOT NULL,
  PRIMARY KEY (`ID_Forma_de_pago`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `formas_de_pago`
--

LOCK TABLES `formas_de_pago` WRITE;
/*!40000 ALTER TABLE `formas_de_pago` DISABLE KEYS */;
INSERT INTO `formas_de_pago` VALUES (1,'Transferencia'),(2,'Debito'),(3,'Tarjeta De Credito');
/*!40000 ALTER TABLE `formas_de_pago` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `formas_depago_pedidos`
--

DROP TABLE IF EXISTS `formas_depago_pedidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `formas_depago_pedidos` (
  `ID_Forma_depago_Pedidos` int NOT NULL AUTO_INCREMENT,
  `ID_pedido` int NOT NULL,
  `ID_forma_de_pago` int NOT NULL,
  `ID_tarjeta` int DEFAULT NULL,
  PRIMARY KEY (`ID_Forma_depago_Pedidos`),
  KEY `ID_pedido_idx` (`ID_pedido`),
  KEY `ID_forma_de_pago_idx` (`ID_forma_de_pago`),
  KEY `ID_tarjeta_idx` (`ID_tarjeta`),
  CONSTRAINT `FK_ID_forma_de_pago` FOREIGN KEY (`ID_forma_de_pago`) REFERENCES `formas_de_pago` (`ID_Forma_de_pago`),
  CONSTRAINT `FK_ID_pedido` FOREIGN KEY (`ID_pedido`) REFERENCES `pedidos` (`ID_pedido`),
  CONSTRAINT `FK_ID_tarjeta` FOREIGN KEY (`ID_tarjeta`) REFERENCES `tarjetas` (`ID_Tarjeta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `formas_depago_pedidos`
--

LOCK TABLES `formas_depago_pedidos` WRITE;
/*!40000 ALTER TABLE `formas_depago_pedidos` DISABLE KEYS */;
/*!40000 ALTER TABLE `formas_depago_pedidos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedidos`
--

DROP TABLE IF EXISTS `pedidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedidos` (
  `ID_pedido` int NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `ID_usuario` int NOT NULL,
  `Total` float NOT NULL,
  `Estado` enum('ACEPTADO','CANCELADO') NOT NULL,
  PRIMARY KEY (`ID_pedido`),
  KEY `ID_usuario_idx` (`ID_usuario`),
  CONSTRAINT `ID_usuario` FOREIGN KEY (`ID_usuario`) REFERENCES `usuarios` (`ID_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedidos`
--

LOCK TABLES `pedidos` WRITE;
/*!40000 ALTER TABLE `pedidos` DISABLE KEYS */;
/*!40000 ALTER TABLE `pedidos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `ID_Producto` int NOT NULL AUTO_INCREMENT,
  `Nombre_producto` varchar(45) NOT NULL,
  `Descripcion` text NOT NULL,
  `Precio` float NOT NULL,
  PRIMARY KEY (`ID_Producto`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'1930 Uruguay Titular','Celebra el legado de Uruguay como el primer campeón mundial con esta camiseta histórica. Los colores celeste y blanco evocan la pasión y la gloria de aquel lejano torneo que marcó el comienzo de una tradición futbolística',25000),(2,'1930 Uruguay Suplente','Camiseta suplente utilizada por el Seleccionado Uruguayo en el primer mundial de la historia',20000),(3,'1934 Italia Titular','Rinde homenaje a Italia como anfitrión del Mundial 1934 con esta camiseta clásica. El azul y el blanco de la Azzurri simbolizan la victoria en casa y la destreza futbolística que los llevó al triunfo',25000),(4,'1934 Italia Suplente ','Camiseta suplente utilizada por el conjunto Italiano en donde obtuvo su primer mundial',20000),(5,'1938 Italia Titular ','Conmemora la segunda victoria consecutiva de Italia en el Mundial 1938 con esta elegante camiseta. El azul y el blanco te transportarán al momento en que Italia consolidó su dominio en el fútbol mundial',30000),(6,'1938 Italia Suplente','Obten la camiseta suplente del primer equipo que obtuvo el titulo mundial por 2da vez consecutiva',20000),(7,'1950 Uruguay Titular','Revive el milagro de Maracaná con esta camiseta icónica de Uruguay. El celeste y blanco te llevarán de vuelta al partido final en el que Uruguay derrotó a Brasil en uno de los momentos más legendarios de la historia del fútbol',25000),(8,'1950 Uruguay Suplente','Accede a la oportunidad unica de obtener la camiseta suplente usada por el conjunto Uruguayo utilizada en el mundial realizado en Brazil ',20000),(9,'1954 Alemania Titular','Celebra la victoria de Alemania en el Mundial 1954 con esta camiseta nostálgica. El blanco y negro evocan la época dorada de Fritz Walter y Helmut Rahn. Únete a la tradición futbolística alemana y conmemora su primera victoria en un Mundial',30000),(10,'1954 Alemania Suplente','Camiseta suplente utilizada por el conjunto Aleman en el mundial realizado en Suiza',20000),(11,'1958 Brazil Titular','Celebra la gloria de Brasil en el Mundial 1958 con esta camiseta icónica. Lleva los colores amarillo y verde que simbolizan la pasión y la destreza futbolística de la selección brasileña. Revive el momento en que Pelé y compañía se coronaron campeones por primera vez en Suecia',30000),(12,'1958 Brazil Suplente','Oportunidad unica de conseguir la camiseta historica suplente de Brazil,utilizada en el mundial de Suecia donde se corono por primera vez como el campeon del mundo',25000),(13,'1962 Brazil Titular','Rinde homenaje a la segunda victoria consecutiva de Brasil en el Mundial 1962 con esta camiseta clásica. Los colores amarillo y verde representan la supremacía de Brasil en el fútbol mundial',30000),(14,'1962 Brazil Suplente','Adquiere la camiseta suplente de la verdeamarela,donde se consagro campeon por 2da vez de manera consecutiva en el mundial realizado en chile',25000),(15,'1966 Inglaterra Titular','Conmemora el histórico triunfo de Inglaterra en el Mundial 1966 con esta camiseta clásica. El rojo y el blanco de la bandera inglesa se combinan en esta prenda que recuerda la hazaña de Bobby Moore y Geoff Hurst en casa',30000),(16,'1966 Inglaterra Suplente','Camiseta utilizada por la seleccion Inglesa en el mundial realizado en dicho pais,donde se corono por primera y unica vez en su historia',25000),(17,'1970 Brazil Titular ','Revive el fútbol mágico de Brasil en el Mundial 1970 con esta camiseta legendaria. Los colores amarillo y verde te transportarán a la época en que Pelé, Jairzinho y Tostão deslumbraron al mundo con su juego',30000),(18,'1970 Brazil Suplente','Una de las camisetas mas iconicas de la historia del futbol.Considerado uno de los mejores equipos de la historia del futbol',25000),(19,'1974 Alemania Titular','Celebra la victoria de Alemania en el Mundial 1974 con esta camiseta histórica. El blanco y negro, junto con el toque de rojo, recuerdan la actuación de Gerd Müller y Franz Beckenbauer en casa',30000),(20,'1974 Alemania Suplente','Camiseta suplente del equipo Aleman usada en el mundial realizado en dicho pais',25000),(21,'1978 Argentina Titular ','Rinde homenaje a Argentina como país anfitrión del Mundial 1978 con esta camiseta clásica. Los colores celeste y blanco representan el triunfo de la Albiceleste en un torneo lleno de emoción y drama',35000),(22,'1978 Argentina Suplente','Camiseta suplente utilizada por la seleccion Argentina con la cual obtuvo su primer titulo mundial',30000),(23,'1982 Italia Titular ','Conmemora la victoria de Italia en el Mundial 1982 con esta elegante camiseta. El azul y el blanco te transportarán a España, donde Paolo Rossi y Dino Zoff se convirtieron en héroes nacionales',30000),(24,'1982 Italia Suplente','Obten la camiseta suplente del conjunto Italiano',25000),(25,'1986 Argentina Titular','Revive la magia de Diego Maradona en el Mundial 1986 con esta camiseta icónica de Argentina. Los colores celeste y blanco te llevarán de vuelta a México, donde Maradona dejó su huella con el \"Gol del Siglo\" y la \"Mano de Dios\"',35000),(26,'1986 Argentina Suplente','Oportunidad unica de obtener la camiseta suplente de Argentina con la que el Diego desplego toda su magia',30000),(27,'1990 Alemania Titular ','Camiseta Titular utilizada por el conjunto Aleman donde derroto a la seleccion Argentina en una de las finales mas polemicas de los mundiales',25000),(28,'1990 Alemania Suplente','Obten la camiseta suplente utilizada por el conjunto Aleman en el mundial realizado en Italia',20000),(29,'1994 Brazil Titular','Conmemora el cuarto título de Brasil en el Mundial 1994 con esta camiseta elegante. Los colores amarillo y verde te recordarán la destreza de Romário y Bebeto en Estados Unidos',30000),(30,'1994 Brazil Suplente','Camiseta suplente del conjunto brasilero que utilizo en el mundial realizado en estados unidos,donde obtuvo su 4ta copa mundial',20000),(31,'1998 Francia Titular','Rinde homenaje a la victoria de Francia en el Mundial 1998 con esta camiseta moderna y elegante. Los colores azul y blanco, con un toque de rojo, simbolizan la unidad y la fuerza de Les Bleus',30000),(32,'1998 Francia Suplente','Camiseta suplente utilizada por el conjunto Frances que se jugo en dicho pais,donde obtuvo su primera conquista a nivel mundial',20000),(33,'2002 Brazil Titular','Celebra la quinta corona mundial de Brasil en el Mundial 2002 con esta camiseta icónica. Los colores amarillo y verde te transportarán a Japón y Corea del Sur, donde Ronaldo se convirtió en el máximo goleador del torneo',30000),(34,'2002 Brazil Suplente','Camiseta Suplente utilizada por el conjunto brasilero jugado en korea/japon,donde obtuvo el pentacampeonato,record que al dia de hoy lo sostiene ',20000),(35,'2006 Italia Titular','Revive el triunfo de Italia en el Mundial 2006 con esta camiseta nostálgica. El azul y el blanco te llevarán de vuelta a Alemania, donde Fabio Cannavaro y Gianluigi Buffon lideraron a la Azzurri hacia la victoria',30000),(36,'2006 Italia Suplente','Obten la camiseta suplente del conjunto Italiano con la que obtuvo su cuarta copa del mundo',20000),(37,'2010 España Titular','Celebra el primer triunfo de España en el Mundial 2010 con esta camiseta de estilo moderno. El rojo y el dorado te transportarán al emocionante fútbol tiki-taka que conquistó el mundo',30000),(38,'2010 España Suplente','Adquiere la camiseta suplente con la que españa consiguio su primer mundial',20000),(39,'2014 Alemania Titular','Celebra el cuarto título de la Copa del Mundo de Alemania con esta camiseta emblemática. El negro y rojo reflejan la determinación y el espíritu de equipo que llevó a la selección alemana a la gloria en Brasil',30000),(40,'2014 Alemania Suplente','Mitica camiseta suplente de Alemania que utilizo en el mundial celebrado en Brazil,ganandole la final a nada menos que a Argentina con un Lionel Messi en su prime',20000),(41,'2018 Francia Titular','Conmemora el 2do titulo obtenido por el conjunto Frances,de la mano de unas de las selecciones mas jovenes de la historia',30000),(42,'2018 Francia Suplente','Camiseta suplente utilizada por el conjunto Frances donde alcanzo su 3ra copa mundial,de la mano de uno de los jugadores mas jovenes en ganarla en la historia,Kilian Mbappe',20000),(43,'2022 Argentina Titular','¡Se dio! la mitica camiseta Titular con la que jugo Argentina y logro el 3er mundial de su historia,y el primer titulo obtenido por considerado mejor de la historia por la mayoria del ambito futbolistico,Lionel Messi',40000),(44,'2022 Argentina Suplente','Camiseta suplente utilizada por el conjunto Argentino en el mundial realizado en Qatar',30000);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos_talles`
--

DROP TABLE IF EXISTS `productos_talles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos_talles` (
  `ID_producto_talle` int NOT NULL AUTO_INCREMENT,
  `ID_producto` int NOT NULL,
  `ID_talle` int NOT NULL,
  `Stock` int NOT NULL,
  PRIMARY KEY (`ID_producto_talle`),
  KEY `ID_talle_idx` (`ID_talle`),
  KEY `producto_ID_idx` (`ID_producto`),
  CONSTRAINT `ID_talle` FOREIGN KEY (`ID_talle`) REFERENCES `talles` (`ID_talle`),
  CONSTRAINT `producto_ID` FOREIGN KEY (`ID_producto`) REFERENCES `productos` (`ID_Producto`)
) ENGINE=InnoDB AUTO_INCREMENT=233 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos_talles`
--

LOCK TABLES `productos_talles` WRITE;
/*!40000 ALTER TABLE `productos_talles` DISABLE KEYS */;
INSERT INTO `productos_talles` VALUES (1,1,1,110),(2,1,2,80),(3,1,3,60),(4,1,4,60),(5,1,5,60),(6,1,6,20),(7,2,1,60),(8,2,2,70),(9,2,3,60),(10,2,4,70),(11,2,5,115),(12,3,1,40),(13,3,2,50),(14,3,3,60),(15,3,4,50),(16,3,5,60),(17,4,1,50),(18,4,2,40),(19,4,3,50),(20,4,4,50),(21,4,5,60),(22,4,6,25),(23,5,1,40),(24,5,2,50),(25,5,3,60),(26,5,4,60),(27,5,5,50),(28,5,6,25),(29,6,1,50),(30,6,2,60),(31,6,3,80),(32,6,4,80),(33,6,5,45),(34,7,1,50),(35,7,2,68),(36,7,3,40),(37,7,4,90),(38,7,5,60),(39,8,1,45),(40,8,2,60),(41,8,3,55),(42,8,4,55),(43,8,5,60),(44,9,1,50),(45,9,2,70),(46,9,3,68),(47,9,4,72),(48,9,5,60),(49,9,6,25),(50,10,1,40),(51,10,2,70),(52,10,3,80),(53,10,4,69),(54,10,5,60),(55,11,1,40),(56,11,2,80),(57,11,3,70),(58,11,4,60),(59,11,5,80),(60,12,1,60),(61,12,2,70),(62,12,3,90),(63,12,4,45),(64,12,5,50),(65,13,1,55),(66,13,2,80),(67,13,3,90),(68,13,4,90),(69,13,5,100),(70,13,6,40),(71,14,1,50),(72,14,2,60),(73,14,3,90),(74,14,4,75),(75,14,5,90),(76,15,1,90),(77,15,2,60),(78,15,3,80),(79,15,4,80),(80,15,5,80),(81,16,1,80),(82,16,2,50),(83,16,3,80),(84,16,4,90),(85,16,5,90),(86,17,1,60),(87,17,2,60),(88,17,3,60),(89,17,4,80),(90,17,5,80),(91,17,6,25),(92,18,1,60),(93,18,2,65),(94,18,3,66),(95,18,4,50),(96,18,5,70),(97,19,1,60),(98,19,2,50),(99,19,3,60),(100,19,4,60),(101,19,5,70),(102,20,1,60),(103,20,2,70),(104,20,3,50),(105,20,4,60),(106,20,5,60),(107,21,1,70),(108,21,2,50),(109,21,3,60),(110,21,4,60),(111,21,5,70),(112,21,6,20),(113,22,1,70),(114,22,2,80),(115,22,3,60),(116,22,4,60),(117,22,5,80),(118,23,1,60),(119,23,2,80),(120,23,3,80),(121,23,4,60),(122,23,5,70),(123,24,1,80),(124,24,2,70),(125,24,3,70),(126,24,4,90),(127,24,5,70),(128,25,1,70),(129,25,2,80),(130,25,3,50),(131,25,4,60),(132,25,5,60),(133,26,1,60),(134,26,2,80),(135,26,3,60),(136,26,4,70),(137,26,5,60),(138,27,1,60),(139,27,2,90),(140,27,3,60),(141,27,4,50),(142,27,5,90),(143,28,1,60),(144,28,2,60),(145,28,3,50),(146,28,4,70),(147,28,5,80),(148,29,1,90),(149,29,2,60),(150,29,3,70),(151,29,4,60),(152,29,5,70),(153,29,6,25),(154,30,1,40),(155,30,2,50),(156,30,3,50),(157,30,4,60),(158,30,5,90),(159,31,1,60),(160,31,2,70),(161,31,3,60),(162,31,4,60),(163,31,5,75),(164,32,1,60),(165,32,2,60),(166,32,3,50),(167,32,4,80),(168,32,5,70),(169,33,1,60),(170,33,2,50),(171,33,3,60),(172,33,4,60),(173,33,5,80),(174,34,1,80),(175,34,2,60),(176,34,3,60),(177,34,4,100),(178,34,5,60),(179,35,1,50),(180,35,2,60),(181,35,3,60),(182,35,4,50),(183,35,5,70),(184,35,6,20),(185,36,1,60),(186,36,2,60),(187,36,3,60),(188,36,4,80),(189,36,5,80),(190,37,1,50),(191,37,2,60),(192,37,3,60),(193,37,4,60),(194,37,5,70),(195,38,1,60),(196,38,2,60),(197,38,3,60),(198,38,4,80),(199,38,5,90),(200,39,1,60),(201,39,2,60),(202,39,3,60),(203,39,4,60),(204,39,5,70),(205,40,1,70),(206,40,2,80),(207,40,3,60),(208,40,4,60),(209,40,5,60),(210,41,1,80),(211,41,2,70),(212,41,3,70),(213,41,4,60),(214,41,5,60),(215,42,1,80),(216,42,2,70),(217,42,3,60),(218,42,4,60),(219,42,5,60),(220,42,6,20),(221,43,1,50),(222,43,2,50),(223,43,3,50),(224,43,4,90),(225,43,5,90),(226,43,6,90),(227,44,1,50),(228,44,2,60),(229,44,3,60),(230,44,4,90),(231,44,5,90),(232,44,6,90);
/*!40000 ALTER TABLE `productos_talles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `talles`
--

DROP TABLE IF EXISTS `talles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `talles` (
  `ID_talle` int NOT NULL AUTO_INCREMENT,
  `Talle` varchar(45) NOT NULL,
  PRIMARY KEY (`ID_talle`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `talles`
--

LOCK TABLES `talles` WRITE;
/*!40000 ALTER TABLE `talles` DISABLE KEYS */;
INSERT INTO `talles` VALUES (1,'XS'),(2,'S'),(3,'M'),(4,'L'),(5,'XL'),(6,'XXL');
/*!40000 ALTER TABLE `talles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tarjetas`
--

DROP TABLE IF EXISTS `tarjetas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tarjetas` (
  `ID_Tarjeta` int NOT NULL AUTO_INCREMENT,
  `Nombre_tarjeta` varchar(100) NOT NULL,
  PRIMARY KEY (`ID_Tarjeta`),
  UNIQUE KEY `Nombre_tarjeta_UNIQUE` (`Nombre_tarjeta`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tarjetas`
--

LOCK TABLES `tarjetas` WRITE;
/*!40000 ALTER TABLE `tarjetas` DISABLE KEYS */;
INSERT INTO `tarjetas` VALUES (3,'American Express'),(2,'Mastercard'),(4,'Pay Pal'),(1,'Visa');
/*!40000 ALTER TABLE `tarjetas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `ID_usuario` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Apellido` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Dni` int NOT NULL,
  `Domicilio` varchar(150) NOT NULL,
  `rol` enum('CLIENTE','ADMIN') NOT NULL,
  PRIMARY KEY (`ID_usuario`),
  UNIQUE KEY `Dni_UNIQUE` (`Dni`),
  UNIQUE KEY `Email_UNIQUE` (`Email`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Jose','Perez','joseperez@gmail.com',33520555,'Chacabuco 200','CLIENTE'),(2,'Diego','Lopez','diegolopez@gmail.com',20222222,'Lima 193','CLIENTE'),(3,'Octavio','Gimenez','octa12@gmail.com',40897789,'Peru 56','CLIENTE'),(4,'Gustavo ','Toscano','gustavotoscano@gmail.com',33666555,'Rondeau 400','ADMIN'),(5,'Cristian','Becarren','cristianbe@gmail.com',40444555,'Las heras 1333','CLIENTE'),(6,'Victoria','Urcula','vicky@gmail.com',30000111,'Delfin 12','CLIENTE'),(7,'Lautaro','Ibarra','lautyiii@gmail.com',36322123,'Colon 4000','CLIENTE'),(8,'Lucas','Peretti','luquitas@gmail.com',20222333,'General Paz 230','CLIENTE');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-23  4:32:24
