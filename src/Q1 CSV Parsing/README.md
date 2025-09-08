**Dataset Overview**

*   **Size:** The dataset contains 100,000 entries (customers) and 11 columns.
*   **Columns:**
    *   `Customer Id`: Unique identifier for each customer (all unique).
    *   `First Name`: Customer's first name.
    *   `Last Name`: Customer's last name.
    *   `Company`: Company associated with the customer.
    *   `City`: City of the customer.
    *   `Country`: Country of the customer.
    *   `Phone 1`: Customer's primary phone number.
    *   `Phone 2`: Customer's secondary phone number.
    *   `Email`: Customer's email address (almost all unique).
    *   `Subscription Date`: Date when the customer subscribed.
    *   `Website`: URL of the website linked to the customer.
*   **No Missing Values:** The dataset appears to have no missing values in any of the columns.
*   **Data Types:** All columns are initially loaded as objects (strings).  The "Subscription Date" column was converted to datetime.

**Key Insights and Potential Analysis Areas**

1.  **Customer Distribution:**
    *   **Companies:** The number of distinct companies is less than the number of customers (71994 Companies), suggesting that multiple customers are associated with the same company.
    *   **Cities:** There are 49154 unique cities. This suggests a diverse geographic spread.
    *   **Countries:** The customer base spans over 243 countries.

2.  **Subscription Trends:**
    *   **Over Time:** The number of customers subscribing appears relatively stable over time. There are slight fluctuations over a year of data, which might be further analyzed for seasonal effects or marketing campaign impact.
    *   **Monthly Analysis:** There are fluctuations over the Year.
       Need to confirm this one as well.

3.  **Phone Number Patterns:**
    *   Phone number patterns are highly standardized in the dataset. This can be investigated to detect if there's a prevalence of certain countries of origin.
    *   Check data quality with patterns.

4.  **Email Domains:**
    *   The large number of unique email domains suggests diverse sources of email accounts and potentially a lack of corporate-specific email addresses.
    *   Analyzing top email domains is a quick way to reveal the most prevalent companies amongst customers.

5. **Top company**
    * Campbell Ltd has the most company subscribers.
    * Company type Group is on top