
-- Install the extension we just compiled

CREATE EXTENSION IF NOT EXISTS vector;

/*
"768" dimensions for our vector embedding are critical - that is the
number of dimensions of our open source embeddings model output, for later in the
article.
*/

CREATE TABLE items (id bigserial PRIMARY KEY, content TEXT, embedding vector(768));

