-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 23, 2022 at 07:06 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pharmacy_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `sr.` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(20) NOT NULL,
  `image` varchar(100) NOT NULL DEFAULT 'default.jpg'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`sr.`, `name`, `email`, `password`, `image`) VALUES
(1, 'Rutik Yogesh Ekre', 'rutik@gmail.com', '123', 'rutik@gmail.jpg'),
(2, 'Saurabh Talegaonkar', 'saurabh@gmail.com', '456', 'saurabh@gmail.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `medicine_stock`
--

CREATE TABLE `medicine_stock` (
  `sr_no` int(11) NOT NULL,
  `medicine_name` varchar(150) NOT NULL,
  `company` varchar(100) NOT NULL,
  `mfg` varchar(50) NOT NULL,
  `expiry` varchar(50) NOT NULL,
  `unit_price` float NOT NULL,
  `total_units` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `medicine_stock`
--

INSERT INTO `medicine_stock` (`sr_no`, `medicine_name`, `company`, `mfg`, `expiry`, `unit_price`, `total_units`) VALUES
(1, 'paracitamol', 'fdc', '2022-04-06', '2022-05-06', 1, 990),
(2, 'corex', 'amt', '2/12/2021', '11/12/2022', 50, 500),
(3, 'crocine', 'fdc', '12/12/2021', '11/12/2022', 56.8, 10),
(4, 'vics', 'p&g', '12/12/2021', '11/12/2022', 12.5, 80),
(7, 'naprocine', 'na', '2022-04-08', '2022-05-07', 9, 900),
(8, 'balm', 'zandu', '2022-04-08', '2022-04-30', 14, 12),
(9, 'naprocine', 'na', '2022-04-08', '2022-05-07', 8, 900),
(10, 'strepsil', 'fdcorp', '2022-04-03', '2022-04-12', 7, 350),
(11, 'ecosprin', 'fdc', '2022-04-02', '2022-05-01', 166, 285),
(12, 'forcox', 'fdc', '2022-04-02', '2022-04-30', 144.9, 123),
(13, 'ecosprin', 'fdc', '2022-04-02', '2022-05-01', 166, 189),
(14, 'Zandu Balm', 'zandu', '2022-04-08', '2022-04-30', 25, 12),
(15, 'corex', 'Emcure', '2022-04-01', '2022-04-30', 50, 500),
(16, 'saurya Balm', 'Self', '2022-04-06', '2022-05-05', 2, 120),
(17, 'crocine', 'fd corp', '2022-04-06', '2022-04-07', 56.8, 10),
(18, 'saurya Balm', 'Self', '2022-04-06', '2022-05-05', 2, 120),
(19, 'vaseline', 'vaseline', '2022-04-18', '2022-05-18', 49, 10);

-- --------------------------------------------------------

--
-- Table structure for table `patient_prescription`
--

CREATE TABLE `patient_prescription` (
  `sr_no` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `age` int(11) NOT NULL,
  `mob` varchar(15) NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  `dr_name` varchar(100) NOT NULL,
  `hosp_name` varchar(150) NOT NULL,
  `description` text NOT NULL,
  `qty` text NOT NULL,
  `expiry` text NOT NULL,
  `unit_price` text NOT NULL,
  `total` double NOT NULL,
  `admin` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `patient_prescription`
--

INSERT INTO `patient_prescription` (`sr_no`, `name`, `age`, `mob`, `date`, `dr_name`, `hosp_name`, `description`, `qty`, `expiry`, `unit_price`, `total`, `admin`) VALUES
(1, 'rutik', 22, '', '2022-04-02 11:46:41', 'dr. kolhe', 'kolhe hosp', 'paracitamol, corex', '10, 2', 'this is not set', 'this is not set', 120, 'Rutik Ekre'),
(2, 'saurabh', 12, '7756968747', '2022-04-02 11:46:41', 'dr. kollhe', 'kolhe hospital', 'ritik, paracitamol', '2, 10', 'this is not set', 'this is not set', 120, 'adminname'),
(3, 'ritik', 20, '7756968747', '2022-04-02 11:46:41', 'dr. kollhe', 'kolhe hospital', 'ritik', '1', 'this is not set', 'this is not set', 10, 'adminname'),
(4, 'kshitij', 21, '7057818747', '2022-04-02 11:46:41', 'dr. harshal', 'sipna hosp', 'paracitamol, corex', '15, 2', 'this is not set', 'this is not set', 115, 'adminname'),
(5, 'kshiitij', 21, '7896541230', '2022-04-18 04:26:33', 'dr. bhagawat', 'sipna', 'vaseline', '1', 'this is not set', 'this is not set', 49, 'adminname'),
(6, 'Sakshi', 19, '7896541230', '2022-04-19 18:54:14', 'dr. Kolhe', 'Kolhe Hospital', 'paracitamol', '1', '1.0', '2022-05-06', 1, 'adminname'),
(7, 'Sakshi', 19, '7896541230', '2022-04-19 18:55:08', 'dr. Kolhe', 'Kolhe Hospital', 'paracitamol', '1', '1.0', '2022-05-06', 1, 'adminname'),
(8, 'gaurav', 15, '1236547890', '2022-04-19 19:22:23', 'dr. bam', 'bam hosp', 'paracitamol', '2', '1.0', '2022-05-06', 2, 'adminname'),
(9, 'kartik', 23, '2136547859', '2022-04-19 19:24:04', 'dr. warner', 'warner hosp', 'vaseline', '2', '49.0', '2022-05-18', 98, 'adminname'),
(10, 'vishal', 35, '7412589632', '2022-04-19 19:33:50', 'dr. gaurav', 'gaurav hosp', 'vaseline, corex', '2, 1', '2022-05-18,2022-05-18', '49.0,22', 148, 'adminname'),
(11, 'alia', 29, '7410258963', '2022-04-19 19:50:08', 'Dr. Hello', 'Hello Hosp', 'vaseline, corex', '1, 1', '2022-05-18,11/12/2022', '49.0,50.0', 99, 'adminname'),
(12, 'rutik', 22, '12365412365', '2022-04-19 20:00:30', 'ddr. hathi', 'hathi hosp', 'paracitamol, crocine', '1, 1', '2022-05-06,11/12/2022', '1.0,56.8', 58, 'adminname'),
(13, 'ranbir', 35, '7410258963', '2022-04-19 20:03:59', 'dr kapoor', 'kapoor hosp', 'paracitamol', '1', '2022-05-06', '1.0', 1, 'rutik@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`sr.`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `medicine_stock`
--
ALTER TABLE `medicine_stock`
  ADD PRIMARY KEY (`sr_no`);

--
-- Indexes for table `patient_prescription`
--
ALTER TABLE `patient_prescription`
  ADD PRIMARY KEY (`sr_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `sr.` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `medicine_stock`
--
ALTER TABLE `medicine_stock`
  MODIFY `sr_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `patient_prescription`
--
ALTER TABLE `patient_prescription`
  MODIFY `sr_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
