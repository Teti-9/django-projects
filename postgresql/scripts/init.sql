CREATE DATABASE django_ninja_project;

CREATE USER teti WITH PASSWORD 'teti123';

ALTER DATABASE django_ninja_project OWNER TO teti;

GRANT CREATE ON SCHEMA public TO django_ninja_project;