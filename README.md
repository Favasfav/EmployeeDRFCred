Employee Management System API
This is a Django REST Framework based Employee Management System API. It allows you to perform CRUD operations (Create, Read, Update, Delete) on employees along with their associated address details, work experiences, qualifications, and projects.

Installation
Clone the repository:


Copy code
git clone https://github.com/your_username/employee-management-api.git
Navigate to the project directory:


Copy code
cd employee-management-api
Install dependencies using pip:

Copy code
pip install -r requirements.txt
Make migrations:

Copy code
python manage.py makemigrations
python manage.py migrate
Run the server:

Copy code
python manage.py runserver
API Endpoints
GET /api/employees/ - Retrieve a list of all employees.
GET /api/employees/{employee_id}/ - Retrieve details of a specific employee.
POST /api/employees/ - Create a new employee.
PUT /api/employees/{employee_id}/ - Update details of a specific employee.
DELETE /api/employees/{employee_id}/ - Delete a specific employee.
Usage
Retrieve all employees: Send a GET request to /api/employees/.
Retrieve a specific employee: Send a GET request to /api/employees/{employee_id}/.
Create a new employee: Send a POST request to /api/employees/ with the required employee data in the request body.
Update an existing employee: Send a PUT request to /api/employees/{employee_id}/ with the updated employee data in the request body.
Delete an employee: Send a DELETE request to /api/employees/{employee_id}/.
