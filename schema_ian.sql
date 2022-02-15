CREATE TABLE people (
	id INT PRIMARY KEY,
	name TEXT NOT NULL,
	username TEXT NOT NULL UNIQUE,
	date_created DATE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE following (
	from_id INT NOT NULL, 
	following_id INT NOT NULL REFERENCES people (id), 
	date_created DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (from_id, following_id),
	FOREIGN KEY (from_id) REFERENCES people (id)
);