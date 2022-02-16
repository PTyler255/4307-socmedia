CREATE TABLE post (
	id INT PRIMARY KEY,
	user_id INT NOT NULL,
	content TEXT NOT NULL,
	date_created DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES people (id)
);

CREATE TABLE comments (
	id INT PRIMARY KEY,
	user_id INT NOT NULL,
	post_id INT NOT NULL,
	reply_id INT,
	content TEXT NOT NULL,
	date_created DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES people (id),
	FOREIGN KEY (post_id) REFERENCES post (id)
);

CREATE TABLE likes (
	id INT PRIMARY KEY,
	user_id INT NOT NULL,
	post_id INT NOT NULL,
	date_created DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES people (id),
	FOREIGN KEY (post_id) REFERENCES post (id) 
);