# credit_rating_mock
To implement the credit rating calculation logic for RMBS. It computes the credit rating based on the composition of the underlying mortgages, the financial status of the borrowers, and various risk factors.

## Instructions for Clonning the Code to the Local System:
1. Ensure yo have Git installed in your local system.
2. Go to the desired directory and Open CMD.
3. Write `git clone https://github.com/Abhiraj6444/credit_rating_mock.git` and hit enter
4. Then follow Instructions for Running the Code

### NOTE
In this project, most of the libraries are in-built, so there is no need to follow step 6. Jump to step 7 directly.

## Instructions for Running the Code:
1. Ensure you have Python installed in your local system `(Windows OS)`.
2. Create a virtual environment using `python -m venv rmbs_env`
3. Activate the virtual environment using `rmbs_env\Scripts\activate`
4. Then type `cd credit_rating_mock`
5. Validate file like `'payload.json, 'credit_rating.py', 'test_credit_rating.py', 'requiremtments.txt'` they should be in the directory.
6. Install dependencies using `pip install -r requiremtments.txt`
7. Run the script using >>> `python credit_rating.py`
8. Run the test script using >>> `python test_credit_rating.py`

## Key Decisions
- A JSON input file is used for flexibility and scalability.
- Unit tests cover core logic and edge cases.