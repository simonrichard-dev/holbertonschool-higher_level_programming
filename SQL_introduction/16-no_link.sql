-- script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
SELECT
    score,
    name
FROM second_table
    WHERE 
    (
        score IS NOT NULL
    AND
        id IS NOT NULL
    AND
        name IS NOT NULL
    );
    ORDER BY DESC;