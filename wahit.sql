-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               11.3.0-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for table wahit_siakad.dosen
CREATE TABLE IF NOT EXISTS `dosen` (
  `nidn` varchar(10) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `gelar` varchar(20) NOT NULL,
  `prodi` varchar(30) NOT NULL,
  PRIMARY KEY (`nidn`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table wahit_siakad.dosen: ~10 rows (approximately)
INSERT INTO `dosen` (`nidn`, `nama`, `gelar`, `prodi`) VALUES
	('D001', 'Dr. Agus Suryanto, S.Kom., M.Kom.', 'Doktor', 'Teknik Informatika'),
	('D002', 'Dr. Rini Handayani, S.Sos., M.Si.', 'Doktor', 'Ilmu Komunikasi'),
	('D003', 'Prof. Dr. Bambang Prasetyo, S.H., M.H.', 'Profesor', 'Hukum'),
	('D004', 'Dr. Eka Purnama, S.E., M.Ak.', 'Doktor', 'Akuntansi'),
	('D005', 'Dr. Rizal Firdaus, S.E., M.M.', 'Doktor', 'Manajemen'),
	('D006', 'Dr. Ir. Dian Kurniawan, M.P.', 'Doktor', 'Peternakan'),
	('D007', 'Dr. Ir. Sri Rahayu, M.Si.', 'Doktor', 'Agroteknologi'),
	('D008', 'Dr. Ir. Nurul Huda, M.Agr.', 'Doktor', 'Pertanian'),
	('D009', 'Ir. Adi Wibowo, S.Kom., M.T.', 'Magister', 'Teknik Informatika'),
	('D010', 'Siti Aisyah, S.I.Kom., M.I.Kom.', 'Magister', 'Ilmu Komunikasi');

-- Dumping structure for table wahit_siakad.khs
CREATE TABLE IF NOT EXISTS `khs` (
  `nim` varchar(10) NOT NULL,
  `semester` int(11) NOT NULL,
  `ipk` decimal(3,2) NOT NULL,
  PRIMARY KEY (`nim`,`semester`),
  CONSTRAINT `khs_nim` FOREIGN KEY (`nim`) REFERENCES `mahasiswa` (`nim`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table wahit_siakad.khs: ~10 rows (approximately)
INSERT INTO `khs` (`nim`, `semester`, `ipk`) VALUES
	('C001', 1, 3.50),
	('C001', 2, 3.25),
	('C002', 1, 3.75),
	('C002', 2, 3.50),
	('C003', 1, 3.00),
	('C003', 2, 2.75),
	('C004', 1, 3.75),
	('C004', 2, 3.50),
	('C005', 1, 3.25),
	('C005', 2, 3.00);

-- Dumping structure for table wahit_siakad.mahasiswa
CREATE TABLE IF NOT EXISTS `mahasiswa` (
  `nim` varchar(10) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `prodi` varchar(30) NOT NULL,
  `kota` varchar(20) NOT NULL,
  `tanggal_lahir` date NOT NULL,
  PRIMARY KEY (`nim`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table wahit_siakad.mahasiswa: ~19 rows (approximately)
INSERT INTO `mahasiswa` (`nim`, `nama`, `prodi`, `kota`, `tanggal_lahir`) VALUES
	('C001', 'Rizki Pratama', 'Teknik Informatika', 'Boyolali', '2001-01-15'),
	('C002', 'Dewi Sartika', 'Ilmu Komunikasi', 'Semarang', '2000-12-20'),
	('C003', 'Andi Setiawan', 'Hukum', 'Klaten', '2001-02-10'),
	('C004', 'Lia Wulandari', 'Akuntansi', 'Salatiga', '2000-11-25'),
	('C005', 'Budi Santoso', 'Manajemen', 'Solo', '2001-03-05'),
	('C006', 'Rina Puspita', 'Peternakan', 'Boyolali', '2000-10-30'),
	('C007', 'Eko Prasetyo', 'Agroteknologi', 'Semarang', '2001-04-01'),
	('C008', 'Siti Nurhaliza', 'Pertanian', 'Klaten', '2000-09-15'),
	('C009', 'Rudi Hartono', 'Teknik Informatika', 'Salatiga', '2001-05-20'),
	('C010', 'Nurul Hidayah', 'Ilmu Komunikasi', 'Solo', '2000-08-10'),
	('C011', 'Wahit Fitriyanto', 'Teknik Informatika', 'Boyolali', '2001-06-15'),
	('C012', 'Ririn Vita', 'Ilmu Komunikasi', 'Semarang', '2000-07-20'),
	('C013', 'Arthur Ashley', 'Hukum', 'Klaten', '2001-08-10'),
	('C014', 'Andi Saputra', 'Akuntansi', 'Salatiga', '2000-09-25'),
	('C015', 'Nanang Irfan', 'Manajemen', 'Solo', '2001-10-05'),
	('C016', 'Adam Bagus', 'Peternakan', 'Boyolali', '2000-11-30'),
	('C017', 'Anang Irfan', 'Akuntansi', 'Salatiga', '2000-09-25'),
	('C018', 'Luna Sinta', 'Manajemen', 'Solo', '2001-10-05'),
	('C019', 'Wahyu Adi', 'Peternakan', 'Boyolali', '2000-11-30');

-- Dumping structure for table wahit_siakad.matkul
CREATE TABLE IF NOT EXISTS `matkul` (
  `kode` varchar(10) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `sks` int(11) NOT NULL,
  `prodi` varchar(30) NOT NULL,
  PRIMARY KEY (`kode`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table wahit_siakad.matkul: ~10 rows (approximately)
INSERT INTO `matkul` (`kode`, `nama`, `sks`, `prodi`) VALUES
	('MK001', 'Algoritma dan Pemrograman', 3, 'Teknik Informatika'),
	('MK002', 'Dasar-Dasar Komunikasi', 3, 'Ilmu Komunikasi'),
	('MK003', 'Pengantar Hukum Indonesia', 3, 'Hukum'),
	('MK004', 'Akuntansi Dasar', 3, 'Akuntansi'),
	('MK005', 'Manajemen Pemasaran', 3, 'Manajemen'),
	('MK006', 'Anatomi dan Fisiologi Hewan', 3, 'Peternakan'),
	('MK007', 'Ilmu Tanah', 3, 'Agroteknologi'),
	('MK008', 'Pengantar Ilmu Pertanian', 3, 'Pertanian'),
	('MK009', 'Struktur Data dan Algoritma', 3, 'Teknik Informatika'),
	('MK010', 'Teori Komunikasi Massa', 3, 'Ilmu Komunikasi');

-- Dumping structure for table wahit_siakad.nilai
CREATE TABLE IF NOT EXISTS `nilai` (
  `nim` varchar(10) NOT NULL,
  `kode` varchar(10) NOT NULL,
  `nilai` char(1) NOT NULL,
  PRIMARY KEY (`nim`,`kode`),
  KEY `kode` (`kode`),
  CONSTRAINT `nilai_ibfk_1` FOREIGN KEY (`nim`) REFERENCES `mahasiswa` (`nim`),
  CONSTRAINT `nilai_ibfk_2` FOREIGN KEY (`kode`) REFERENCES `matkul` (`kode`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table wahit_siakad.nilai: ~10 rows (approximately)
INSERT INTO `nilai` (`nim`, `kode`, `nilai`) VALUES
	('C001', 'MK001', 'A'),
	('C001', 'MK009', 'B'),
	('C002', 'MK002', 'A'),
	('C002', 'MK010', 'B'),
	('C003', 'MK003', 'B'),
	('C004', 'MK004', 'A'),
	('C005', 'MK005', 'B'),
	('C006', 'MK006', 'A'),
	('C007', 'MK007', 'B'),
	('C008', 'MK008', 'A');

-- Dumping structure for table wahit_siakad.presensi
CREATE TABLE IF NOT EXISTS `presensi` (
  `nim` varchar(10) NOT NULL,
  `kode` varchar(10) NOT NULL,
  `pertemuan` int(11) NOT NULL,
  `status` varchar(10) NOT NULL,
  PRIMARY KEY (`nim`,`kode`,`pertemuan`),
  KEY `kode` (`kode`),
  CONSTRAINT `presensi_ibfk_1` FOREIGN KEY (`nim`) REFERENCES `mahasiswa` (`nim`),
  CONSTRAINT `presensi_ibfk_2` FOREIGN KEY (`kode`) REFERENCES `matkul` (`kode`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table wahit_siakad.presensi: ~10 rows (approximately)
INSERT INTO `presensi` (`nim`, `kode`, `pertemuan`, `status`) VALUES
	('C001', 'MK001', 1, 'Hadir'),
	('C001', 'MK001', 2, 'Hadir'),
	('C001', 'MK009', 1, 'Hadir'),
	('C001', 'MK009', 2, 'Izin'),
	('C002', 'MK002', 1, 'Hadir'),
	('C002', 'MK002', 2, 'Hadir'),
	('C002', 'MK010', 1, 'Hadir'),
	('C002', 'MK010', 2, 'Sakit'),
	('C003', 'MK003', 1, 'Hadir'),
	('C003', 'MK003', 2, 'Alfa');

-- Dumping structure for table wahit_siakad.staff_rektorat
CREATE TABLE IF NOT EXISTS `staff_rektorat` (
  `nip` varchar(10) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `gelar` varchar(20) NOT NULL,
  `jabatan` varchar(30) NOT NULL,
  PRIMARY KEY (`nip`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table wahit_siakad.staff_rektorat: ~10 rows (approximately)
INSERT INTO `staff_rektorat` (`nip`, `nama`, `gelar`, `jabatan`) VALUES
	('S001', 'Dr. Ir. Ahmad Subagyo, M.M.', 'Doktor', 'Rektor'),
	('S002', 'Dr. Ir. Rini Astuti, M.Si.', 'Doktor', 'Wakil Rektor I'),
	('S003', 'Dr. Ir. Budi Santosa, M.T.', 'Doktor', 'Wakil Rektor II'),
	('S004', 'Dr. Ir. Siti Aminah, M.Pd.', 'Doktor', 'Wakil Rektor III'),
	('S005', 'Dr. Ir. Eko Prasetyo, M.Kom.', 'Doktor', 'Wakil Rektor IV'),
	('S006', 'Ir. Dian Kurniawan, M.M.', 'Magister', 'Sekretaris Rektor'),
	('S007', 'Ir. Sri Rahayu, M.Ak.', 'Magister', 'Bendahara Rektor'),
	('S008', 'Ir. Nurul Huda, M.Si.', 'Magister', 'Kepala Biro Akademik'),
	('S009', 'Ir. Adi Wibowo, M.T.', 'Magister', 'Kepala Biro Kemahasiswaan'),
	('S010', 'Siti Aisyah, S.E., M.M.', 'Magister', 'Kepala Biro Umum');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
