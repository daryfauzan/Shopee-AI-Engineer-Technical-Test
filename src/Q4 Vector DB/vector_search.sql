-- Schema
CREATE TABLE vectors (
  id SERIAL PRIMARY KEY,
  vec FLOAT8[],
  norm FLOAT8,
  payload JSONB
);

-- Cosine similarity search
CREATE OR REPLACE FUNCTION search_vectors(qvec FLOAT8[], topk INT)
RETURNS TABLE (item_id INT, payload JSONB, similarity FLOAT8) AS $$
DECLARE
    qnorm FLOAT8;
BEGIN
    qnorm := sqrt((SELECT sum(x^2) FROM unnest(qvec) AS t(x)));

    RETURN QUERY
    SELECT v.id, v.payload, 
           (SELECT sum(x * y)
            FROM unnest(v.vec, qvec) AS t(x,y)) / (v.norm * qnorm) AS cosine_similarity
    FROM vectors v
    ORDER BY cosine_similarity DESC
    LIMIT topk;
END;
$$ LANGUAGE plpgsql;