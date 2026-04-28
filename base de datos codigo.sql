-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`departamentos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`departamentos` (
  `iddepartamentos` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NULL,
  `descripcion` VARCHAR(255) NULL,
  `personacargo` INT NULL,
  PRIMARY KEY (`iddepartamentos`),
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`empleado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`empleado` (
  `idempleado` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NULL,
  `email` VARCHAR(255) NULL,
  `direccion` VARCHAR(255) NULL,
  `telefono` VARCHAR(30) NULL,
  `fecha_inicio` DATE NULL,
  `salario` DECIMAL NULL,
  PRIMARY KEY (`idempleado`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `telefono_UNIQUE` (`telefono` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`proyecto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`proyecto` (
  `idproyecto` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NULL,
  `descripcion` VARCHAR(255) NULL,
  `fecha_inicio` DATE NULL,
  PRIMARY KEY (`idproyecto`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`RegistroTiempo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`RegistroTiempo` (
  `idRegistroTiempo` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATE NULL,
  `horas_trabajadas` VARCHAR(45) NULL,
  `descripcion` VARCHAR(255) NULL,
  `empleado_idempleado` INT NOT NULL,
  PRIMARY KEY (`idRegistroTiempo`),
  INDEX `fk_RegistroTiempo_empleado1_idx` (`empleado_idempleado` ASC) VISIBLE,
  CONSTRAINT `fk_RegistroTiempo_empleado1`
    FOREIGN KEY (`empleado_idempleado`)
    REFERENCES `mydb`.`empleado` (`idempleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`asignacion_proyecto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`asignacion_proyecto` (
  `empleado_idempleado` INT NOT NULL,
  `proyecto_idproyecto` INT NOT NULL,
  `idasignacionproyecto` INT NOT NULL AUTO_INCREMENT,
  INDEX `fk_empleado_has_proyecto_proyecto1_idx` (`proyecto_idproyecto` ASC) VISIBLE,
  INDEX `fk_empleado_has_proyecto_empleado_idx` (`empleado_idempleado` ASC) VISIBLE,
  PRIMARY KEY (`idasignacionproyecto`),
  UNIQUE INDEX `empleado_idempleado_UNIQUE` (`empleado_idempleado` ASC) VISIBLE,
  CONSTRAINT `fk_empleado_has_proyecto_empleado`
    FOREIGN KEY (`empleado_idempleado`)
    REFERENCES `mydb`.`empleado` (`idempleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_empleado_has_proyecto_proyecto1`
    FOREIGN KEY (`proyecto_idproyecto`)
    REFERENCES `mydb`.`proyecto` (`idproyecto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`asignacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`asignacion` (
  `empleado_idempleado` INT NOT NULL,
  `departamentos_iddepartamentos` INT NOT NULL,
  `idasignacion` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`idasignacion`),
  INDEX `fk_empleado_has_departamentos_departamentos1_idx` (`departamentos_iddepartamentos` ASC) VISIBLE,
  INDEX `fk_empleado_has_departamentos_empleado1_idx` (`empleado_idempleado` ASC) VISIBLE,
  CONSTRAINT `fk_empleado_has_departamentos_empleado1`
    FOREIGN KEY (`empleado_idempleado`)
    REFERENCES `mydb`.`empleado` (`idempleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_empleado_has_departamentos_departamentos1`
    FOREIGN KEY (`departamentos_iddepartamentos`)
    REFERENCES `mydb`.`departamentos` (`iddepartamentos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`informes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`informes` (
  `idinformes` INT NOT NULL AUTO_INCREMENT,
  `nombre_informe` VARCHAR(100) NULL,
  `RegistroTiempo_idRegistroTiempo` INT NOT NULL,
  `empleado_idempleado` INT NOT NULL,
  `departamentos_iddepartamentos` INT NOT NULL,
  PRIMARY KEY (`idinformes`),
  INDEX `fk_informes_RegistroTiempo1_idx` (`RegistroTiempo_idRegistroTiempo` ASC) VISIBLE,
  INDEX `fk_informes_empleado1_idx` (`empleado_idempleado` ASC) VISIBLE,
  INDEX `fk_informes_departamentos1_idx` (`departamentos_iddepartamentos` ASC) VISIBLE,
  CONSTRAINT `fk_informes_RegistroTiempo1`
    FOREIGN KEY (`RegistroTiempo_idRegistroTiempo`)
    REFERENCES `mydb`.`RegistroTiempo` (`idRegistroTiempo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_informes_empleado1`
    FOREIGN KEY (`empleado_idempleado`)
    REFERENCES `mydb`.`empleado` (`idempleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_informes_departamentos1`
    FOREIGN KEY (`departamentos_iddepartamentos`)
    REFERENCES `mydb`.`departamentos` (`iddepartamentos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`admin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`admin` (
  `idadmin` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(255) NULL,
  `email` VARCHAR(100) NULL,
  PRIMARY KEY (`idadmin`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`admin_cargo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`admin_cargo` (
  `informes_idinformes` INT NOT NULL,
  `admin_idadmin` INT NOT NULL,
  `idadmin_cargo` INT NOT NULL AUTO_INCREMENT,
  INDEX `fk_informes_has_admin_admin1_idx` (`admin_idadmin` ASC) VISIBLE,
  INDEX `fk_informes_has_admin_informes1_idx` (`informes_idinformes` ASC) VISIBLE,
  PRIMARY KEY (`idadmin_cargo`),
  CONSTRAINT `fk_informes_has_admin_informes1`
    FOREIGN KEY (`informes_idinformes`)
    REFERENCES `mydb`.`informes` (`idinformes`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_informes_has_admin_admin1`
    FOREIGN KEY (`admin_idadmin`)
    REFERENCES `mydb`.`admin` (`idadmin`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
