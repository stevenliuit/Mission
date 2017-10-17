-- MySQL dump 10.13  Distrib 5.6.35, for Linux (x86_64)
--
-- Host: localhost    Database: devops
-- ------------------------------------------------------
-- Server version	5.6.35-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '账号ID',
  `role_id` smallint(6) NOT NULL DEFAULT '0' COMMENT '角色ID',
  `uuid` char(32) DEFAULT NULL COMMENT '唯一标识',
  `name` char(20) NOT NULL DEFAULT '' COMMENT '账号',
  `pwd` char(32) NOT NULL COMMENT '密码',
  `user_name` char(10) DEFAULT '' COMMENT '姓名',
  `tel` char(11) NOT NULL DEFAULT '' COMMENT '电话号',
  `email` char(50) NOT NULL DEFAULT '' COMMENT '邮件',
  `status` tinyint(4) NOT NULL DEFAULT '1' COMMENT '账号状态:1-开启，2-停用',
  `last_login_ip` char(15) DEFAULT '' COMMENT '最后登录IP',
  `last_login_time` datetime DEFAULT NULL COMMENT '最后登录时间',
  `is_super` tinyint(1) NOT NULL DEFAULT '0' COMMENT '超管标识',
  `ssh_key_pwd` int(11) DEFAULT NULL COMMENT 'SSH-KEY密码',
  `create_at` datetime DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_name` (`name`),
  UNIQUE KEY `unique_tel` (`tel`),
  UNIQUE KEY `unique_email` (`email`),
  UNIQUE KEY `unique_uuid` (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COMMENT='管理员';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,1,'1','admin','4abb3fc49446ecdfa10eaf1ea4d415c4','超级管理员','11','mefuwei@163.com',1,'111.204.59.114','2017-06-20 13:46:48',1,NULL,NULL);
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('08zmmdrt55s6o7fzq7me6o8chm0m9oui','NmRhZGQ1MGYyNzNjYzA2ZjJlNTFkYmIxMWVmZGUzYTI0MjVkYTRjOTp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjksImN1cnJlbnRfcm9sZV9pZCI6Mn0=','2017-01-30 11:16:22'),('0czc0zbx45knaf6ewxfjpn81due8n2nm','YzQxZGRhZmM2NDMxMzRmZTgxMWE3ZGNlZGQyNjdjM2ZlMzEzMjE1ZDp7ImN1cnJlbnRfdmlld19uYW1lIjoiaW5kZXgiLCJjdXJyZW50X2FkbWluX2lkIjoxLCJjdXJyZW50X3JvbGVfaWQiOjF9','2017-06-14 21:11:28'),('0gh7aqzgp7x6w48vuulk5q5ypi438157','MTZkNDJlOWRjZjM4ZTIxMjkzYTI4MWM1OWJjZGY1ZmFjZGRlYTdiMDp7ImN1cnJlbnRfdmlld19uYW1lIjoicHJvamVjdF9saXN0IiwiY3VycmVudF9hZG1pbl9pZCI6MSwiY3VycmVudF9yb2xlX2lkIjoxfQ==','2016-12-29 08:25:59'),('0yu2bthcx343li0npiiqi1drevvabd5w','MjJjMzgxZjkyMWUwZDZjNTZhY2M4ODA5ZWU5MmFkNTYzODdjNGZiMjp7ImN1cnJlbnRfdmlld19uYW1lIjoib3BlcmF0aW9uX2xvZ19zaG93IiwiY3VycmVudF9hZG1pbl9pZCI6MSwiY3VycmVudF9yb2xlX2lkIjoxfQ==','2017-06-14 21:07:13'),('1w758ptsr1xn9aju3wlcmm8m8n2920bn','NzUwNDkxNzVhZmI3ZDZmOWQ3YmQ2MDk1N2Y0YmZhYmFkMmYxZGE4Mjp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjEsImN1cnJlbnRfcm9sZV9pZCI6MX0=','2016-12-17 09:00:39'),('1xzltgnsa66d70qanklxsobiyrki7m9u','NzUwNDkxNzVhZmI3ZDZmOWQ3YmQ2MDk1N2Y0YmZhYmFkMmYxZGE4Mjp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjEsImN1cnJlbnRfcm9sZV9pZCI6MX0=','2017-02-02 13:14:31'),('20s0ojqw6ib0uqckzg3rcvg5aqvd24eb','ZjRlOTRhZmZlMzMyOTBkZjcxMGNmM2MxNmNkNTBlMWYyMGE3ZmFiMjp7ImN1cnJlbnRfdmlld19uYW1lIjoicHJvamVjdF9lbnZfZGV0YWlsIiwiY3VycmVudF9hZG1pbl9pZCI6MTEsImN1cnJlbnRfcm9sZV9pZCI6NH0=','2017-03-03 10:51:16'),('22gtk2qryvcx4lb7bux21vngo4herpma','NDMwYTYxYzk5YWE3NmNmM2FiNWMzZGNmMWY4MzIwY2U2Njg5MzU5Mzp7ImN1cnJlbnRfdmlld19uYW1lIjoib3N1c2VyX2FkZCIsImN1cnJlbnRfYWRtaW5faWQiOjEsImN1cnJlbnRfcm9sZV9pZCI6MX0=','2016-12-23 07:19:15'),('32wxcyic8pm5v1oc7gg59k9iw0btinkl','Y2Q1ZDA3OWVkMWU1Y2YyM2YzNzY0NThmZjNiZmRiZDRkMDljYTQ1ZTp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjEzLCJjdXJyZW50X3JvbGVfaWQiOjN9','2017-03-13 14:58:37'),('64a2cuvj1hfl8moebkv0rsjwtppq3ddw','ODI5ODZiOWNhOGU0ODM2ZmU0NDg3ZGY5NTM2ZjBjM2MxMWVkODFiMjp7ImN1cnJlbnRfdmlld19uYW1lIjoicHJvamVjdF9lbnZfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjEsImN1cnJlbnRfcm9sZV9pZCI6MX0=','2017-01-30 18:14:40'),('6n99b31t0fvadrvh4d2eqg1v8bvmgswi','ZWM3ZGJmNzc2MTY4OTVjZWVjM2E2MDNhZDNmMDA5OWJlZDc2OTlhNzp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjE1LCJjdXJyZW50X3JvbGVfaWQiOjN9','2017-01-11 17:43:51'),('6tgc3c5ftv0a7isullcvychbv1p43r9p','YzQxZGRhZmM2NDMxMzRmZTgxMWE3ZGNlZGQyNjdjM2ZlMzEzMjE1ZDp7ImN1cnJlbnRfdmlld19uYW1lIjoiaW5kZXgiLCJjdXJyZW50X2FkbWluX2lkIjoxLCJjdXJyZW50X3JvbGVfaWQiOjF9','2017-03-08 13:08:10'),('7fvfp6ayz3e8ky9vod4s3gjexeag172s','YmM1ZGQzZjE5ZTAyM2IwNjFiOGVhYmJhNTVkNjhmNjQ3M2E0MDVlOTp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjE0LCJjdXJyZW50X3JvbGVfaWQiOjJ9','2017-03-14 17:17:58'),('7k8k0honvhjohsk3od9ed4td4wnq61u2','NzUwNDkxNzVhZmI3ZDZmOWQ3YmQ2MDk1N2Y0YmZhYmFkMmYxZGE4Mjp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjEsImN1cnJlbnRfcm9sZV9pZCI6MX0=','2017-03-13 10:40:34'),('7xhtdksc5g6xalpzzm6jg4667qnbnsfu','MGVhMTIyZTdmMWRmMGMyODczNzAxYjYxODVhMGY5MDU1ZTYzYWZmOTp7ImN1cnJlbnRfdmlld19uYW1lIjoicHJvamVjdF9lbnZfYWRkIiwiY3VycmVudF9hZG1pbl9pZCI6MSwiY3VycmVudF9yb2xlX2lkIjoxfQ==','2016-12-28 09:47:20'),('8m02io9h8kan2m0josfoppmdoub5nwoo','YTAyZDg0ZjNmNmE5ZDViMmUxMzRlMjllMTE1Y2JhOWI0MzJhMzI4ODp7ImN1cnJlbnRfdmlld19uYW1lIjoiZXNlcnZlcl9saXN0IiwiY3VycmVudF9hZG1pbl9pZCI6MSwiY3VycmVudF9yb2xlX2lkIjoxfQ==','2017-07-04 14:47:38'),('8sazni14bc51ssyyc3qgrp0uugnhtul2','MTZkNDJlOWRjZjM4ZTIxMjkzYTI4MWM1OWJjZGY1ZmFjZGRlYTdiMDp7ImN1cnJlbnRfdmlld19uYW1lIjoicHJvamVjdF9saXN0IiwiY3VycmVudF9hZG1pbl9pZCI6MSwiY3VycmVudF9yb2xlX2lkIjoxfQ==','2017-01-05 13:30:41'),('8tgr640ku3yuu1j8jynzhk7h7e1duzcl','MjI4NDY4Zjk5Y2UzZWZmZmFkY2ViNTUzOGFlYzM0OTBjNmVlNWVhMDp7ImN1cnJlbnRfdmlld19uYW1lIjoicHJvamVjdF9saXN0IiwiY3VycmVudF9hZG1pbl9pZCI6MjgsImN1cnJlbnRfcm9sZV9pZCI6M30=','2017-02-27 16:56:49'),('9jw06plufci8wjr3cggbdx6caqjsbq6t','NzU2OTA5OWU5ZGQ5Y2Q4MTA2ZmQwNDU5MjJmZWM2M2YwMjkwOTg4Mjp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseSIsImN1cnJlbnRfYWRtaW5faWQiOjEsImN1cnJlbnRfcm9sZV9pZCI6MX0=','2017-03-08 15:05:57'),('9ppprslcg1y1e13p8q9h179fln23sv9n','ZWM3ZGJmNzc2MTY4OTVjZWVjM2E2MDNhZDNmMDA5OWJlZDc2OTlhNzp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjE1LCJjdXJyZW50X3JvbGVfaWQiOjN9','2017-03-08 14:58:29'),('9qoglmu4l8b390yaxwpayfl53n4qns1d','OWUwNGZkOGZhNjAyYjViYmQzOTM4ZTA5MGIyYjViODM0Nzk5YWI0ODp7ImN1cnJlbnRfdmlld19uYW1lIjoiaG9zdF9saXN0IiwiY3VycmVudF9hZG1pbl9pZCI6MjMsImN1cnJlbnRfcm9sZV9pZCI6NH0=','2017-02-02 18:00:24'),('a7onfsltbv5a6929ehnxqo61ky87cwn1','YmJjMjZhZjAxODFhZTRiNGVjYjhjYWUyNzg0YTRmOGJiNTU1MjY0Yzp7ImN1cnJlbnRfdmlld19uYW1lIjoiaWRjX2xpc3QiLCJjdXJyZW50X2FkbWluX2lkIjoyMywiY3VycmVudF9yb2xlX2lkIjo0fQ==','2017-02-01 13:29:12'),('a8io8lwtf84wvvjhjj8cqhelwq6533j4','MGM0M2EwMzRmOWRjYjdjNDk5NzYzOGM4ODJjYzEwODQ0ZWNkMzk3ZDp7ImN1cnJlbnRfdmlld19uYW1lIjoib3BlcmF0aW9uX2xvZ19saXN0IiwiY3VycmVudF9hZG1pbl9pZCI6MSwiY3VycmVudF9yb2xlX2lkIjoxfQ==','2017-05-24 16:17:42'),('ar4wbvpcf4916z7n2h7yh7qxsjzajktz','MmMwYTRiNWM4NmU0NjBlZTk3ZDQ4ODZiYjE0YWI3ZDVlYTY0MGI0OTp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjI3LCJjdXJyZW50X3JvbGVfaWQiOjN9','2017-02-28 10:11:06'),('arv4ay78716qb0tg8lgtmc2ew4ybvmww','NmRhZGQ1MGYyNzNjYzA2ZjJlNTFkYmIxMWVmZGUzYTI0MjVkYTRjOTp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjksImN1cnJlbnRfcm9sZV9pZCI6Mn0=','2017-01-25 10:55:18'),('ch9toa4bkfcct4h0ex4tzz5nejw4mpgt','MmYyYjdiNTE5ODNkMzUwMTRmOTU5MjQxYWNlMmQ4NjhkMTQzYjNiZDp7ImN1cnJlbnRfdmlld19uYW1lIjoiaW5kZXgiLCJjdXJyZW50X2FkbWluX2lkIjoyMywiY3VycmVudF9yb2xlX2lkIjo0fQ==','2017-01-31 17:27:11'),('ck5gj9g2jzfuuczj1xvcnjc18hd6c4e5','YmVhMmNlMzBhNDAzY2FlMzU4NDA3ZGJjMjdiNWUzNzg1NWMwZGEyMTp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjE5LCJjdXJyZW50X3JvbGVfaWQiOjN9','2017-02-02 12:11:39'),('cmt3r4a3qffv77uvnf1w3px5pcyzcka7','YjRmZGY3NmJlYjgyNzk0OGNhMDg3MDlkYTM2MjZlMGFiZDcyZmU1Zjp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjEyLCJjdXJyZW50X3JvbGVfaWQiOjN9','2017-01-20 16:02:34'),('cq7fx2rjnjlg2hkiss7ho9ire3vgw5ck','MGM0M2EwMzRmOWRjYjdjNDk5NzYzOGM4ODJjYzEwODQ0ZWNkMzk3ZDp7ImN1cnJlbnRfdmlld19uYW1lIjoib3BlcmF0aW9uX2xvZ19saXN0IiwiY3VycmVudF9hZG1pbl9pZCI6MSwiY3VycmVudF9yb2xlX2lkIjoxfQ==','2017-05-19 14:33:48'),('d9inx7hnk3zqn3vje94mbhrg08d4o1nq','NmRhZGQ1MGYyNzNjYzA2ZjJlNTFkYmIxMWVmZGUzYTI0MjVkYTRjOTp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjksImN1cnJlbnRfcm9sZV9pZCI6Mn0=','2017-01-19 17:43:38'),('domzv80km9fnfmxt99yjmpjxvff4z2io','MDYyZmNlOWE4OGI3MzEzOTg1YTc2NmZmYmQ2MThkNDY1MmI4NjQwZDp7ImN1cnJlbnRfdmlld19uYW1lIjoicHJvamVjdF9saXN0IiwiY3VycmVudF9hZG1pbl9pZCI6MTksImN1cnJlbnRfcm9sZV9pZCI6Nn0=','2017-03-14 19:24:50'),('dp6m2mfov0xen4riwj6qx2d42n6aisk3','NmRhZGQ1MGYyNzNjYzA2ZjJlNTFkYmIxMWVmZGUzYTI0MjVkYTRjOTp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjksImN1cnJlbnRfcm9sZV9pZCI6Mn0=','2017-02-05 15:18:23'),('dpi6g37mx77f39nkmvolmfb3kyyw7kui','ZmI3ZmUxOTc0NmVmMDhjMDk3MDc0ZDZiODJkMmJhNzc1ZDc5NWY0Njp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjIzLCJjdXJyZW50X3JvbGVfaWQiOjR9','2017-02-03 16:07:39'),('f43gs3wyocylqsx8a42h6t014qseb915','NmRhZGQ1MGYyNzNjYzA2ZjJlNTFkYmIxMWVmZGUzYTI0MjVkYTRjOTp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjksImN1cnJlbnRfcm9sZV9pZCI6Mn0=','2017-01-30 10:39:22'),('fi7q1gjs2b43xlf64qnzlws6a83z0622','M2RiMjRiNmQ4YmViOWQ4OTlmM2Q5MmVhNTExMjk2OGE0ZTIyYTZiYjp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfZGV0YWlsIiwiY3VycmVudF9hZG1pbl9pZCI6MjQsImN1cnJlbnRfcm9sZV9pZCI6M30=','2017-02-01 20:18:39'),('fimg2f1l0nqli3e6nllyvl0dev0fz19u','YzQxZGRhZmM2NDMxMzRmZTgxMWE3ZGNlZGQyNjdjM2ZlMzEzMjE1ZDp7ImN1cnJlbnRfdmlld19uYW1lIjoiaW5kZXgiLCJjdXJyZW50X2FkbWluX2lkIjoxLCJjdXJyZW50X3JvbGVfaWQiOjF9','2016-12-30 10:01:55'),('fjguaijxpny59a4los1hiox85n4yuexs','MzY2ZjZmYWI2N2QxMmNhOTYxMjEwYmU4OTJkMjg4NzAxYTAwYjNkNzp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjI4LCJjdXJyZW50X3JvbGVfaWQiOjN9','2017-03-15 10:14:53'),('fpz02jylaaareefvs39fy75dpkkpgmgo','ZjQ3YmE3NjM2YTBiMGJjMzEzYTQ3OGEyN2RlNzQ5YmJmYWMyZmIzZjp7ImN1cnJlbnRfdmlld19uYW1lIjoiYWRtaW5fbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjEsImN1cnJlbnRfcm9sZV9pZCI6MX0=','2017-07-04 15:01:50'),('g4mjqdrftgicmsnx4vr49llf85virrgn','OWUwNGZkOGZhNjAyYjViYmQzOTM4ZTA5MGIyYjViODM0Nzk5YWI0ODp7ImN1cnJlbnRfdmlld19uYW1lIjoiaG9zdF9saXN0IiwiY3VycmVudF9hZG1pbl9pZCI6MjMsImN1cnJlbnRfcm9sZV9pZCI6NH0=','2017-02-02 09:37:39'),('g7wnqk5r5ay65ybp5cpu9wij6yw9wq41','YmM1ZGQzZjE5ZTAyM2IwNjFiOGVhYmJhNTVkNjhmNjQ3M2E0MDVlOTp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjE0LCJjdXJyZW50X3JvbGVfaWQiOjJ9','2017-02-03 14:36:25'),('hajdu702ptvj8wyj97a94bjg1ipzk36i','YzExMmFlMWFiYjlkNTNlNTk0Y2UyMjg0ZjJhYjJiYzg5MjdiNjE0OTp7ImN1cnJlbnRfdmlld19uYW1lIjoiZ3JvdXBfYWRkIiwiY3VycmVudF9hZG1pbl9pZCI6MSwiY3VycmVudF9yb2xlX2lkIjoxfQ==','2016-12-22 08:25:09'),('hwsf5yg3xhitn1lr0jqxv0hlvvezsfxc','NzU2OTA5OWU5ZGQ5Y2Q4MTA2ZmQwNDU5MjJmZWM2M2YwMjkwOTg4Mjp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseSIsImN1cnJlbnRfYWRtaW5faWQiOjEsImN1cnJlbnRfcm9sZV9pZCI6MX0=','2017-01-17 15:17:23'),('iedq6ontcmi7aigjwgu6y2emvpevsa1e','NzYxYzc1OTI2YjE2MjExZTgxMGYzOTgwMzQwMTI3MjIwYzBlNGI3NTp7ImN1cnJlbnRfdmlld19uYW1lIjoiaG9zdF9saXN0IiwiY3VycmVudF9hZG1pbl9pZCI6MSwiY3VycmVudF9yb2xlX2lkIjoxfQ==','2016-12-19 10:17:43'),('ixlygnm4pwahjntricxzc392k2gago7q','MzY2ZjZmYWI2N2QxMmNhOTYxMjEwYmU4OTJkMjg4NzAxYTAwYjNkNzp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjI4LCJjdXJyZW50X3JvbGVfaWQiOjN9','2017-03-09 16:59:27'),('izujg9gh4eimbuyuattkiwv46eoy81ts','MGFjNmM4M2IxYWJhOTc2Zjg5NmFmODRjZWU0NGRlMDM1YjdjZTM0Zjp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjI5LCJjdXJyZW50X3JvbGVfaWQiOjJ9','2017-03-14 16:00:33'),('jge25se54m45c97bu5fcizw56sn7vwkr','NDk0ZGE0YzI5M2E4YzI3YzdlZWM0YjBmNGY4M2Y3ZjZmMzAyZDU5NTp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfZGV0YWlsIiwiY3VycmVudF9hZG1pbl9pZCI6MTYsImN1cnJlbnRfcm9sZV9pZCI6M30=','2017-03-03 13:45:45'),('kar4fcz3wbmjb1z5xqgug13gjq916dek','YzZjYTI4MGFlMzg5YzY3NmUwMjFkZTkwZmI1ODY2ZTBlNmFhYWYwNzp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjIxLCJjdXJyZW50X3JvbGVfaWQiOjN9','2017-02-03 15:25:25'),('m6g1vp55c87yak1t74wrpnl1go3nc3ic','YzFjZTI0MTg5MWE1MjQ4ZTM5MTlkZDZiMGRiNzY0OTUzZDkwM2RjNzp7ImN1cnJlbnRfdmlld19uYW1lIjoiY2hhbmdlX21hbmFnZV9saXN0IiwiY3VycmVudF9hZG1pbl9pZCI6MSwiY3VycmVudF9yb2xlX2lkIjoxfQ==','2017-04-25 18:29:16'),('mbxto32wq6ww2cko5ac556bw4oxphy88','ZDY0OTQzOTM3YjQ5YzY1Yjc0ODA2ODdmMTM0YWJhNTM0ZmJmOWMwMDp7ImN1cnJlbnRfdmlld19uYW1lIjoicm9sZV9saXN0IiwiY3VycmVudF9hZG1pbl9pZCI6MjUsImN1cnJlbnRfcm9sZV9pZCI6NX0=','2017-02-02 18:56:59'),('mxsc7ert52irr7zgwktudvwkgybfvt3w','YzQxZGRhZmM2NDMxMzRmZTgxMWE3ZGNlZGQyNjdjM2ZlMzEzMjE1ZDp7ImN1cnJlbnRfdmlld19uYW1lIjoiaW5kZXgiLCJjdXJyZW50X2FkbWluX2lkIjoxLCJjdXJyZW50X3JvbGVfaWQiOjF9','2017-05-01 20:02:16'),('myzwae99nda1g56fh9ytzvhzdapg94mk','OGYyYjhiMzU4Njk5N2I4MmY5OThjYTE1YThhNGUwNDQ1YjI3NzZmODp7ImN1cnJlbnRfdmlld19uYW1lIjoicHJvamVjdF9saXN0IiwiY3VycmVudF9hZG1pbl9pZCI6MTQsImN1cnJlbnRfcm9sZV9pZCI6Mn0=','2017-02-03 14:33:16'),('ncyt21rec6k3dzifvnspav3qhz47roow','ODJhY2E3ZTliOGIwYzA0MzU5MDRhYzc5YmE2NWM1ZmMzMjVhNzBlMzp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjI0LCJjdXJyZW50X3JvbGVfaWQiOjN9','2017-03-08 17:37:31'),('olatroxhfnkpmtmhajlo1usd5nglofh8','ZjQ3YmE3NjM2YTBiMGJjMzEzYTQ3OGEyN2RlNzQ5YmJmYWMyZmIzZjp7ImN1cnJlbnRfdmlld19uYW1lIjoiYWRtaW5fbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjEsImN1cnJlbnRfcm9sZV9pZCI6MX0=','2017-06-14 21:01:23'),('om7rx6un45rlvyk9pcyb17kpihfx23zh','NWNlZTQyOGNhZDIzYWRkMWY1ZGY3MzY5N2JhMzU0NWVhOGNjMTBiYjp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjIwLCJjdXJyZW50X3JvbGVfaWQiOjN9','2017-01-24 17:57:05'),('qehuyt8a0daf1220hyfd7z1z8m2m3quv','NmRhZGQ1MGYyNzNjYzA2ZjJlNTFkYmIxMWVmZGUzYTI0MjVkYTRjOTp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjksImN1cnJlbnRfcm9sZV9pZCI6Mn0=','2017-01-19 17:37:48'),('rg3f8tqojipi9ibhbhxv3ck8c6odg660','YTRmMWExZTZlZjhmZjQ1NzYyNWYyYzNlM2UwNzhlOWFiMmJhN2E1ZDp7ImN1cnJlbnRfdmlld19uYW1lIjoiaG9zdF9lZGl0IiwiY3VycmVudF9hZG1pbl9pZCI6MSwiY3VycmVudF9yb2xlX2lkIjoxfQ==','2016-12-30 02:27:54'),('rlr9sgd8c0x4qj2h2uy4g4gpj0eb0mq3','NzUwNDkxNzVhZmI3ZDZmOWQ3YmQ2MDk1N2Y0YmZhYmFkMmYxZGE4Mjp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjEsImN1cnJlbnRfcm9sZV9pZCI6MX0=','2017-02-08 18:11:26'),('sfbn7tuvehdvyu1140tqelx0vfza9tzs','YzZjYTI4MGFlMzg5YzY3NmUwMjFkZTkwZmI1ODY2ZTBlNmFhYWYwNzp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjIxLCJjdXJyZW50X3JvbGVfaWQiOjN9','2017-03-02 15:11:34'),('sfn7d91p8acu2uebcce0y17lax7wu6qu','NzYxYzc1OTI2YjE2MjExZTgxMGYzOTgwMzQwMTI3MjIwYzBlNGI3NTp7ImN1cnJlbnRfdmlld19uYW1lIjoiaG9zdF9saXN0IiwiY3VycmVudF9hZG1pbl9pZCI6MSwiY3VycmVudF9yb2xlX2lkIjoxfQ==','2016-12-26 11:11:47'),('t7r75vxkzyrffh2vz7rl5tt1oe6wvnh7','NzUwNDkxNzVhZmI3ZDZmOWQ3YmQ2MDk1N2Y0YmZhYmFkMmYxZGE4Mjp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjEsImN1cnJlbnRfcm9sZV9pZCI6MX0=','2017-03-15 10:19:40'),('ta67xbeyl6q2sc1o4277d51krds9xik1','YTRmMWExZTZlZjhmZjQ1NzYyNWYyYzNlM2UwNzhlOWFiMmJhN2E1ZDp7ImN1cnJlbnRfdmlld19uYW1lIjoiaG9zdF9lZGl0IiwiY3VycmVudF9hZG1pbl9pZCI6MSwiY3VycmVudF9yb2xlX2lkIjoxfQ==','2017-01-02 09:28:50'),('tcitpytefrmuhq7td0bn32kq0dp7ogda','ZWM3ZGJmNzc2MTY4OTVjZWVjM2E2MDNhZDNmMDA5OWJlZDc2OTlhNzp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjE1LCJjdXJyZW50X3JvbGVfaWQiOjN9','2017-03-13 17:23:46'),('tg6dtuejf7aueewxy35hlkdjr0ecer5i','YjRmZGY3NmJlYjgyNzk0OGNhMDg3MDlkYTM2MjZlMGFiZDcyZmU1Zjp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjEyLCJjdXJyZW50X3JvbGVfaWQiOjN9','2016-12-30 09:57:14'),('th7tne0qcu1l47hajslemrp6yxhgq4tf','YzQxZGRhZmM2NDMxMzRmZTgxMWE3ZGNlZGQyNjdjM2ZlMzEzMjE1ZDp7ImN1cnJlbnRfdmlld19uYW1lIjoiaW5kZXgiLCJjdXJyZW50X2FkbWluX2lkIjoxLCJjdXJyZW50X3JvbGVfaWQiOjF9','2016-12-27 08:50:32'),('tnf6tum3klruqfxopauwmvur8pjinb7y','YzQxZGRhZmM2NDMxMzRmZTgxMWE3ZGNlZGQyNjdjM2ZlMzEzMjE1ZDp7ImN1cnJlbnRfdmlld19uYW1lIjoiaW5kZXgiLCJjdXJyZW50X2FkbWluX2lkIjoxLCJjdXJyZW50X3JvbGVfaWQiOjF9','2017-04-27 21:56:43'),('tpwodp3f6ph33kiuc5q32mktslcwoqth','MjVkYTYyZDk2YjQ4NjgwNzk2M2I5N2Q3N2U5YzQ5MmQxOTJjZGNjNDp7ImN1cnJlbnRfdmlld19uYW1lIjoiZ3JvdXBfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjEsImN1cnJlbnRfcm9sZV9pZCI6MX0=','2016-12-19 02:33:49'),('u2bhm535bd8v007e3bmksh9c393l8vql','NGRhYmIwMjVlZWIxMjFhOWJmOGFlYWJhMzFhNjJkMDZkMTJkNWMwZTp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjQsImN1cnJlbnRfcm9sZV9pZCI6Mn0=','2016-12-21 06:03:04'),('up1u4xe85q2ai7x8rt4l8iwjkxwnka9i','ODJiNWMwZDViMjI0ZmJlZTkxZTZlZGMwOTM0ODk1NTA3YjczZDU1Njp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjIyLCJjdXJyZW50X3JvbGVfaWQiOjN9','2017-01-30 11:00:14'),('uzxsv2embqre1ola8f87q2mdzzp7azhu','NmRhZGQ1MGYyNzNjYzA2ZjJlNTFkYmIxMWVmZGUzYTI0MjVkYTRjOTp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjksImN1cnJlbnRfcm9sZV9pZCI6Mn0=','2017-02-02 18:28:05'),('wnhy1xycphh2ow5bv6qdy0vklywukci4','YzQxZGRhZmM2NDMxMzRmZTgxMWE3ZGNlZGQyNjdjM2ZlMzEzMjE1ZDp7ImN1cnJlbnRfdmlld19uYW1lIjoiaW5kZXgiLCJjdXJyZW50X2FkbWluX2lkIjoxLCJjdXJyZW50X3JvbGVfaWQiOjF9','2017-01-23 13:51:44'),('x1kpyvo289iuq5vycnmmbe3t2fb6gkrm','NmRhZGQ1MGYyNzNjYzA2ZjJlNTFkYmIxMWVmZGUzYTI0MjVkYTRjOTp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjksImN1cnJlbnRfcm9sZV9pZCI6Mn0=','2017-01-18 16:37:24'),('x9d9f5y9ysffvcm8fni38yg37dgte3ty','MGU5M2VlZmY1ZTU0ZGM2NzEzODQwZTVhZWU2NDdjODU1MjBkYjMyYjp7ImN1cnJlbnRfdmlld19uYW1lIjoib3BlcmF0aW9uX2xvZ19saXN0IiwiY3VycmVudF9hZG1pbl9pZCI6MTQsImN1cnJlbnRfcm9sZV9pZCI6Mn0=','2017-03-14 11:50:05'),('xdfkk0ys2mfjh41nxrmmna9gbv7fsu5u','ODI5ODZiOWNhOGU0ODM2ZmU0NDg3ZGY5NTM2ZjBjM2MxMWVkODFiMjp7ImN1cnJlbnRfdmlld19uYW1lIjoicHJvamVjdF9lbnZfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjEsImN1cnJlbnRfcm9sZV9pZCI6MX0=','2017-02-21 17:13:23'),('xj384oc66all3f90tgll0wd029mxtjk8','NzUwNDkxNzVhZmI3ZDZmOWQ3YmQ2MDk1N2Y0YmZhYmFkMmYxZGE4Mjp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjEsImN1cnJlbnRfcm9sZV9pZCI6MX0=','2017-01-06 14:35:12'),('y3y5hq2gubn4tf9haoed9uquswb2edsw','OWUwNGZkOGZhNjAyYjViYmQzOTM4ZTA5MGIyYjViODM0Nzk5YWI0ODp7ImN1cnJlbnRfdmlld19uYW1lIjoiaG9zdF9saXN0IiwiY3VycmVudF9hZG1pbl9pZCI6MjMsImN1cnJlbnRfcm9sZV9pZCI6NH0=','2017-02-02 13:34:12'),('y41wloicgyt4k3t3l2up54hcfsvrqmy3','NzUwNDkxNzVhZmI3ZDZmOWQ3YmQ2MDk1N2Y0YmZhYmFkMmYxZGE4Mjp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjEsImN1cnJlbnRfcm9sZV9pZCI6MX0=','2017-03-14 16:38:45'),('y9xelks1gnz83skr14gu9wt0i294rjs3','NGYzZjg0YjI3YTU5ZWRiMjZkYjE0NjdjYjI1ODJjODQ4YzEzZDkwMTp7ImN1cnJlbnRfdmlld19uYW1lIjoicHJvamVjdF9saXN0IiwiY3VycmVudF9hZG1pbl9pZCI6MTYsImN1cnJlbnRfcm9sZV9pZCI6M30=','2017-01-23 11:57:16'),('ydyf43ndvu5wqhxtxfvqkju2go7l5lw3','ZTE0NjQ2NDBhZjM2YjQ5NmZlODI4YTBiMDNkOTZkYTQ4YWQzMjU3ZDp7ImN1cnJlbnRfdmlld19uYW1lIjoicHJvamVjdF9saXN0IiwiY3VycmVudF9hZG1pbl9pZCI6MzEsImN1cnJlbnRfcm9sZV9pZCI6M30=','2017-03-14 13:35:05'),('yk0o6l81thjo2ld82gx926bvxmoqxahf','NmRhZGQ1MGYyNzNjYzA2ZjJlNTFkYmIxMWVmZGUzYTI0MjVkYTRjOTp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjksImN1cnJlbnRfcm9sZV9pZCI6Mn0=','2017-02-06 13:52:54'),('ym288mmaucfmrs1xm6dhnh77rxgz9gl6','Y2Q1ZDA3OWVkMWU1Y2YyM2YzNzY0NThmZjNiZmRiZDRkMDljYTQ1ZTp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjEzLCJjdXJyZW50X3JvbGVfaWQiOjN9','2017-02-22 17:46:12'),('yzv5vfl06uq4b0q4n1afan51pul74b3j','NzYxYzc1OTI2YjE2MjExZTgxMGYzOTgwMzQwMTI3MjIwYzBlNGI3NTp7ImN1cnJlbnRfdmlld19uYW1lIjoiaG9zdF9saXN0IiwiY3VycmVudF9hZG1pbl9pZCI6MSwiY3VycmVudF9yb2xlX2lkIjoxfQ==','2016-12-28 06:36:26'),('zrhaqumn6ry5d76l4u38kgw15f9wirsq','MDliMjVkMTNlNmRjMWEwZDU4MDI4MTFjYzQ5MmY0M2QxOTBjODgwMjp7ImN1cnJlbnRfdmlld19uYW1lIjoicHVzaF9hcHBseV9sb2dfbGlzdCIsImN1cnJlbnRfYWRtaW5faWQiOjMwLCJjdXJyZW50X3JvbGVfaWQiOjN9','2017-03-14 15:16:16');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eproject`
--

DROP TABLE IF EXISTS `eproject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `eproject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pname` varchar(20) DEFAULT '' COMMENT '项目名称',
  `created_at` datetime DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eproject`
--

LOCK TABLES `eproject` WRITE;
/*!40000 ALTER TABLE `eproject` DISABLE KEYS */;
INSERT INTO `eproject` VALUES (1,'SI','2017-06-01 15:57:46'),(2,'ST','2017-06-01 15:57:49'),(3,'SF','2017-06-01 15:57:52'),(4,'GF','2017-06-01 15:57:54');
/*!40000 ALTER TABLE `eproject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eserver`
--

DROP TABLE IF EXISTS `eserver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `eserver` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `eproject_id` int(11) unsigned NOT NULL,
  `hostname` varchar(50) NOT NULL,
  `host` varchar(50) NOT NULL,
  `dport` int(10) NOT NULL DEFAULT '3306',
  `hport` int(10) NOT NULL DEFAULT '22',
  `huser` varchar(50) DEFAULT 'root',
  `hpassword` varchar(50) NOT NULL,
  `descr` varchar(50) DEFAULT NULL,
  `created_at` datetime NOT NULL COMMENT '添加时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eserver`
--

LOCK TABLES `eserver` WRITE;
/*!40000 ALTER TABLE `eserver` DISABLE KEYS */;
INSERT INTO `eserver` VALUES (1,1,'DBV1','10.32.14.1',3306,22,'root','*1C34E20E5F306AC4B1D219C80CD219FB20481952','test','2017-06-02 22:17:04'),(2,2,'DBV2','10.32.14.2',3306,22,'root','*1C34E20E5F306AC4B1D219C80CD219FB20481952','132131','2017-06-08 16:03:53'),(6,1,'DBV6','10.32.14.6',3306,22,'root','*1C34E20E5F306AC4B1D219C80CD219FB20481952','1','2017-06-08 16:14:02'),(7,1,'DBV7','10.32.14.7',3306,22,'root','*1C34E20E5F306AC4B1D219C80CD219FB20481952','1','2017-06-08 16:16:26'),(8,3,'DBV8','10.32.14.8',3306,22,'root','*1C34E20E5F306AC4B1D219C80CD219FB20481952','','2017-06-08 16:18:49'),(9,2,'DBV9','10.32.14.9',3306,22,'root','*1C34E20E5F306AC4B1D219C80CD219FB20481952','3231','2017-06-08 16:31:11'),(10,3,'DBV10','10.32.14.10',3306,22,'root','*1C34E20E5F306AC4B1D219C80CD219FB20481952','','2017-06-08 16:33:46'),(11,2,'ECEJ_DB1','10.32.14.11',3309,22,'dbaadmin','3e3c4e9582e9592a0923dc4a8a4e548e','','2017-06-08 16:42:13'),(12,1,'fuck','10.32.32.45',3306,22,'hello','helloword','','2017-06-12 17:25:42'),(14,2,'134','134',14,14,'asdad','YXNkYWRhZGFk\n','asdad','2017-06-12 17:29:32'),(15,3,'world','10.89.8.9',2203,22,'world','d29ybGQ=','world','2017-06-12 17:31:18');
/*!40000 ALTER TABLE `eserver` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menu` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '菜单ID',
  `module_id` int(6) NOT NULL DEFAULT '0' COMMENT '模块ID',
  `privilege_id` int(11) DEFAULT '-1' COMMENT '权限ID',
  `menu_name` char(10) NOT NULL DEFAULT '' COMMENT '菜单名称',
  `target` char(10) NOT NULL DEFAULT '_self' COMMENT '跳转目标',
  `target_url` varchar(200) DEFAULT '' COMMENT '跳转URL',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '状态：1-启用，2-停用',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6003 DEFAULT CHARSET=utf8 COMMENT='菜单';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (1001,100,100103,'用户管理','_self','',1),(1002,100,100203,'角色管理','_self','',1),(1003,100,100303,'模块管理','_self','',1),(1004,100,100403,'权限组管理','_self','',1),(1005,100,100503,'权限管理','_self','',1),(1006,100,100603,'菜单管理','_self','',1),(1007,100,100701,'日志管理','_self','',1),(6001,600,600101,'环境分类','_self','eproject_list',1),(6002,600,600102,'服务器列表','_self','eserver_list',1);
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `module`
--

DROP TABLE IF EXISTS `module`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `module` (
  `id` int(5) unsigned NOT NULL AUTO_INCREMENT COMMENT '模块ID',
  `module_name` char(10) NOT NULL DEFAULT '' COMMENT '模块名称',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '状态：1-启用，2-停用',
  `list_order` int(11) NOT NULL DEFAULT '0' COMMENT '排序',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=601 DEFAULT CHARSET=utf8 COMMENT='模块';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `module`
--

LOCK TABLES `module` WRITE;
/*!40000 ALTER TABLE `module` DISABLE KEYS */;
INSERT INTO `module` VALUES (100,'系统管理',1,2),(600,'环境管理',1,3);
/*!40000 ALTER TABLE `module` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operation_log`
--

DROP TABLE IF EXISTS `operation_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `operation_log` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '日志ID',
  `admin_id` int(11) NOT NULL COMMENT '账号ID',
  `admin_name` char(20) DEFAULT NULL COMMENT '账号',
  `privilege_id` int(11) NOT NULL COMMENT '权限ID',
  `request_method` varchar(10) NOT NULL DEFAULT 'POST' COMMENT 'HTTP请求方法',
  `query_string` varchar(100) DEFAULT NULL COMMENT '请求参数',
  `change_data` varchar(500) DEFAULT NULL COMMENT '修改的数据',
  `ip` char(15) NOT NULL DEFAULT '' COMMENT '操作者IP',
  `create_at` datetime NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41231 DEFAULT CHARSET=utf8 COMMENT='系统操作日志';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operation_log`
--

LOCK TABLES `operation_log` WRITE;
/*!40000 ALTER TABLE `operation_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `operation_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `privilege`
--

DROP TABLE IF EXISTS `privilege`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `privilege` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '权限ID',
  `privilege_group_id` int(6) NOT NULL DEFAULT '1' COMMENT '权限分组',
  `privilege_name` char(20) NOT NULL DEFAULT '' COMMENT '权限名称',
  `request_path` char(100) NOT NULL COMMENT '请求路径',
  `view_func` char(50) NOT NULL DEFAULT '' COMMENT 'view函数名称',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '状态：1-启用，2-停用',
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_url` (`view_func`)
) ENGINE=InnoDB AUTO_INCREMENT=600104 DEFAULT CHARSET=utf8 COMMENT='权限';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `privilege`
--

LOCK TABLES `privilege` WRITE;
/*!40000 ALTER TABLE `privilege` DISABLE KEYS */;
INSERT INTO `privilege` VALUES (100101,1001,'用户添加','/account/admin/add','admin_add',1),(100102,1001,'用户编辑','/account/admin/edit','admin_edit',1),(100103,1001,'用户列表','/account/admin/list','admin_list',1),(100104,1001,'用户状态变更','/account/admin/change_status','admin_change_status',1),(100105,1001,'重置密码','/account/admin/reset_pwd','admin_reset_pwd',1),(100201,1002,'角色添加','/account/role/add','role_add',1),(100202,1002,'角色编辑','/account/role/edit','role_edit',1),(100203,1002,'角色列表','/account/role/list','role_list',1),(100204,1002,'角色状态变更','/account/role/change_status','role_change_status',1),(100301,1003,'模块添加','/account/module/add','module_add',1),(100302,1003,'模块编辑','/account/module/edit','module_edit',1),(100303,1003,'模块列表','/account/module/list','module_list',1),(100304,1003,'模块状态变更','/account/module/change_status','module_change_status',1),(100401,1004,'权限组添加','/account/privilege_group/add','privilege_group_add',1),(100402,1004,'权限组编辑','/account/privilege_group/edit','privilege_group_edit',1),(100403,1004,'权限组列表','/account/privilege_group/list','privilege_group_list',1),(100404,1004,'权限组状态变更','/account/privilege_group/change_status','privilege_group_change_status',1),(100501,1005,'权限添加','/account/privilege/add','privilege_add',1),(100502,1005,'权限编辑','/account/privilege/edit','privilege_edit',1),(100503,1005,'权限列表','/account/privilege/list','privilege_list',1),(100504,1005,'权限状态变更','/account/privilege/change_status','privilege_change_status',1),(100601,1006,'菜单添加','/account/menu/add','menu_add',1),(100602,1006,'菜单编辑','/account/menu/edit','menu_edit',1),(100603,1006,'菜单列表','/account/menu/list','menu_list',1),(100604,1006,'菜单状态变更','/account/menu/change_status','menu_change_status',1),(100701,1007,'日志列表','/account/operation_log/list','operation_log_list',1),(100702,1007,'日志详情','/account/operation_log/show','operation_log_show',1),(600101,6001,'环境分类','eproject_list','eproject_list',1),(600102,6001,'服务器列表','eserver_list','eserver_list',1),(600103,6001,'添加服务器','eserver_add','eserver_add',1);
/*!40000 ALTER TABLE `privilege` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `privilege_group`
--

DROP TABLE IF EXISTS `privilege_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `privilege_group` (
  `id` int(5) unsigned NOT NULL AUTO_INCREMENT COMMENT '权限组ID',
  `group_name` char(20) NOT NULL DEFAULT '' COMMENT '权限组名称',
  `module_id` int(6) NOT NULL COMMENT '模块ID',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '状态：1-启用，2-停用',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6002 DEFAULT CHARSET=utf8 COMMENT='权限组';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `privilege_group`
--

LOCK TABLES `privilege_group` WRITE;
/*!40000 ALTER TABLE `privilege_group` DISABLE KEYS */;
INSERT INTO `privilege_group` VALUES (1001,'用户管理',100,1),(1002,'角色管理',100,1),(1003,'模块管理',100,1),(1004,'权限组管理',100,1),(1005,'权限管理',100,1),(1006,'菜单管理',100,1),(1007,'日志管理',100,1),(6001,'环境分类管理',600,1);
/*!40000 ALTER TABLE `privilege_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `id` int(5) unsigned NOT NULL AUTO_INCREMENT COMMENT '角色ID',
  `role_name` char(20) NOT NULL DEFAULT '' COMMENT '角色名称',
  `description` varchar(200) NOT NULL DEFAULT '' COMMENT '角色描述',
  `status` tinyint(1) NOT NULL DEFAULT '0' COMMENT '状态：1-开启，0-停用',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COMMENT='角色表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'超级管理员','所有权限',1),(3,'开发工程师','开发工程师开发工程师',1),(4,'运维工程师','运帷工程师运帷工程师',1);
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role_privilege`
--

DROP TABLE IF EXISTS `role_privilege`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role_privilege` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `role_id` int(11) NOT NULL COMMENT '角色ID',
  `privilege_id` int(6) NOT NULL COMMENT '权限ID',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=212 DEFAULT CHARSET=utf8 COMMENT='角色&权限表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role_privilege`
--

LOCK TABLES `role_privilege` WRITE;
/*!40000 ALTER TABLE `role_privilege` DISABLE KEYS */;
INSERT INTO `role_privilege` VALUES (1,4,400101),(2,4,400102),(3,4,400103),(4,4,400104),(5,4,400105),(6,4,400202),(7,4,400203),(8,4,400204),(9,4,400205),(10,4,400302),(11,4,400308),(12,4,400309),(13,4,400201),(14,2,500101),(15,2,500102),(16,2,500103),(17,2,500104),(18,2,400302),(19,2,400303),(20,2,400305),(21,2,400306),(22,2,400307),(23,2,400310),(24,3,500103),(25,3,500101),(26,3,500102),(27,3,400103),(28,3,500104),(29,3,400105),(31,3,400301),(32,3,400302),(33,3,400205),(34,3,400306),(37,2,400105),(41,2,400103),(43,2,100701),(44,2,100702),(45,4,500101),(46,4,500102),(47,4,500103),(48,4,500104),(49,4,200201),(50,4,200202),(51,4,200203),(52,4,200101),(53,4,200102),(54,4,200103),(55,4,300201),(56,4,300202),(57,4,300203),(58,4,300204),(59,4,300101),(60,4,300102),(61,4,300103),(62,4,200401),(63,4,200402),(64,4,200403),(65,4,200301),(66,4,200302),(67,4,200303),(68,3,400311),(69,4,10200104),(70,5,500203),(71,5,400206),(72,5,100101),(73,5,100102),(74,5,100103),(75,5,500104),(76,5,200201),(77,5,200202),(78,5,200203),(79,5,500215),(80,5,400301),(81,5,100401),(82,5,100501),(83,5,100502),(84,5,100503),(85,5,100504),(86,5,500207),(87,5,500101),(88,5,400305),(89,5,200101),(90,5,200102),(91,5,200103),(92,5,10200104),(93,5,300201),(94,5,300202),(95,5,300203),(96,5,300204),(97,5,300205),(98,5,400302),(99,5,400303),(100,5,100104),(101,5,100402),(102,5,100403),(103,5,100404),(104,5,400309),(105,5,400310),(106,5,500105),(107,5,400308),(108,5,500204),(109,5,400306),(110,5,100202),(111,5,300101),(112,5,300102),(113,5,500102),(114,5,400204),(115,5,400201),(116,5,400202),(117,5,400203),(119,5,400205),(120,5,100302),(121,5,100301),(122,5,100304),(123,5,200401),(124,5,200402),(125,5,200403),(126,5,400311),(127,5,100303),(128,5,400307),(129,5,100702),(130,5,400105),(131,5,500103),(132,5,400101),(133,5,400102),(134,5,400103),(135,5,400104),(136,5,100201),(137,5,500202),(138,5,100203),(139,5,100204),(140,5,500205),(141,5,500206),(142,5,200303),(143,5,200302),(144,5,100701),(145,5,10200105),(146,5,100603),(147,5,500201),(148,5,100601),(149,5,100602),(150,5,300103),(151,5,100604),(152,5,400106),(153,5,200301),(154,3,10300101),(155,6,10300101),(156,6,400103),(157,6,400105),(158,6,10300105),(159,6,400203),(160,6,400301),(161,6,400302),(162,6,400205),(164,6,400306),(165,6,400307),(166,6,400308),(167,6,400309),(168,6,400310),(169,6,400311),(170,6,400303),(171,6,500104),(172,6,500105),(173,6,500101),(174,6,500102),(175,6,500103),(176,6,400305),(177,6,100702),(178,6,100701),(179,6,600101),(180,6,600102),(181,6,600103),(182,4,100101),(183,4,100102),(184,4,100103),(185,4,100104),(186,4,100105),(187,4,100501),(188,4,100502),(189,4,100503),(190,4,100504),(191,4,600101),(192,4,600102),(193,4,600103),(194,4,100401),(195,4,100402),(196,4,100403),(197,4,100404),(198,4,100301),(199,4,100302),(200,4,100303),(201,4,100304),(202,4,100701),(203,4,100702),(204,4,100201),(205,4,100202),(206,4,100203),(207,4,100204),(208,4,100601),(209,4,100602),(210,4,100603),(211,4,100604);
/*!40000 ALTER TABLE `role_privilege` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `server`
--

DROP TABLE IF EXISTS `server`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cabinet_id` int(11) DEFAULT '1',
  `server_type` tinyint(1) DEFAULT '1' COMMENT '1-物理机、2-虚拟机、3-云主机',
  `manage_ip` varchar(32) DEFAULT NULL COMMENT '管理IP',
  `inside_ip` varchar(50) DEFAULT NULL COMMENT '内网IP,''：''分割',
  `outside_ip` varchar(40) DEFAULT NULL COMMENT '外网IP,''：''分割',
  `hostname` varchar(128) NOT NULL DEFAULT '' COMMENT '主机名',
  `port` int(11) DEFAULT NULL COMMENT 'SSH端口',
  `brand` varchar(64) DEFAULT NULL COMMENT '品牌型号',
  `mac` varchar(20) DEFAULT NULL COMMENT 'MAC地址',
  `cpu` varchar(64) DEFAULT NULL COMMENT 'CPU',
  `memory` varchar(100) DEFAULT NULL COMMENT '内存',
  `disk` varchar(200) DEFAULT NULL,
  `system_type` varchar(32) DEFAULT NULL COMMENT '系统类型',
  `system_version` varchar(50) DEFAULT NULL,
  `system_arch` varchar(160) DEFAULT NULL COMMENT '系统平台',
  `position` varchar(10) DEFAULT NULL COMMENT '机柜位置',
  `status` tinyint(1) DEFAULT '1' COMMENT '状态：1-使用，2-闲置，3-废弃，4-维修',
  `sn` varchar(128) DEFAULT NULL COMMENT '服务器编号',
  `comment` varchar(128) DEFAULT NULL COMMENT '备注',
  `create_at` datetime NOT NULL COMMENT '添加时间',
  `update_at` datetime NOT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `hostname` (`hostname`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8 COMMENT='服务器表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `server`
--

LOCK TABLES `server` WRITE;
/*!40000 ALTER TABLE `server` DISABLE KEYS */;
INSERT INTO `server` VALUES (1,1,2,'192.168.10.20','','','vip-dev-web',22,'VMware, Inc.','00:50:56:a2:68:40','1','3791MB','sda : 50.00 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'4222A582-8916-C0F2-F7E1-4FABA75572C6','数据中心开发机','2016-12-27 17:40:12','2017-04-07 00:00:11'),(2,1,2,'192.168.10.42','','','vip-web-01',22,'VMware, Inc.','00:50:56:a2:4c:f0','1','3791MB','sda : 50.00 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'4222CA7A-FEA4-9A92-A8A9-9651767F0102','VIP线上WEB01','2016-12-27 17:40:12','2017-04-07 00:00:11'),(3,1,1,'192.168.10.58','','','dev-uc-web',22,'VMware, Inc.','00:50:56:a2:45:5c','1','3791MB','sda : 50.00 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'42223E9C-E897-4A9B-2385-394BEF9C0538','VIP用户中心开发机','2016-12-20 15:51:41','2017-04-07 00:00:12'),(4,1,1,'61.172.238.249','','','dev-xdq-web',22,'','00:16:3e:2d:2c:29','16','23933MB','xvde : 400.00 GB  xvdb : 80.00 GB  xvdc : 20.00 GB  xvda : 20.00 GB  ','','CentOS 6 x86_64','Intel(R) Xeon(R) CPU E5-2640 v3 @ 2.60GHz','',1,'','信贷圈开发机','2016-12-27 17:40:12','2017-04-07 00:00:12'),(5,1,2,'210.14.153.139','','','bs_service_03',22206,'Red Hat','52:54:00:f1:ae:8c','4','3734MB','vda : 100.00 GB  ','','CentOS 6 x86_64','QEMU Virtual CPU version (cpu64-rhel6)','',1,'3CA84BC6-4C08-B104-FBEE-81942BD69C3F','基础服务03','2016-12-28 14:49:20','2017-04-07 00:00:11'),(6,1,2,'192.168.10.71','','','user-center-web01',22,'VMware, Inc.','00:50:56:a2:29:90','4','3791MB','sda : 10.00 GB  sdb : 300.00 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'42223519-AAEB-A3F3-7D3F-0712B18AA7F2','用户中心线上web01','2017-01-04 14:14:24','2017-04-07 00:00:12'),(7,1,2,'192.168.10.72','','','user-center-web02',22,'VMware, Inc.','00:50:56:a2:18:2c','4','3791MB','sda : 48.09 GB  sdb : 300.00 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'422259A1-5C4B-D12D-C89B-0BC7AB4C95E9','用户中心线上web02','2017-01-04 14:25:12','2017-04-07 00:00:12'),(8,1,2,'192.168.10.61','','','baoxian-dev-web01',22,'VMware, Inc.','00:50:56:a2:35:fa','1','3791MB','sda : 50.00 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'42229701-4D08-6F69-EEE5-AE22AD78532E','保险平台开发WEB','2017-01-06 16:49:01','2017-04-07 00:00:11'),(9,1,1,'192.168.10.69','','','baoxian-web01',22,'VMware, Inc.','00:50:56:a2:1d:c5','1','3791MB','sda : 50.00 GB  sdb : 300.00 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'4222C892-7FFA-FFA0-2A3B-82BD62E1ED69','保险平台web01','2017-01-06 17:08:58','2017-04-07 00:00:12'),(10,1,2,'192.168.10.70','','','baoxian-web02',22,'VMware, Inc.','00:50:56:a2:69:29','4','3791MB','sda : 75.76 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'422225F3-FE1F-78B2-7182-30A022E6634D','保险平台web02','2017-01-06 17:09:41','2017-04-07 00:00:11'),(11,1,2,'125.208.12.56','','','release-xdq-web',22,'Fedora Project','00:3e:07:c1:4b:e2','2','1869MB','vda : 20.00 GB  vdb : 20.00 GB  sr1 : 1.52 MB  vdc : 100.00 GB  ','','CentOS 6 x86_64','QEMU Virtual CPU version (cpu64-rhel6)','',1,'64A6743D-2668-7D48-8177-001819EB11D5','信贷圈仿真机器','2017-01-10 11:04:16','2017-04-07 00:00:11'),(12,1,2,'192.168.10.94','','','shebao-online01',22,'VMware, Inc.','00:50:56:a2:5b:52','2','1840MB','sda : 200.00 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'422275C4-6971-9516-6F4E-FE638E574556','社保前端web01','2017-02-13 10:43:34','2017-04-07 00:00:12'),(13,1,2,'192.168.10.95','','','shebao-online02',22,'VMware, Inc.','00:50:56:a2:26:01','2','1840MB','sda : 200.00 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'4222B463-0CEA-051F-98D6-490FFE67697A','社保前端web02','2017-02-13 10:44:56','2017-04-07 00:00:12'),(14,1,2,'192.168.10.93','','','shebao-test',22,'VMware, Inc.','00:50:56:a2:66:5a','1','1840MB','sda : 50.00 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'42223A57-6BF3-B4ED-7204-15BD1BF576F0','社保平台测试','2017-02-13 10:46:07','2017-04-07 00:00:11'),(15,1,2,'210.14.153.139','','','shebao-web-01',22203,'Red Hat','52:54:00:40:d3:2f','4','3734MB','vda : 100.00 GB  ','','CentOS 6 x86_64','QEMU Virtual CPU version (cpu64-rhel6)','',1,'65EC4719-E2D9-CF0F-FC16-4C950E8A262A','社保平台后端','2017-02-22 13:58:55','2017-04-07 00:00:12'),(16,1,2,'210.14.153.139','','','shebao-web-02',22204,'Red Hat','52:54:00:46:42:95','4','3734MB','vda : 30.00 GB  ','','CentOS 6 x86_64','QEMU Virtual CPU version (cpu64-rhel6)','',1,'11E8E810-2DE1-50F7-A9F5-9BEEE64D95BB','社保平台后端','2017-02-22 13:59:54','2017-04-07 00:00:12'),(17,1,1,'192.168.10.63','','','vip-web-02',22,'VMware, Inc.','00:50:56:a2:1f:78','1','3791MB','sda : 50.00 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'42220008-8740-DF01-7177-872E9DD70691','VIP线上WEB02','2017-02-28 10:20:16','2017-04-07 00:00:11'),(18,1,1,'192.168.10.80','','','vip-web-03',22,'VMware, Inc.','00:50:56:a2:21:50','1','3791MB','sda : 50.00 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'42227154-8339-83A1-FD78-2351A35411B5','VIP线上WEB03','2017-02-28 10:21:19','2017-04-07 00:00:11'),(19,1,1,'192.168.10.142','','','platfrom-test-web02',22,'VMware, Inc.','00:50:56:b5:25:c3','2','1839MB','sda : 50.00 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'4235DE8D-21D7-E94F-7B1E-C88B35C26960','产品平台服务开发机','2017-03-07 11:11:20','2017-04-07 00:00:11'),(20,1,2,'192.168.10.150','','','yunwei-test2-10-150',22,'VMware, Inc.','00:50:56:b5:27:c6','2','3791MB','sda : 50.00 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'4235DEAE-C9F7-0166-C259-4AF100FB9694','运维测试机','2017-03-21 14:31:58','2017-04-07 00:00:11'),(21,1,2,'192.168.10.129','','','huoban-web01-129',22,'VMware, Inc.','00:50:56:a2:26:55','2','3791MB','sda : 50.00 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'4222A26F-6D56-8B1D-96D3-AB76B99215A5','伙伴运营web01','2017-03-23 16:04:34','2017-04-07 00:00:11'),(22,1,2,'192.168.10.130','','','huoban-web02-130',22,'VMware, Inc.','00:50:56:a2:1a:cf','2','3791MB','sda : 50.00 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'42228728-29B1-D70B-24C7-63FAB70B6D4A','伙伴运营web02','2017-03-23 16:05:55','2017-04-07 00:00:12'),(23,1,2,'192.168.10.34','','','guanggao-web1-34',22,'VMware, Inc.','00:50:56:b5:77:f8','2','1840MB','sda : 50.00 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'4235B465-5907-C849-693B-BFC3B337D4A7','广告与平台共用WEB','2017-03-27 15:42:48','2017-04-07 00:00:12'),(24,1,2,'192.168.10.35','','','guanggao-web2-35',22,'VMware, Inc.','00:50:56:b5:3b:40','2','1840MB','sda : 50.00 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'42354B50-CE17-CFDD-7D8E-E5F8FE8881D0','广告与平台共用WEB2','2017-03-27 16:01:00','2017-04-07 00:00:12'),(25,1,2,'192.168.10.155','','','DevOps-test-155',22,'VMware, Inc.','00:50:56:b5:03:5e','2','3791MB','sda : 50.00 GB  sdb : 100.00 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'42357EE8-890A-BD0C-F7C2-BF89D0BD4D7F','102-DevOps-test-10.155','2017-03-30 15:41:02','2017-04-07 00:00:12'),(26,1,2,'192.168.10.10','','','yun-test-10',22,'VMware, Inc.','00:50:56:b5:0b:50','2','3791MB','sda : 50.00 GB  sdb : 100.00 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'42357B13-A433-CBF2-175F-239700870169','yum click测试机','2017-03-31 16:56:32','2017-04-07 00:00:11'),(27,1,2,'192.168.10.147','','','yun-click1-147',22,'VMware, Inc.','00:50:56:b5:7b:3a','2','3791MB','sda : 50.00 GB  sdb : 100.00 GB  ','','CentOS 7 x86_64','Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz','',1,'4235FCCB-23F0-1FA4-64D0-47F6AF783EE3','click正式机','2017-04-01 14:34:01','2017-04-07 00:00:12');
/*!40000 ALTER TABLE `server` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service`
--

DROP TABLE IF EXISTS `service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `service` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `server_id` int(11) NOT NULL DEFAULT '1' COMMENT '服务器ID',
  `service_type` tinyint(1) NOT NULL DEFAULT '1' COMMENT '类型：1-WEB-SERVER，2-MYSQL，3-REDIS，4-MONGODB，5-MQ，6-其它',
  `service_name` varchar(32) NOT NULL DEFAULT '' COMMENT '服务名字',
  `port` smallint(6) NOT NULL DEFAULT '1' COMMENT '端口',
  `config_file` varchar(200) DEFAULT NULL COMMENT '配置文件',
  `install_path` varchar(200) DEFAULT NULL COMMENT '安装目录',
  `log_path` varchar(200) DEFAULT NULL COMMENT '日志目录',
  `status` tinyint(2) NOT NULL DEFAULT '1' COMMENT '状态：1-启用,2-停用',
  `create_at` datetime NOT NULL COMMENT '添加时间',
  `update_at` datetime NOT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_name` (`service_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='服务表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service`
--

LOCK TABLES `service` WRITE;
/*!40000 ALTER TABLE `service` DISABLE KEYS */;
/*!40000 ALTER TABLE `service` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-06-20 15:02:14
