# urlshortener


### URL Shortener API

A simple URL shortening API project built in Django Rest Framework. 


---

### Features:
- **URL Shortening**: User can provide a long URL and receive its shortened version.
- **Original URL Retrieval**: User can use the shortened URL to redirect to the original page.
---

### Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/Tomasz98/urlshortener.git
   ```

2. Navigate to the project directory:
   ```bash
   cd urlshortener
   ```

3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Perform database migrations:
   ```bash
   python manage.py migrate
   ```

---

### Running:

1. Start the development server:
   ```bash
   python manage.py runserver
   ```
---

### Using the API:

1. **URL Shortening**:
   - Endpoint: `http://localhost:8000/api/create/`
   - Method: POST
   - Input: JSON with "original_url"

2. **Original URL Retrieval**:
   - Endpoint: `http://localhost:8000/api/shrt/<short_code>/`
   - Method: GET

---

### Testing:

To run the tests, use the following command:

```bash
python manage.py test
```

---

### Tools and Technologies:

- Django Rest Framework

---

### Author:

Tomasz Bogucki

---
