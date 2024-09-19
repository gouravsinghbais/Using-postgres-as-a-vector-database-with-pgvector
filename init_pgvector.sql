
-- Install the extension you just compiled

CREATE EXTENSION IF NOT EXISTS vector;

/*
"768" dimensions for your vector embedding are critical; that is the
number of dimensions of your open source embeddings model output, for later in the
article.
*/

CREATE TABLE items (id bigserial PRIMARY KEY, content TEXT, embedding vector(768));

