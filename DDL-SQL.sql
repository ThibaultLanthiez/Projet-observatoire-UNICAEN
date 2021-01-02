CREATE TABLE communes(
    code_commune TEXT PRIMARY KEY, -- code insee
    departement TEXT,
    ville TEXT,
    longitude REAL,
    latitude REAL
);
    
CREATE TABLE LP( -- Licence
  code INT PRIMARY KEY,
  type_diplome TEXT,
  q6_7 TEXT, -- type d’employeur
  q6_8 TEXT, -- secteur activite
  q6_9a TEXT, -- departement
  q6_9b TEXT, -- pays
  q6_9c TEXT, -- ville
  q6_14_6 TEXT -- nom etablissement
);

CREATE TABLE MASTER(
  code INT PRIMARY KEY,
  type_diplome TEXT,
  q6_7 TEXT, -- type d’employeur
  q6_8 TEXT, -- secteur activite
  q6_9a TEXT, -- departement
  q6_9b TEXT, -- pays
  q6_9c TEXT, -- ville
  q6_14_6 TEXT -- nom etablissement
);

CREATE TABLE SIRENE(
  code_entreprise VARCHAR,
  code_etablissement VARCHAR,
  departement VARCHAR,
  ville VARCHAR(100),
  nom_etablissement VARCHAR(100),
  code_naf VARCHAR
);

CREATE INDEX departement_index ON SIRENE(departement);

CREATE TABLE NAF(
    NIV5 VARCHAR(7),
    NIV1 VARCHAR(1)
);











