SELECT
    job_postings_fact.job_id,
    company_dim.name,
    job_postings_fact.job_title_short
FROM
    job_postings_fact
LEFT JOIN company_dim
    ON job_postings_fact.company_id = company_dim.company_id;

