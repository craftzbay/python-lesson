-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Oct 18, 2019 at 12:25 PM
-- Server version: 5.7.23
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blogapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
CREATE TABLE IF NOT EXISTS `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `body` text COLLATE utf8_unicode_ci NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `post_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `post_to_comment` (`post_id`),
  KEY `user_to_comment` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `comments`
--

INSERT INTO `comments` (`id`, `body`, `created`, `post_id`, `user_id`) VALUES
(1, 'World', '2019-10-18 11:24:10', 1, 2),
(2, 'Hello', '2019-10-18 11:24:10', 1, 3),
(3, 'c++', '2019-10-18 11:24:10', 1, 4),
(4, 'c', '2019-10-18 11:24:10', 2, 1),
(5, 'c#', '2019-10-18 11:24:10', 2, 2),
(6, 'insert', '2019-10-18 11:24:10', 2, 3),
(7, 'comments', '2019-10-18 11:24:10', 3, 1),
(8, 'post_id', '2019-10-18 11:24:10', 3, 3),
(9, 'Huser_idello', '2019-10-18 11:24:10', 3, 4),
(10, 'World', '2019-10-18 11:24:10', 4, 2),
(11, 'Hello', '2019-10-18 11:24:10', 4, 3),
(12, 'c++', '2019-10-18 11:24:10', 4, 4),
(13, 'c', '2019-10-18 11:24:10', 5, 1),
(14, 'c#', '2019-10-18 11:24:10', 5, 2),
(15, 'insert', '2019-10-18 11:24:10', 5, 3),
(16, 'comments', '2019-10-18 11:24:10', 6, 1),
(17, 'post_id', '2019-10-18 11:24:10', 6, 3),
(18, 'Huser_idello', '2019-10-18 11:24:10', 6, 4),
(19, 'World', '2019-10-18 11:24:47', 4, 2),
(20, 'Hello', '2019-10-18 11:24:47', 4, 3),
(21, 'c++', '2019-10-18 11:24:47', 7, 4),
(22, 'c', '2019-10-18 11:24:47', 9, 1),
(23, 'c#', '2019-10-18 11:24:47', 8, 2),
(24, 'insert', '2019-10-18 11:24:47', 11, 3),
(25, 'comments', '2019-10-18 11:24:47', 12, 1),
(26, 'post_id', '2019-10-18 11:24:47', 12, 3),
(27, 'Huser_idello', '2019-10-18 11:24:47', 12, 4),
(28, 'World', '2019-10-18 11:24:47', 11, 2),
(29, 'Hello', '2019-10-18 11:24:47', 11, 3),
(30, 'c++', '2019-10-18 11:24:47', 12, 4),
(31, 'c', '2019-10-18 11:24:47', 9, 1),
(32, 'c#', '2019-10-18 11:24:47', 9, 2),
(33, 'insert', '2019-10-18 11:24:47', 8, 3),
(34, 'comments', '2019-10-18 11:24:47', 8, 1),
(35, 'post_id', '2019-10-18 11:24:47', 7, 3),
(36, 'Huser_idello', '2019-10-18 11:24:47', 7, 4);

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
CREATE TABLE IF NOT EXISTS `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `body` text COLLATE utf8_unicode_ci NOT NULL,
  `img` blob NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `category` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_to_post` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`id`, `title`, `body`, `img`, `created`, `category`, `user_id`) VALUES
(1, 'writen by Admin', 'Hello body pythonnnnnnnn', 0x6e756c6c, '2019-10-18 11:13:40', 'angilal1', 1),
(2, 'writen by Admin', 'Hello body pythonnnnnnnn', 0x6e756c6c, '2019-10-18 11:15:17', 'angilal2', 1),
(3, 'writen by Admin', 'Hello body pythonnnnnnnn', 0x6e756c6c, '2019-10-18 11:15:17', 'angilal1', 1),
(4, 'Post4', 'Hello body pythonnnnnnnn', 0x6e756c6c, '2019-10-18 11:15:40', 'angilal2', 2),
(5, 'Post5', 'Hello body pythonnnnnnnn', 0x6e756c6c, '2019-10-18 11:15:40', 'angilal1', 2),
(6, 'Post6', 'Hello body pythonnnnnnnn', 0x6e756c6c, '2019-10-18 11:15:40', 'angilal1', 2),
(7, 'Post7', 'Hello body pythonnnnnnnn', 0x6e756c6c, '2019-10-18 11:15:53', 'angilal2', 3),
(8, 'Post8', 'Hello body pythonnnnnnnn', 0x6e756c6c, '2019-10-18 11:15:53', 'angilal1', 3),
(9, 'Post9', 'Hello body pythonnnnnnnn', 0x6e756c6c, '2019-10-18 11:15:53', 'angilal1', 3),
(10, 'Post10', 'Hello body pythonnnnnnnn', 0x6e756c6c, '2019-10-18 11:17:40', 'angilal2', 4),
(11, 'Post11', 'Hello body pythonnnnnnnn', 0x6e756c6c, '2019-10-18 11:17:40', 'angilal1', 4),
(12, 'Post12', 'Hello body pythonnnnnnnn', 0x6e756c6c, '2019-10-18 11:17:40', 'angilal3', 4);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(25) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(25) COLLATE utf8_unicode_ci NOT NULL,
  `type` varchar(5) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password`, `type`) VALUES
(1, 'admin', 'admin@blog.com', 'password', 'admin'),
(2, 'bat', 'bat@blog.com', 'bataa', 'user'),
(3, 'saraa', 'saraa@gmail.com', 'saraa123', 'user'),
(4, 'admin', 'delger@email.com', 'delger', 'user'),
(5, 'user1', 'user1@user.com', 'user', 'user');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `comments`
--
ALTER TABLE `comments`
  ADD CONSTRAINT `post_to_comment` FOREIGN KEY (`post_id`) REFERENCES `posts` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `user_to_comment` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `posts`
--
ALTER TABLE `posts`
  ADD CONSTRAINT `user_to_post` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
