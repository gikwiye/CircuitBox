CREATE OR REFRESH STREAMING TABLE circuitbox.lakehouse.bronze_customers
COMMENT "Bronze table for customer data"
AS SELECT *,_metadata.file_path AS file_path, current_timestamp() AS ingestion_date
FROM cloud_files('/Volumes/circuitbox/landing/operational_data/customers','json',map('cloudFiles.inferColumnTypes','true'));


