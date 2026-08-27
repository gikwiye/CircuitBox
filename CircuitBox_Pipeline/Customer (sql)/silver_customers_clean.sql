CREATE OR REFRESH STREAMING TABLE circuitbox.lakehouse.silver_customers_clean
(
    CONSTRAINT valid_customer_id Expect (customer_id IS NOT NULL) on VIOLATION FAIL UPDATE,
    CONSTRAINT valid_customer_name EXPECT (customer_name IS NOT NULL) ON VIOLATION DROP ROW,
    CONSTRAINT VALID_telephone EXPECT (LENGTH(telephone)>=10),
    CONSTRAINT valid_email EXPECT (email IS NOT NULL),
    CONSTRAINT valid_date_of_birth EXPECT (date_of_birth>='1920-01-01')
    )
COMMENT "Silver table for customer data"
AS SELECT 
customer_id,
customer_name,
CAST(date_of_birth AS DATE) AS date_of_birth,
telephone,
email,
CAST(Created_date AS DATE) as created_date
FROM STREAM(LIVE.bronze_customers);

/*
Setup for history tracking
*/

CREATE OR REFRESH STREAMING TABLE circuitbox.lakehouse.silver_customers
COMMENT 'SCD Type 1 customer Data'
TBLPROPERTIES ('quality'='silver');

APPLY CHANGES INTO LIVE.silver_customers
FROM STREAM(LIVE.silver_customers_clean)
KEYS (CUSTOMER_ID)
SEQUENCE BY created_date
STORED AS SCD TYPE 1;
