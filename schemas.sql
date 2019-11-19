---------------------------------------------------
-- DROP 3 primary TABLES
-- If they exist
DROP TABLE categories;

---------------------------------------------------
-- CREATE TABLE SCHEMAS
-- Remember when importing to select the following
-- FORMAT: csv
-- ENCODING:  LATIN-1 (ISO/IEC 8859-1)
-- DELIMITER: ,
-- QUOTE: "
CREATE TABLE categories(
    labels VARCHAR,
    job_description VARCHAR
);