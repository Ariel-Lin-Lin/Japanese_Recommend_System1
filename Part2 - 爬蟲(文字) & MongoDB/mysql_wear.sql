CREATE DATABASE IF NOT EXISTS wear;

USE wear;

CREATE TABLE UserInfo 
(
  Uid            VARCHAR(20),
  Gender         VARCHAR(10),
  Height          VARCHAR(10),
  UserURL        VARCHAR(100),
  UserRanking     VARCHAR(10),
  CONSTRAINT UserInfo PRIMARY KEY (Uid)
) ENGINE = INNODB;

CREATE TABLE OftenUseBrand
(
  Uid            VARCHAR(20),
  Brands         VARCHAR(20),
  CONSTRAINT OftenUseBrand_Uid_FK FOREIGN KEY (Uid) REFERENCES UserInfo (Uid)
) ENGINE = INNODB;

CREATE TABLE Outfit
(
  OutfitId         VARCHAR(50),
  Uid              VARCHAR(20),
  Likes            VARCHAR(10),
  PicUploadTime    VARCHAR(20),
  PicUrl           VARCHAR(120),

  CONSTRAINT Outfit_Uid_FK FOREIGN KEY (Uid) REFERENCES UserInfo (Uid),
  CONSTRAINT Outfit_OutfitId_PK PRIMARY KEY (OutfitId)
)ENGINE = INNODB;

CREATE TABLE Style
(
  OutfitId            VARCHAR(40),
  Style               VARCHAR(50),

  CONSTRAINT Style_OutfitId_FK FOREIGN KEY (OutfitId) REFERENCES Outfit (OutfitId)
)ENGINE = INNODB;



CREATE TABLE ItemInfo
(
  ItemId             VARCHAR(20),
  purchaseUrl        VARCHAR(200),
  ItemType           VARCHAR(20),
  color				VARCHAR(20),
  brand              VARCHAR(20),
  CONSTRAINT ItemInfo_ItemId_PK PRIMARY KEY (ItemId)
)ENGINE = INNODB;

CREATE TABLE Item
(
  OutfitId            VARCHAR(30),
  ItemId              VARCHAR(30),

  CONSTRAINT Item_OutfitId_FK FOREIGN KEY (OutfitId) REFERENCES Outfit (OutfitId),
  CONSTRAINT ItemInfo_ItemId_FK FOREIGN KEY (ItemId) REFERENCES ItemInfo (ItemId),
  CONSTRAINT Item_OutfitId_ItemId_PK PRIMARY KEY (OutfitId,ItemId)
)ENGINE = INNODB;