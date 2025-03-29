-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 28, 2025 at 03:13 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbtaller_mecanico`
--

-- --------------------------------------------------------

--
-- Table structure for table `clientes`
--

CREATE TABLE `clientes` (
  `cliente_id` int(10) NOT NULL,
  `usuario_id` int(10) NOT NULL,
  `nombre` varchar(10) NOT NULL,
  `rfc` varchar(20) NOT NULL,
  `telefono` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `clientes`
--

INSERT INTO `clientes` (`cliente_id`, `usuario_id`, `nombre`, `rfc`, `telefono`) VALUES
(1, 1, 'Joss', '123423425', '2354'),
(2, 1, 'Batman', 'SANFIJF3908', '3124235'),
(3, 3, 'Superman', 'WOGN', '33145');

-- --------------------------------------------------------

--
-- Table structure for table `detalle_reparacion`
--

CREATE TABLE `detalle_reparacion` (
  `detalle_id` int(10) NOT NULL,
  `folio` int(10) DEFAULT NULL,
  `pieza_id` int(10) DEFAULT NULL,
  `cantidad` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `detalle_reparacion`
--

INSERT INTO `detalle_reparacion` (`detalle_id`, `folio`, `pieza_id`, `cantidad`) VALUES
(1, 1, 1, 5),
(2, 1, 1, 1),
(3, 2, 1, 1),
(4, 3, 3, 20),
(5, 3, 1, 5),
(6, 4, 1, 5),
(7, 4, 3, 20),
(8, 4, 2, 10),
(9, 4, 2, 5);

-- --------------------------------------------------------

--
-- Table structure for table `piezas`
--

CREATE TABLE `piezas` (
  `pieza_id` int(10) NOT NULL,
  `descripcion` varchar(20) NOT NULL,
  `existencia` int(10) NOT NULL,
  `precio` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `piezas`
--

INSERT INTO `piezas` (`pieza_id`, `descripcion`, `existencia`, `precio`) VALUES
(1, 'Bujía', 25, 50),
(2, 'Pieza2', 25, 20.5),
(3, 'Pieza3', 30, 30.99);

-- --------------------------------------------------------

--
-- Table structure for table `reparaciones`
--

CREATE TABLE `reparaciones` (
  `folio` int(10) NOT NULL,
  `matricula` varchar(10) NOT NULL,
  `fecha_entrada` varchar(10) NOT NULL,
  `fecha_salida` varchar(10) NOT NULL,
  `usuario_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `reparaciones`
--

INSERT INTO `reparaciones` (`folio`, `matricula`, `fecha_entrada`, `fecha_salida`, `usuario_id`) VALUES
(1, 'X02', '1', '1', 1),
(2, 'X02', '1', '1', 1),
(3, 'X02', '1', '1', 1),
(4, 'X02', '1', '1', 1);

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `usuario_id` int(10) NOT NULL,
  `nombre` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `username` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `perfil` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`usuario_id`, `nombre`, `username`, `password`, `perfil`) VALUES
(1, 'Joss', 'Joss', 'Joss', 'Administrador'),
(2, 'Katy', 'Katy', 'Katy', 'Administrador'),
(3, 'Di', 'Di', 'Di', 'Auxiliar'),
(4, 'Ziz', 'Ziz', 'Zizumbo', 'Mecanico');

-- --------------------------------------------------------

--
-- Table structure for table `vehiculos`
--

CREATE TABLE `vehiculos` (
  `matricula` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cliente_id` int(10) NOT NULL,
  `marca` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `modelo` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `usuario_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vehiculos`
--

INSERT INTO `vehiculos` (`matricula`, `cliente_id`, `marca`, `modelo`, `usuario_id`) VALUES
('X01', 2, 'Dodge', 'Charger', 1),
('X02', 2, 'asf', 'sdf', 1),
('X03', 3, 'Coche', 'Coche', 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`cliente_id`),
  ADD KEY `usuario_id_fk` (`usuario_id`);

--
-- Indexes for table `detalle_reparacion`
--
ALTER TABLE `detalle_reparacion`
  ADD PRIMARY KEY (`detalle_id`),
  ADD KEY `folio_fk` (`folio`),
  ADD KEY `pieza_id_fk` (`pieza_id`);

--
-- Indexes for table `piezas`
--
ALTER TABLE `piezas`
  ADD PRIMARY KEY (`pieza_id`);

--
-- Indexes for table `reparaciones`
--
ALTER TABLE `reparaciones`
  ADD PRIMARY KEY (`folio`),
  ADD KEY `matriucla_fk` (`matricula`),
  ADD KEY `usuario_id_rep_fk` (`usuario_id`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`usuario_id`);

--
-- Indexes for table `vehiculos`
--
ALTER TABLE `vehiculos`
  ADD PRIMARY KEY (`matricula`),
  ADD KEY `usuario_id` (`usuario_id`),
  ADD KEY `cliente_id_fk` (`cliente_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `clientes`
--
ALTER TABLE `clientes`
  ADD CONSTRAINT `usuario_id_fk` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`usuario_id`);

--
-- Constraints for table `detalle_reparacion`
--
ALTER TABLE `detalle_reparacion`
  ADD CONSTRAINT `folio_fk` FOREIGN KEY (`folio`) REFERENCES `reparaciones` (`folio`),
  ADD CONSTRAINT `pieza_id_fk` FOREIGN KEY (`pieza_id`) REFERENCES `piezas` (`pieza_id`);

--
-- Constraints for table `reparaciones`
--
ALTER TABLE `reparaciones`
  ADD CONSTRAINT `matriucla_fk` FOREIGN KEY (`matricula`) REFERENCES `vehiculos` (`matricula`),
  ADD CONSTRAINT `usuario_id_rep_fk` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`usuario_id`);

--
-- Constraints for table `vehiculos`
--
ALTER TABLE `vehiculos`
  ADD CONSTRAINT `cliente_id_fk` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`cliente_id`),
  ADD CONSTRAINT `vehiculos_usuario_id_fk` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`usuario_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
