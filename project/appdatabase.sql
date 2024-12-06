-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 30, 2024 at 10:33 AM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `appdatabase`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add tenue', 7, 'add_tenue'),
(26, 'Can change tenue', 7, 'change_tenue'),
(27, 'Can delete tenue', 7, 'delete_tenue'),
(28, 'Can view tenue', 7, 'view_tenue'),
(29, 'Can add facture', 8, 'add_facture'),
(30, 'Can change facture', 8, 'change_facture'),
(31, 'Can delete facture', 8, 'delete_facture'),
(32, 'Can view facture', 8, 'view_facture'),
(33, 'Can add image modele', 9, 'add_imagemodele'),
(34, 'Can change image modele', 9, 'change_imagemodele'),
(35, 'Can delete image modele', 9, 'delete_imagemodele'),
(36, 'Can view image modele', 9, 'view_imagemodele'),
(37, 'Can add client', 10, 'add_client'),
(38, 'Can change client', 10, 'change_client'),
(39, 'Can delete client', 10, 'delete_client'),
(40, 'Can view client', 10, 'view_client'),
(41, 'Can add tenue commande', 11, 'add_tenuecommande'),
(42, 'Can change tenue commande', 11, 'change_tenuecommande'),
(43, 'Can delete tenue commande', 11, 'delete_tenuecommande'),
(44, 'Can view tenue commande', 11, 'view_tenuecommande'),
(45, 'Can add commande', 12, 'add_commande'),
(46, 'Can change commande', 12, 'change_commande'),
(47, 'Can delete commande', 12, 'delete_commande'),
(48, 'Can view commande', 12, 'view_commande');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `client`
--

CREATE TABLE `client` (
  `idclient` int NOT NULL,
  `nom` varchar(100) DEFAULT NULL,
  `prenom` varchar(100) DEFAULT NULL,
  `contact` varchar(10) DEFAULT NULL,
  `ajout` timestamp NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `commande`
--

CREATE TABLE `commande` (
  `idcom` int NOT NULL,
  `idclient` int NOT NULL,
  `debutcom` date NOT NULL,
  `fincom` date NOT NULL,
  `montantcom` int NOT NULL,
  `statut` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'En Cours',
  `creation` timestamp NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `coutureapp_client`
--

CREATE TABLE `coutureapp_client` (
  `idclient` int NOT NULL,
  `nom` varchar(100) DEFAULT NULL,
  `prenom` varchar(100) DEFAULT NULL,
  `contact` varchar(10) DEFAULT NULL,
  `ajout` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `coutureapp_client`
--

INSERT INTO `coutureapp_client` (`idclient`, `nom`, `prenom`, `contact`, `ajout`) VALUES
(1, 'Stanis', 'kouame', '0768197436', '2024-10-28 20:46:17.475886'),
(3, 'kouassi', 'konan Maurice', '0768197436', '2024-10-28 21:20:03.808239'),
(5, 'kouassi', 'affoua diane', '0768197436', '2024-10-28 21:42:12.940310'),
(7, 'Samake', 'Ben', '0768197436', '2024-10-28 22:04:37.704150'),
(9, 'kouassi', 'solange', '0768197436', '2024-10-29 10:03:58.810769'),
(10, 'kouassi', 'affoua', '0768197436', '2024-10-29 10:34:05.900816'),
(11, 'kouassi', 'affoua', '0768197436', '2024-10-29 16:50:58.901189'),
(12, 'Samake', 'Ben', '0768197436', '2024-10-29 17:16:48.408968'),
(13, 'Samake', 'Ben', '0768197436', '2024-10-29 17:17:32.050903'),
(15, 'Ngoran', 'Adjoua', '0768197436', '2024-11-06 05:59:36.522238'),
(16, 'Boni', 'Eliaza', '0768197436', '2024-11-06 06:59:33.524650'),
(17, 'Sanogo', 'Djiotigui', '0768197436', '2024-11-07 13:16:59.784354'),
(18, 'Alabi', 'adeyemi', '0768197436', '2024-11-08 08:54:46.939396'),
(19, 'boni', 'samuel', '0768197436', '2024-11-20 19:22:14.655233'),
(20, 'Yao', 'William', '0768197436', '2024-11-26 05:02:28.982294');

-- --------------------------------------------------------

--
-- Table structure for table `coutureapp_commande`
--

CREATE TABLE `coutureapp_commande` (
  `idcom` int NOT NULL,
  `debutcom` date NOT NULL,
  `fincom` date NOT NULL,
  `creation` datetime(6) NOT NULL,
  `idclient_id` int NOT NULL,
  `montantcom` int NOT NULL,
  `statut` varchar(51) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `coutureapp_commande`
--

INSERT INTO `coutureapp_commande` (`idcom`, `debutcom`, `fincom`, `creation`, `idclient_id`, `montantcom`, `statut`) VALUES
(1, '2024-11-22', '2024-11-26', '2024-10-31 15:00:44.821287', 3, 23500, 'En Attente'),
(2, '2024-11-20', '2024-11-22', '2024-10-31 15:13:37.641046', 1, 110000, 'Livrée'),
(7, '2024-11-26', '2024-11-29', '2024-11-06 06:47:24.104643', 1, 393000, 'En Attente'),
(9, '2024-11-07', '2024-11-16', '2024-11-07 13:17:24.427165', 17, 101000, 'En Attente'),
(10, '2024-11-20', '2024-11-23', '2024-11-20 19:23:17.614738', 19, 36000, 'En Attente'),
(11, '2024-11-08', '2024-11-24', '2024-11-23 08:42:25.798898', 3, 1008000, 'En Attente'),
(12, '2024-11-26', '2024-11-30', '2024-11-26 05:02:53.752510', 20, 38500, 'En Attente');

-- --------------------------------------------------------

--
-- Table structure for table `coutureapp_facture`
--

CREATE TABLE `coutureapp_facture` (
  `idfacture` int NOT NULL,
  `date_facture` datetime(6) NOT NULL,
  `idclient_id` int NOT NULL,
  `idcom_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `coutureapp_imagemodele`
--

CREATE TABLE `coutureapp_imagemodele` (
  `idmg` int NOT NULL,
  `photos` varchar(100) DEFAULT NULL,
  `libelle` varchar(100) NOT NULL,
  `ajout` datetime(6) NOT NULL,
  `idtenu_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `coutureapp_imagemodele`
--

INSERT INTO `coutureapp_imagemodele` (`idmg`, `photos`, `libelle`, `ajout`, `idtenu_id`) VALUES
(1, 'tenue_images/Stanislogo-02.jpg', 'logo', '2024-11-08 07:38:42.192153', 1),
(3, 'tenue_images/Capture_décran_20.png', 'Capture Ecran', '2024-11-26 04:07:23.986622', 10);

-- --------------------------------------------------------

--
-- Table structure for table `coutureapp_tenue`
--

CREATE TABLE `coutureapp_tenue` (
  `idtenu` int NOT NULL,
  `prix` int NOT NULL,
  `avance` int NOT NULL,
  `reste` int NOT NULL,
  `modele` longtext NOT NULL,
  `description` varchar(300) NOT NULL,
  `ajout` datetime(6) NOT NULL,
  `idcom_id` int NOT NULL,
  `etat` varchar(100) DEFAULT NULL,
  `etat_tenue` varchar(100) NOT NULL,
  `modifierle` date NOT NULL,
  `montant` int NOT NULL,
  `qte` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `coutureapp_tenue`
--

INSERT INTO `coutureapp_tenue` (`idtenu`, `prix`, `avance`, `reste`, `modele`, `description`, `ajout`, `idcom_id`, `etat`, `etat_tenue`, `modifierle`, `montant`, `qte`) VALUES
(1, 10000, 10000, 100000, 'Costume Femme', '2 Pagnes', '2024-11-07 08:28:22.493198', 2, NULL, 'Non Soldé', '2024-11-13', 110000, 11),
(4, 25000, 25000, 25000, 'Costume Femme', 'bazin', '2024-11-07 13:19:21.393511', 9, NULL, 'Non Soldé', '2024-11-13', 50000, 2),
(5, 78000, 50000, 340000, 'Mesticaine', '3Tissues rouges', '2024-11-13 08:49:45.795392', 7, NULL, 'Non Soldé', '2024-11-13', 390000, 5),
(6, 9000, 1000, 35000, 'Costume Femme', '', '2024-11-20 19:24:25.640742', 10, NULL, 'Non Soldé', '2024-11-20', 36000, 4),
(7, 23500, 23500, 0, 'Chemise Manche courte simple', '', '2024-11-21 12:20:20.118090', 1, NULL, 'Soldé', '2024-11-21', 23500, 1),
(8, 6000, 36000, 0, 'Pantalon simple', '', '2024-11-23 07:32:38.070551', 9, NULL, 'Soldé', '2024-11-23', 36000, 6),
(9, 7500, 3500, 11500, 'Chemise Manche Longue Pantalon', '3 Morceaux Bazin', '2024-11-23 07:33:32.785132', 9, NULL, 'Non Soldé', '2024-11-23', 15000, 2),
(10, 3000, 3000, 0, 'Tunique homme', '2 Pagnes', '2024-11-26 04:05:07.787732', 7, NULL, 'Soldé', '2024-11-26', 3000, 1),
(11, 63000, 230000, 778000, 'Toge', 'Corale', '2024-11-26 04:20:11.093803', 11, NULL, 'Non Soldé', '2024-11-26', 1008000, 16),
(12, 3500, 10000, 7500, 'Chemise Manche Longue simple', '', '2024-11-26 05:04:20.135336', 12, NULL, 'Non Soldé', '2024-11-26', 17500, 5),
(13, 3500, 10000, 11000, 'Chemise Manche Longue simple', '', '2024-11-26 05:05:16.163124', 12, NULL, 'Non Soldé', '2024-11-26', 21000, 6);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(10, 'coutureApp', 'client'),
(12, 'coutureApp', 'commande'),
(8, 'coutureApp', 'facture'),
(9, 'coutureApp', 'imagemodele'),
(7, 'coutureApp', 'tenue'),
(11, 'coutureApp', 'tenuecommande'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-10-24 12:04:23.255770'),
(2, 'auth', '0001_initial', '2024-10-24 12:04:28.732352'),
(3, 'admin', '0001_initial', '2024-10-24 12:04:29.714242'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-10-24 12:04:29.770413'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-10-24 12:04:29.834816'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-10-24 12:04:30.834444'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-10-24 12:04:31.269800'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-10-24 12:04:31.561403'),
(9, 'auth', '0004_alter_user_username_opts', '2024-10-24 12:04:31.607650'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-10-24 12:04:31.928044'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-10-24 12:04:32.021106'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-10-24 12:04:32.088006'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-10-24 12:04:32.464778'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-10-24 12:04:32.842958'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-10-24 12:04:32.931237'),
(16, 'auth', '0011_update_proxy_permissions', '2024-10-24 12:04:32.973674'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-10-24 12:04:33.340139'),
(18, 'sessions', '0001_initial', '2024-10-24 12:04:33.641100'),
(19, 'coutureApp', '0001_initial', '2024-10-25 13:14:44.985241'),
(20, 'coutureApp', '0002_tenue_idcom_delete_tenuecommande', '2024-11-07 01:43:54.812614'),
(21, 'coutureApp', '0003_alter_imagemodele_photos', '2024-11-08 07:28:36.079464'),
(22, 'coutureApp', '0004_tenue_etat_tenue_tenue_modifierle_and_more', '2024-11-13 07:43:45.244108'),
(23, 'coutureApp', '0005_remove_facture_montantdonne_and_more', '2024-11-17 06:41:37.395202'),
(24, 'coutureApp', '0006_commande_statut_alter_commande_montantcom', '2024-11-17 07:09:55.123527'),
(25, 'coutureApp', '0007_alter_tenue_montant_alter_tenue_qte', '2024-11-17 07:31:00.500686'),
(26, 'coutureApp', '0008_alter_commande_statut', '2024-11-26 05:52:31.439242'),
(27, 'coutureApp', '0009_alter_commande_statut', '2024-11-26 05:58:31.723493');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `facture`
--

CREATE TABLE `facture` (
  `idfacture` int NOT NULL,
  `idclient` int NOT NULL,
  `idcom` int NOT NULL,
  `montantdonne` int NOT NULL,
  `montantfacture` int NOT NULL,
  `reste` int NOT NULL,
  `date_facture` timestamp NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `imagemodele`
--

CREATE TABLE `imagemodele` (
  `idmg` int NOT NULL,
  `idtenu` int NOT NULL,
  `photos` longblob NOT NULL,
  `libelle` varchar(100) NOT NULL,
  `ajout` timestamp NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tenue`
--

CREATE TABLE `tenue` (
  `idtenu` int NOT NULL,
  `prix` int NOT NULL,
  `qte` int NOT NULL,
  `montant` int GENERATED ALWAYS AS ((`prix` * `qte`)) VIRTUAL NOT NULL,
  `avance` int NOT NULL,
  `reste` int NOT NULL,
  `modele` text NOT NULL,
  `description` varchar(300) NOT NULL,
  `ajout` timestamp NOT NULL,
  `idcom` int NOT NULL,
  `etat_tenue` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `modifierle` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`idclient`);

--
-- Indexes for table `commande`
--
ALTER TABLE `commande`
  ADD PRIMARY KEY (`idcom`),
  ADD KEY `idclient` (`idclient`);

--
-- Indexes for table `coutureapp_client`
--
ALTER TABLE `coutureapp_client`
  ADD PRIMARY KEY (`idclient`);

--
-- Indexes for table `coutureapp_commande`
--
ALTER TABLE `coutureapp_commande`
  ADD PRIMARY KEY (`idcom`),
  ADD KEY `coutureApp_commande_idclient_id_7e34877e_fk_coutureAp` (`idclient_id`);

--
-- Indexes for table `coutureapp_facture`
--
ALTER TABLE `coutureapp_facture`
  ADD PRIMARY KEY (`idfacture`),
  ADD KEY `coutureApp_facture_idclient_id_e2183b20_fk_coutureAp` (`idclient_id`),
  ADD KEY `coutureApp_facture_idcom_id_e5f34e30_fk_coutureAp` (`idcom_id`);

--
-- Indexes for table `coutureapp_imagemodele`
--
ALTER TABLE `coutureapp_imagemodele`
  ADD PRIMARY KEY (`idmg`),
  ADD KEY `coutureApp_imagemode_idtenu_id_73eb68b1_fk_coutureAp` (`idtenu_id`);

--
-- Indexes for table `coutureapp_tenue`
--
ALTER TABLE `coutureapp_tenue`
  ADD PRIMARY KEY (`idtenu`),
  ADD KEY `coutureApp_tenue_idcom_id_35f1ec2b_fk_coutureApp_commande_idcom` (`idcom_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `facture`
--
ALTER TABLE `facture`
  ADD PRIMARY KEY (`idfacture`),
  ADD KEY `idclient` (`idclient`,`idcom`),
  ADD KEY `idcom` (`idcom`);

--
-- Indexes for table `imagemodele`
--
ALTER TABLE `imagemodele`
  ADD PRIMARY KEY (`idmg`),
  ADD KEY `idtenu` (`idtenu`);

--
-- Indexes for table `tenue`
--
ALTER TABLE `tenue`
  ADD PRIMARY KEY (`idtenu`),
  ADD KEY `idcom` (`idcom`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `client`
--
ALTER TABLE `client`
  MODIFY `idclient` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `commande`
--
ALTER TABLE `commande`
  MODIFY `idcom` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `coutureapp_client`
--
ALTER TABLE `coutureapp_client`
  MODIFY `idclient` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `coutureapp_commande`
--
ALTER TABLE `coutureapp_commande`
  MODIFY `idcom` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `coutureapp_facture`
--
ALTER TABLE `coutureapp_facture`
  MODIFY `idfacture` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `coutureapp_imagemodele`
--
ALTER TABLE `coutureapp_imagemodele`
  MODIFY `idmg` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `coutureapp_tenue`
--
ALTER TABLE `coutureapp_tenue`
  MODIFY `idtenu` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `facture`
--
ALTER TABLE `facture`
  MODIFY `idfacture` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `imagemodele`
--
ALTER TABLE `imagemodele`
  MODIFY `idmg` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tenue`
--
ALTER TABLE `tenue`
  MODIFY `idtenu` int NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `commande`
--
ALTER TABLE `commande`
  ADD CONSTRAINT `commande_ibfk_1` FOREIGN KEY (`idclient`) REFERENCES `client` (`idclient`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `coutureapp_commande`
--
ALTER TABLE `coutureapp_commande`
  ADD CONSTRAINT `coutureApp_commande_idclient_id_7e34877e_fk_coutureAp` FOREIGN KEY (`idclient_id`) REFERENCES `coutureapp_client` (`idclient`);

--
-- Constraints for table `coutureapp_facture`
--
ALTER TABLE `coutureapp_facture`
  ADD CONSTRAINT `coutureApp_facture_idclient_id_e2183b20_fk_coutureAp` FOREIGN KEY (`idclient_id`) REFERENCES `coutureapp_client` (`idclient`),
  ADD CONSTRAINT `coutureApp_facture_idcom_id_e5f34e30_fk_coutureAp` FOREIGN KEY (`idcom_id`) REFERENCES `coutureapp_commande` (`idcom`);

--
-- Constraints for table `coutureapp_imagemodele`
--
ALTER TABLE `coutureapp_imagemodele`
  ADD CONSTRAINT `coutureApp_imagemode_idtenu_id_73eb68b1_fk_coutureAp` FOREIGN KEY (`idtenu_id`) REFERENCES `coutureapp_tenue` (`idtenu`);

--
-- Constraints for table `coutureapp_tenue`
--
ALTER TABLE `coutureapp_tenue`
  ADD CONSTRAINT `coutureApp_tenue_idcom_id_35f1ec2b_fk_coutureApp_commande_idcom` FOREIGN KEY (`idcom_id`) REFERENCES `coutureapp_commande` (`idcom`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `facture`
--
ALTER TABLE `facture`
  ADD CONSTRAINT `facture_ibfk_1` FOREIGN KEY (`idclient`) REFERENCES `client` (`idclient`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `facture_ibfk_2` FOREIGN KEY (`idcom`) REFERENCES `commande` (`idcom`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `imagemodele`
--
ALTER TABLE `imagemodele`
  ADD CONSTRAINT `imagemodele_ibfk_1` FOREIGN KEY (`idtenu`) REFERENCES `tenue` (`idtenu`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tenue`
--
ALTER TABLE `tenue`
  ADD CONSTRAINT `tenue_ibfk_1` FOREIGN KEY (`idcom`) REFERENCES `commande` (`idcom`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
